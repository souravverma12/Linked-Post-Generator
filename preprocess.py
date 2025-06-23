import json
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from llm_helper import llm


def process_posts(raw_file_path,processed_file_path="data/processed_posts.json"):
    enriched_posts=[]
    with open(raw_file_path,encoding='utf-8') as file:
        posts=json.load(file)
        # print(posts)
        for post in posts:
            metadata=extract_metadata(post['text'])
            post_with_metadata = post | metadata #we want posts and metadata together
            enriched_posts.append(post_with_metadata) #so here we appended it


    unified_tags=get_unified_tags(enriched_posts)

    for post in enriched_posts:
        current_tags=post['tags']
        new_tags= {unified_tags[tag] for tag in current_tags}
        post['tags']=list(new_tags)

    with open(processed_file_path,encoding='utf-8',mode="w") as outfile:
        json.dump(enriched_posts,outfile,indent=4)

        # {
        #     "Jobseeker":"job Search",
        #     "job Hunting":"Job search",
        #
        # }






def extract_metadata(post):
    template = '''
    YYou are given a LinkedIn post. You need to extract metadata.
    Return ONLY a valid JSON object with exactly three keys: "line_count", "language", and "tags".
    language should be English or Hinglish (Hinglish means Hindi + English) and there should be only two tags
    DO NOT include any other text, preambles, or explanations.

Example output format:
```json
{{
    "line_count": 10,
    "language": "English",
    "tags": ["Career", "Networking"]
}}

    Here is the actual post on which you need to perform this task:  
    {post}
    '''

    pt = PromptTemplate.from_template(template)
    chain = pt | llm
    response = chain.invoke(input={"post": post})

    try:
        json_parser = JsonOutputParser()
        res = json_parser.parse(response.content)
    except OutputParserException:
        raise OutputParserException("Context too big. Unable to parse jobs.")
    return res


def get_unified_tags(posts_with_metadata):
    unique_tags = set()
    for post in posts_with_metadata:
        unique_tags.update(post['tags'])

    unique_tags_list = ','.join(unique_tags)

    template = ''' I will give you a list of tags. You need to unify tags.
    Return ONLY a JSON object mapping original tags to their unified tags, with no preamble or additional text.
    DO NOT include any other text, preambles, or explanations.

    Requirements for unification:

    Tags are unified and merged to create a shorter list. Example 1: "Jobseekers", "Job Hunting" can be all merged into a single "Job Search". Example 2: "Motivation", "Inspiration", "Drive" can be mapped to "Motivation". Example 3: "Personal Growth", "Personal Development", "Self Improvement" can be mapped to "Self Improvement". Example 4: "Scam Alert", "Job Scam" etc. can be mapped to "Scams".
    Each unified tag should follow title case convention. Example: "Motivation", "Job Search".
    
    For example:{{"Jobseekers":"Job Search","Job Hunting":"Job Search","Motivation":"Motivation"}}

    Here is the list of tags:
    {tags}
    '''
    pt = PromptTemplate.from_template(template)
    chain = pt | llm
    response = chain.invoke(input={"tags": str(unique_tags_list)})

    try:
        json_parser = JsonOutputParser()
        res = json_parser.parse(response.content)
    except OutputParserException:
        raise OutputParserException("Content too big.Unable to parse jobs.")
    return res



if __name__=="__main__":
    process_posts("data/raw_posts.json","data/processed_posts.json")
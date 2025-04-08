from openai import OpenAI
client = OpenAI()
import json

def get_sentiment(text: list) -> list:
    """
    This function takes in a list of strings and uses the OpenAI API to analyze the sentiment of each review. 
    Args: 
        text (list): A list of strings of reviews to be analyzed for sentiment.
    
    Returns:
        list: A list of strings representing the sentiment of each review including
        'positive', 'neutral', 'negative' or 'irrelevant'.
    """
    system_prompt = """You are an expert in interpreting human sentiment across different cultures. Ensure each review (each item in the list) should be evaluated as a whole and not just by the keywords. For example, a review may start with 'I want to love this ....' but end with 'I was shocked with how disgusting the taste was.' This would be categorized as a negative even though there may be positive words like love and excited. Try to be as quick and consistent as possible. Thank you.
    """

    prompt = f"""
    For each line of text in the string below, please categorize the review
    as either positive, neutral, negative, or irrelevant.

    Use only a one-word response per line. Do not include any numbers.
    {text}
    """

    allStrings = True
    for data in text:
        if data != str(data):
            allStrings = False
            break   

    if len(text) == 0 or not allStrings:
        return "Wrong input. text must be an array of strings." 

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
	    { "role": "developer",  "content": system_prompt },
        { "role": "user",  "content": prompt }
        ]
    )
    output = []
    
    for each in completion.choices[0].message.content.splitlines():
        output.append(each.strip())
    
    return output

    # sentiments = {'positive':[], 'neutral':[], 'negative':[], 'irrelevant':[]}

    # for data in range(len(text)):
    #     sentiments[output[data]].append(text[data])

    # for key in sentiments:
    #     print(len(sentiments[key]))
        
    # with open("sentiment_output.json", "w") as file:
    #     json.dump(sentiments, file, indent=4)


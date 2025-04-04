from openai import OpenAI
client = OpenAI()

def get_sentiment(text: list) -> list:
    """
    INSERT DOCSTRING HERE
    """
    system_prompt = """You are an expert in interpreting human sentiment across different cultures. Ensure each review (each item in the list) should be evaluated as a whole and not just by the keywords. For example, a review may start with 'I want to love this ....' but end with 'I was shocked with how disgusting the taste was.' This would be categorized as a negative even though there may be positive words like love and excited. 
    """

    prompt = f"""
    For each line of text in the string below, please categorize the review
    as either positive, neutral, negative, or irrelevant.

    Use only a one-word response per line. Do not include any numbers.
    {text}
    """

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
	    { "role": "developer",  "content": system_prompt },
        { "role": "user",  "content": prompt }
        ]
    )
    output = []
    allStrings = True
    for data in text:
        if data != str(data):
            allStrings = False
            break

    if len(text) == 0 or not allStrings:
        return "Wrong input. text must be an array of strings."    
    
    for each in completion.choices[0].message.content.splitlines():
        output.append(each.strip())


    file = open("sentiment_output.text","w")
    for data in range(len(output)):
        file.write(f"sentiment: {output[data]} - review: {text[data]}\n")
    file.close()

    return output

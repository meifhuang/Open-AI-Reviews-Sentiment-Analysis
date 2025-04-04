from label import get_sentiment
from visualize import make_plot

import json


def run(filepath: str):
    """
    This function reads a json file containing reviews, extracts the reviews and then uses the get_sentiment function to analyze the sentiment of each review. It then plots a visualization of the sentiment ratio and returns a list of sentiments for each review. 

    Args: 
        filepath (str): The filepath to a json object 
    
    Returns:
        list: A list of strings representing the sentiment of each review including
        'positive', 'neutral', 'negative' or 'irrelevant'.
    """
    # open the json object
    data_file = open(filepath)
    data_json = data_file.read()
    reviews = json.loads(data_json)
    
    # extract the reviews from the json file
    results = reviews["results"]

    # get a list of sentiments for each line using get_sentiment
    sentiments = get_sentiment(results)

    # plot a visualization expressing sentiment ratio
    make_plot(sentiments)

    # return sentiments
    return sentiments


if __name__ == "__main__":
    print(run("data/raw/reviews.json"))

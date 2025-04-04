import matplotlib.pyplot as plt


def make_plot(sentiments: list) -> list:
    """
    This function takes in a list of string of sentiments and counts the number of times each sentiment appears which is graphed onto a bar graph and saved into a folder called images. 
     
    Args: 
        sentiments (list): A list of strings of sentiments
        
    """

    count = { 'positive': 0, 'neutral': 0, 'negative': 0, 'irrelevant': 0 }
    for sentiment in sentiments:
        if sentiment in count:
            count[sentiment] += 1
    
    x = list(count.keys())
    y = list(count.values())
    plt.bar(x,y, color="blue")
    plt.title("Sentiment Analysis Count")
    plt.xlabel("Sentiment")
    plt.ylabel("Count")
    plt.savefig("images/sentiment_analysis_count.png")
    
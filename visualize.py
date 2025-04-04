import matplotlib.pyplot as plt


def make_plot(sentiments: list) -> list:
    """
    INSERT DOCSTRING HERE
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
    
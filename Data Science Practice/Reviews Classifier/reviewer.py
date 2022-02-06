class Review:
    def __init__(self, review, rating):
        self.review = review
        self.rating = rating
        self.sentiment = self.set_sentiment()
    
    def set_sentiment(self):
        if self.rating <= 3:
            return "Negative"
        else:
            return "Positive"
        
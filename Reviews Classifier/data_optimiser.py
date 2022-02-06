class DataOptimizer:
    def __init__(self, data):
        self.equal_data = self.equally_distribute(data)
    
    def equally_distribute(self, data):
        pos_reviews = list(filter(lambda x: x.sentiment == 'Positive', data))
        neut_reviews = list(filter(lambda x: x.sentiment == 'Neutral', data))
        neg_reviews = list(filter(lambda x: x.sentiment == 'Negative', data))
        min_rev = min([len(pos_reviews), len(neut_reviews), len(neg_reviews)])
        reviews = pos_reviews[:min_rev] + neut_reviews[ :min_rev] + neg_reviews[:min_rev]
        return reviews
    
    def get_reviews_ratings(self):
        reviews = [x.review for x in self.equal_data]
        sentiments = [x.sentiment for x in self.equal_data]
        return reviews, sentiments

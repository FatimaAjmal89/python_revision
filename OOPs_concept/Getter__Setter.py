class Book:
    review = 0
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.review = []

    def new_review(self,review):
        self.review.append(review)

    def count_review(self):

        print(f"total reviews {len(self.review) }")

    def display(self):
        for r in self.review:
            print(f"review : { r}")

b1 = Book ("dumbo" ,"huzaifa" )
b1.new_review("good")
b1.new_review("gooddddd")
b1.count_review()
b1.display()
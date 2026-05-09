class Product:
    count = 0
    def __init__(self,name,price):
        self.name = name
        self.price = price
        Product.count +=1

    def info(self):
        print(f"product name = {self.name} and price {self.price}")

    @classmethod
    def total_count(cls):
        print(f"total products= {cls.count}")

    @staticmethod
    def discount(percent,product_price):
        final_price = product_price -(percent *product_price /100)
        print(f"before discount {product_price} and after discount {final_price}")


p1 = Product("ipad",100000)
p2 = Product("laptopHP",30000)
p11 = Product("macbook",20000)

p1.info()
Product.total_count()
Product.discount(10,2000)

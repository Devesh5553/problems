class ProductOfNumbers:

    def __init__ (self):
        self.prefixProduct = [1]
        self.size = 0

    def add(self, num: int) -> None:
        if num == 0:
            self.prefixProduct = [1]
            self.size = 0
        else:
            self.prefixProduct.append(self.prefixProduct[self.size] * num)
            self.size += 1

    def getProduct(self, k: int) -> int:
        if k > self.size:
            return 0
        return (self.prefixProduct[self.size] // self.prefixProduct[self.size - k])


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
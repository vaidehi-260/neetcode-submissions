class StockSpanner:

    def __init__(self):
        self.s=[]

    def next(self, price: int) -> int:
        self.s.append(price)
        span = 1
        i = len(self.s)-2
        while i>=0 and self.s[i]<=price:
            span+=1
            i-=1
        return span



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
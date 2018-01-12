class Share:
    def __init__(self, code, name, current, price, diff, per_diff):
        self.code = code
        self.name = name
        self.current = current
        self.price = price
        self.diff = diff
        self.per_diff = per_diff
    
    def get_rss_item(self, fe):
        fe.title(self.name)
        fe.id(self.code)
        fe.content(self.code + ',' + self.name + ',' + self.current.encode('utf-8') + ',' + self.price.encode('utf-8') + ',' + self.diff.encode('utf-8') + ',' + self.per_diff.encode('utf-8'))
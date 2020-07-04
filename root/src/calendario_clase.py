class calendarioo:
    def __init__(self,day):
        a=day.split("/")

        self.dayy=int(a[0])
        self.monthh=int(a[1])
        self.yearr=int(a[2])
    def day(self):
        return self.dayy

    def month(self):
        return self.monthh

    def year(self):

        return self.yearr

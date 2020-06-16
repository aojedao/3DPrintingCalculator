
class nodd:
    def __init__(self,otherr,day):

        self.valuee=otherr[0]
        self.otherr=otherr
        self.nextt=None
        self.day=day
class Hash_table:
    def __init__(self):
        self.m=1000000
        self.p=1000017
        self.p2=1000031
        self.arr=[0]*self.m
        self.a=73
        self.b=34
        self.x=21

    def Polihash(self,letter,new_node=False):
        letter.replace(" ","")
        hash=0
        for i in range(len(letter)):
            hash+=(ord(letter[i])*(self.x**i))%self.p

        return self.hashing(hash,new_node) if new_node else self.hashing(hash)
    def hashing(self,number,new_node=False):
        hash=((self.a*number +self.b)%self.p2)%self.m
        a=self.arr[hash]

        if new_node:

            if not a:
                self.arr[hash]=new_node

            else:

                while a.nextt:
                    a=a.nextt
                a.nextt=new_node
        else:
            if not a:
                return False
        return hash
    def search_hash(self,letter):
        print("dasd")
        a=self.Polihash(letter)
        print("siii",a)
        if a:
            print((self.arr[a].otherr[1]))
            return self.arr[a]
        else:
            return False
    def delete(self,name):

        a=self.Polihash(name)
        self.arr[a]=0

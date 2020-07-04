class node_avl:
    def __init__(self,day,name):
        self.value=day
        self.height=1
        self.right=None
        self.left=None
        self.parent=None
        self.nodes=[name]

class AVL_tree:
    def __init__(self):
        self.root=None
        self.maxx=-1
    def getheight(self,nod):
        if nod:
            return nod.height
        else:
            return 0
    def adjust_height(self,nod):

        b=0 if not nod.left else nod.left.height
        c=0 if not nod.right else nod.right.height
        nod.height=1+max(b,c)

    def rebalance(self,nod):
        a=nod.parent
        b=0 if not nod.left else nod.left.height
        c=0 if not nod.right else nod.right.height
        if b>c+1:
            self.rebalance_right(nod)
        elif c>b +1:
            self.rebalance_left(nod)
        self.adjust_height(nod)
        if a:
            self.rebalance(a)

    def rebalance_right(self,nod):
        m=nod.left
        if m:
            b=0 if not m.left else m.left.height
            c=0 if not m.right else m.right.height
            if b<c:
                self.rotate_left(m)

        self.rotate_right(nod)

    def rebalance_left(self,nod):
        m=nod.right

        if m:
            b=0 if not m.left else m.left.height
            c=0 if not m.right else m.right.height
            if b>c:
                self.rotate_right(m)
        self.rotate_left(nod)




    def rotate_right(self,nod):
        a=nod.left
        b=a.right
        c=nod.parent
        a.parent=c

        nod.parent=a
        nod.left=b
        if b:
            b.parent=nod

        a.right=nod
        if not c:
            self.root=a
        elif c.right==nod:
            c.right=a
        else:
            c.left=a

        nod.height=1+max(self.getheight(nod.left),self.getheight(nod.right))
        a.height=1+max(self.getheight(a.left),self.getheight(a.right))


    def rotate_left(self,nod):
        a=nod.right
        b=a.left
        c=nod.parent

        a.parent=c

        nod.parent=a
        nod.right=b
        if b:
            b.parent=nod

        a.left=nod
        if not c:
            self.root=a
        elif c.right==nod:
            c.right=a
        else:
            c.left=a

        nod.height=1+max(self.getheight(nod.left),self.getheight(nod.right))
        a.height=1+max(self.getheight(a.left),self.getheight(a.right))


    def left_descendent(self,nod_a):
        if not nod_a.left:
            return nod_a
        else:
            return self.left_descendent(nod_a.left)

    def right_ancestor(self,node_b):

        if node_b.value.year()<node_b.parent.value.year() or (node_b.value.year()==node_b.parent.value.year() and node_b.value.month()<node_b.parent.value.month()) or (node_b.value.year()==node_b.parent.value.year() and node_b.value.month()==node_b.parent.value.month() and node_b.value.day()<node_b.parent.value.day()):
            return node_b.parent
        else:
            return self.right_ancestor(node_b.parent)
    def next(self,nod):

        if nod.right:

            return self.left_descendent(nod.right)
        else:
            if self.maxx.year()==nod.value.year() and self.maxx.month()==nod.value.month() and  self.maxx.day()==nod.value.day():

                return nod
            else:

                return self.right_ancestor(nod)

    def find(self,k,R):

        if R.value.day()==k.day() and R.value.month()==k.month() and R.value.year()==k.year():
            return R
        elif R.value.year()>k.year() or (R.value.year()==k.year() and R.value.month()>k.month()) or (R.value.year()==k.year() and R.value.month()==k.month() and R.value.day()>k.day()):
            if R.left:
                return self.find(k,R.left)
            return R
        elif  R.value.year()<k.year() or (R.value.year()==k.year() and R.value.month()<k.month()) or (R.value.year()==k.year() and R.value.month()==k.month() and R.value.day()<k.day()):
            if R.right:
                return self.find(k,R.right)
            return R
    def insertar(self,value,name):

        if not self.root:

            a=node_avl(value,name)
            self.root=a
            self.maxx=value

        else:
            pos=self.find(value,self.root)

            if value.year()==pos.value.year() and value.month()==pos.value.month() and value.day()==pos.value.day():
                pos.nodes.append(name)
                return pos
            else:
                new_node=node_avl(value,name)
                new_node.parent=pos
                if value.year()>self.maxx.year() or (value.year()==self.maxx.year() and value.month()>self.maxx.month()) or(value.year()==self.maxx.year() and value.month()==self.maxx.month() and value.day()>self.maxx.day()):
                    self.maxx=value

                if value.year()>pos.value.year() or (value.year()==pos.value.year() and value.month()>pos.value.month()) or(value.year()==pos.value.year() and value.month()==pos.value.month() and value.day()>pos.value.day()):
                    pos.right= new_node
                else:
                    pos.left=new_node
                return new_node

        return self.root
    def delete_value(self,day,value):

        a=self.find(day,self.root)

        if not a:
            return -1
        for i in a.nodes:
            if i==value:
                a.nodes.remove(i)
                if len(a.nodes)<1:

                    self.delete(a.value,a)
                break
    def delete(self,val,a):
        if self.maxx.year()==self.root.value.year() and self.maxx.month()==self.root.value.month() and self.maxx.day()==self.root.value.day() :

            self.root=None
            self.maxx=None
        else:
            if val.year()==self.maxx.year() and val.month()==self.maxx.month() and val.day()==self.maxx.day():
                if a.left:
                    self.maxx=self.only_right(a.left).value
                else:
                    self.maxx=a.parent.value


            if not a.right:

                if a==self.root:
                    self.root=a.left
                    if a.left:
                        a.left.parent=None
                        self.rebalance(a.left)
                else:
                    if a.parent.left==a:
                        a.parent.left=a.left

                    else:
                        a.parent.right=a.left
                    if a.left:
                        a.left.parent=a.parent
                    self.rebalance(a.parent)
            else:
                b=self.next(a)

                c=b.parent
                d=a.parent
                if a==c:
                    b.parent=d
                    b.left=a.left
                    if a.left:
                        a.left.parent=b
                    if d:
                        if d.left==a:
                            d.left=b
                        else:
                            d.right=b
                        self.rebalance(d)
                    else:

                        self.root=b
                        self.rebalance(b)

                else:
                    if c.left==b:
                        c.left=b.right

                    else:
                        c.right=b.right
                    if b.right:
                        b.right.parent=c
                    b.right=a.right
                    b.left=a.left
                    if d:
                        if d.left==a:
                            d.left=b
                        else:
                            d.right=b
                    else:
                        self.root=b

                    b.parent=d
                    if a.left:
                        a.left.parent=b
                    a.right.parent=b


                    self.rebalance(c)

    def avl_insert(self,day,name):
        b=self.insertar(day,name)
        self.rebalance(b)
    def search_range(self,m1,m2):

        if self.root:

            if m1.year()>self.maxx.year() or (m1.year()==self.maxx.year() and m1.month()>self.maxx.month()) or (m1.year()==self.maxx.year() and m1.month()==self.maxx.month() and m1.day()>self.maxx.day()):
                return False
            else:

                a=self.find(m1,self.root)

                if (m1.year()==self.maxx.year() and m1.month()==self.maxx.month() and m1.day()==self.maxx.day()) and (m1.year()<a.value.year() or (m1.year()==a.value.year() and m1.month()<a.value.month()) or (m1.year()==a.value.year() and m1.month()==a.value.month() and m1.day()<a.value.day())):
                    return False

                c=[]

                while  ((a.value.year()==m2.year() and a.value.month()==m2.month() and a.value.day()==m2.day()) or (a.value.year()<m2.year() or (a.value.year()==m2.year() and a.value.month()<m2.month()) or (a.value.year()==m2.year() and a.value.month()==m2.month() and a.value.day()<m2.day()))) and (a.value.year()<self.maxx.year() or (a.value.year()==m2.year() and a.value.month()<self.maxx.month()) or (a.value.year()==self.maxx.year() and a.value.month()==self.maxx.month() and a.value.day()<self.maxx.day())):
                    
                    if (a.value.year()==m1.year() and a.value.month()==m1.month() and a.value.day()==m1.day()) or (a.value.year()>m1.year() or (a.value.year()==m1.year() and a.value.month()>m1.month()) or (a.value.year()==m1.year() and a.value.month()==m1.month() and a.value.day()>m1.day())):
                        c+=a.nodes
                    a=self.next(a)
                if (m2.year()==self.maxx.year() and m2.month()==self.maxx.month() and m2.day()==self.maxx.day()) or  (m2.year()>self.maxx.year() or (m2.year()==self.maxx.year() and m2.month()>self.maxx.month()) or (m2.year()==self.maxx.year() and m2.month()==self.maxx.month() and m2.day()>self.maxx.day())):
                    c+=a.nodes

            return c
    def only_right(self,nod):
        while nod.right:
            nod=nod.right
        return nod

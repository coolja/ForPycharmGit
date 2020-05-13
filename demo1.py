class Person:
    def __str__(self):
        if self.hp<=0:
            return "%s当前生命值为0"%self.name
        else:
            return "%s当前生命值为%d" % (self.name, self.hp)
    def __init__(self,name):
        self.name=name
        self.hp=100
class Hero(Person):
    def fire(self,p):
        damage=20
        p.hp-=20
        print("%s向%s开枪，造成了%d伤害"%(self.name,p.name,damage))
class Is(Person):
    def fire(self,p):
        damage=5
        p.hp-=5
        print("%s向%s开枪，造成了%d伤害"%(self.name,p.name,damage))
    pass

def main():
    h=Hero("【英雄】")
    is1=Is("【恐怖分子1】")
    is2 = Is("【恐怖分子2】")
    is3 = Is("【恐怖分子3】")
    round = 1
    while True:
        print("------------第%d回合------------"%round)
        h.fire(is1)
        if is1.hp>0:
            is1.fire(h)
        h.fire(is2)
        if is2.hp > 0:
            is2.fire(h)
        h.fire(is3)
        if is3.hp > 0:
            is3.fire(h)
        print("================================")
        print(h)
        print(is1)
        print(is2)
        print(is3)
        print("================================")
        if h.hp<=0:
            print("%s死亡，枪战结束"%h.name)
            break
        if is1.hp<=0 and is2.hp<=0 and is3.hp<=0:
            print("恐怖分子全体死亡，枪战结束")
            break
        if is1.hp<=0:
            print("%s死亡"%is1.name)
        if is2.hp<=0:
            print("%s死亡"%is2.name)
        if is3.hp<=0:
            print("%s死亡"%is3.name)
        round+=1



main()

class Human:
    def __init__(self,name,nickname,height,weight,sex,age):
        self.name = name
        self.nickname = nickname
        self.height = height
        self.weight = weight
        self.sex = sex
        self.age = age

    def hello(self):
        print(f'{self.name} : สวัสดีจ้าทุกคน')

    def sit(self):
        print('ฉันกำลังนั่ง')

    def stand(self):
        print('ฉันกำลังยืน')

    def walk(self):
        print('ฉันกำลังเดินไปข้างหน้า')

    def stop(self):
        print('ฉันหยุดเดินแล้ว')

class Car(Human):
    def __init__(self,brand,price,time,name,nickname,height,weight,sex,age):
        super().__init__(name,nickname,height,weight,sex,age)
        self.brand = brand 
        self.price = price
        self.time = time
        self.money = 10000

    def chooseCar(self):
        print(f'ฉันมีเงิน : {self.money}')
        print(f'วันนี้ฉันจะเดินทางด้วยรถ {self.brand} ราคา {self.price}')
        print(f'เวลาที่ฉันเดินทางถึงบ้าน คือ {self.time}')

Hu = Human('chat','ouy',175,75,'Male',40)
print(f'My name is {Hu.name}')
print(f'My nickname is {Hu.nickname}')
print(f'ฉันมีอายุ {Hu.age}')
Hu.hello()
Hu.sit()
Hu.stand()
Hu.walk()
Hu.stop()
print('--------------------------------------------------------------')
drive = Car('benz','3million','very fast','chat','ouy',175,75,'Male',40)

drive.chooseCar()
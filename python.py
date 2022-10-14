class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result
    
    def mul(self):
        result = self.first * self.second
        return result
    
    def div(self):
        result = self.first / self.second
        return result

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first**self.second
        return result

A=MoreFourCal(2,6)

class SafeFourCal(MoreFourCal):
    def div(self):
        if self.seond==0:
            return 0
        else:
            result = self.first / self.second
            return result

class Family:
    lastname= "Kwon"

K = Family()
print(K.lastname)

print(A.pow())
#Class안에 있는 함수를 메소드
#Class에서 a(=객체 즉 새로만든 인스턴스) == setdata의 self로 전달된다
#class는 똑같은 기능을 하는 함수를 여러개 만들어아야할때, 각각의 새로운 변수를 할당하고 만드는게 아니라
#일종의 form이다. 이렇게 클래스로 만들어진 객체들은 각각 따로 작동한
#a는 쿠키다 , a는 Cookie()의 인스턴스다
#메서드의 첫번째 매개변수 self는 특별한 의미를 가진다
#클래스 안의 함수는 메서드이다.
#파이썬 메서드에서는 객체를 호출할때 본인이 전달된다. 다만 표기할때는 생략한다
import sys
print(sys.argv)

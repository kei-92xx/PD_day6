class score:
    def __init__(self, name="홍길동", kor=80, eng=70, mat=90):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat
        self.calculate()
        
    def calculate(self):
        self.total = self.kor + self.eng + self.mat #중간에 변수 추가를 해도 된다
        self.avg = round( self.total / 3 )
        
    def output(self):
        print(f"{self.name} {self.kor} {self.eng} {self.mat} {self.total} {self.avg}")
        
p1 = score()
p2 = score("임꺽정",60,50,50)
p3 = score("장길산")
p4 = score("강감찬",mat=70)

p1.output()
p2.output()
p3.output()
p4.output()
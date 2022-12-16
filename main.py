class Car:
    Model = ''
    Mark = ''
    power = 0
    length = 0
    width = 0
    height = 0

    def __init__(self):
        print('Created object Car')
        self.Model = '1993'
        self.Mark = 'Ferrari'
        self.power = 320
        self.length = 4230
        self.width = 1894
        self.height = 1170

    def ShowOn(self):
        print(
            f'Model: {self.Model}\nMark: {self.Mark}\nPower: {self.power}\nLength: {self.length}\nWidth: {self.width}\nHeight: {self.height}')

    def __del__(self):
        print('Deleted object Car')

if __name__ == '__main__':
    car = Car()
    car.ShowOn()


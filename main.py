class Phone:
    Model = ''
    Mark = ''
    power = 0
    screen = 0

    def __init__(self):
        print('Created object Phone')
        self.Model = 'Galaxy Flip4 F721B'
        self.Mark = 'Samsung'
        self.screen = 6.7


    def ShowOn(self):
        print(
            f'Model: {self.Model}\nMark: {self.Mark}\nScreen: {self.screen}')

    def __del__(self):
        print('Deleted object Phone')

if __name__ == '__main__':
    phone = Phone()
    phone.ShowOn()
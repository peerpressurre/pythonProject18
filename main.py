class Drums:
    Model = ''
    Mark = ''
    rods = 0
    length = 0
    width = 0
    height = 0

    def __init__(self):
        print('Created object Drums')
        self.Model = '16 kit'
        self.Mark = 'Alessis'
        self.rods = 6


    def ShowOn(self):
        print(
            f'Model: {self.Model}\nMark: {self.Mark}\nRods: {self.rods}')

    def __del__(self):
        print('Deleted object Drums')

if __name__ == '__main__':
    drums = Drums()
    drums.ShowOn()
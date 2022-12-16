class Teacher:
    Model = ''
    Mark = ''


    def __init__(self):
        print('Created object Teacher')
        self.Model = 'Primary'
        self.Mark = '3rd grade'


    def ShowOn(self):
        print(
            f'Model: {self.Model}\nMark: {self.Mark}')

    def __del__(self):
        print('Deleted object Teacher')

if __name__ == '__main__':
    teacher = Teacher()
    teacher.ShowOn()
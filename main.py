class Post:
    length = 0
    width = 0
    height = 0

    def __init__(self):
        print('Created object Post')
        self.length = 45
        self.width = 45
        self.height = 60

    def ShowOn(self):
        print(
            f'Length: {self.length}\nWidth: {self.width}\nHeight: {self.height}')

    def __del__(self):
        print('Deleted object Post')

if __name__ == '__main__':
    post = Post()
    post.ShowOn()

import dropbox

class DataTransfering:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self, file_f , file_t):
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_f , 'rb') as f:
            dbx.files_upload(f.read(), file_t)


def functionMain():
    access_token = "sl.BF4LO8EX2A9bpJIt1TCmqsLjx8e9HVt0qaf9ldwxjWBcU5uIs5-7_jgcBmZKWbynf4MnC4VJ7ibTr1VSlflWMmjAfXE-VxyJstx_d7ntaKiHm0OJkDI-Dmir7JrcNy5_myRa8kjU8LA"
    transferData = DataTransfering(access_token)

    file_f = 'test.txt'
    file_t = r'C:\Users\rajat\Dropbox\test.txt'

    transferData.upload_file(file_f, file_t)


if __name__ == '__main__':
    functionMain()
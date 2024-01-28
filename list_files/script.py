import os





def start():
    istr=input("")


    list_files=os.listdir(path=".")
    for i in list_files:
        if os.path.isfile(i):
            print(f'file: {i}')
        else:
            print(f'dir: {i}')

if __name__=="__main__":
    start()
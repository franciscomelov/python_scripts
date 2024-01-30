import os





def start():
    d_dict=input("")


    list_files=os.listdir(path=d_dict)
    for i in list_files:
        if os.path.isfile(i):
            print(f'file: {i}',os.stat(i).st_size,os.stat(i).st_ctime)
        else:
            print(f'dir: {i}')

if __name__=="__main__":
    start()
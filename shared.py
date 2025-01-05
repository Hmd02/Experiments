import multiprocessing
import logging

logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

x=20

def numbers(id):
    global x
    x+=1
    print(id," ",x)

if __name__=='__main__':
    p1=multiprocessing.Process(target=numbers,args=(1,))
    p2=multiprocessing.Process(target=numbers,args=(2,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Main",x)
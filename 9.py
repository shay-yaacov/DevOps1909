
import datetime
from mydev import test as mydev_test
from myotherdave import test as my_other_dev_test


my_other_dev_test()
mydev_test()

def wait_for_print():
    from time import sleep
    sleep (5)
    print ("hellow word")



print (datetime.datetime.now())


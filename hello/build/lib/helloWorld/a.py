from helloWorld.b import func_b
from time import sleep

def func_a():
    print("func_a")
    sleep(1)
    func_b()

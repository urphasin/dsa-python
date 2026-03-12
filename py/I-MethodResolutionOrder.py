class A:
    def __init__(self):
        print("A init")
        super().__init__()

class B:
    def __init__(self):
        print("B init")
        super().__init__()

class C(A, B):
    def __init__(self):
        print("C init")
        super().__init__()

print("",C.mro(),"")


print(f"\x1b[92m{C.mro()}\x1b[0m")
import tkinter


# class Example:
#     # Frame = tkinter.TK()
#
#     def __init__(self,parent):
#         parent.mainloop()
#
#         def initUI(self):
#             print('UI')
#
#
# __name__ = '__main__'
# root = tkinter.Tk()
# some = Example(root)

# z =10

class A:
    # x=4
    # global z
    # z =-1
    def __init__(self):
        self.octopus ='squid'
        print('A')
    # def printocto(self):
    #     print(self.octopus)


class B(A):
    def __init__(self):
        print('B')
    # y=3
    # global z
    # z =5

# a = A()
# b = B()
# # print(b.y + z)
# a.printocto()
# b.printocto()

b = B()
                                #Sets
s = set() #A function which creates a set, but items are unique. No two same elements are shown.
s.add(1)
s.add(2)
s.add(3)
s.add(5)
s.add(3)
print(s)

                            #A usage of {} and def main()
def square(x):
    return x * x

def main():
    for i in range(10): #Until the number 9
        print("{} squared is {}".format(i, square(i))) #{} is a placeholder, later which is specified with .format i and square(i)
    #this is an older way of plugging values in python strings
if __name__ = "__main__": #This is needed in order to seperate the main part with the function when imported.
    main()


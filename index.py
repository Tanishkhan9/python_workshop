# import time
# def timemeassure (func):
#     def wrapper(*args, **kwargs):
#         start=time.time()
#         result=func(*args, **kwargs)
#         end=time.time()
#         print(end-start)
#         return result
#     return wrapper

# xyz =54654796846549849
# print(len(xyz))   #int don't work with len function

# xyz="kkniabiibaiuciau"
# print(len(xyz)) #intstring  work with len function

# xyz=int("123456789")
# print(type(xyz))

# xyz="123456789"
# print(type(xyz))
# num=int(xyz)
# print(type(num))
# sum=str(num)
# print(type(sum))


# LIST=int([1,2,3,4,5,6,7,8,"16"])
# print(sum(LIST))

# LIST=[1,2,3,4,5,6,7,7,9,0,8]
# LIST.sort()
# print(LIST)





# LIST=[1,2,3,4,5,6,7,7,9,0,8]
# def sortedlist(LIST):
#     return sorted(LIST)
# print(sortedlist(LIST))






# LIST=[1,2,3,4,5,6,7,7,9,0,8]
# print(min(LIST))


# LIST=[1,2,3,4,5,6,7,7,9,0,8]
# print(max(LIST))


# LIST=[1,2,3,4,5]

# num=-547986547896548976541789654321789965432197865432178965432178946532178465321540+556949845465465465165416565416511654j
# print(abs(num))


# pi=3.141592653589
# print(round(pi))


# LIST=[1,2,3,4,5,6,7,9]
# for i , value in enumerate(LIST):
#     print(f'index {i} has value {value}')
# pi=3.148289
# print(f'{pi:.2f}')


# SQUARE=lambda x,y:x*y
# NUM=int(input("Number"))
# NUM2=int(input("Number"))
# print(f'{NUM}*{NUM2} is{SQUARE(NUM,NUM2)}')




# SQUARE=lambda x,y:x*y
# print(f'{SQUARE(int(input("please input a square")),int(input("please enter another number")))}')

# class XYZ:
#     def __init__(self):
#         self.ABC="123"
#     def get(self):
#         return self.ABC
# DECLARE_CLASS=XYZ()
# VALUE=DECLARE_CLASS.get()

# print(VALUE)
    
class XYZ:
    def __init__(self):
        self._balance_=0
    def deposit(self, amount):
        self._balance_+=amount
        return True
    def withdraw(self, amount):
        if 0<amount<=self._balance_:
            self._balance_-=amount
            return True
        return False

    def get(self):
        return self._balance_
class saving:
    def si():
        


ABC=XYZ()

print(ABC.get())
ABC.deposit(10000)
print(ABC.get())

ABC.withdraw(1000)

print(ABC.get())

ABC.withdraw(1000)

print(ABC.get())
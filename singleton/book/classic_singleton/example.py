from singleton import Singleton

singleton1 = Singleton("aaa")
singleton2 = Singleton("bbb")

print(singleton1 is singleton2)
print(singleton1.value)
print(singleton2.value)
singleton1.value = "ccc"
print(singleton1.value)
print(singleton2.value)


class Child(Singleton):
    pass


child = Child("ddd")
print(child is singleton1)
print(singleton1.value)
print(child.value)

import singletone

print(singletone.only_one_var)

singletone.only_one_var += " after modification"
print(singletone.only_one_var)
import module2

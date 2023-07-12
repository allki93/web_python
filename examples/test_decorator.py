# функция декоратор
# def dec(f_arg):
#     def wrapper():
#         # доп функциональность "ДО"
#         print("Before")
#         f_arg()
#         # доп функциональность "ПОСЛЕ"
#         print("After")
#     return wrapper

def foo():
    def dec(f_arg):
        def wrapper():
            # доп функциональность "ДО"
            print("Before")
            f_arg()
            # доп функциональность "ПОСЛЕ"
            print("After")
        return wrapper
    return dec


# новый способ декорирования
# @dec
@foo()
# целевая функция
def func_1():
    print("Hello!")

# старый способ декорирования
# func_1 = dec(func_1)

# вызов целевой функции
func_1()
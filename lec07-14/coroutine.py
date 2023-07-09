def simple_coroutine():
    print("-> 코루틴 시작")
    x = yield
    print(f"-> 코루틴이 받은 데이터 : {x}")


my_coro = simple_coroutine()
print(my_coro)
# next(my_coro)
# my_coro.send(10)
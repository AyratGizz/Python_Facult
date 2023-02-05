def fun():
    def fun_inside():
        nonlocal n
        n = 2
        print(n)

    n = 1
    fun_inside()
    print(n)


n = 0
fun()
print(n)

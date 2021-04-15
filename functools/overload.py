from functools import singledispatch


@singledispatch
def add(a, b):
    raise NotImplementedError('Unsupported type')


@add.register(int)
@add.register(str)
@add.register(list)
def _(a, b):
    print("First argument is of type ", type(a))
    print(a + b)


if __name__ == '__main__':
    print(add.registry.keys())
    add(1, 2)
    add('Python', 'Programming')
    add([1, 2, 3], [5, 6, 7])

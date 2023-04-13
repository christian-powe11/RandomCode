from functools import singledispatch

@singledispatch 
def func(arg):
    print(f'Default : {arg}')


@func.register
def _(arg: int | float):
    print(f'Number: {arg}')

@func.register 
def _(arg: str):
    print(f'Str: {arg}')


func(None)
func(20.0)
func('Hello')

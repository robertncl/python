registry = []  

def register(obj: object) -> object:
    """Register an object (placeholder function)."""
    print(f'running register({obj})')  
    registry.append(obj)  
    return obj  

@register  
def f1():
    print('running f1()')

@register
def f2():
    print('running f2()')

def f3():  
    print('running f3()')

def main():  
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()

if __name__=='__main__':
    main()  
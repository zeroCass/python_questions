class A:
    def __init__(self, a) -> None:
        print('A')
        self.a = a
    

class B:
    def __init__(self, b) -> None:
        print('B')
        self.b = b


class C(A, B):
    def __init__(self, a, b, c) -> None:
        super().__init__(a)
        super(A, self).__init__(b)
        print('C')
        self.c = c



class First:
    def __init__(self, first, **kwargs) -> None:
        print('First init')
        super().__init__(**kwargs)
        self.first = first


class Second:
    def __init__(self, second, **kwargs) -> None:
        print('Second init')
        super().__init__(**kwargs)
        self.second = second

class Third:
    def __init__(self, third, **kwargs) -> None:
        print('Third init')
        super().__init__(**kwargs)
        self.third = third

class Combined(First, Second, Third):
    def __init__(self, first, second, third, **kwargs) -> None:
        print('Combined')
        super().__init__(first = first,second = second, third = third, **kwargs)



combined = Combined('A', 'B', 'C')
c = C(1, 2, 3)
print(c.a, c.b, c.c)




books = {
    'hobbit':{
        'mual':'tolkin',
        'yili':1800,
        'narxi':400
    },
    }
def add(name):
    mual = input('muallifi>>> ')
    yili = input('yili>>> ')
    narxi = input('narxi>>> ')
    books[name] = {'mual':mual, 'yili':yili , 'narxi':narxi}
    
    
def check(name):
    if name in books:
        print('bu kitob mavjud')
        surov = input('kitobdi qushmoqchimisz>>> ')
        if surov == 'xa'or'ha':
            add(name)
            return books
        else:
            return "ok"
    else:
        print('kitob mavjud emas')
        ask = input('bu kitob mni qushmoqchimisiz>>> ')
        if ask == 'ha' or 'xa':
            add(name)
        return books

def metod1():
    dict_ = {'name': 'john', 'lastname': 'Snow', 12: 'age'}
    try:
        my_list = { key +'abc' for key in dict_.keys()}

    except Exception as e:
        print(e)
        my_list = {str(key)+str(value) if type(key)== type(str) and type(value)== type(str) else ''for key,value in dict_.items()  }
    print(dict_)

def metod2():
    dict_ = {'name': 'john', 'lastname': 'Snow', 12: 'age'}
    for x in dict_.keys():
        try:
            x + 'abc'
        except TypeError:
            str(x)+'abc'
    print(dict_)
metod1()
metod2()   


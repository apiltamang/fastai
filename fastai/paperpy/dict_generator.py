class DictGenerator:

    @staticmethod
    def getDicts():
        dict0 = {x:x for x in range(10)}
        import string
        string.ascii_uppercase

        dict1 = {y:string.ascii_uppercase[y-10] for y in range(10,36)}

        dict2 = {36:'a', 37:'b', 38:'d', 39:'e', 40:'f', 41:'g', 42:'h', 43:'n', 44:'q', 45:'r', 46:'t'}

        tmp = {**dict0, **dict1}

        classToChar = {**tmp, **dict2}

        charToClass = {value: key for key,value in classToChar.items()}
        return classToChar, charToClass
def nested(l): 
        def capitalize(s):
            return s.capitalize()
        for n, i in enumerate(l):       
            if type(i) is list:
                l[n] = nested(l[n])
            elif type(i) is str:
                l[n] = capitalize(i)
        return l

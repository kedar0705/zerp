import json


def precedence(a: str = None, b: str = None, c: str = None):
    if a == b == c:
        res = []
        rank = 0
        for i in [a, b, c]:
            dict_ = {}
            rank += 1
            dict_['rank'] = rank
            dict_['value'] = i
            res.append(dict_)
        return res

    elif c is None:
        res = []
        rank = 0
        for i in [a, b]:
            dict_ = {}
            rank += 1
            dict_['rank'] = rank
            dict_['value'] = i
            res.append(dict_)
        return res

    elif b is None:
        if a == c:
            res = []
            rank = 0
            for i in [a, c]:
                dict_ = {}
                rank += 1
                dict_['rank'] = rank
                dict_['value'] = i
                res.append(dict_)
            return res


print(precedence('a', 'a'))

def get_indices_of_item_weights(weights, length, limit):
    # code will pass 3 of 4 tests
    # hash = {}
    # for x in range(length):
    #     print('weight',weights[x])
    #     if weights[x] in hash:
    #         if weights[x] * 2 == limit:
    #             return x, weights.index(weights[x])
    #     hash[weights[x]] = limit - weights[x]
    #     print('calc:', limit - weights[x])
    # for x in hash:
    #     weight = x
    #     limit = hash[x]
    #     print('weight:', weight, 'to limit:', limit)
    #     if limit in hash:
    #         if limit > weight:
    #             return (weights.index(weight), weights.index(limit))
    #         elif limit <= weight:
    #             return (weights.index(limit), weights.index(weight))
    #
    #         else:
    #             return None

    hash = {}
    for x in range(length):
        if weights[x] in hash:
            if limit-weights[x] in hash:
                print(hash[weights[x]], x)
                return x, hash[weights[x]]
        hash[weights[x]] = x
    for x in hash:
        weight = x
        to_limit = limit - weight
        if to_limit in hash:
            return hash[to_limit], hash[weight]
            # if to_limit > weight:
            #     print(hash[to_limit], hash[weight])
            #     return hash[to_limit], hash[weight]
            # if weight > to_limit:
            #     print(hash[weight], hash[to_limit])
            #     return hash[weight], hash[to_limit]
    return None

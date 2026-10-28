dict_tuff= {
    "Jeet": [ (1, 0), (1, 0) ],
    "Jeet 2": [ (1, 0 ), (1, 0 ), (1, 0) ]
}

for counter, items in enumerate(dict_tuff["Jeet"]):
    dict_tuff["Jeet"][counter] = (items[0] + 1, items[1])
print(dict_tuff["Jeet"])

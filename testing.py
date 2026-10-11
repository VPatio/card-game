big_blah = [1, 1, 1]
all_blahs = [1, 1]
if all( blah in big_blah for blah in all_blahs ):
    print("True")
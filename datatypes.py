string: str = 'hi'
# not the good way:
_t: tuple[int] = (1,2,3,4)
# better way:
_t: tuple[int, ...] = (1,2,3)
# also possible
_t: tuple[int or str , ...] = ('fg',1,"2")

print(_t)
print(_t[0] , "," , _t[1] , "," , _t[2])

wishlist : list[str]  = []
wishlist.append("jolo")
wishlist.append("phone")

print(wishlist)
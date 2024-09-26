currencies = ["US Dollar", "Euro", "Japanese Yen", "British Pound", "Australian Dollar", "Canadian Dollar", "Swiss Franc", "Chinese Yuan", "Indian Rupee", "Brazilian Real"]
print(currencies)
print("the 4th index is",currencies[3])
currencies[6] = "euro"
print(currencies)
del currencies[-2]
print(currencies)
print("the last index is",currencies[-1])
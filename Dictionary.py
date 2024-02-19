
def add_value():
    capitals = {"India:": "New Dilli"}
    print(capitals)
    capitals1 = {"Nepal:": "Kathmandu"}
    capitals2 = [("England:", "London")]
    capitals.update(Japan="Tokiyo")
    capitals.update(capitals1)
    capitals.update(capitals2)
    del capitals["Japan"]
    val = capitals.pop("Nepal:")
    val1= capitals.popitem()
    print(capitals)
    print(val)
    print(val1)


add_value()
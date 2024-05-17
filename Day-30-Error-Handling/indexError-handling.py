fruits = ["Apple", "Pear", "Orange"]
# 🚨 Do not change the code above

# TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except:
        print("Fruit pie")
    else:
        print(fruit + " pie")


# 🚨 Do not change the code below
make_pie(4)
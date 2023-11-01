def hello():
    print("Hello, user!")

def pack(arg1, arg2, arg3):
    packed_list = [arg1, arg2, arg3]
    return packed_list

# Function to describe lunch items
def eat_lunch(food_list):
    if not food_list:
        print("My lunchbox is empty!")
    else:
        print("First I eat " + food_list[0])
        for i in range(1, len(food_list)):
            print("Next I eat " + food_list[i])

hello()
# Testing the pack() function
packed_items = pack("sandwich", "chips", "apple")
print("Packed items:", packed_items)

# Testing the eat_lunch() function
lunch_items = ["sandwich", "chips", "apple"]
eat_lunch(lunch_items)

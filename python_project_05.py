#create a new random file

# import random

# subjects = [
#     "shakib khan",
#     "amir kahn",
#     "Jamat a amir Dc. Shofiqur rohman",
#     "Prime minister Modi",
#     "I'm very hungry",
#     "Mere Desh bohot jamela",
#     "Aotu Riskar diver of dhaka"
# ]

# actions = [
#     "launchues",
#     "celebrates",
#     "dance with",
#     "eats",
#     "decliars",
#     "orders",
#     "world war"
# ]

# place_ananounting = [
#     "at red fort",
#     "in Mumbai local trin",
#     "in ploate of somosa",
#     "inside parlamant",
#     "a gange chat",
#     "the part of trank",
#     "thing the advance nirbacon"
# ]
# while True:

#     subject = random.choice(subjects)
#     action = random.choice(actions)
#     place = random.choice(place_ananounting)

#     heading = f'BRACKING NEWS: {subject} {action} {place} '
#     print('\n ' + heading)

#     user_input = input('\n do you want annther headling (Yes/No)?: ').strip()
#     if user_input == 'no':
#         break

# print("\n Create the random number")



##computer python restaurant


menu = {
    "Pizza": 40,
    "Pastha": 50,
    "Burger": 70,
    "Salat": 30,
    "Coffee": 40
}

print(f'-----Welcome To Our Restaurant------')
print(f'Our Item Active:\n Pizza: TK40\n Pastha: 50TK\n Burger: 70TK\n Salat: 30TK\n Coffee: 40TK')

taotal_amount = 0

user_need_item01 = input("Enter the name of item you want order: ").capitalize()
if user_need_item01 in menu:
    taotal_amount += menu[user_need_item01]
    print("thanks the order") 
else:
    print(f'The item not available! Choice another item')


another_item = input("Do you need another item (Yes/No)?: ").capitalize()
if another_item == 'Yes':
    user_need_item02 = input("Enter your new item, do you want: ").capitalize()
    if user_need_item02 in menu:
        taotal_amount += menu[user_need_item02]
        print("thank for again the order") 
    else:
        print("Not available! please try agin")

 

print(f'Your Total Rastaurant Bill: {taotal_amount}')






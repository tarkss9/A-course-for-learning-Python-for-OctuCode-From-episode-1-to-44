# بسم الله

# الاكواد من سلسلة تعليم لغة  بايثون لقناه OctuCode

# اذا اردت فتح الكود علم على الكود بالماوس كامل واضغط ( / + Ctrl )

# هذا الملف من حلقة 1 حتى 44 لجميع الاكواد في السلسلة




# ضرب عددين

# name1=input ("please enter tow digits:\n")
# nam =int(name1[0])
# secont=int(name1[1])
# print(nam*secont)


# حساب طول وعرض الغرفة مع السعر

# str0=input ("please type length:\n")
# str1=input ("please type width:\n")
# str3=input ("how much for 1 meter?: \n")
#
# length= float(str0)
# width= float(str1)
# meter=float(str3)
#
# area= length*width
# meters= meter*area
#
# strr= str(area)
# strr2= str(meters)
#
# print("the total area is : " + strr)
# print("give the guy $ : " + strr2)



# حساب الساعات بالدقائق

# total_minutes = input ("please type the number of minutes: \n")
# int_minutes = int(total_minutes)
# hours = int_minutes // 60
# minutes = int_minutes % 60
# print("this course is: " + str(hours) + " hours, " + str(minutes) + " minutes long")

# حساب الساعات والدقائق بالثواني

# total_seconds = int(input("please type the number of seconds : \n"))
# hours = total_seconds // 3600
# minuts = ((total_seconds) - (hours*3600)) // 60
# seconds = total_seconds % 60
# print("total time is " +  str(hours) + " hours " + str(minuts) + " minuts " + str(seconds) + " seconds ")

# حساب الساعات والدقائق بالثواني مختصر بسطرين فقط

# seconds=int(input('Enter the number in seconds:\n'))
# print(f"the number is: {seconds//3600} hours and {(seconds%3600)//60} minutes and {(seconds%3600)%60} seconds")


# حساب العمر

# int_age= int(input("how old are you ?\n"))
# print(f"you were born in the year:{2024- int_age}")

# حساب العمر لاستخدام التطبيق

# print("welcome to my application")
# old=int(input("how old are you? \n"))
# if old >=12:
#     print("you are old enough")
# else:
#     print("you are not old enough")


# هل الرقم فوق الصفر ام انقص

# number=float(input("Enter a number:\n"))
# if number>0:
#     print("the number is positive")
# elif number<0:
#     print("the number is negative")
# else:
#     print("the number is zero")


# حساب علامات الطلاب

# print("Welcome to my application")
# student_ponkt = float(input("type your ponkt:\n"))
# if student_ponkt>=90:
#   print("Excellent")
# elif student_ponkt>=75:
#   print("Good")
# elif student_ponkt>=50:
#   print("Acceptable")
# else:
#   print("ايها الكسول")



# ادخل الرمز السري

# password = input("please enter your password: \n")
# correct_password ="abc"
# if password == correct_password:
#     print("Welcome to the app")
# else:
#     print("sorry you entered wrong password")



# ماذا كتبت

# typed = input("please type (yes), (no), or (maybe): \n")
# if typed == "yes":
#     print(f"You typed {typed}")
# elif typed == "no":
#     print(f"You typed {typed}")
# elif typed == "maybe":
#     print(f"You typed {typed}")
# else:
#   print(f"You typed {typed}, which is not an option \n please stick to the option above")




#  خمن الرقم

# guessed = int(input("please guess a number:\n"))
# correct_number = 7
# if guessed == correct_number:
#     print ("Correct!")
# else:
#   print (f"you guessed {guessed}, but the correct number is {correct_number}")



#اختار منطقة

# area = input ("chose an area: (cairo), (alexandria), or (tanta):\n")
# if area.lower() == "cairo":
#     print("yuo chose cairo")
# elif area.upper() =="TANTA":
#     print("tanta is nice!")
# elif area.lower() == "alexandria":
#     print("feels like summer!")
# else:
#     print(f"sorry, {area} is not on our list!")




# والباسورد الاسم اكتب

# name = input("please enter your name: ")
# password = input("please enter your password: ")
# if name .lower() =="ibrahim" and password == "hithere":
#     print("welcome back")
# else:
#    print("sorry wrong name or password!")





# age = int (input("please enter your age: "))
# license = input("please enter your license? type (yes) or (no): ")
# if age >= 18 and license.lower() == "yes":
#     print("you can drive!")
# elif age < 10 or license.lower() == "no":
#    print("sorry, you cannot drive!")
# else:
#    print(f"sorry,your entery of [ {license} ] is not understood")





# is_egyptian= input("are you egyption ? type 'yes' or 'no': ").lower()
# if is_egyptian == 'yes':
#     print("good, that's the first step")
#     is_18 = input("are you 18 ? type 'yes' or 'no': ").lower()
#     if is_18 == 'yes':
#         print("you can have and id")
#     else:
#         print("sorry, you have to be 18 or older \n please try again when you are 18")
#
# else:
#     print("sorry, an egyptian id is give only to egyptian")







# print("welcome to my island!")
# print("there are tow doors in front of you! a red door and a blue door")
# door=input("which door do you want to open?").lower()
#
# if door==("red"):
#     print("great! now you entered a room")
#     print("you found three boxes: white, black, green")
#     box = input("which box do you want to open?").lower()
#
#     if box == "white":
#         print("Oops! you opened a box filled with snakes")
#     elif box == "green":
#         print("congratulation! you found the treasure!")
#     elif box == "black":
#         print("Oops! you opened a box filled with spiders")
#     else:
#         print("invalid choice!")
#
# elif door == ("blue"):
#     print("Oops! you chose the crocodile door.")
#     print("game over!")
# else:
#    print("invalid choice!")





# import random
# my_random=random.randint(1,100)
# print(my_random)

# import random
# my_random=random.randint(-5,+5)
# print(my_random)







# import random
# pin_cod = random.randint(1000, 9999)
#
# user_input = int(input("enter a 4-digit pin code: "))
#
# if len(str(user_input)) !=4:
#     print("please enter 4 digit")
# elif user_input == pin_cod:
#     print("success! pin code matched")
# else:
#     print("failure! pin code not matched")
#     print(f"the computer generated this pin:{pin_cod}")




# import random
#
#
# random_number = random.random() * 100
# print(random_number)



# import random
# print("welcome to the virtual coin toss game")
# input("press enter to start....")
# random_number = random.randint(0, 1)
# if random_number == 0:
#     print("heads")
# else:
#     print("tails")





# import random
#
# print("welcome to the coin guessing game!\nchoose a method to toss the coin:")
#
# print("1. using random.random()")
# print("2. using random.randint()")
# choice = input("enter your choice (1 or 2):")
#
# if choice == "1":
#     random_random = random.random()
#     if random_random >= 0.5:
#         computer_choice = "heads"
#     else:
#         computer_choice = "tails"
# elif choice == "2":
#     if random.randint(0,1) == 0:
#         computer_choice = "heads"
#     else:
#         computer_choice = "tails"
# else:
#     print("invalid choice. please select either 1 or 2.")
#
# user_choice = input("enter your choice (heads or tails): ")
#
# if user_choice.lower() == choice.lower():
#     print("you win!")
# else:
#     print("you lose!")
#
# print(f"the computer choice is {choice}")




# frend = [ "omar", "abdullah","osama" ]
#
# print(f"the first frend on our list is {frend[0]} and the last frend on our list is {frend[-1]}")




# colors = []
# colors.append("red")
# colors.append("green")
# print(colors)



# colors = []
# fav_color = input("add the first color you like: ")
# colors.append(fav_color)
# choice = input ("do you want to add another colors? yes or no: ").lower()
# if choice == "yes":
#     fav_color = input("add the second color you like: ")
#     colors.append(fav_color)
#     print("the colors you like are: ")
#     print(colors)
# else:
#    print("the colors you like are:")
#    print(colors)





# library = []
# wishlist = []
#
# book_name = input("enter the name of a book you own: ")
# library.append(book_name)
#
# book_name = input("enter the name of another book you own (or press 'enter' to skip) : ")
# if book_name:
#     library.append(book_name)
# print("\nyour library: ", library)
#
#
# book_name = input("\nenter the name of a book you wish to have in the future: ")
# wishlist.append(book_name)
# book_name = input ("enter the name of another book you wish to have (or press 'enter' to skip): ")
# if book_name:
#     wishlist.append(book_name)
# print("\nyour library: ", wishlist)
#
# acquired_book = input("\nenter the name of a book from your wishlist that you've acquired (or press 'enter' to skip): ")
# if acquired_book in wishlist:
#     library.append(acquired_book)
#     wishlist.remove(acquired_book)
#
# print("\nupdated library: ", library)
# print("updated wishlist: ", wishlist)
#
# donated_book = input("\nenter the name of a book from your library you wish to donate (or press 'enter' to skip): ")
# if donated_book in library:
#     library.remove(donated_book)
#
# print("\nfinal library after donations: ", library)






# names_string = input("enter names separated by a comma...\n")
# names = names_string.split(", ")
# print(type(names))
# print(names)


# names = ["tarik", "osama", "hamam"]
# print(len(names))




# import random
# names_string = input("welcom to 'whose wallet?\nyou will give me a list of names, and i will pick a person to pay "
#       "\nif you're ready, enter the names separate by a comma: ")
# names = names_string.split(", ")
# length = len(names) -1
# random_number = random.randint(0,length)
# random_person = names[random_number]
# print(f"please ask ' {random_person} ' to take his wallet out. dinner is on him")




# import random
# print("welcom to 'whose wallet?\nyou will give me a list of names, and i will pick a person to pay")
# print(f"please ask { random.choice(input('enter the names seaparated by a comma: ').split(', '))}"
#       f"to take out his wallet . dinner is on him")




# basket = [ ["apples", "bananas"] , ["milk", "water"] ]
# print(basket[0][0], basket[1][0])



# books = ["book2", "book3", "book5"]
# books.insert(0, "book1")
# books.insert(3,"book4")
# print(books)





# basket = [ ["apples", "bananas"],["milk", "water"] ]
# print(basket)
# input("press enter to change the content....")
#
# basket[0].insert(0,"oranges")
# basket[0].append("kiwis")
# basket[1].remove("water")
# basket[1].insert(0, "coffee")
# basket[1].append("tea")
# basket.append([1,2,3,4])
# print(basket)
# print("here is the updated basket")






# print("welcom to place the rabbit")
# field = [  ["🌿", "🌿", "🌿"],["🌿", "🌿", "🌿"],["🌿", "🌿", "🌿"]  ]
#
# print(f"{field[0]} \n{field[1]} \n{field[2]}")
# print("\nwhere should the rabbit go? 🐇")
#
# position = (input("please chose a row and a column: "))
# row = int(position[0])
# column = int(position[1])
#
# field[row-1][column-1] = "🐇"
#
# print("\n success ....\n")
#
# print(f"{field[0]} \n{field[1]} \n{field[2]}")






# import random
#
# rock_ascii = "🤜"
# paper_ascii = "✋"
# scissors_ascii = "🤞"
#
# print("\nwelcom to the rock, paper, scissors game")
# confirm = input("press enter to continue or type (help) for the rules: ").lower()
#
# if confirm == "help":
#     print("""             ******RULES******
#     1) you choose and the computer chooses
#     2) rock smashes scissors -> rock wins
#     3) scissors cut paper -> scissors win
#     4) paper covers rock -> paper wins""")
#
# user_choice = input("enter your choice (rock, paper, scissors): ").lower()
# if user_choice not in ["rock", "paper", "scissors"]:
#     print("invalid choice. please run the program again")
# else:
#     if user_choice == "rock":
#         print(f"\nyou chose:\n{rock_ascii}")
#     elif user_choice == "paper":
#         print(f"\nyou chose:\n{paper_ascii}")
#     else:
#         print(f"\nyou chose:\n{scissors_ascii}")
#
#
#     computer_choice = random.choice(["rock", "paper", "scissors"])
#     if computer_choice == "rock":
#         print(f"\ncomputer chose:\n{rock_ascii}")
#     elif computer_choice == "paper":
#         print(f"\ncomputer chose:\n{paper_ascii}")
#     else:
#         print(f"\ncomputer chose:\n{scissors_ascii}")
#
#
#     if user_choice == computer_choice:
#         print("its a tie!")
#     elif (
#             (user_choice == "rock" and computer_choice == "scissors")
#         or
#             (user_choice == "paper" and computer_choice == "rock")
#         or
#             (user_choice == "scissors" and computer_choice == "paper")
#     ):
#         print(f"you win! {user_choice} beats {computer_choice}.")
#     else:
#         print(f"you lose! {computer_choice} beats {user_choice}.")

































































































# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combined_string= name1+name2
lower_combinedstring=combined_string.lower()

numberoflove=lower_combinedstring.count("l")+lower_combinedstring.count("o")+lower_combinedstring.count("v")+lower_combinedstring.count("e")
numberoftrue=lower_combinedstring.count("t")+lower_combinedstring.count("r")+lower_combinedstring.count("u")+lower_combinedstring.count("e")
lovescore=str(numberoflove)+str(numberoftrue)
newlovescore=int(lovescore)



if (newlovescore< 10) or (newlovescore> 90):
  print(f"Your score is {newlovescore}, you go together like coke and mentos.")
elif (newlovescore>=40) or (newlovescore<=50):
  print(f"Your score is {newlovescore}, you are alright together")
else:
  print(f"your score is-{newlovescore}")
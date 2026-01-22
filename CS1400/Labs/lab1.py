print('''Hi there, I am a friendly chatbot!
What is your name?''')
name = input() #function
count = len(name)
#len() <-- same as length() in Java
#always variable should belong the left side
#in python, if you want to space, must use under box (_)
print(f'''Welcome {name}, I think we are going to be great friends!
Did you know there are {count} characters in your name?''')
#using f str for using variable and sentences at the same line

#python -->
# , ! = 공백무시 X 공백포함 출력됨
# + ! = 공백무시 O 공백빼고 출력됨



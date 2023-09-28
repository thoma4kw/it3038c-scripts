import time
start_time = time.time()

time.time()
int(time.time())
start_time = time.time()
start_time
time.time() - start_time
int(time.time() - start_time)



print('What is your name?')
myName = input()
print('Hello, ' + myName+ '. That is a good name. How old are you?')

myAge = int(input())
print(myAge+'? That's funny, I'm only a few seconds old.')
print("I wish I was" + (myAge) * 2 + "years old") 

myAge = input()
programAge = int(time.time() - start_time)
print("%s? That's funny, I'm only %s seconds old." %  (myAge, programAge))
print("I wish I was %s years old" % (myAge * 2))

time.sleep(3)
print("I'm tired. I go sleep now.")




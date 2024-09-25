import string 
#password ="asshole"
password =input("enter yur pasword:")



#for i in password:
 # if i in  string.ascii_uppercase:
  #   upper_case=[1]

upper_case =any([1 if c in string.ascii_uppercase else 0 for c in password])
lower_case =any([1 if c in string.ascii_lowercase else 0 for c in password])
special=any([1 if c in string.punctuation else 0 for c in password])
digits =any([1 if c in string.digits else 0 for c in password])

#print(upper_case)
#print(lower_case)
#print(special)
#print(digits)

characters = [upper_case, lower_case, special, digits]

#print(characters)
#print(sum(characters))

length = len(password)

score =0 

with open('common.txt', 'r') as f:
	common = f.read().splitlines()
	
if password in common:
	print("password was found in common passowrd. choose another password")
	exit()

if length > 6:
    score+=1
if length > 8:
    score+=1
if length > 14:
    score+=2
    

if sum(characters) > 1:
  score+=1
if sum(characters) > 2:
  score+=2
if sum(characters) > 3:
  score+=3

 
 
if  score < 4 :
   print("your password is week")
elif score < 6 :
   print("you can increase your strength of your passowrd ")
elif score < 8 :
   print("your password is strong")
elif score >= 8:
   print("your passowrd in very strong")  
 
 
 
 
 
 
 
 
 
 
 
 
 
       
#print(score)

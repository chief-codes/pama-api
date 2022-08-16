import random 
import string

#For password to be accepted it must meet the following requirements:
    #Not be less than 12 characters
    #Must contain at least 1 number
    #Must contain both lower and uppercase letters
    #Must contain special characters or punctuation

lower = string.ascii_lowercase # saves lowercase alphabets to lower
upper = string.ascii_uppercase # saves uppercase alphabets to upper
numbers = string.digits # saves numbers to numbers
punctuation = string.punctuation

def password_generator():
            all = lower + upper + numbers + punctuation #.... combines lower, upper and numbers to form a list
            temp = random.sample(all, 16) # selects randomly 8 characters anf saves them as temp
            separator = ""
            Password = separator.join(temp) 
            print(Password)

def pass_val(password):
    l,u,n,p = 0,0,0,0
    password = input("Enter password: ")
    if len(password) >= 16:
        for char in password:
            if (char in lower):
                l+=1
                    
            if (char in upper):
                u+=1
                    
            if (char in numbers): 
               n+=1
                
            if (char in punctuation):
                p+=1
                
        if (l>=1 & u>=1 & n>=1 & p>=1):
            print("Password is VALID !!!!")
        elif l<1:
            print("Password must contain at least one lower case")
        elif u<1:
            print("Password must contain at least one upper case")
        elif n<1:
            print("Password must contain at least one number")
        elif p<1:
            print("Password must contain at least one punctuation")

    else:
        print("Password should be 16 or more characters!!!")
            
            
            
            
            
    



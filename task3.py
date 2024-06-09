import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
         'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','I','U','V','W','X','Y','Z']

numbers=['0','1','2','3','4','5','6','7','8','9']

symbols=['!','@','#','$','%','&','*','(',')','+']

print("*****WELCOME TO  GENERATE PASSWORD*****")

n_letters=int(input("enter how many letters you want in your password?:\n"))
n_numbers=int(input("enter how many numbers you want in your password?:\n"))
n_symbols=int(input("enter how many symbols you want in your password?:\n"))

password_list=(random.choices(letters,k=n_letters)+
               random.choices(numbers,k=n_numbers)+
               random.choices(symbols,k=n_symbols))

random.shuffle(password_list)

password="".join(password_list) 
print("Generated Password:",password)
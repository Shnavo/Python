# The assignment is:
# Create a password strength checker that evaluates a given password based on the following criteria:
# 1. Length (at least 8 characters),
# 2. Contains at least:
#     -one uppercase letter,
#     -one lowercase letter,
#     -one digit,
#     -one special character
# Display a message about the strenth of the password (e.g., "Weak", "Medium", "Strong").
# 2 różne rozwiązania:
#   1. Strong = wszystkie (5) założenia spełnione, Medium = 3 założenia spełnione, Weak = 1 założenie spełnione
#   2. Założenia to bare minimum, siła jest sprawdzana w inny sposób (????????????)

# region ROZWIĄZANIE 1

# password = "Test123!" # input("Type in your password to check it's strength: ")
# digits = (tuple(range(10)))
# # up_letters = ('A', 'B', 'C') # one way to create a tuple
# # low_letters = tuple(['a', 'b', 'c']) # 2nd way to create a tuple
# low_letters = tuple(chr(l) for l in range(ord('a'), ord('z') + 1))
# up_letters = tuple(chr(u) for u in range(ord("A"), ord("Z") + 1))
# special_char = ('!', '@', '#', '$')

#region STUPID
# reqs = 0
# # print(digits)
# # print(up_letters)
# if len(password) > 7:
#     reqs += 1

# for letter in password:
#     if letter in low_letters:
#         reqs += 1
#         break

# for letter in password:
#     if letter in up_letters:
#         reqs += 1
#         break

# for number in password:
#     if number in up_letters:
#         continue
#     elif number in low_letters:
#         continue
#     elif number in special_char:
#         continue
#     elif int(number) in digits:
#         reqs += 1
#         break

# for symbol in password:
#     if symbol in special_char:
#         reqs += 1
#         break

# if reqs >= 5:
#     print("Your password is strong")
# elif reqs < 5 and reqs > 2:
#     print("Your password is of medium strength")
# else:
#     print("Your password is weak")
#endregion

def password_length_checker(password):
    pass

def main():
    test = False
    password = input("Type in your password to check it's strength. "
                    + "Your password should fulfill the below requirements:\n"
                    + "The password should be 8 characters long and "
                    + "it should contain at least:\n"
                    + "   - one uppercase letter,\n"
                    + "   - one lowercase letter,\n"
                    + "   - one digit,\n"
                    + "   - one special character: \n")
    while not test:
        password = input("Password to short message")
    print(password)



main()




















# reqs = []
# sum_of_reqs = 0
# print(up_letters)

# if len(password) > 8:
#     reqs.append(0)

# for symbol in password:
#     if symbol in digits:
#         reqs.append(1)
#     elif symbol in up_letters:
#         reqs.append(2)
#     elif symbol in low_letters:
#         reqs.append(3)
#     elif symbol in special_char:
#         reqs.append(4)

# if reqs.count(0) > 0:
#     sum_of_reqs + 1
# if reqs.count(1) > 0:
#     sum_of_reqs + 1
# if reqs.count(2) > 0:
#     sum_of_reqs + 1
# if reqs.count(3) > 0:
#     sum_of_reqs + 1
# if reqs.count(4) > 0:
#     sum_of_reqs + 1


# if sum_of_reqs == 5:
#     print("Your password is strong")
# elif sum_of_reqs < 5 and sum_of_reqs > 2:
#     print("Your password is of medium strength")
# else:
#     print("Your password is weak")

# reqs.sort
# reqs.count
# print(reqs.index(2))



#endregion

# region ROZWIĄZANIE 2



#endregion
samp = [
    {"name" : "Shazil", "age" : 22},
    {"name" : "Moiz", "age" : 23},
    {"name" : "Ali", "age" : 24}
]

print(samp[0]["name"])

friends = {"name": "Shazil", "Age": 22}
friends1 = ["Shazil","Moiz","Ali"]
print(friends.items())
print(friends.values())
starts_with_s = [friend for friend in friends if friend.startswith("S")]

print(friends)
print(starts_with_s)
print(friends is starts_with_s)
x = 5
def say_name(m,n=x):
    sum = m + n
    print(sum)
say_name(5)


def my_function():
    print('Bob')


result = my_function()


print ((lambda x,y : x+y)(5,7))


def double(x):
    return x * 2

sequence = [1,3,5,9]
doubled = [double(x) for x in sequence]
doubled = map(double,sequence)


users = [
    (0, "Shazil", "password"),
    (1, "Rolf", "bob123"),
    (2, "Jose", "jose123"),
    (3, "username", "1234")
]

# Create a dictionary using usernames as keys
username_mapping = {user[1]: (user[0], user[2]) for user in users}

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

if username_input in username_mapping:
    user_id, stored_password = username_mapping[username_input]


    if password_input == stored_password:
        print("Your details are correct.")
    else:
        print("Your password is incorrect.")
else:
    print("Username not found.")

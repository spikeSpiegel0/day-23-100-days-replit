print("REPLIT LOGIN SYSTEM")
print()
def logIn():
  while True:
    username = input("\033[36mWhat is your username: \033[0m")
    password = input("\033[36mWhat is your password: \033[0m")
    print()
    if username == "bojo" and password == "sex1234":
      print("Welcome to REPLIT")
      break
      print()
    else:
      print("Username or password incorrect, please try again!")
      print()
      continue


logIn()
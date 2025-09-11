import os
import sys

print(os.name) 
print(os.getuid())


user = dict(os.environ)["USER"]
charset = dict(os.environ)["LANG"]

print(f" {user} är den inloggade användaren och de använda charsetet är : {charset}") 

arguemnts = sys.argv 
scriptname = sys.argv[0]

print("sysargv:", sys.argv) 

if len(sys.argv) > 1:
    first_argument = sys.arg[1]
    print(f"first argument:{first_argument}")
else:
    first_argument = None 


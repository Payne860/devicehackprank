print("-------------------")
print("DeviceHack 0.1 launched")
print("-------------------")
import time
import dvhackfunctions
time.sleep(0.5)
username = input("Enter username to log in: ")
print("Username:", username)
time.sleep(1)
password = input("Enter your password: ")   
if username == "oMy" and password == "scrtmnu":
    dvhackfunctions.scrtmnufunc()
else:
    time.sleep(0.3)
print("Succesfully logged in to the account", username)
time.sleep(0.3)
print("Entering operating system...")
time.sleep(0.5)
print("Entered...")
time.sleep(0.3)
print("Injecting DeviceHack...")
time.sleep(1.5)
print("Process failed.")
time.sleep(0.2)
print("Attempt secondary route?")
time.sleep(0.3)
print("Username:", username)
passwordcrack = input("Enter password to continue: ")
if passwordcrack == password:
    print("Attempting secondary route...")
    time.sleep(1)
    print("Entering internal software...")
    time.sleep(1)
    print("Success!")
    time.sleep(0.3)
    print("Brute forcing into device...")
    time.sleep(0.7)
    print("Success!")
    time.sleep(0.5)
    print("You can now minimize this window.")
    print("-----------------------------------")
    print("Thank you for using DeviceHack!")
    print("-----------------------------------")
else:
    print("-----------------------------------")
    print("DeviceHack has crashed!")
    print("Incorrect password")
    print("Please relaunch")
    print("-----------------------------------")
    exit()
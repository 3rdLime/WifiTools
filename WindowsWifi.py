import subprocess

print()
print("Grabbing the list of WiFi passwords from your Windows device.")
print()
print("Starting with the profiles...")
print()
#Grab profiles
netshCmd = "netsh wlan show profiles"
netshCmdOutput = subprocess.check_output(netshCmd).decode('utf-8')
profileNames = [line.split(":")[1].strip() for line in netshCmdOutput.split("\n") if "All User Profile" in line]

print("Grabbing the password for each of the profiles.")
print()

#Retrieve password for the profile
for profileName in profileNames:
    #Run the netsh command to get the profile key
    passwordCmd = ['netsh', 'wlan', 'show', 'profile', 'name=' + profileName, 'key=clear']
    passwordOutput = subprocess.check_output(passwordCmd).decode('utf-8')
    
    keyOutput = [line.split(":")[1].strip() for line in passwordOutput.split("\n") if "Key Content" in line]

    #print(keyOutput)    
    if keyOutput:
        print(f"WiFi Proflie: {profileName}")
        print(f"Password: {keyOutput[0]}")
        print()

    else:
        print(f"WiFi Profile: {profileName}")
        print("Password: N/A")
        print()
    
    

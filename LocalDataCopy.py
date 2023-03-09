# Local Profile Data Copy - version 1.0 - J Bancroft
# This Code copies key local user profile data from an old laptop to a new laptop via the network (without additional manual intervention).
# Only key user data is copied to the exclusion of non-useful files (for example, app data / temp fles / pst files)

import subprocess
import webbrowser
import time
import os

clear = lambda: os.system('cls')

print("""
--------------------------------------------------------
Local Profile Data Copy - Version 1.0
--------------------------------------------------------

This program will copy the following local user profile data from one device to another via the Network:
Desktop, Documents, Internet Favourites, Media, Downloads and Chrome User Data.

For best results, please ensure both devices are connected via LAN cable.

----------------------------------------
Step 1 - Enter User & Device Details
----------------------------------------
""")

# Variables

username = input("Enter the AD Username: ")
src_asset = input("Asset Tag of the Source device: ")
dst_asset = input("Asset Tag of the Destination device: ")
path1 = "\\\\" + src_asset + "\\c$\\"
path2 = "\\\\" + dst_asset + "\\c$\\"

# Collated Queries - this code defines the source and destination network UNC paths, specific to the user level.

colquery1 = "xcopy \\\\" + src_asset + "\\c$\\users\\" + username + "\\Desktop" + " \\\\" + dst_asset + "\\c$\\users\\" + username + "\\Desktop" + "\ /h/c/k/e/r/y"
colquery2 = "xcopy \\\\" + src_asset + "\\c$\\users\\" + username + "\\Documents" + " \\\\" + dst_asset + "\\c$\\users\\" + username + "\\Documents" + "\ /h/c/k/e/r/y"
colquery3 = "xcopy \\\\" + src_asset + "\\c$\\users\\" + username + "\\Downloads" + " \\\\" + dst_asset + "\\c$\\users\\" + username + "\\Downloads" + "\ /h/c/k/e/r/y"
colquery4 = "xcopy \\\\" + src_asset + "\\c$\\users\\" + username + "\\Favorites" + " \\\\" + dst_asset + "\\c$\\users\\" + username + "\\Favorites" + "\ /h/c/k/e/r/y"
colquery5 = "xcopy \\\\" + src_asset + "\\c$\\users\\" + username + "\\Music" + " \\\\" + dst_asset + "\\c$\\users\\" + username + "\\Music" + "\ /h/c/k/e/r/y"
colquery6 = "xcopy \\\\" + src_asset + "\\c$\\users\\" + username + "\\Videos" + " \\\\" + dst_asset + "\\c$\\users\\" + username + "\\Videos" + "\ /h/c/k/e/r/y"
colquery7 = 'xcopy "\\\\' + src_asset + '\\c$\\users\\' + username + '\\AppData\\Local\\Google\\Chrome\\User Data\\Default"' + ' "\\\\' + dst_asset + '\\c$\\users\\' + username + '\\AppData\\Local\\Google\\Chrome\\User Data\\Default"' + ' /h/i/c/k/r/y'

clear()

# Authentication layer. This code can be run from either the source or destination device.
# It can even be executed on a tertiary device, however, this requires both layers of authentication.

print("""
----------------------------------------
Step 2 - Connecting to Source Device....
----------------------------------------

An Explorer window will open - close this manually.

Please authenticate access to source filesystem with your Admin credentials if necessary. 

""")
webbrowser.open('file:///' + path1)

os.system('pause')

print("""
---------------------------------------------
Step 3 - Connecting to Destination Device....
---------------------------------------------

An Explorer window will open - close this manually.

Authenticate access to destination filesystem with your Admin credentials if necessary. 
 
""")
webbrowser.open('file:///' + path2)

os.system('pause')

clear()

### Authentication layer complete, the file transfer process can now run.

print("""
-----------------------------------------
Step 4 - Network File Transfer
-----------------------------------------

Preparing files for transfer.....


Note: If the program quits unexpectedly, please ensure that your 
account is authenticated on both devices and restart the application

""")

time.sleep(5)

print("""

-----------------------------------------
Stage 1 of 7 - Copying Desktop
-----------------------------------------

""")
subprocess.call(colquery1)
print("""

-----------------------------------------
Stage 2 of 7 - Copying Documents
-----------------------------------------

""")
subprocess.call(colquery2)
print("""

-----------------------------------------
Stage 3 of 7 - Copying Downloads
-----------------------------------------

""")
subprocess.call(colquery3)
print("""

-----------------------------------------
Stage 4 of 7 - Copying Favorites
-----------------------------------------

""")
subprocess.call(colquery4)
print("""

-----------------------------------------
Stage 5 of 7 - Copying Music
-----------------------------------------

""")
subprocess.call(colquery5)
print("""

-----------------------------------------
Stage 6 of 7 - Copying Videos
-----------------------------------------

""")
subprocess.call(colquery6)
print("""

-----------------------------------------
Stage 7 of 7 - Copying Chrome Data
-----------------------------------------

""")
subprocess.call(colquery7)
print(colquery7)

print("""

-----------------------------------------

Process Finished. 

""")

os.system('pause')
exit()
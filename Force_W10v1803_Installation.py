import subprocess
import os

_func = True
_undef = True
_sitedp = ""
_rcopy = ""

print("""
--------------------------------------------------------
                Windows 1803 Upgrade 
--------------------------------------------------------

Script written by J Bancroft (2020)

This program will force a manual install of the Windows 10 1803 OS Feature Update from the closest geographical SCCM distribution point.
Estimated time for completion over VPN connection is 2-4 hours, depending on bandwidth.

[Servernames redacted : to use this script, please update %SERVERNAME% and make sure content exists]

-------------------------------------------------------
                  Select Location               
--------------------------------------------------------""")

while _undef:
    _usrselect = input("""
Please enter 2 letter country code of SCCM Distribution server (ie. UK, DE, CH etc.): """).upper()
    if _usrselect == "USA":
        _sitedp = "%SERVERNAME%"
        print("You have selected the site 'USA'")
        _undef = False
    elif _usrselect == "DE":
        _sitedp = "%SERVERNAME%"
        print("You have selected the site 'Germany'")
        _undef = False
    elif _usrselect == "UK":
        _sitedp = "%SERVERNAME%"
        print("You have selected the site 'United Kingdom'")
        _undef = False
    elif _usrselect == "BE":
        _sitedp = "%SERVERNAME%"
        print("You have selected the site 'Belgium'")
        _undef = False
    elif _usrselect == "AT":
        _sitedp = "%SERVERNAME%"
        print("You have selected the site 'Austria'")
        _undef = False
    elif _usrselect == "NL":
        _sitedp = "%SERVERNAME%"
        print("You have selected the site 'Netherlands'")
        _undef = False
    elif _usrselect == "ES":
        _sitedp = "%SERVERNAME%"
        print("You have selected the site 'Spain'")
        _undef = False
    elif _usrselect == "GR":
        _sitedp = "%SERVERNAME%"
        print("You have selected the site 'Greece'")
        _undef = False
    elif _usrselect == "FR":
        _sitedp = "%SERVERNAME%"
        print("You have selected the site 'France'")
        _undef = False
    elif _usrselect == "ZA":
        _sitedp = "%SERVERNAME%"
        print("You have selected the site 'South Africa'")
        _undef = False
    elif _usrselect == "UA":
        _sitedp = "%SERVERNAME%"
        print("You have selected the site 'Ukraine'")
        _undef = False
    elif _usrselect == "DK":
        _sitedp = "%SERVERNAME%"
        print("You have selected the site 'Denmark'")
        _undef = False
    elif _usrselect == "IT":
        _sitedp = "%SERVERNAME%"
        print("You have selected the site 'Italy'")
        _undef = False
    else:
        print("Site code not recognised")

print("""
--------------------------------------------------------
                  Select Option              
--------------------------------------------------------

    [1] Pre-copy install source files from network to local disk > Install locally after data copy is complete
    [2] Install directly from network
    [3] Check Windows Version""")

while _func:
    _dplocation = '\\\\' + _sitedp + '\\Content\\Microsoft\\Windows 10 x64 1803 Source'
    try:
        _select = int(input("""
        Please enter option [1, 2, 3]: """))

        if _select == 1:
            _func = False
            print("Copying files to local machine")
            _rcopy = 'robocopy.exe ' + '"' + _dplocation + '" ' + 'C:\\TEMP\\Windows10_1803' + ' /E /R:3 /W:15'
            subprocess.call(_rcopy)
            _cmdquery = 'start /w "" "' + "C:\\TEMP\\Windows10_1803\\setup.exe" + '" /auto upgrade /quiet'
            os.system('cmd /k ' + '"' + _cmdquery + '"')
            print("Complete...")
        elif _select == 2:
            _func = False
            print("Installing from Network...")
            _cmdquery = 'start /w "" "' + _dplocation + "\\setup.exe" + '" /auto upgrade /quiet /noreboot'
            os.system('cmd /k ' + '"' + _cmdquery + '"')
            print("Complete...")
        elif _select == 3:
            subprocess.call("winver")
        else:
            print("Choice not recognised, please enter 1, 2 or 3")
    except ValueError:
        print('You entered a non integer value, try again.')
        continue
exit()
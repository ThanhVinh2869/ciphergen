# Description
CipherGen is a command-line interface based program written in Python to generate random passwords. Users can customize what type of characters (uppercase, lowercase, numbers, special characters) will be included in the generated passwords. The program allows users to keep regenerating as many passwords as they want with the same settings until they exit the generator or the program is interrupted.

# Author
Vincent - Vinh Thanh Nguyen

### My Socials
[Github](https://github.com/ThanhVinh2869)  
[LinkedIn](www.linkedin.com/in/vincent2869)  
Discord: vincentng0708

# Features
## Starting the generator
When running the program, a list of available commands will be displayed in the terminal:
```
  ..|'''.|  ||           '||                       ..|'''.|
.|'     '  ...  ... ...   || ..     ....  ... ..  .|'     '    ....  .. ...   
||          ||   ||'  ||  ||' ||  .|...||  ||' '' ||    .... .|...||  ||  ||  
'|.      .  ||   ||    |  ||  ||  ||       ||     '|.    ||  ||       ||  ||  
 ''|....'  .||.  ||...'  .||. ||.  '|...' .||.     ''|...'|   '|...' .||. ||. 
                 ||
                ''''
CUSTOMIZATION
-------------------------------------
.length [int] -> Set password length
.enable/disable [upper/lower/number/special] -> Enable/disable the corresponding type of character
.number [int] -> Set the minimum amount of numbers
.special [int] -> Set the minimum amount of special characters

UTILITY
-------------------------------------
.settings -> See current settings
.reset -> Reset settings to default
.generate -> Generate a random password with current settings
.help -> Display available commands
.exit -> Exit application
```
This list can be displayed again by entering `.help` in the terminal. The generator will keep accepting commands until the user exits the generator using `.exit` or raises `KeyboardInterrupt` with `Ctrl + C`.
## Shorten Commands
In CipherGen, most of the time you don't have to type out the whole command syntax and its argument, the generator will accept a `.` syntax plus the first 3 letters. For example:
- `.settings` -> `.set`
- `.length 20` -> `.len 20`
- `.enable uppercase` -> `.ena upp`
- `.disable lowercase` -> `.dis low`
## Change Password Length
To set password length, input `.length [n]` in the terminal after running the generator with `[n]` being a number from 5 to 128.  
```
$ .length 13
Password length set to 13
```
The generator will raise an error and display a warning message if:

- There is no `[n]` provided
```
$ .length
Missing 1 additional argument
```
- `[n]` is not an integer
```
$ .length hello
Password length must be an integer
```
- `[n]` is not in the range 5 to 128
```
$ .length 130
Password length must be from 5 to 128
```
- `[n]` is lower than minimum values (minimum amount of numbers + minimum amount of numbers + 3)
```
$ .length 20
Password length set to 20

$ .number 4
Minimum amount of numbers is set to 4

$ .special 5
Minimum amount of special characters is set to 5

$ .length 5
Minimum values exceed input length (12)
```
## Enable/Disable Character Types
CipherGen allows users to generate passwords using 4 different types of ASCII characters, all of which can be enabled/disabled:
- Uppercase alphabetic characters: ABCDEFGHIJKLMNOPQRSTUVWXYZ
- Lowercase alphabetic characters: abcdefghijklmnopqrstuvwxyz
- Numbers: 0123456789
- Special characters: !"#$%&'()*+,-./:;<=>?@[\]^_\`{|}~

To enable/disable a character type, enter `.enable` or `.disable` and follow up with either `uppercase`, `lowercase`, `number`, or `special`.  
No action will be executed if the user only enters `.enable` or `.disable` without providing a valid character type.  
```
$ .enable
Missing 1 additional valid argument

$ .enable upper
Enabled uppercase characters

$ .enable lower
Enabled lowercase characters

$ .enable number
Enabled numbers

$ .enable special
Enabled special characters
```
```
$ .disable 
Missing 1 additional valid argument

$ .disable upper
Disabled uppercase characters

$ .disable lower 
Disabled lowercase characters

$ .disable number
Disabled numbers
```
However, if you decide to disable all character types, the program will raise an error
```
$ .disable special
Cannot set all attributes to False
```
## Set Minimum Amount of Numbers and Special Characters
If enabled, numbers and special characters have to appear in the generated password for a certain amount of time. That amount can be set using `.number [n]` and `.special [n]` respectively. If that type of character is disabled via `.disable`, you cannot set the minimum for that type.  
```
$ .number 3
Minimum amount of numbers is set to 3
```
The generator will raise an error and display a warning message if:
- There is no `[n]` provided:
```
$ .number
Missing 1 additional argument

$ .special
Missing 1 additional argument
```
- That type of character is disabled with `.disable`
```
$ .disable number 
Disabled numbers

$ .disable special
Disabled special characters

$ .number 7
Numbers are disabled

$ .special 5
Special characters are disabled
```
- `[n]` is not an integer
```
$ .number hello
Minimum value must be an integer

$ .special world
Minimum value must be an integer
```
- `[n]` is out of range 1 to 9
```
$ .number 10
Minimum value must be from 1 to 9
```
After setting minimum values using `.number` or `.special`, if the minimum values (minimum amount of numbers + minimum amount of numbers + 3) are greater than the password length, the program will automatically adjust the password length and display a message
```
$ .length 6
Password length set to 6

$ .number 4
Minimum amount of numbers is set to 4

$ .special 9
Minimum amount of special characters is set to 9
Current minimum values exceed password length. New length is set to 16
```
## Display Current Settings and Restore Default Settings
Enter `.settings` in the terminal will display a summary of all the current settings.  
If numbers or special characters are disabled, the minimum value of that type of character will not be displayed.  
```
CURRENT SETTINGS
-------------------------------------
Password length: 20
Include uppercase (A-Z): True
Include lowercase (a-z): True
Include numbers (0-9): False
Include special: True
Minimum special: 9
```
To reset all attributes to default, `.reset` will prompt the user to confirm the action, `y` to reset and `n` to cancel. The default values are:
- All character types are enabled
- Password length is 5
- Minimum amounts of numbers and special characters are 1
## Generate Password
Users can enter `.generate [n]` and repeat as much as they want to generate new passwords based on current settings.  
The amount of passwords generated by each command is determined by `[n]` in the range of 1 to 10.  
If `[n]` is not provided, only 1 password is generated. The generator will raise error if `[n]` is not an integer.  
```
$ .len 20
Password length set to 20

$ .gen
g!o@l0('Q!(9L^@_4E7U

$ .gen 5
,zM_!Mt9h'@yB_(VrI>0
N>w#fy%=DLl4wK(F3K;X
#?I5v:^6KUW:+!8V6?|x
Br*2DA_f%N1s0C?^m@UZ
oaSWV:%65$&fvre6ImfU

$ .gen 20
Can only generate 1 to 10 passwords at once

$ .gen five
Argument must be an integer
```

# After the Project
This simple password generator was my submission for the Harvard CS50P 2024 Final Project and also the very first coding project that I worked on. It took me a bit over a week to complete and finalize. It is not the best but not the worst amount of time that I possibly need to finish this project. But overall I'm happy about how CipherGen turns out.

# Inspiration
- My main text message app is Discord and I absolutely love using `Discord bots`. I like the type of interaction between the user and the bot, in which the user can type a specific command syntax that will trigger an action from the bot, which later on I found out is called `command-line interaction (CLI)`.  
- Unlike some basic password generators that manually prompt users to enter their inputs and then based on those inputs to generate a password, I tried to replicate that same interaction with Discord bots in VS Code using `Python`, where unless the user enters a command with a valid input, no action will be executed.  
- This slightly levels up the complexity of `CipherGen` which I think makes it a great challenge for me to explore the process of working on a project.

# What have I learned from this Project?
## Libraries
- I use some basic libraries like `string` or `random` in my code, which I found that every basic password generator uses. What I found useful was the use of `pytest` to test my functions in a more efficient and organized way rather than just manually typing every test case in the terminal like I used to do.
- I also learned how to test a function that takes user input from the terminal using `monkeypatch`:
```
from io import StringIO
from file import module
def test_module(monkeypatch):
	monkeypatch.setattr('sys.stdin', StringIO('input')):
	assert module() == 'expected result'
```
- Even though I still don't fully understand what some syntax in the code above does, I'm happy that I know how to implement test cases for functions that require input.

## Separate Code into multiple Modules
- By separating my code into different modules and functions, I can easily manage and change some parts of the code without scrolling back and forth to make the same change.
- For example, in some functions, I wanted to check whether the user's input consisted of 2 parts: command syntax and input value. Instead of `ctrl + C` `ctrl + V` the same lines of code for every function, I can just create another function to do the job and execute that function whenever I need _(I learned this the hard way)_.

## Classes
- Classes took me the longest time to understand, in this project I practiced using `Getter & Setter` for my attributes. I got really confused about `decorators` and naming `Getter & Setter` and attributes, but in the end, I had a hang of it.
- This helped me modify and restrict values that are valid to set to attributes.

## Exception Handling
- I learned how to correctly identify error types and display the corresponding error message.
- I predicted some bugs that users might encounter while using the generator and adjusted my code to fix them.

# Will I do anything further with CipherGen?
- No. Not really. `CipherGen` is a basic password generator that does not stand out from the rest of online generators. This project is purely for education.
- However, I might turn this project into a `Discord bot` when I learn how to work with API. `CipherGen` will act as a baseline knowledge for my future projects.

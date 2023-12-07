# Command line arguments in python: 

Command-line arguments in Python are the inputs provided to a Python script when it's executed in the command line or terminal. When you run a Python script from the command line, you can pass additional information or parameters to the script.

### Python provides access to these command-line arguments through the `sys.argv` list in the `sys` module. Here's a breakdown of `sys.argv` :

--> `sys.argv[0]` contains the name of the Python script being executed.
--> `sys.argv[1]` `sys.argv[2]`, and so on contain the additional command-line arguments provided when running the script.

### See the code in this repo to understand in better way.

## Environment variables in Python. 

Environment variables in Python are like sticky notes that hold important information your program might need. They're tiny bits of data your computer keeps handy for any program running on it. These bits can be things like where to find specific files, settings for how a program should behave, or even secret codes like passwords.

Python provides access to environment variables through the `os` module's `os.environ` dictionary. This dictionary contains the current environment variables, where the keys are variable names, and the values are their corresponding values.

In the env.py code you need to export the variable. In this case we are exporting password variable.
`export password="1223344"`
Type it inside your terminal.

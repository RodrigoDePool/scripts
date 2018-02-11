## Script collection
The scripts on this folder are prepared to be executed from Unix. To use a script
just make it an executable using the command: `chmod +x "script_name"`

All the scripts in this collection are written in python therefore the python 
interpreter is necessary to execute them.

---
### Clone
This command aims to replace the traditional `git clone`.

- Given one argument it works exactly the same as git clone.
- Given two arguments ( "usr\_of\_owner", "repository_name" ) it calls:  
`git clone https://github.com/usr_of_owner/repository_name.git` 
- In any other case, it does nothing.

---
### Automake
This command aims to automate the command `make` while compiling little projects.

When used, this script will execute `make` everytime there is a change in the
current directory. Allowing the user to receive feedback immediately when
modifying the code. To end the script just use ctrl+c.

---
### mdtopdf
An alias for _pandoc -s -o_ (converts markdown into pdf).  
Requires pandoc and texlive-full packages

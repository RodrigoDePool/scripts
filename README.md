## Script collection
The scripts on this folder are prepared to be executed from Unix. To use a script
just make it an executable using the command: `chmod +x "script name"`

All the scripts in this collection are written in python therefore you will need
the python interpreter to execute them.

---
### Clone
This command aims to replace the traditional `git clone`.

-Given one argument it works exactly the same as git clone.
-Given two arguments ("usr\_of\_owner","repository_name") it calls
`git clone https://github.com/usr_of_owner/repository_name.git` 

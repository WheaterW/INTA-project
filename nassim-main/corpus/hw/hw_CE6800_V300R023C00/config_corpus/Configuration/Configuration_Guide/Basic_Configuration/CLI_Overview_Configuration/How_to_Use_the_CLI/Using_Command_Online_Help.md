Using Command Online Help
=========================

You can use command online help to obtain real-time assistance, avoiding the need to memorize a large number of complex commands.

When entering commands, you can enter a question mark (?) at any time to obtain online help. You can choose to obtain either full or partial help.

#### Full Help

When entering a command, you can use the full help function to obtain all the keywords and parameters of the command. Use any of the following methods to obtain full help for commands.

* Enter a question mark (?) in any command view to obtain all the commands and their simple descriptions in this command view. For example:
  ```
  <HUAWEI> ?
  Current view commands:
    activate        Activate locked user
    cd              Change current directory
    clear           Clear operation
    clock           Clock status and configuration information
    copy            Copy from one file to another
  ...
  ```
* Enter some keywords of a command and a question mark (?) separated by a space to display all the keywords associated with this command, as well as simple descriptions. For example:
  ```
  <HUAWEI> system-view
  [~HUAWEI] user-interface vty 0 4
  [~HUAWEI-ui-vty0-4] authentication-mode ?
    aaa       AAA authentication
    password  Authentication through the password of a user terminal interface
  ```
  
  In the preceding command output, the description of the **aaa** keyword is **AAA authentication**, and the description of the **password** is **Authentication through the password of a user terminal interface**.
* Enter some keywords of a command and a question mark (?) separated by a space to display all the parameters associated with this keyword, as well as simple descriptions. For example:
  ```
  <HUAWEI> system-view
  [~HUAWEI] ssh server timeout ?
    INTEGER<1-35791>  Set the authentication timeout, the default value is 60 seconds 
  [~HUAWEI] ssh server timeout 35 ?
   <cr>
  [~HUAWEI] ssh server timeout 35
  ```
  
  **INTEGER<1-35791>** describes the value range of the parameter. **Set the authentication timeout, the default value is 60** briefly describes the function of this parameter. **<cr>** indicates that there is no keyword or parameter in this position. You can press **Enter** to run this command.

#### Partial Help

If you enter one or more of the first few characters of a command keyword, partial help provides all the keywords that begin with this character or character string. Use any of the following methods to obtain partial help for commands.

* Enter a character string followed directly by a question mark (?) to display all keywords that begin with this character string. For example:
  ```
  <HUAWEI> d?
    debugging                               delete
    dir                                     display
  <HUAWEI> d
  ```
* Enter a command and a string followed directly by a question mark (?) to display all the keywords that begin with this character string. For example:
  ```
  <HUAWEI> display s?
    sysname                                     system  
  ```
* Enter the first several letters of a keyword in a command and press **Tab** to display a complete keyword. However, the first several letters must uniquely identify the keyword. Otherwise, keep pressing **Tab** to display different keywords and select the required one.

![](public_sys-resources/note_3.0-en-us.png) 

The command output obtained through the online help function is used for reference only.
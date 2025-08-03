help (SFTP client view)
=======================

help (SFTP client view)

Function
--------



The **help** command displays the format of all the commands in the SFTP client view.




Format
------

**help** [ *command-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *command-name* | Displays the format of the specified command in the SFTP client view. | The value is a string of 1 to 255 characters. |



Views
-----

SFTP client view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

You can use this command to get the help information and format of the specified command in the SFTP client view.You can use help or ? to get the help information of **SFTP** commands.


Example
-------

# Display the format of get command.
```
<HUAWEI> system-view
[~HUAWEI] sftp 10.1.1.1
Trying 10.1.1.1 ...
Press CTRL+K to abort
Connected to 10.1.1.1 ...
Please input the username:client001
Enter password:
sftp-client> help get
get Remote file name STRING<1-128> [Local file name STRING<1-128>]     Download file.    
Default local file name is the same with remote file.

```

# Display all the commands in the SFTP client view.
```
<HUAWEI> system-view
[~HUAWEI] sftp 10.1.1.1
Trying 10.1.1.1 ...
Press CTRL+K to abort
Connected to 10.1.1.1 ...
Please input the username:client001
Enter password:
sftp-client> help
cd 
cdup 
dir 
get 
help/? 
ls 
mkdir 
put 
pwd 
quit/exit/bye 
rename 
remove/delete 
rmdir

```
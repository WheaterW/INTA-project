display history-command all-users
=================================

display history-command all-users

Function
--------

The **display history-command all-users** command displays all historical commands saved on the current device.



Format
------

**display history-command all-users**



Parameters
----------

None


Views
-----

All views



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

To check the historical commands that have been executed by the current user, including the commands that fail to be matched, run the **display history-command all-users** command.

You can run this command to view historical command execution records of all users, including user information, command execution date and time, and command lines.

**Precautions**

When using the **display history-command all-users** command, pay attention to the following:

* The format of the saved history command is the same as that of the command entered by the user. If the user uses an incomplete command, the saved history command is also incomplete.
* If a user runs the same command multiple times, only the latest command is saved in historical commands. If a command is entered in different formats, they are considered as different commands.
* To access the previous historical command, press the up arrow key or Ctrl\_P. If there is a later historical command, the previous historical command is displayed. Otherwise, an alarm is generated.
* For the HyperTerminal of Windows 9X, the Up cursor key is invalid because this key is used for other purposes on the Windows 9X HyperTerminal. In this case, you can use Ctrl\_P to replace the key.
* To access the next historical command, press the down arrow key or Ctrl\_N. If there is a later historical command, the next historical command is displayed. Otherwise, the command is cleared and an alarm is generated.
* To modify the maximum number of historical commands that can be buffered, run the **history-command max-size** command. By default, 10 history commands are saved.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png)
 

The actual command output varies according to the device. The command output here is only an example.



# Display information about historical commands executed by all users.
```
<HUAWEI> display history-command all-users
User    : huawei, VTY2, 10.134.146.150                                      
Time    : 2017-05-08 16:08:35                                                   
Command : diagnose                                                              

User    : huawei, VTY5, 10.179.117.219                                      
Time    : 2017-05-08 16:08:35                                                   
Command : display clock

```


**Table 1** Description of the
**display history-command all-users** command output

| Item | Description |
| --- | --- |
| User | Information about the user who enters the command, including the user name, user interface, and login IP address. If no user name is specified upon login, the user name is displayed as \*\*. |
| Time | Time when a command is executed. |
| Command | Command executed. |
display history-command
=======================

display history-command

Function
--------

The **display history-command** command displays the historical commands saved on the device.

By default, the last 10 historical commands are displayed.



Format
------

**display history-command**



Parameters
----------

None


Views
-----

All views



Default Level
-------------

0: Visit level



Usage Guidelines
----------------

**Usage Scenario**

You can run the **display history-command** command to view the historical commands that have been executed recently by the current user, including the commands that fail to be matched. This helps you search for information.

**Precautions**

When using the **display history-command** command, pay attention to the following points:

* The device saves commands in the same way as how users enter them. For example, if a user enters an incomplete command, the saved command will also be incomplete. For example, if dis is entered for the **display this** command, the dis this command instead of the **display this** command is saved.
* If a user runs the same command several times, only the most recently entered command is saved. If a command is entered in different formats, the command in each of these formats is considered different. For example, sysname DeviceA and sysname DeviceB are saved as different commands.
* To view the previous historical command, press the up arrow key or Ctrl\_P. If there is a later historical command, press the up arrow key or Ctrl\_P to display the previous historical command. Otherwise, an alarm is generated.
* For a Windows 9X HyperTerminal, the up arrow key is invalid because this key is used for other purposes on the Windows 9X HyperTerminal. In this case, you can use Ctrl\_P to replace the key.
* To view the next historical command, press the up arrow key or Ctrl\_N. If there is a later historical command, press the up arrow key or Ctrl\_N to display the previous historical command. If there is no later historical command, the command is cleared, no information is displayed, and an alarm is generated.
* You can run the **history-command max-size** command to change the maximum number of historical commands that can be cached.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png)
 

The actual command output varies according to the device. The command output here is only an example.



# Display historical commands.
```
<HUAWEI> display history-command
  display current-configuration
  display this
  display clock
  display device

```
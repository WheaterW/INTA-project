hotkey
======

hotkey

Function
--------



The **hotkey** command assigns a shortcut key to a command.

The **undo hotkey** command restores the default setting of a shortcut key.



By default, the system specifies default values for shortcut keys CTRL\_G, CTRL\_L, and CTRL\_O. The default values of other shortcut keys are empty.

* CTRL\_G corresponds to the display current-configuration command.
* CTRL\_L corresponds to the display ip routing-table command.
* CTRL\_O corresponds to the undo debugging all command.


Format
------

**hotkey CTRL\_G** *command-text*

**hotkey CTRL\_L** *command-text*

**hotkey CTRL\_O** *command-text*

**hotkey CTRL\_U** *command-text*

**undo hotkey CTRL\_G**

**undo hotkey CTRL\_L**

**undo hotkey CTRL\_O**

**undo hotkey CTRL\_U**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *command-text* | Specifies the command line for a shortcut key. | It is a string of 1 to 240 case-sensitive characters, with spaces supported. A shortcut key can be configured for each command supported by the device.  When defining shortcut keys, mark the command with double quotation marks if the command consists of several words or the command includes spaces, and do not mark the command with double quotation marks if the command consists of only one word or the command includes no space. |
| **CTRL\_L** | Assigns the shortcut key Ctrl+L to a command. | - |
| **CTRL\_O** | Assigns the shortcut key Ctrl+O to a command. | - |
| **CTRL\_U** | Assigns the shortcut key Ctrl+U to a command. | - |
| **CTRL\_G** | Assigns the shortcut key Ctrl+G to a command. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

You can assign a shortcut key to a command that is often used or change the default setting of the shortcut key that is defined by the system according to requirements.After running the hotkey command to associate a specified command line with a shortcut key, you can press the shortcut key as an alternative to the associated command line.

**Implementation Procedure**

When specifying command-text, you can enter the abbreviation form of a command. For example, you can enter the hotkey CTRL\_G "display cur" command instead of the hotkey CTRL\_G "display current-configuration" command. These commands in two formats function the same.

**Configuration Impact**

One shortcut key can be associated with only one command. If you run this command for a number of times to associate a shortcut key with multiple commands, the last association takes effect.

**Precautions**

When you define a shortcut key, ensure that the command does not contain sensitive information, such as the password, to prevent information leaks.When assigning a shortcut key to a command, you need to enclose the command with double quotation marks if the command includes spaces. If the command includes no space, you do not need not to enclose the command with double quotation marks.


Example
-------

# Associate the shortcut key Ctrl+G with the display tcp status command.
```
<HUAWEI> system-view
[~HUAWEI] hotkey ctrl_g "display tcp status"

```
mmi-mode enable
===============

mmi-mode enable

Function
--------



The **mmi-mode enable** command displays the machine-to-machine mode.

The **undo mmi-mode enable** command displays the human-to-machine mode.



By default, the current VTY user is in human-to-machine mode.


Format
------

**mmi-mode enable**

**undo mmi-mode enable**


Parameters
----------

None

Views
-----

User view


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

After you enter the machine-to-machine mode by using the **mmi-mode enable** command, the command output is displayed in one screen.After you enter the machine-to-machine mode by using the **mmi-mode enable** command, some important commands that you need to use with caution can be used directly. As a result, this command cannot be found in command lines or be obtained through any help mode. In the human-to-machine mode, users should use this command with caution.


Example
-------

# Enter the machine-to-machine mode.
```
<HUAWEI> mmi-mode enable

```
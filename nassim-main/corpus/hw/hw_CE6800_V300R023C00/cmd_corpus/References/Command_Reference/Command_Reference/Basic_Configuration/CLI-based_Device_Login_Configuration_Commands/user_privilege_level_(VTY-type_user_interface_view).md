user privilege level (VTY-type user interface view)
===================================================

user privilege level (VTY-type user interface view)

Function
--------



The **user privilege level** command configures the command level for the user interface.

The **undo user privilege level** command restores the default command level.



By default, users logging in from a VTY user interface can use commands at Level 0. The default command level for the console port on the user interface is 3.


Format
------

**user privilege level** *level*

**undo user privilege level**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *level* | Specifies a command level. | The value of level ranges from 0 to 3. |



Views
-----

VTY-type user interface view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

If the command level configured on the user interface is inconsistent with the actual level, the actual level is considered as the valid level. For example, the command level corresponding to user 001 is 3 but the command level configured on VTY 0 for the user 001 is 2. When the user logs in to the system through VTY 0, it can use the commands of level 3 or below level 3.

**Precautions**

If precise management of user rights is required, run the **command-privilege level** command to enhance the command level.


Example
-------

# Configure the user privilege level as 2 in VTY 0 view.
```
<HUAWEI> system-view
[~HUAWEI] user-interface vty 0
[*HUAWEI-ui-vty0] user privilege level 2

```

# Configure the user privilege level as 2 in console 0 view.
```
<HUAWEI> system-view
[~HUAWEI] user-interface console 0
[~HUAWEI-ui-console0] user privilege level 2

```
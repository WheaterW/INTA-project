command-privilege
=================

command-privilege

Function
--------



The **command-privilege** command sets the command level of a specified view.

The **undo command-privilege** command removes the configured command level.



By default, the level of a command is its default one.


Format
------

**command-privilege level** *level* **view** *view-name* *command-key*

**undo command-privilege** [ **level** *level* ] **view** *view-name* *command-key*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **level** *level* | Specifies the privilege level of a command. | The value is an integer ranging from 0 to 3. |
| **view** *view-name* | Specifies a view name. Before specifying a view name, you can enter a question mark (?) to check in which views all commands of a specified level can be run.  For example:   * shell: user view. * system: system view. * global: all views. | Specifies the view name. You can enter a question mark (?) on the terminal interface to obtain all the view names that can be selected in the command view. |
| *command-key* | Specifies the command to be configured. | The value is a string of 1 to 1604 characters, spaces supported. The command-privilege command can be configured for each command supported by the device. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

The command-privilege level command is used to set a level for a specified command. An administrator grants configuration access to users by setting levels for the users. Users at a specified level can configure commands equal to and lower than the specified level.A login user can configure commands according to the configured privilege corresponding to the user name (through the **user privilege level** command).

**Precautions**

To ensure high security, do not lower the command level.Changing a command level affects the use of the command by other users. Therefore, change the command level only when necessary.The command-key parameter specifies the command of which the level is to be changed. The view view-name parameter specifies the view to which the command belongs. The command matching rule is prefix-based matching. For example, command-privilege level 2 view shell display interface indicates that the levels of the commands starting with display interface in the user view are changed to 2. For example, the command-privilege level 2 view shell display interface command changes the level of all commands starting with display interface in the user view to level 2.Command levels are classified into visit, monitoring, configuration, and management, which are identified by the numbers 0, 1, 2, and 3, respectively.


Example
-------

# Set the privilege level of the save command to 3.
```
<HUAWEI> system-view
[~HUAWEI] command-privilege level 3 view shell save

```

# Set the privilege level of the display current-configuration command to 3.
```
<HUAWEI> system-view
[~HUAWEI] command-privilege level 3 view global display current-configuration

```
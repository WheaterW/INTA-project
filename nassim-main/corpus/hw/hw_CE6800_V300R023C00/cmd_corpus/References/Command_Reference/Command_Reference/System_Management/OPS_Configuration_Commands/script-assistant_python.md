script-assistant python
=======================

script-assistant python

Function
--------



The **script-assistant python** command creates a Python script assistant.

The **undo script-assistant python** command deletes a created Python script assistant.



By default, no Python script assistant is created.


Format
------

**script-assistant python** *script-name*

**undo script-assistant python** *script-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *script-name* | Specifies the file name of a script assistant. | The value is a string of 4 to 64 case-sensitive characters, spaces not supported. The first character in the file name cannot be an underscore (\_). |



Views
-----

OPS view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

You can use maintenance assistant task functions to set working conditions and tasks. When working conditions are met, the system automatically performs the corresponding working task.Maintenance assistants are classified into the following types:

* Command assistant: The working conditions and tasks of a command assistant are configured using commands.
* Script assistant: The working conditions and tasks of a script assistant are defined using scripts.A script assistant supports command, timer, and routing events. To create a script assistant, run the **script-assistant python** command.

**Prerequisites**

The script assistant has been uploaded to the root directory and installed using the **ops install file** command.

**Follow-up Procedure**

Run the **shutdown script-assistant script-name** command to shut down the script assistant if a script assistant does not need to be run.


Example
-------

# Create a Python script assistant with a file name of cron.py.
```
<HUAWEI> system-view
[~HUAWEI] ops
[~HUAWEI-ops] script-assistant python cron.py

```
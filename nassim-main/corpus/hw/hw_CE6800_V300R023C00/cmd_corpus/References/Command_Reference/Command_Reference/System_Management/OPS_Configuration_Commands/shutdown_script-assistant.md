shutdown script-assistant
=========================

shutdown script-assistant

Function
--------



The **shutdown script-assistant** command shuts down a script assistant.

The **undo shutdown script-assistant** command starts a script assistant.



By default, a created script assistant is started.


Format
------

**shutdown script-assistant** *script-name*

**undo shutdown script-assistant** *script-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *script-name* | Specifies the file name of a script assistant. | The value is a string of 4 to 64 case-sensitive characters, spaces not supported. |



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
* Script assistant: The working conditions and tasks of a script assistant are defined using scripts.If a script assistant does not need to be run, run the **shutdown script-assistant** command to shut down the script assistant.

**Prerequisites**

A script assistant has been created using the **script-assistant python** command.

**Precautions**


Example
-------

# Shut down a script assistant with a file name of cron.py.
```
<HUAWEI> ops install file cron.py
<HUAWEI> system-view
[~HUAWEI] ops
[~HUAWEI-ops] script-assistant python cron.py
[*HUAWEI-ops] shutdown script-assistant cron.py

```
run
===

run

Function
--------



The **run** command executes a user-view command in a non-user view.




Format
------

**run** *command-line*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *command-line* | Specifies the command to be run. | The value is a string of 1 to 1604 characters, spaces supported. |



Views
-----

All views except the user view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To **run** commands, which can be run only in the user view, in the system view, you must return to the user view. After completing this configuration task, you can run the **run** command to run such commands in a non-user view without returning to the user view.

**Precautions**

* When running the **run** command, ensure that the specified command format can be run in the user view.
* You can run the **display history-command** command to view the historical commands saved on the terminal. The historical commands record only entered commands. The command format is command-line.
* Only the actually executed commands are recorded in CLI/5/CMDRECORD logs. The command format is command-line.
* The **run** command cannot be applied to configuration rollback or system software behavior changes, such as rollback configuration, quit, and patch load.


Example
-------

# View .cfg files in the system view.
```
<HUAWEI> system-view
[~HUAWEI] run dir *.cfg
Directory of flash:/
  Idx  Attr     Size(Byte)  Date        Time       FileName
    0  -rw-         11,970  Mar 14 2012 19:11:22   9300_31.cfg
    1  -rw-         12,033  Apr 22 2012 17:10:30   9300_31_new.cfg
509,256 KB total (118,784 KB free)

```
execute
=======

execute

Function
--------



The **execute** command executes a specified batch file or VRP Shell Languages (VSL) script.




Format
------

**execute** *filename* [ *parameter* [ *parameter* [ *parameter* [ *parameter* [ *parameter* [ *parameter* [ *parameter* [ *parameter* ] ] ] ] ] ] ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *filename* | Specifies the name and path of a batch file. | The value is a string of 5 to 64 characters. The file name extension is .bat or .cfg. If the batch file to be processed is in the current directory; you can only input the name of a batch file. |
| *parameter* | Specifies a VSL parameter. | The value is a string of 1 to 32 case-sensitive characters. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

* The commands in a batch file are run one by one. A batch file cannot contain any invisible character except the carriage return and line feed characters. If an invisible character such as Tab is detected, the execute command exits from the current process and no rollback is performed.
* The execute command does not ensure that all commands can be run. The execute command is not hot backed up, and no restriction is on the format or contents of the command.
* Running the execute command functions the same as running the commands one by one manually.

**Precautions**

When a .bat file is a VSL script, the execute command configures services automatically and commands in the batch file as well as performs configurations for services specified by parameter at a time.Whether a character is invisible is determined based on the ASCII character table. Characters whose ASCII character value ranges from 32 to 126 are visible (the ASCII character value 32 indicates spaces). Other characters are invisible.


Example
-------

# Execute the VSL script vsl.bat and enter the parameter HUAWEI.
```
<HUAWEI> cd flash:/
<HUAWEI> system-view
[~HUAWEI] execute vsl.bat HUAWEI

```
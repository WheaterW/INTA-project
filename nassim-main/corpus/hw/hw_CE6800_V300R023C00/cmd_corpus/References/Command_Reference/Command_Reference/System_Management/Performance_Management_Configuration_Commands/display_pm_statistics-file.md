display pm statistics-file
==========================

display pm statistics-file

Function
--------



The **display pm statistics-file** command displays performance statistics files.




Format
------

**display pm statistics-file** [ *task-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *task-name* | Displays the performance statistics files generated for a performance statistics task. | The value is a string of 1 to 31 characters, spaces not supported. The string contains letters, digits, and underscores (\_), and must start with letters or digits. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

After a performance statistics task starts, the system automatically generates performance statistics files for the task. To view the performance statistics files generated for the performance statistics task, run the display pm statistics-file command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display performance statistics files for all performance statistics tasks.
```
<HUAWEI> display pm statistics-file
Total files count: 4
--------------------------------------------------------------------------------
Task Name: 1
  120120107030001.txt
  120120107040002.txt
  120120107050003.txt
  120120107060004.txt

```

**Table 1** Description of the **display pm statistics-file** command output
| Item | Description |
| --- | --- |
| Total files count | Number of performance statistics files. |
| Task Name | Name of a performance statistics task. |
file-format
===========

file-format

Function
--------



The **file-format** command sets the format for performance statistics files to be uploaded.



By default, a performance statistics file is generated in the text format.


Format
------

**file-format** { **text** | **xml** }

**undo file-format**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **text** | Specifies text as the format for performance statistics files. | - |
| **xml** | Specifies xml as the format for performance statistics files. | - |



Views
-----

Statistics task view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To set the format of performance statistics files to .text or .xml, run the file-format command.

* The format of a .text file is tasknameyyyymmddhhmmindexnum.txt.
* The format of an .xml file is tasknameyyyymmddhhmmindexnum.xml.A performance statistics file consists of a file header and a file body:
* File header: includes the name of a device, software version running on the device, and interval at which performance statistics are collected.
* File body: includes the time when performance statistics collection starts, performance statistics objects and their types, counters of a performance statistics object, and counter values within a performance statistics cycle.

**Precautions**

An .xml file occupies more storage space than a .text file does. However, an .xml file is more readable, expandable.If the format for the performance statistics files is .text, historical statistics collected within the number of intervals set using the **record-interval** command will be recorded. If the format for the performance statistics files is .xml, historical statistics collected within the latest one interval will be recorded.


Example
-------

# Set the format of the performance statistics files to be generated for the performance statistics task named task1 to .text.
```
<HUAWEI> system-view
[~HUAWEI] pm
[~HUAWEI-pm] statistics-task task1
[*HUAWEI-pm-statistics-task1] file-format text

```
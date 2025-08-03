retry
=====

retry

Function
--------



The **retry** command sets the number of retransmissions for a performance statistics file.

The **undo retry** command restores the number of retransmissions for a performance statistics file to the default value.



The default number of retransmissions for a performance statistics file is 3.


Format
------

**retry** *retry-times*

**undo retry**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *retry-times* | Sets the number of retransmissions for a performance statistics file. | The value is an integer ranging from 1 to 3. |



Views
-----

PM server view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The system generates performance statistics files and transmits these files to a PM server. To set the number of retransmissions for a performance statistics file, run the retry command.


Example
-------

# Set the number of retransmissions for a performance statistics file to 2.
```
<HUAWEI> system-view
[~HUAWEI] pm
[~HUAWEI-pm] pm-server a
[*HUAWEI-pm-server-a] retry 2

```
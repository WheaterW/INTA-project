reset qos queue statistics
==========================

reset qos queue statistics

Function
--------



The **reset qos queue statistics** command clears queue-based traffic statistics.




Format
------

**reset qos queue statistics** { **interface** *interface-name* | **interface** *interface-type* *interface-number* | **slot** *slot-id* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-name* | Specifies the name of an interface. | The value is a string case-sensitive characters, spaces not supported. |
| *interface-type* | Specifies the type of an interface. | - |
| *interface-number* | Specifies the number of an interface. | The value is a string case-sensitive characters, spaces not supported. |
| **slot** *slot-id* | Specifies the slot ID. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To collect queue-based statistics within a certain period, run the reset qos queue statistics command to clear the existing statistics first.

**Precautions**

Queue-based statistics cannot be restored after you clear them. Therefore, exercise caution when you run the command.


Example
-------

# Clear queue-based traffic statistics on slot 1.
```
<HUAWEI> reset qos queue statistics slot 1

```

# Clear queue-based traffic statistics on a specified interface.
```
<HUAWEI> reset qos queue statistics interface 100GE 1/0/1

```
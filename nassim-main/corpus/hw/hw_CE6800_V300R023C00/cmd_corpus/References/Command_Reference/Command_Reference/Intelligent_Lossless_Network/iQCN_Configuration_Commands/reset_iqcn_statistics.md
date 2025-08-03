reset iqcn statistics
=====================

reset iqcn statistics

Function
--------



The **reset iqcn statistics** command clears statistics about CNPs proactively sent by the device and those sent by each interface.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**reset iqcn statistics** [ **interface** { *interface-name* | *interface-type* *interface-number* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-number* | Clears CNP statistics on a specified interface of a forwarding device.   * interface-type specifies the interface type. * interface-number specifies the interface number. | - |
| **interface** *interface-name* | Clears CNP statistics on a specified interface of a forwarding device.  interface-name specifies the name of an interface. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

You can run this command to clear statistics about CNPs proactively sent by the device and those sent by each interface.


Example
-------

# Clear statistics about CNPs on the device.
```
<HUAWEI> reset iqcn statistics

```
reset npcc statistics
=====================

reset npcc statistics

Function
--------



The **reset npcc statistics** command clears statistics about CNPs proactively sent by an NPCC-enabled forwarder.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**reset npcc statistics** [ **interface** { *interface-name* | *interface-type* *interface-number* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-number* | Clears CNP statistics on a specified interface.   * interface-type specifies the interface type. * interface-number specifies the interface number.   If no interface is specified, CNP statistics on the chip and all interfaces are cleared. | - |
| **interface** *interface-name* | Clears CNP statistics on a specified interface. interface-name specifies the name of an interface.  If no interface is specified, CNP statistics on the chip and all interfaces are cleared. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

You can run this command to clear statistics about CNPs proactively sent by a forwarder with the NPCC function enabled on its interface.


Example
-------

# Clear statistics about CNPs proactively sent by an NPCC-enabled forwarder.
```
<HUAWEI> reset npcc statistics interface 100GE 1/0/1

```
display mib-index interface
===========================

display mib-index interface

Function
--------



The **display mib-index interface** command displays interface indexes in a management information base (MIB).




Format
------

**display mib-index interface** [ *interface-type* [ *interface-number* ] | *interface-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-type* | Displays the index value of a specified type of interface in the MIB. | The value is of the enumerated type. |
| *interface-number* | Displays the index value of an interface with a specified number in the MIB. | - |
| *interface-name* | Specifies the name of an interface. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



To view the values of interface indexes in a MIB, run the display mib-index interface command. This configuration helps the NMS view the interface indexes mapped to interface names.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display indexes of all interfaces.
```
<HUAWEI> display mib-index interface
IfName                          IfIndex   PortIndex
---------------------------------------------------
100GE1/0/1                      7         3
100GE1/0/1                      8         4
100GE1/0/2                      9         5
MEth0/0/0                       4         --
NULL0                           2         --
Nve1                            14        --

```

**Table 1** Description of the **display mib-index interface** command output
| Item | Description |
| --- | --- |
| IfName | Interface name. |
| IfIndex | Index value of an interface. |
| PortIndex | Index value of a port. |
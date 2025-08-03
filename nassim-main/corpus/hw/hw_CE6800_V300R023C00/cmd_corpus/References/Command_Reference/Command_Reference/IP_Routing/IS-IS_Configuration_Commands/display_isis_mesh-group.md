display isis mesh-group
=======================

display isis mesh-group

Function
--------



The **display isis mesh-group** command displays the configuration of the IS-IS mesh-group.




Format
------

**display isis** *process-id* **mesh-group**

**display isis mesh-group** [ *process-id* | **vpn-instance** *vpn-instance-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies an IS-IS process ID. | The value is an integer ranging from 1 to 4294967295. |
| **vpn-instance** *vpn-instance-name* | Displays mesh-group information about a specified VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

When an interface that does not belong to an IS-IS mesh-group receives an LSP, the interface sends the LSP to all the other interfaces. On an NBMA network with multiple connections and P2P links, the same LSP will flood the network and consume bandwidth.After an interface joins a mesh-group, the interface sends the received LSP only to interfaces that do not belong to the mesh-group and the interface does not send the same LSP back. Therefore, LSP flooding is avoided, link pressure is reduced, and network resources are saved.The **display isis mesh-group** command is used to check the mesh-group to which an interface belongs so that the LSP-flooding area can be identified.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the IS-IS mesh-group.
```
<HUAWEI> display isis mesh-group
Mesh Group information for ISIS(1)
--------------------------------------
Interface                       Status
100GE1/0/1                         100
100GE1/0/1                         100

```

**Table 1** Description of the **display isis mesh-group** command output
| Item | Description |
| --- | --- |
| Interface | Type and number of an interface in the mesh-group. |
| Status | Mesh-group number. |
display isis link-group
=======================

display isis link-group

Function
--------



The **display isis link-group** command displays the status of a link group and information about the link members in the link group.




Format
------

**display isis** { *process-id* **link-group** | **link-group** *process-id* } *group-name*

**display isis** { [ *process-id* ] **link-group** | **link-group** [ *process-id* ] }

**display isis link-group vpn-instance** *vpn-instance-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Displays information about the link group in a specified IS-IS process. | The value is an integer ranging from 1 to 4294967295. |
| *group-name* | Displays information about the link group of the specified name. | The value is a string of 1 to 32 case-sensitive characters.When quotation marks are used around the string, spaces are allowed in the string. |
| **vpn-instance** *vpn-instance-name* | Displays information about the link group in a specified VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To check the status of a link group and information about the link members in the link group, run the display isis link-group command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about the link group in IS-IS process 1.
```
<HUAWEI> display isis link-group 1
Link-group information for ISIS(1)
                       ----------------------------------

 GroupName : a
 minMembers: 2   revertMembers: 2   costOffset: 100
 ------------------------------------------------------------
 IPV4 MT 0    L1 GroupState   :   DOWN  
                 Members          CircuitState
                 ---------------------------
                 100GE1/0/1       DOWN(Reason:circ has no adj)
 IPV4 MT 0    L2 GroupState   :   DOWN  
                 Members          CircuitState
                 ---------------------------
                 100GE1/0/1       UP
 IPV6 MT 2    L1 GroupState   :   DOWN  
                 Members          CircuitState
                 ---------------------------
                 100GE1/0/1       DOWN(Reason:circ has no adj)
 IPV6 MT 2    L2 GroupState   :   DOWN  
                 Members          CircuitState
                 ---------------------------
                 100GE1/0/1       UP

```

**Table 1** Description of the **display isis link-group** command output
| Item | Description |
| --- | --- |
| GroupName | Link group name. |
| MT | The topology of interface, and the number is MT-ID. |
| GroupState | Link group status:   * UP: The status is Up when the number of available member links in a link group reaches or exceeds revert-number. * DOWN: The status is Down when the number of available member links in a link group falls below min-members. |
| Members | Member link in a link group. |
| CircuitState | Interface status:   * UP. * DOWN: The status is Down due to the following causes: * circ has no adj: The interface has no neighbor or its neighbor has been suppressed. * circ quality is low: The quality of the link of the interface is low. * circ ldp sync state is HoldMaxCost: The LDP session associated with the interface goes Down. |
| minMembers | Number of available member links that triggers a link cost adjustment. |
| revertMembers | Number of available member links that triggers a link cost restoration. |
| costOffset | Offset to be added to the link cost of the member links when the number of available member links falls below a specified number. |
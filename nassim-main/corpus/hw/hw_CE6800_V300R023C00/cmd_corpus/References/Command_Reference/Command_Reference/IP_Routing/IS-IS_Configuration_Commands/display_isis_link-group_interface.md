display isis link-group interface
=================================

display isis link-group interface

Function
--------



The **display isis link-group interface** command displays information about the link group to which an IS-IS interface has been bound.




Format
------

**display isis link-group interface** { *interface-name* | *interface-type* *interface-number* }

**display isis** { [ *process-id* ] **link-group** | **link-group** [ *process-id* ] } **interface**

**display isis link-group interface vpn-instance** *vpn-instance-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-type* | Displays information about the link group to which a specified IS-IS interface has been bound. | - |
| *interface-number* | Displays information about the link group to which a specified IS-IS interface has been bound. | - |
| *process-id* | Displays information about the link group to which the IS-IS interface in a specified process has been bound. | The value is an integer ranging from 1 to 4294967295. |
| **vpn-instance** *vpn-instance-name* | Displays information about the link group to which the IS-IS interface in a specified VPN instance has been bound. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To check information about the link group to which an IS-IS interface has been bound, run the display isis link-group interface command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about the link groups to which the IS-IS interfaces in all processes have been bound.
```
<HUAWEI> display isis link-group interface
Interface link-group information for ISIS(1)
                       --------------------------------------------

 Interface 100GE1/0/1
  IPV4:
     L1 GroupName    :  a
        GroupState   :  DOWN
        CircState    :  DOWN(Reason:circ has no adj)
        CostOffset   :  100
     L2 GroupName    :  a
        GroupState   :  DOWN
        CircState    :  UP
        CostOffset   :  100
  IPV6:
     L1 GroupName    :  a
        GroupState   :  DOWN
        CircState    :  DOWN(Reason:circ has no adj)
        CostOffset   :  100
     L2 GroupName    :  a
        GroupState   :  DOWN
        CircState    :  UP
        CostOffset   :  100

```

**Table 1** Description of the **display isis link-group interface** command output
| Item | Description |
| --- | --- |
| L1 GroupName | Level-1 link group name. |
| GroupState | Link group status:   * UP: The status is Up when the number of available member links in a link group reaches or exceeds revert-members. * DOWN: The status is Down when the number of available member links in a link group falls below min-members. |
| CircState | Interface status:   * UP. * DOWN: The status is Down due to the following causes: * circ has no adj: The interface has no neighbor or its neighbor has been suppressed. * circ quality is low: The quality of the link of the interface is low. * circ ldp sync state is HoldMaxCost: The LDP session associated with the interface goes Down. |
| CostOffset | Offset to be added to the link cost of the member links when the number of available member links falls below a specified number. |
| L2 GroupName | Level-2 link group name. |
| IPV4 | IPV4 process. |
| IPV6 | IPV6 process. |
display igmp snooping qinq-port-info interface
==============================================

display igmp snooping qinq-port-info interface

Function
--------



The **display igmp snooping qinq-port-info interface** command displays entries on a specified sub-interface for dot1q VLAN tag termination.




Format
------

**display igmp snooping qinq-port-info interface** { *interface-type* *interface-number* | *interface-name* } [ **group-address** *group-address* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-type* | Specifies the interface type and number. | - |
| *interface-number* | Specifies the interface number added to the multicast group. | - |
| *interface-name* | Specifies the interface name added to the multicast group. | - |
| **group-address** *group-address* | Specifies the IP address of the multicast group. | The value is in dotted decimal notation and ranges from 224.0.1.0 to 239.255.255.255. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To display the entries on a specified dot1q termination sub-interface, run the display igmp snooping qinq-port-info command.Before using the display igmp snooping qinq-port-info command, note the following:

* If no optional parameter is specified, entries about all multicast groups on the sub-interface are displayed.
* If group-address is specified, the entry about the specified multicast group on the sub-interface is displayed.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display entries about all multicast groups on the sub-interface for dot1q termination sub-interface 10GE1/0/1.1.
```
<HUAWEI> display igmp snooping qinq-port-info interface 10ge1/0/1.1
Interface 10GE1/0/1.1, 2 Group(s)
(Source,Group)              PPE-VID/CE-VID       LiveTime          Flag
-------------------------------------------------------------------------------
(*,226.0.0.1)               1/0                  00:00:23           -D
(*,226.0.0.2)               1/0                  00:00:02           -D

```

**Table 1** Description of the **display igmp snooping qinq-port-info interface** command output
| Item | Description |
| --- | --- |
| Group(s) | Indicates the number of multicast groups. |
| (Source,Group) | Source indicates the address of the multicast source.  Group indicates the address of the multicast group. |
| LiveTime | Indicates the live time of a multicast group member interface. |
| Flag | Indicates the entry type. Currently, the following entry types are provided:   * D: indicates a dynamically learnt entry. * S: indicates a manually configured entry. When "S" is displayed in the Flag field, spaces is displayed in the LiveTime field. * M: indicates an SSM mapping entry. * SD: indicates that both static and dynamic entries exist on the sub-interface. |
| PE-VID/CE-VID | Indicates VLAN information about a multicast group member interface.  PE-VID indicates the outer tag and CE-VID indicates the inner tag. |
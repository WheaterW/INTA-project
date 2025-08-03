display multicast boundary
==========================

display multicast boundary

Function
--------



The **display multicast boundary** command displays information about the multicast boundary configured on an interface.




Format
------

**display multicast** { **vpn-instance** *vpn-instance-name* | **all-instance** } **boundary** [ *group-address* [ *mask* | *mask-length* ] ] [ **interface** { *interface-type* *interface-number* | *interface-name* } ]

**display multicast boundary** [ *group-address* [ *mask* | *mask-length* ] ] [ **interface** { *interface-type* *interface-number* | *interface-name* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of case-sensitive characters. |
| **all-instance** | Specifies all instances. | - |
| *group-address* | Specifies a multicast group address. If this parameter is specified, information about the multicast boundary configured for the group is displayed. | The value ranges from 224.0.0.0 to 239.255.255.255, in dotted decimal notation. |
| *mask* | Specifies the mask of a multicast group address. If this parameter is specified, information about the multicast boundary configured for the groups in the specified range is displayed. | The address is in dotted decimal notation. |
| *mask-length* | Specifies the mask length of a multicast group address. If this parameter is specified, information about the multicast boundary configured for the groups in the specified range is displayed. | The value is an integer ranging from 4 to 32. |
| **interface** *interface-name* | Specifies the name of an interface. | - |
| *interface-type* | Specifies the type of an interface. If this parameter is specified, information about the multicast boundary configured on the interface is displayed. | - |
| *interface-number* | Specifies the number of an interface. If this parameter is specified, information about the multicast boundary configured on the interface is displayed. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

After a multicast boundary has been configured by using the **multicast boundary** command, run the display **multicast boundary** command to view configurations.

**Precautions**

If neither vpn-instance nor all-instance is specified, information about multicast boundaries configured on the interfaces in the public network instance is displayed.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about multicast boundaries configured on all the interfaces in the public network instance.
```
<HUAWEI> display multicast boundary
Multicast boundary information of VPN Instance: public net
Total: 1
 Interface           Boundary
100GE1/0/1            225.0.0.0/24

```

**Table 1** Description of the **display multicast boundary** command output
| Item | Description |
| --- | --- |
| Multicast boundary information of VPN Instance | VPN instance to which multicast boundary information belongs. |
| Interface | Interface configured with a multicast boundary. |
| Boundary | Address of the interface configured with the multicast boundary. |
| Total | Total number of multicast boundaries configured on the device. |
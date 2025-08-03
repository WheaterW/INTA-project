display l2-multicast ipv6 forwarding-table
==========================================

display l2-multicast ipv6 forwarding-table

Function
--------



The **display l2-multicast ipv6 forwarding-table** command displays the IPv6 Layer 2 multicast forwarding table. If a VLAN is specified, the forwarding entries of the specified VLAN are displayed. If no VLAN is specified, all forwarding entries are displayed.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display l2-multicast ipv6 forwarding-table** [ **vlan** *vlan-id* [ [ **source** *source-address-v6* ] **group** *group-address-v6* ] ] [ **slot** *slot-id* [ **cpu** *cpu-id* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vlan** *vlan-id* | Displays entries in a specified VLAN. | The value is an integer ranging from 1 to 4094. |
| **source** *source-address-v6* | Specifies a multicast source address and displays information about the forwarding table corresponding to the multicast source. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| **group** *group-address-v6* | Indicates the address of an IPv6 multicast group. It is used to specify an IPv6 multicast group and display the forwarding table corresponding to the group. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| **slot** *slot-id* | Displays entry information in the specified slot. | The value is a string of 1 to 23 case-sensitive characters, spaces not supported. |
| **cpu** *cpu-id* | Displays entry information of the specified CPU ID. | The value is an integer ranging from 0 to 4. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

You can use this command to view information about the Layer 2 multicast forwarding table, including dynamically generated and statically added entries.An entry contains information about the multicast source, multicast group, outbound interface, and VLAN to which the packet belongs.

**Configuration Impact**

This command displays Layer 2 multicast forwarding entries of a VLAN only when at least one interface in the VLAN is up.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the multicast forwarding table of VLAN 100.
```
<HUAWEI> display l2-multicast ipv6 forwarding-table vlan 100
-------------------------------------------------------------------------------- 
Forwarding Mode: IP                                 
--------------------------------------------------------------------------------
VLAN  Total                      (Source,Group)  Interface 
--------------------------------------------------------------------------------  
100    1          
                                 (*, FF1E::1)  GE1/0/1    
--------------------------------------------------------------------------------

```

**Table 1** Description of the **display l2-multicast ipv6 forwarding-table** command output
| Item | Description |
| --- | --- |
| Forwarding Mode | Multicast packet forwarding mode in a VLAN:   * IP. * MAC.   The current version supports only IP. |
| VLAN | ID of the VLAN to which the forwarding entry belongs. |
| Total | Total number of forwarding entries. |
| (Source,Group) | (Source, Group) information. |
| Interface | Outbound interface. |
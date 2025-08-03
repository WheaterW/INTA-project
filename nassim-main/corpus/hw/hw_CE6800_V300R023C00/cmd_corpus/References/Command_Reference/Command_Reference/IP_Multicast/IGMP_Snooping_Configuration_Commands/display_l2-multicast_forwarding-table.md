display l2-multicast forwarding-table
=====================================

display l2-multicast forwarding-table

Function
--------



The **display l2-multicast forwarding-table** command displays the IPv4 Layer 2 multicast forwarding table.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**display l2-multicast forwarding-table** [ **vlan** *vlan-id* [ [ **source** *source-address* ] **group** *group-address* ] ] [ **slot** *slot-id* [ **cpu** *cpu-id* ] ]

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**display l2-multicast forwarding-table** [ **bridge-domain** *bridge-domain-id* [ **group** *group-address* ] ] [ **slot** *slot-id* [ **cpu** *cpu-id* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vlan** *vlan-id* | Specifies the VLAN ID. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **source** *source-address* | Displays forwarding information corresponding to the specified multicast source address. | The value is in dotted decimal notation. |
| **group** *group-address* | Displays forwarding information corresponding to the specified multicast group address. | The value is in dotted decimal notation. |
| **slot** *slot-id* | Displays entry information in the specified slot. | The value is a string of 1 to 23 case-sensitive characters, spaces not supported. |
| **cpu** *cpu-id* | Displays entry information of the specified CPU ID. | The value is an integer ranging from 0 to 4. |
| **bridge-domain** *bridge-domain-id* | Specifies a bridge domain ID.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is an integer ranging from 1 to 16777215. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

You can use this command to view information about the Layer 2 multicast forwarding table, including dynamically generated and statically added entries.An entry contains information about the multicast source, multicast group, outbound interface, and VLAN or bridge domain to which the packet belongs. When the IGMP snooping version is set to v3 in a VLAN, or when the IGMP snooping version is earlier than v3 but SSM mapping is configured in a VLAN, you can view accurate (S, G) information.

**Configuration Impact**

This command displays Layer 2 multicast forwarding entries of a VLAN only when at least one interface in the VLAN is up.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the multicast forwarding table of VLAN 100.
```
<HUAWEI> display l2-multicast forwarding-table vlan  100
-------------------------------------------------------------------------------- 
Forwarding Mode: IP                                 
--------------------------------------------------------------------------------
VLAN  Total                      (Source,Group)  Interface 
--------------------------------------------------------------------------------  
100    1          
                                 (*, 225.0.0.1)  GE1/0/1    
--------------------------------------------------------------------------------

```

**Table 1** Description of the **display l2-multicast forwarding-table** command output
| Item | Description |
| --- | --- |
| Forwarding Mode | Multicast packet forwarding mode in a VLAN:   * IP. * MAC.   The current version supports only IP. |
| VLAN | ID of the VLAN to which the forwarding entry belongs. |
| Total | Total number of forwarding entries. |
| (Source,Group) | (Source, Group) information. |
| Interface | Outbound interface. |
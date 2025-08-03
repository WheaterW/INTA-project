display igmp snooping port-info
===============================

display igmp snooping port-info

Function
--------



The **display igmp snooping port-info** command displays information about member ports on the router, including static member ports, SSM mapping-enabled ports, and dynamic member ports.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**display igmp snooping port-info** [ **vlan** *vlan-id* [ **group-address** *group-address* ] ] [ **verbose** ]

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display igmp snooping port-info bridge-domain** *bd-id* [ **group-address** *group-address* ] [ **verbose** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vlan** *vlan-id* | Displays information about multicast interfaces in a specified VLAN. | The value is an integer that ranges from 1 to 4094. |
| **group-address** *group-address* | Displays information about interfaces related to a specified multicast group. | The group-address value ranges from 224.0.1.0 to 239.255.255.255. |
| **verbose** | Displays detailed information about member ports. | - |
| **bridge-domain** *bd-id* | Displays information about member ports in a specified BD.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The bd-id value is an integer ranging from 1 to 16777215. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

The command output is displayed only after IGMP snooping is enabled globally and in a VLAN.Information about member interfaces is displayed only when the member interfaces are in Up state.

* The **display igmp snooping port-info** command displays information about all multicast interfaces.
* The **display igmp snooping port-info vlan** command displays information about all multicast interfaces in a specified VLAN.
* The **display igmp snooping port-info vlan group-address** command displays information about the interface of a specified multicast group in a VLAN.You can run the display igmp snooping port info bridge-domain group-address command to view information about interfaces in a specified multicast group in a BD only after IGMP snooping is enabled in the BD.

The command output is displayed only after IGMP snooping is enabled globally and in a VLAN.Information about member interfaces is displayed only when the member interfaces are in Up state.

* The **display igmp snooping port-info** command displays information about all multicast interfaces.
* The **display igmp snooping port-info vlan** command displays information about all multicast interfaces in a specified VLAN.
* The **display igmp snooping port-info vlan group-address** command displays information about the interface of a specified multicast group in a VLAN.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about the multicast group member port list in VLAN 10.
```
<HUAWEI> display igmp snooping port-info vlan 10
-----------------------------------------------------------------------------------
  Flag: S:Static     D:Dynamic     M:Ssm-mapping
        A:Active     P:Protocol    T:Trill       
                     (Source, Group)  Port                                      Flag
 -----------------------------------------------------------------------------------
 VLAN 10, 2 Entry(s)
                     (*, 224.0.1.22)                                            P--
                                      100GE1/0/1                                   -D-
                                                        1 port(s) include
                (*, 239.255.255.253)                                            P--
                                      100GE1/0/1                                   -D-
                                                        1 port(s) include
 -----------------------------------------------------------------------------------

```

**Table 1** Description of the **display igmp snooping port-info** command output
| Item | Description |
| --- | --- |
| Port | Information about member ports of the multicast group. |
| Flag | Entry type:   * P: entries generated based on protocol packets or statically configured. * A: entries triggered by multicast data traffic. * T: entries generated after Trill configuration.   Port type:   * S: static member ports. * D: dynamic member ports. * M: SSM mapping-enabled ports. |
| Source | Multicast source address. |
| Group | Multicast group address. |
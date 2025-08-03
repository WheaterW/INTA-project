display bgp evpn group
======================

display bgp evpn group

Function
--------



The **display bgp evpn group** command displays information about BGP EVPN peer groups.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp evpn group** [ *group-name* ]

**display bgp** [ **instance** *instance-name* ] **evpn** **group** [ *group-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **instance** *instance-name* | Displays information about EVPN peer group of a specified BGP instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

Configuring BGP EVPN peer groups simplifies BGP EVPN network configuration and improves route advertisement efficiency.The **display bgp evpn group** command displays BGP EVPN peer group information, including peers in the peer group and configuration information about the BGP EVPN peer group. The **display bgp evpn group** command is used in the following scenarios:

* Verify the configuration after a peer group is configured using the **group** command.
* Verify the configuration after a peer is added to a peer group using the **peer group** command.
* Verify the configuration after a peer is deleted from a peer group using the **undo peer group** command.
* Verify the configuration after modifying the configuration of a peer group.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about all BGP EVPN peer groups.
```
<HUAWEI> display bgp evpn group
Group in BGP-EVPN:
 BGP peer-group: gp1
 Remote AS: 100
 Authentication type configured: None
 Type : internal
 PeerSession Members: 
 10.2.2.9                                 
 Peer Members: 
 10.2.2.9

```

**Table 1** Description of the **display bgp evpn group** command output
| Item | Description |
| --- | --- |
| BGP peer-group | Name of a BGP peer group. |
| Remote AS | Number of the AS where a peer group resides. |
| Authentication type configured | BGP authentication type:   * MD5. * None: indicates that no BGP authentication is configured. |
| Type | Type of a peer group:   * internal: indicates that the peer group is an IBGP peer group. * external: indicates that the peer group is an EBGP peer group. |
| PeerSession Members | BGP peers with which sessions have been established. |
| Peer Members | Peer information. |
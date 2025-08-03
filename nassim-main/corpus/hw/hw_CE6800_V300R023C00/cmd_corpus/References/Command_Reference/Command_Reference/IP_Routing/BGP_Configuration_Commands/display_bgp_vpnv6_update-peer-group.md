display bgp vpnv6 update-peer-group
===================================

display bgp vpnv6 update-peer-group

Function
--------



The **display bgp vpnv6 update-peer-group** command displays information about BGP VPNv6 update peer-groups.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp** { **vpnv6** **vpn-instance** *vpn-instance-name* | **vpnv6** **all** } **update-peer-group** [ **index** *update-group-index* ]

**display bgp instance** *bgpName* **vpnv6** **vpn-instance** *vpn-instance-name* **update-peer-group** [ **index** *update-group-index* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Specifies a VPN instance name. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **all** | Displays all information about VPNv6 and IPv6 VPN instances. | - |
| **index** *update-group-index* | Index of update peer group. | The value is an integer ranging from 0 to 65535. |
| **instance** *bgpName* | Specifies the BGP multi-instance name. | The value is a string of 1 to 31 case-sensitive characters without spaces. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The **display bgp vpnv6 update-peer-group** command displays information about BGP VPNv6 update peer-groups. Details about update peer-groups can be displayed based on the update peer-group index.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about BGP VPNv6 update peer-groups.
```
<HUAWEI> display bgp vpnv6 all update-peer-group index 0
 Group ID : 0
 BGP Version : 4
 Group Type : external
 Addr Family : VPNv6
 Total Peers : 1
 AdvMinTimeVal : 30
 Leader Peer : 192.168.1.2

 Total format packet number : 3
 Total send packet number : 3
 Total replicate packet number : 0
 The replication percentages(%) : 0

 Peers List : 192.168.1.2

```

**Table 1** Description of the **display bgp vpnv6 update-peer-group** command output
| Item | Description |
| --- | --- |
| Group ID | Update group ID of the BGP peer. |
| Group Type | Type of an update peer-group:   * external: EBGP. * internal: IBGP. * unknown: unknown type. |
| BGP Version | BGP version. |
| Addr Family | Address family. |
| Total Peers | Indicates the total number of peers in an update-group. |
| Total format packet number | Total format packet number. |
| Total send packet number | Total number of sent packets. |
| Total replicate packet number | Total number of sent packets - Total number of formatted packets. |
| Peers List | List of peers. |
| AdvMinTimeVal | Minimum interval at which Update messages with the same route prefix are sent. |
| Leader Peer | IP addresses of peers in an update peer-group. |
| The replication percentages(%) | Replication percentage: (Total number of sent packets - Total number of formatted packets) x 100/Total number of formatted packets. |
display bgp vpnv6 group
=======================

display bgp vpnv6 group

Function
--------



The **display bgp vpnv6 group** command is used to display the VPNv6 peer group information.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp** [ **instance** *bgpName* ] **vpnv6** **vpn-instance** *vpn-instance-name* **group**

**display bgp** [ **instance** *bgpName* ] **vpnv6** **vpn-instance** *vpn-instance-name* **group** *group-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **instance** *bgpName* | Specifies the BGP multi-instance name. | The value is a string of 1 to 31 case-sensitive characters without any spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **vpn-instance** *vpn-instance-name* | Specify a VPN-Instance (VRF) name. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| *group-name* | Specifies a peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The **display bgp vpnv6 group** command is used to display the VPNv6 peer group information.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the VPNv6 peer group information.
```
<HUAWEI> display bgp vpnv6 vpn-instance vpn6 group
BGP peer-group      : g1
 Remote AS 65410
 Type               : external
 PeerSession Members:
   2001:DB8:2000::2
 
 Peer Members:
   2001:DB8:2000::2

```

**Table 1** Description of the **display bgp vpnv6 group** command output
| Item | Description |
| --- | --- |
| BGP peer-group | BGP peer group name. |
| Remote AS | Number of the AS where a peer group resides. |
| Type | Type of a peer group:   * internal: IBGP peer group. * external: EBGP peer group. |
| PeerSession Members | Peers that set up session connections. |
| Peer Members | The following information is about peers. |
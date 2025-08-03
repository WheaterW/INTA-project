display bgp vpnv6 all group
===========================

display bgp vpnv6 all group

Function
--------



The **display bgp vpnv6 all group** command displays all the VPNv6 peer groups information.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp** [ **instance** *bgpName* ] **vpnv6** **all** **group** [ *group-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **instance** *bgpName* | Specifies the name of a BGP multi-instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| *group-name* | Specifies a peer-group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The **display bgp vpnv6 all group** command is used to display all the VPNv6 peer group information.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display all the VPNv6 peer groups information.
```
<HUAWEI> display bgp vpnv6 all group
Group in VPNV6:
 
 BGP peer-group     : 123
 Remote AS number isn't specified
 Type               : external
 PeerSession Members:
   2001:DB8:1::1
 
 Peer Members:
  No Peer Exists
 ***********************
 
 BGP peer-group     : 222
 Remote AS 200
 Type               : internal
 PeerSession Members:
   2001:DB8:2::2
 
 Peer Members:
  No Peer Exists
 ***********************
 
 BGP peer-group     : 333
 Remote AS 400
 Type               : external
 PeerSession Members:
   2001:DB8:3::3
 
 Peer Members:
  No Peer Exists
 
 
Group in VPN-Instance:
 
 BGP peer-group           : 55
 Remote AS number isn't specified
 VPN-Instance(IPv6-family): vpn1
 
 Type : external
 PeerSession Members:
   2001:DB8:4::4
 
 Peer Members:
   2001:DB8:4::4

```

**Table 1** Description of the **display bgp vpnv6 all group** command output
| Item | Description |
| --- | --- |
| Group in VPN-Instance | Information about peer groups in a VPN instance is displayed. |
| Group in VPNV6 | Information about all VPNv6 peer groups is displayed. |
| Remote AS number isn't specified | This item is displayed when the peer group is a mixed EBGP peer group. |
| Type | Type of a peer group:   * internal: indicates that the peer group is an IBGP peer group. * external: indicates that the peer group is an EBGP peer group. * listen internal: indicates that the peer group is a dynamic IBGP peer group. * listen external: indicates that the peer group is a dynamic EBGP peer group. * listen confederation-external: indicates that the peer group is a dynamic confederation EBGP peer group. |
| PeerSession Members | Peers with which sessions have been established. |
| Peer Members | Peer information. |
| VPN-Instance | VPN instance name. |
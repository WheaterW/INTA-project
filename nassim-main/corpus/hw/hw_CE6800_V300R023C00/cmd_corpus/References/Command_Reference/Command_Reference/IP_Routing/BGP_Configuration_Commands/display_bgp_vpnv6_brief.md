display bgp vpnv6 brief
=======================

display bgp vpnv6 brief

Function
--------



The **display bgp vpnv6 brief** command displays brief information about IPv6 VPN instances.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp** [ **instance** *bgpName* ] **vpnv6** **all** **brief**

**display bgp** [ **instance** *bgpName* ] **vpnv6** **vpn-instance** *vpn-instance-name* **brief**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **instance** *bgpName* | Specifies the name of a BGP multi-instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. |
| **all** | Displays information about all VPN instances. | - |
| **vpn-instance** *vpn-instance-name* | Specifies the name of an IPv6 VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

When you run the **display bgp vpnv6 brief** command to view information about IPv6 VPN instances, the IPv6 VPN instances are listed in lexicographic order by name.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display brief information about VPNv6 and all IPv6 VPN instances.
```
<HUAWEI> display bgp vpnv6 all brief
VPNV6 :
  Rd Num              Peer Num            Route Num
  0                   1                   0

VPN-Instance(IPv6-family):
  VPN-Instance Name   Peer Num            Route Num
  vrf0                   0                   0
  vrf1                   0                   0
  vrf11                  0                   0
  vrf12                  0                   0
  vrf13                  0                   0
  vrf14                  0                   0
  vrf2                   0                   20
  vrf3                   0                   20
  vrf4                   0                   24
  vrf5                   0                   24
  vrf6                   0                   0

```

**Table 1** Description of the **display bgp vpnv6 brief** command output
| Item | Description |
| --- | --- |
| VPNV6 | BGP-VPNv6 address family. |
| Rd Num | Number of RDs. |
| Peer Num | Number of peers. |
| Route Num | Number of routes. |
| VPN-Instance Name | Name of a VPN instance. |
| VPN-Instance(IPv6-family) | BGP-VPN instance IPv6 address family. |
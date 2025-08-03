display bgp vpnv6 network
=========================

display bgp vpnv6 network

Function
--------



The **display bgp vpnv6 network** command displays the routes imported into the BGP VPNv6 routing table using the network command.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp** [ **instance** *bgpName* ] **vpnv6** **all** **network**

**display bgp** [ **instance** *bgpName* ] **vpnv6** **vpn-instance** *vpn-instance-name* **network**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **instance** *bgpName* | Specifies the BGP multi-instance name. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **all** | Display all information on VPNv6 routes. | - |
| **vpn-instance** *vpn-instance-name* | Specifies a VPN instance name. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The **display bgp vpnv6 network** command displays the routes imported into the BGP VPNv6 routing table using the **network** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the routes imported into the BGP VPNv6 routing table using the network command.
```
<HUAWEI> display bgp vpnv6 all network
BGP Local Router ID is 10.2.2.9
Local AS Number is 100

Route Distinguisher: 100:5
(vrf1)
Network          Prefix            Route-policy
2001:DB8:3::3    128

Route Distinguisher: 100:9
(vrf2)
Network          Prefix            Route-policy
2001:DB8:8::9    128

```

**Table 1** Description of the **display bgp vpnv6 network** command output
| Item | Description |
| --- | --- |
| BGP Local Router ID is | Router ID of the local device, in the format of an IPv4 address. |
| Local AS Number is | Local AS number. |
| Router ID | Router ID of the device. |
| Route Distinguisher | Route distinguisher. |
| Network | Locally advertised network address. |
| Prefix | Network address mask of an imported route. |
| Route-policy | Used routing policy. |
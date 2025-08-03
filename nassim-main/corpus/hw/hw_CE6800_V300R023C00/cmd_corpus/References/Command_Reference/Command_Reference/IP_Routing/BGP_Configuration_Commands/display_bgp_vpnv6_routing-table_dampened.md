display bgp vpnv6 routing-table dampened
========================================

display bgp vpnv6 routing-table dampened

Function
--------



The **display bgp vpnv6 routing-table dampened** command displays dampened BGP VPNv6 routes.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp** [ **instance** *bgpName* ] **vpnv6** **vpn-instance** *vpn-instance-name* **routing-table** **dampened**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **instance** *bgpName* | Specifies the name of a BGP multi-instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **vpn-instance** *vpn-instance-name* | Specify a VPN-Instance (VRF) name. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The **display bgp vpnv6 routing-table dampened** command displays dampened BGP VPNv6 routes.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display dampened BGP VPNv6 routes.
```
<HUAWEI> display bgp vpnv6 vpn-instance vpn1 routing-table dampened
 BGP Local router ID is 10.1.1.1
 Status codes: * - valid, > - best, d - damped, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
 Origin      : i - IGP, e - EGP, ? - incomplete
 Total Number of Routes: 3
    Network           From              Reuse     Path/Origin
 d  2001:DB8:1::1     2001:DB8:20::20   00:09:33  1.1 100?
 d  2001:DB8:1::2     2001:DB8:20::20   00:09:33  1.1 100?
 d  2001:DB8:1::3     2001:DB8:20::20   00:09:33  1.1 100?

```

**Table 1** Description of the **display bgp vpnv6 routing-table dampened** command output
| Item | Description |
| --- | --- |
| Total Number of Routes | Total number of routes. |
| Network | Indicates the network address in the BGP routing table. |
| From | IP address of the peer from which the route is learned. |
| Reuse | Reuse value (in seconds). |
| Path | Indicates the AS\_Path number and the Origin attribute. |
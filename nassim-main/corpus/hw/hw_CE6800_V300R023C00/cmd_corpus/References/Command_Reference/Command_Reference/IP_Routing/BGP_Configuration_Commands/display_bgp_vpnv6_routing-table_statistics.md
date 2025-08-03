display bgp vpnv6 routing-table statistics
==========================================

display bgp vpnv6 routing-table statistics

Function
--------



The **display bgp vpnv6 routing-table statistics** command displays statistics about BGP VPNv6 routes.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp vpnv6** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **statistics**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Displays BGP VPNv6 routes and BGP4+ routes of VPN instances. | - |
| **vpn-instance** *vpn-instance-name* | Displays the BGP routing information of the specified VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run this command to view statistics about BGP VPNv6 routes and BGP4+ VPN routes.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about BGP VPNv6 routes.
```
<HUAWEI> display bgp vpnv6 all routing-table statistics
 
 Total number of routes from all PE: 2

 VPN-Instance vrf, Router ID 10.1.123.1:
 Total Number of Routes: 2

```

**Table 1** Description of the **display bgp vpnv6 routing-table statistics** command output
| Item | Description |
| --- | --- |
| Total number of routes from all PE | Total number of VPNv6 routes. |
| Total Number of Routes | Number of routes in a VPN instance. |
| VPN-Instance | Name of a VPN instance. |
| Router ID | Router ID of the VPN instance. |
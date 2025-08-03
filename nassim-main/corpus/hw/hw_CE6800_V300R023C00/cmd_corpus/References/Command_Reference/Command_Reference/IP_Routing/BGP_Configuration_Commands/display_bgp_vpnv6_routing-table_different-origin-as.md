display bgp vpnv6 routing-table different-origin-as
===================================================

display bgp vpnv6 routing-table different-origin-as

Function
--------



The **display bgp vpnv6 routing-table different-origin-as** command is used to display the VPNv6 routes with the same destination address but different source AS numbers.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp** [ **instance** *bgpName* ] **vpnv6** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **different-origin-as**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **instance** *bgpName* | Specifies the BGP multi-instance name. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **all** | Displays all the routes in the specified address family. | - |
| **vpn-instance** *vpn-instance-name* | Specifies a VPN instance name. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The **display bgp vpnv6 routing-table different-origin-as** command is used to display the VPNv6 routes with the same destination address but different source AS numbers.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the BGP VPNv6 routes with the same destination address but different source AS numbers.
```
<HUAWEI> display bgp vpnv6 all routing-table different-origin-as
 
 Total number of routes from all PE: 0

```

**Table 1** Description of the **display bgp vpnv6 routing-table different-origin-as** command output
| Item | Description |
| --- | --- |
| Total number of routes from all PE | Total number of BGP VPNv6 routes received by the device from its peer PEs. |
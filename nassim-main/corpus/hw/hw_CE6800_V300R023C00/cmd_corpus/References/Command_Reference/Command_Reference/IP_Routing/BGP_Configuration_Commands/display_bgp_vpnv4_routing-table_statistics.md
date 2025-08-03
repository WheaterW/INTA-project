display bgp vpnv4 routing-table statistics
==========================================

display bgp vpnv4 routing-table statistics

Function
--------



The **display bgp vpnv4 routing-table statistics** command displays statistics about BGP VPNv4 routes.




Format
------

**display bgp vpnv4** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **statistics**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Displays BGP routing information of VPNv4 and VPN instances. | - |
| **vpn-instance** *vpn-instance-name* | Displays the BGP routing information of the specified VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run this command to view statistics about BGP VPNv4 routes and BGP VPN routes.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about BGP VPNv4 routes.
```
<HUAWEI> display bgp vpnv4 all routing-table statistics
 
 Total number of routes from all PE: 2

 VPN-Instance vrf, Router ID 10.1.123.1:
 Total Number of Routes: 2

```

**Table 1** Description of the **display bgp vpnv4 routing-table statistics** command output
| Item | Description |
| --- | --- |
| Total number of routes from all PE | Total number of VPNv4 routes. |
| Total Number of Routes | Number of routes in a VPN instance. |
| VPN-Instance | Name of a VPN instance. |
| Router ID | Router ID of the VPN instance. |
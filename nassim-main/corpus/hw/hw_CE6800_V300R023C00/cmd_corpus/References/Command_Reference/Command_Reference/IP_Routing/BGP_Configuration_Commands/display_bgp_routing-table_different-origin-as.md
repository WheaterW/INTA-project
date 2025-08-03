display bgp routing-table different-origin-as
=============================================

display bgp routing-table different-origin-as

Function
--------



The **display bgp vpnv4 routing-table different-origin-as** command displays information about routes with the same destination address&mask but originating from different origin ASs.




Format
------

**display bgp vpnv4** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **different-origin-as**

**display bgp instance** *instance-name* **vpnv4** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **different-origin-as**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Displays statistics about all BGP VPNv4 routes. | - |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **different-origin-as** | Displays routes that have the same destination address but different source AS numbers. | - |
| **instance** *instance-name* | Specifies a BGP instance. | The value is a string of 1 to 31 case-sensitive characters without spaces. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The **display bgp vpnv4 routing-table different-origin-as** command displays information about routes with the same destination address&mask but originating from different origin ASs.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about the routes with the same destination address but different origin AS numbers in the BGP-VPNv4 address family.
```
<HUAWEI> display bgp vpnv4 all routing-table different-origin-as
 
 Total number of routes from all PE: 0

```

**Table 1** Description of the **display bgp routing-table different-origin-as** command output
| Item | Description |
| --- | --- |
| Total number of routes from all PE | Number of routes with the same destination address but different origin AS numbers. |
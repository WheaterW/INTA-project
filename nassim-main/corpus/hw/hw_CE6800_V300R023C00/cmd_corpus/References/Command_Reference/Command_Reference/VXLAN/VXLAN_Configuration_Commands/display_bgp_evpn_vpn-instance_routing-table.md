display bgp evpn vpn-instance routing-table
===========================================

display bgp evpn vpn-instance routing-table

Function
--------



The **display bgp evpn vpn-instance routing-table** command displays information about BGP-EVPN routes.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp evpn vpn-instance** *evpn-name-value* **routing-table** { **ad-route** | **es-route** | **inclusive-route** | **mac-route** }

**display bgp evpn vpn-instance** *evpn-name-value* **routing-table** { **ad-route** | **inclusive-route** | **mac-route** } **extcommunity** { **rt** *strExtCommunity* } &<1-33>

**display bgp evpn vpn-instance** *evpn-name-value* **routing-table** { **ad-route** | **inclusive-route** | **mac-route** } **extcommunity** { **rt** *strExtCommunity* } &<1-33> **match-any**

**display bgp instance** *bgpName* **evpn** **vpn-instance** *evpn-name-value* **routing-table** { **ad-route** | **inclusive-route** | **mac-route** } **extcommunity** { **rt** *strExtCommunity* } &<1-33>

**display bgp instance** *bgpName* **evpn** **vpn-instance** *evpn-name-value* **routing-table** { **ad-route** | **inclusive-route** | **mac-route** } **extcommunity** { **rt** *strExtCommunity* } &<1-33> **match-any**

**display bgp instance** *bgpName* **evpn** **vpn-instance** *evpn-name-value* **routing-table** { **ad-route** | **es-route** | **inclusive-route** | **mac-route** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ad-route** | Displays information about Ethernet A-D routes. | - |
| **es-route** | Displays information about Ethernet segment routes. | - |
| **inclusive-route** | Displays information about inclusive multicast routes. | - |
| **mac-route** | Displays information about MAC advertisement routes. | - |
| **vpn-instance** *evpn-name-value* | Displays information about EVPN routes of a specified EVPN instance. | The value is a string of 1 to 31 case-sensitive characters without spaces. When double quotation marks are used around the string, spaces are allowed in the string. |
| **extcommunity** | Displays the routes with the specified extended community attribute. | - |
| **rt** *strExtCommunity* | Specifies the extended community attribute of the VPN-Target type. | The options are as follows:   * as-number:nn * 4as-number:nn * ipv4-address:nn   as-number specifies the AS number. The value is an integer that ranges from 0 to 65535.  4as-number is a 4-byte AS number, which can be:   * The value is an integer that ranges from 65536 to 4294967295. * The value is in the format of x.y, where x and y are integers ranging from 0 to 65535.   ipv4-address is an IPv4 address in dotted decimal notation. nn is an integer. For as-number and 4as-number, the value ranges from 0 to 4294967295. For ipv4-address, the value ranges from 0 to 65535. |
| **match-any** | Displays information about the routes that match any of the specified extended community attributes. | - |
| **instance** *bgpName* | Displays the routes of a specified BGP multi-instance. | The value is a string of 1 to 31 case-sensitive characters without spaces. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To check information about all active and inactive BGP-EVPN routes, run the display bgp mvpn routing-table command. You can specify different parameters to check specific routing information.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display MAC routes filtered based on RTs.
```
<HUAWEI> display bgp evpn vpn-instance e1 routing-table mac-route extcommunity rt 1:1
 BGP Local router ID is 10.1.1.1
 Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
               Origin : i - IGP, e - EGP, ? - incomplete

 
  EVPN-Instance e1:
 Number of Mac Routes: 1
       Network(EthTagId/MacAddrLen/MacAddr/IpAddrLen/IpAddr)  NextHop                                      Extcommunity
 *>i   0:48:00e0-fc12-3456:0:0.0.0.0                          2001:DB8:1::144                              RT <1 : 1>, SoO <10.1.1.144 : 0>, Mac Mobility <flag:1 seq:0 res:0>

```

**Table 1** Description of the **display bgp evpn vpn-instance routing-table** command output
| Item | Description |
| --- | --- |
| BGP Local router ID | Router ID of the local device. |
| EVPN-Instance | EVPN instance name. |
| Number of Mac Routes | Number of MAC routes. |
| Mac Mobility | Extended community attribute for MAC address migration. |
| NextHop | Next hop information about routes. |
| Extcommunity | Extended community attribute. |
| SoO | SoO extended community attribute. |
| Network | Network information of the route. |
| EthTagId | VLAN ID. |
| MacAddrLen | MAC address length. |
| MacAddr | MAC address. |
| IpAddrLen | Length of the IP address mask. |
| IpAddr | IPv4 address. |
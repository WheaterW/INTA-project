display pim ipv6 claimed-route
==============================

display pim ipv6 claimed-route

Function
--------



The **display pim ipv6 claimed-route** command displays IPv6 unicast routes used by PIM.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display pim ipv6 claimed-route** [ *ipv6-source-address* ]

**display pim ipv6** { **vpn-instance** *instance-name* | **all-instance** } **claimed-route** [ *ipv6-source-address* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-source-address* | Specifies the IPv6 address of a multicast source. | The address is in the format of X:X:X:X:X:X:X:X. |
| **vpn-instance** *instance-name* | Displays information about unicast routes in a specified VPN instance.  vpn-instance-name specifies the name of a VPN instance. | The value is a string of case-sensitive characters. |
| **all-instance** | Specifies all VPN instance. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The **display pim ipv6 claimed-route** command is used to display IPv6 unicast routes used by PIM. The command output includes information about reverse path forwarding (RPF) neighbors, detailed interface information, route types, and route selection policies.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the IPv6 unicast routes to multicast source 2001:DB8:1::1.
```
<HUAWEI> display pim ipv6 claimed-route 2001:DB8:1::1
VPN-Instance: public net
RPF information about: 2001:DB8:1::1 in PIM-SM routing table
RPF interface: 100GE1/0/1, RPF neighbor: FE80::A01:100:1
Referenced route/mask: 2001:DB8:1::/64
Referenced route type: igp
RPF-route selecting rule: preference-preferred
The (S, G) or (*, G) list dependent on this route entry
(2001:DB8:1::1, FF03::1)

```

# Display information about unicast routes in the VPN instance VPNA after an NG MVPN is configured.
```
<HUAWEI> display pim ipv6 vpn-instance vpn1 claimed-route
 VPN-Instance: vpn1
 RPF information about: 2001:DB8:1::1 in PIM-SM routing table
     RPF interface: through-BGP, RPF neighbor: ::FFFF:12.12.12.12 
     Referenced route/mask: 2001:DB8:1::/64 
     Referenced route type: unicast
     RPF-route selecting rule: preference-preferred 
     VRF Route Import Extended Community : 12.12.12.12:1
     Source AS Extended Community : 100
     The (S, G) or (*, G) list dependent on this route entry
     (*, FF2E::1)

```

**Table 1** Description of the **display pim ipv6 claimed-route** command output
| Item | Description |
| --- | --- |
| RPF information about | RPF route with the specified IPv6 address as the source in the PIM-SM routing table. |
| RPF interface | RPF interface. |
| RPF neighbor | RPF neighbor. |
| Referenced route/mask | Referenced route/mask. |
| Referenced route type | Reference route type:   * unicast: unicast routes. * unicast (direct): unicast direct routes. * egp: Exterior Gateway Protocol (EGP) routes. * mbgp: MBGP routes. * multicast static: multicast static routes. * igp: IGP routes. |
| RPF-route selecting rule | RPF route selection rule. |
| VRF Route Import Extended Community | VRF Route Import Extended Community attribute in the MVPN extended community attributes. |
| Source AS Extended Community | Source AS Extended Community attribute in the MVPN extended community attributes. |
| VPN-Instance | VPN instance to which the output information belongs. |
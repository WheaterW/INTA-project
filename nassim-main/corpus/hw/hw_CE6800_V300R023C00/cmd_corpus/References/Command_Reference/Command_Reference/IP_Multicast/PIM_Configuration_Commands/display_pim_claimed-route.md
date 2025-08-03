display pim claimed-route
=========================

display pim claimed-route

Function
--------



The **display pim claimed-route** command displays information about unicast routes used by PIM.




Format
------

**display pim** { **vpn-instance** *vpn-instance-name* | **all-instance** } **claimed-route** [ *source-address* ]

**display pim claimed-route** [ *source-address* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of case-sensitive characters. |
| **all-instance** | Specifies all instances. | - |
| *source-address* | Displays information about unicast routes to a specified multicast source.  source-address specifies the address of a multicast source. | The value is in dotted decimal notation. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

The **display pim claimed-route** command can be used to display the information about unicast routes used by PIM. The command output includes information about reverse path forwarding (RPF) neighbors, detailed interface information, route types, and route selection policies.

**Precautions**

Differences between the **display pim claimed-route** command and the **display multicast rpf-info** command are as follows:

* The **display multicast rpf-info** command displays information about RPF neighbors, RPF interfaces, and whether there is a route to a specified source address.
* The **display pim claimed-route** command displays information about unicast routes used by multicast routing and entries of the routes.If neither vpn-instance nor all-instance is specified, the command displays information about unicast routes used by PIM in the public network instance.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about unicast routes used by PIM-DM in the public network instance.
```
<HUAWEI> display pim claimed-route
 VPN-Instance: public net
 RPF information about: 10.1.4.100 in PIM-DM routing table
     RPF interface: 100GE1/0/1, RPF neighbor: 10.1.3.1
     Referenced route/mask: 10.1.4.0/24
     Referenced route type: igp
     RPF-route selecting rule: preference-preferred
     The (S,G) list dependent on this route entry
     (10.1.4.100, 225.1.1.1)

```

# Display information about unicast routes used by PIM-SM in the public network instance.
```
<HUAWEI> display pim claimed-route
 VPN-Instance: public net
 RPF information about: 10.1.0.0 in PIM-SM routing table
     RPF interface: 100GE1/0/1, RPF neighbor: 10.1.2.2
     Referenced route/mask: 10.1.0.0/24
     Referenced route type: igp
     RPF-route selecting rule: preference-preferred
     The (S, G) or (*, G) list dependent on this route entry
     (10.1.0.1, 225.0.0.1)

```

# Display information about unicast routes in the VPN instance VPNA after an NG MVPN is configured.
```
<HUAWEI> display pim vpn-instance VPNA claimed-route
 VPN-Instance: VPNA
 multicast load-splitting rule: source-group
 RPF information about: 10.1.0.0 in PIM-SM routing table
     RPF interface: 100GE1/0/1, RPF neighbor: 10.1.2.2
     Referenced route/mask: 10.1.0.0/24
     Referenced route type: igp
     RPF-route selecting rule: preference-preferred
     VRF Route Import Extended Community : 10.1.1.1:123
     Source AS Extended Community :  12346:0
     The (S, G) or (*, G) list dependent on this route entry
     (10.1.0.1, 225.0.0.1)

```

**Table 1** Description of the **display pim claimed-route** command output
| Item | Description |
| --- | --- |
| RPF interface | RPF interface. |
| RPF neighbor | RPF neighbor. |
| RPF information about: 10.1.0.0 in PIM-SM routing table | RPF route with the source IP address in the PIM-SM routing table. |
| RPF information about: 10.1.4.100 in PIM-DM routing table | RPF route with the source IP address in the PIM-DM routing table. |
| Referenced route/mask | Referenced route/mask. |
| Referenced route type | Type of the referenced unicast route:   * unicast: unicast routes. * unicast (direct): unicast direct routes. * egp: External Gateway Protocol (EGP) routes. * mbgp: multicast BGP routes. * multicast static: multicast static routes. * migp: multicast IGP routes. * igp: IGP routes. * multicast: multicast routes. |
| RPF-route selecting rule | RPF route selection rule. preference-preferred indicates that routes are selected based on the preferences of routing protocols. |
| VRF Route Import Extended Community | VRF Route Import Extended Community attribute in the MVPN extended community attributes. |
| Source AS Extended Community | Source AS Extended Community attribute in the MVPN extended community attribute. |
| VPN-Instance | Instance in which information about unicast routes is displayed. |
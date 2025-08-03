display multicast ipv6 rpf-info
===============================

display multicast ipv6 rpf-info

Function
--------



The **display multicast ipv6 rpf-info** command displays Reverse Path Forwarding (RPF) routing information of an IPv6 source or an IPv6 source group, including currently used topology name and information about all routes.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display multicast ipv6 rpf-info** *ipv6-source-address* [ *ipv6-group-address* ] [ **rpt** | **spt** ] [ **verbose** ]

**display multicast ipv6** { **vpn-instance** *instance-name* | **all-instance** } **rpf-info** *ipv6-source-address* [ *ipv6-group-address* ] [ **rpt** | **spt** ] [ **verbose** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-source-address* | Specifies the IPv6 address of a multicast source. If this parameter is specified, RPF routing information of this multicast source is displayed. | The address is in the format of X:X:X:X:X:X:X:X. |
| *ipv6-group-address* | Specifies the IPv6 address of a multicast group. If this parameter is specified, RPF routing information of this source group is displayed. | The address ranges from FF00::0 to FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF. |
| **rpt** | Display the information of shortest path tree (SPT). | - |
| **spt** | Display the information of rendezvous point tree (RPT). | - |
| **verbose** | Displays detailed RPF information. | - |
| **vpn-instance** *instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **all-instance** | Specifies all VPN instance. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

An RPF route is an optimal route with the destination address being source-address and selected from the unicast routing table and static multicast routing table.To display the RPF routing information of a specified multicast source, such as the information about the multicast source, status of the RPF interface, RPF neighbor, and routing information, run the **display multicast ipv6 rpf-info** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display detailed information about the RPF route to source 2001:db8:1::.
```
<HUAWEI> display multicast ipv6 all-instance rpf-info 2001:DB8:1:: verbose
 VPN-Instance: vpn1
 RPF information about source: 2001:DB8:1::
     RPF used topology: default
     RPF interface: pseudo, RPF neighbor: 2001:DB8:2::
     Referenced route/mask: 2001:DB8:1::/128
     Referenced route type: bgp
     Route selection rule: preference-preferred
     Load splitting rule: disable
     VRF Route Import Extended Community : <2001:DB8:2:: . 1>
     Source AS Extended Community : 100
     Backup RPF used topology: default
     Backup RPF interface: pseudo, RPF neighbor: 2001:DB8:3::
     Backup VRF Route Import Extended Community : <2001:DB8:3:: . 1>
     Backup Source AS Extended Community : 100
 Total route information about source 2001:DB8:1::
 1  .Referenced interface: 
     Referenced route/mask: 2001:DB8:1::/128
     Referenced route type: bgp
     Referenced route preference: 255
     Referenced route cost: 3
     Referenced route nexthop: 2001:DB8:2::

```

# Display detailed information about the RPF route to source 2001:db8:1::.
```
<HUAWEI> display multicast ipv6 rpf-info 2001:db8:1:: verbose
VPN-Instance: public net
 RPF information about source: 2001:DB8:1::
     RPF used topology: default
     RPF interface: 100GE1/0/1, RPF neighbor: FE80:4000::7 
     Referenced route/mask: 2001:DB8:1::/64                                           
     Referenced route type: unicast
     Load splitting rule: balance-preferred                                     
 Total route information about source 2001:DB8:1::
 1. Referenced interface:100GE1/0/2
    Referenced route/mask: 2001:DB8:1::/64
    Referenced route type: unicast
    Referenced route preference: 15
    Referenced route cost: 20
    Referenced route nexthop: FE80:3000::7   
 2. Referenced interface: 100GE1/0/1.1
    Referenced route/mask: 2001:DB8:1::/64 
    Referenced route type: unicast
    Referenced route preference: 15
    Referenced route cost: 20
    Referenced route nexthop: FE80::2E0:CBFF:FE53:8242
 3. Referenced interface: 100GE1/0/1
    Referenced route/mask: 2001:DB8:1::/64
    Referenced route type: unicast
    Referenced route preference: 15
    Referenced route cost: 20
    Referenced route nexthop: FE80:4000::7

```

# Display information about the RPF route to multicast source 2001:db8:1::1.
```
<HUAWEI> display multicast ipv6 rpf-info 2001:db8:1::1
VPN-Instance: public net
RPF information about source: 2001:DB8:1::1
RPF interface: 100GE1/0/1
Referenced route/mask: 2001:DB8:1::/64
Referenced route type: unicast
Load splitting rule: disable

```

**Table 1** Description of the **display multicast ipv6 rpf-info** command output
| Item | Description |
| --- | --- |
| RPF information about source | Multicast source to which RPF information belongs. |
| RPF interface | RPF interface. |
| RPF used topology | Topology used by the RPF route. |
| RPF neighbor | RPF neighbor. |
| Referenced route/mask | Referenced route and its mask. |
| Referenced route type | Referenced route type.   * unicast: unicast route. * MBGP: MBGP route. * mstatic: static multicast routes. * MIGP: MIGP route. |
| Referenced interface | Outbound interface of a route. |
| Referenced route preference | Priority. |
| Referenced route cost | Route cost. |
| Referenced route nexthop | Next hop. |
| Route selection rule | RPF route selection rule. preference-preferred indicates that routes are selected based on the preferences of routing protocols. |
| Load splitting rule | Multicast load splitting rules:   * disable: Multicast load splitting is disabled. * stable-preferred: stable-preferred load splitting. * source: source address-based load splitting. * group: group address-based load splitting. * source-group: source and group addresses-based load splitting. |
| VRF Route Import Extended Community | VRF Route Import Extended Community attribute in the MVPN extended community attributes. |
| Source AS Extended Community | Source AS Extended Community attribute in the MVPN extended community attributes. |
| Backup RPF interface | Backup RPF interface. |
| Backup VRF Route Import Extended Community | VRF Route Import Extended Community attribute in the backup route. |
| Backup Source AS Extended Community | Source AS Extended Community attribute in the backup route. |
| Backup RPF used topology | Topology used by the backup RPF route. |
| Total route information about source 2001:DB8:1:: | Information about all RPF routes to source 2001:DB8:1::. |
| VPN-Instance | VPN instance to which RPF routing information belongs. |
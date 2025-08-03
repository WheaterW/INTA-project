display multicast rpf-info
==========================

display multicast rpf-info

Function
--------



The **display multicast rpf-info** command displays the Reverse Path Forwarding (RPF) routes of a specified multicast source or source/group, including currently used topology name and information about all routes.




Format
------

**display multicast** { **vpn-instance** *vpn-instance-name* | **all-instance** } **rpf-info** *source-address* [ *group-address* ] [ **rpt** | **spt** ] [ **verbose** ]

**display multicast rpf-info** *source-address* [ *group-address* ] [ **rpt** | **spt** ] [ **verbose** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **all-instance** | Specifies all instances. | - |
| *source-address* | Specifies the address of a multicast source, used to display the information of RPF routing corresponding to the source. | The value is in dotted decimal notation. |
| *group-address* | Specifies the multicast group address, used to display the information of RPF routing corresponding to the source/group. | The address is in dotted decimal notation. The value ranges from 224.0.0.0 to 239.255.255.255. |
| **rpt** | Display the information of rendezvous point tree (RPT). | - |
| **spt** | Display the information of shortest path tree (SPT). | - |
| **verbose** | Displays detailed RPF information. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

The RPF route with the source-address as the destination address is an optimal route selected from unicast routes and multicast static routes.The **display multicast rpf-info** command can be used to display the information about the RPF route to a specified multicast source, such as the information about the multicast source, status of the RPF interface, RPF neighbor, and route.

**Precautions**

If neither vpn-instance nor all-instance is specified, the command displays information about PIM interfaces in the public network instance.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display RPF routes of VPN BLUE with the source address 10.1.1.2 in VPN RED after an MVPN extranet is configured.
```
<HUAWEI> display multicast vpn-instance RED rpf-info 10.1.1.2 228.0.0.1
 VPN-Instance: RED
 RPF information about source 10.1.1.2 and group 228.0.0.1
     RPF interface: MCAST_Extranet
     RPF Source VPN-Instance: BLUE
     Referenced route/mask: 10.1.1.0/24
     Referenced route type: unicast
     Route selection rule: preference-preferred
     Load splitting rule: disable

```

# Display all the RPF routes to the source address 172.16.0.1 in the public network instance.
```
<HUAWEI> display multicast rpf-info 172.16.0.1
VPN-Instance: public net
 RPF information about source: 172.16.0.1
     RPF interface: 100GE1/0/1, RPF neighbor: 10.1.5.2
     Referenced route/mask: 172.16.0.0/24
     Referenced route type: unicast
     Route selection rule: preference-preferred
     Load splitting rule: disable

```

**Table 1** Description of the **display multicast rpf-info** command output
| Item | Description |
| --- | --- |
| RPF information about source | Multicast source to which the RPF route belongs. |
| RPF interface | RPF interface, including the actual interface and MVPN extranet interface. |
| RPF neighbor | RPF neighbor. |
| RPF Source VPN-Instance | Source VPN instance of the RPF route. |
| Referenced route/mask | Referenced route and its mask. |
| Referenced route type | Protocol type:   * unicast. * mstatic. * migp. * mbgp. * bgp. * bgp-multicast. |
| Route selection rule | RPF route selection rule. preference-preferred indicates that routes are selected based on the preferences of routing protocols. |
| Load splitting rule | Load splitting rules:   * disable: load splitting disabled. * stable-preferred: stable-preferred load splitting. * source: source address-based load splitting. * group: group address-based load splitting. * source-group: source and group addresses-based load splitting. |
| VPN-Instance | VPN instance to which displayed information belongs. |
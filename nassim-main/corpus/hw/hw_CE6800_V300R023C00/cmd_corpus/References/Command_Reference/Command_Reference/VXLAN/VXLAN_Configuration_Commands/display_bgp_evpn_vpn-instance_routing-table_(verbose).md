display bgp evpn vpn-instance routing-table (verbose)
=====================================================

display bgp evpn vpn-instance routing-table (verbose)

Function
--------



The **display bgp evpn vpn-instance routing-table** command displays information about BGP-EVPN routes.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp evpn vpn-instance** *evpn-name-value* **routing-table** { **ad-route** | **es-route** | **inclusive-route** | **mac-route** } *prefix*

**display bgp** [ **instance** *bgpName* ] **evpn** **vpn-instance** *evpn-name-value* **routing-table** { **ad-route** | **es-route** | **inclusive-route** | **mac-route** } *prefix*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ad-route** | Displays information about Ethernet A-D routes. | - |
| **es-route** | Displays information about Ethernet segment routes. | - |
| **inclusive-route** | Displays information about inclusive multicast routes. | - |
| **mac-route** | Displays information about MAC advertisement routes. | - |
| *prefix* | Specifies the prefix of an EVPN route. | An EVPN route prefix has the following formats:  Inclusive multicast route. The value is in the format of M:L:X.X.X.X, where:   * M is fixed at 0. * X.X.X.X indicates the source address configured for the device originating the route. * L indicates the mask length of the source address configured for the device originating the route.   MAC advertisement route. The value is in the format of E:M:H-H-H:L:X.X.X.X or E:M:H-H-H:L: [X:X::X:X], where:   * E indicates the ID of the VLAN to which the MAC address belongs. * M is fixed at 48, indicating the length of the MAC address. * H-H-H indicates the MAC address. The value is a 12-digit hexadecimal number, in the format of H-H-H. Each H contains 1 to 4 digits, such as 00e0 or fc01. If an H contains fewer than 4 digits, the left-most digits are padded with 0s. For example, e0 is displayed as 00e0. * L is fixed at 0, indicating the mask length of the IP address corresponding to the MAC address. * X.X.X.X indicates the IP address corresponding to the MAC address. Currently, this part can only be displayed as 0.0.0.0. * X:X::X:X indicates the IPv6 address corresponding to the MAC address.   IP prefix route. The value is in the format of L:X.X.X.X:M or L:[X:X::X:X]:M, where:   * L is fixed at 0. * X.X.X.X indicates the IP address of host routes. * M indicates the mask length of host routes. * X:X::X:X indicates the IPv6 address of host routes. |
| **vpn-instance** *evpn-name-value* | Displays information about EVPN routes of a specified EVPN instance. | The value is a string of 1 to 31 case-sensitive characters without spaces. When double quotation marks are used around the string, spaces are allowed in the string. |
| **instance** *bgpName* | Displays the routes of a specified BGP multi-instance. | The value is a string of 1 to 31 case-sensitive characters without spaces. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can specify different parameters in this command to view information about routes as required.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about EVPN routes with the MAC route prefix 0:48:00e0-fc12-3456:0:0.0.0.0.
```
<HUAWEI> display bgp evpn vpn-instance e1 routing-table mac-route 0:48:00e0-fc12-3456:0:0.0.0.0


 BGP local router ID : 10.1.1.43
 Local AS number : 100


 EVPN-Instance e1:
 Number of Mac Routes: 1
 BGP routing table entry information of 0:48:00e0-fc12-3456:0:0.0.0.0:
 Route Distinguisher: 1:1
 Remote-Cross route
 Label information (Received/Applied): 3/NULL
 From: 2001:db8:1::1 (10.1.1.141)
 Route Duration: 0d00h03m39s
 Relay IP Nexthop: FE80::AA49:4DFF:FE84:32F6
 Relay IP Out-Interface: 100GE1/0/1
 Relay Tunnel Out-Interface:
 Original nexthop: 2001:DB8:1::2
 Qos information : 0x0
 Ext-Community: RT <1 : 1>, SoO <10.1.1.144 : 0>, Mac Mobility <flag:1 seq:0 res:0>
 Prefix-sid: 2001:DB8:2::1
 AS-path Nil, origin igp, localpref 100, pref-val 0, valid, internal, best, select, pre 255, IGP cost 20
 Originator: 10.1.1.144
 Cluster list: 10.1.1.141
 Route Type: 2 (MAC Advertisement Route)
 Ethernet Tag ID: 0, MAC Address/Len: 00e0-fc12-3456/48, IP Address/Len: 0.0.0.0/0, ESI:0000.0144.0144.0144.0144
 Not advertised to any peer yet

```

**Table 1** Description of the **display bgp evpn vpn-instance routing-table (verbose)** command output
| Item | Description |
| --- | --- |
| BGP local router ID | Router ID of the local device. |
| BGP routing table entry information of | Routing entry information. |
| local | Local route. |
| Local AS number | Local AS number. |
| EVPN-Instance | EVPN instance name. |
| Number of Mac Routes | Number of MAC advertisement routes. |
| Mac Mobility | Extended community attribute for MAC address migration. |
| Route Distinguisher | RD of the EVPN routes. |
| Route Duration | Duration for route advertisement. |
| Route Type | EVPN route type:   * Ethernet auto-discovery route. * MAC advertisement route. * Inclusive multicast route. * Ethernet segment route. * IP prefix route. |
| Remote-Cross route | Route received from a peer and leaked into an EVPN instance. |
| Label information (Received/Applied) | Label information (received label/advertised label). |
| Relay IP Nexthop | IP recursive next hop. |
| Relay Tunnel Out-Interface | Outbound interface of the recursive tunnel. |
| Relay IP Out-Interface | Outbound interface obtained during the recursion. |
| IP Address/Len | IP address and length in a host route. |
| Original nexthop | Original next hop IP address. |
| Qos information | QoS information. |
| SoO | SoO extended community attribute. |
| AS-path | AS\_Path attribute (Nil indicates that the attribute value is null.). |
| origin | Origin attribute of a BGP route. |
| pref-val | Preferred value. |
| pre | The priority of the route. |
| IGP cost | IGP cost. |
| Cluster list | Cluster list. |
| Ethernet Tag ID | Configured VLAN ID. The current value is always 0. |
| MAC Address/Len | MAC address and length in a MAC route. |
| Not advertised to any peer yet | Route that is not advertised to any EVPN peer. |
| ESI | ID of an Ethernet link network segment. |
| From | IP address of the device that sends the route. |
| Ext-Community | BGP EVPN extended community attribute. |
| valid | Valid route. |
| best | Optimal route. |
| select | Local AS number. |
| Originator | IP address of the device that has originated routes. |
| Community | Community attribute. |
| Prefix-sid | Prefix SID. |
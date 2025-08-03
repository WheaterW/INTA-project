display bgp mvpn routing-table type 4 route-key-type
====================================================

display bgp mvpn routing-table type 4 route-key-type

Function
--------



The **display bgp mvpn routing-table type 4 route-key-type** command displays BGP Multicast Virtual Private Network (MVPN) Leaf A-D routes.




Format
------

**display bgp mvpn** { **all** | **route-distinguisher** *route-distinguisher* } **routing-table** **type** **4** **route-key-type** { **1** | **2** | **3** } *leaf-s-pmsi*

**display bgp mvpn vpn-instance** *vpn-instance-name* **routing-table** **type** **4** **route-key-type** { **1** | **2** | **3** } *leaf-s-pmsi*

**display bgp mvpn all routing-table peer** *ipv4-address* **advertised-routes** **type** **4** **route-key-type** { **1** | **2** | **3** } *leaf-s-pmsi*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Displays all BGP MVPN routes. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **route-distinguisher** *route-distinguisher* | Displays BGP routes of the specified Route Distinguisher (RD). | The RD can be in any of the following formats:   * 2-byte AS number:4-byte user-defined number, for example, 101:3. The AS number ranges from 0 to 65535, and the user-defined number ranges from 0 to 4294967295. If both the AS number and user-defined number are 0, that is, the RD is 0:0, the MVPN instance is a public network MVPN instance. * 4-byte AS number in integer format:2-byte user-defined number, for example, 65537:3. An AS number ranges from 65536 to 4294967295, and a user-defined number ranges from 0 to 65535. * 4-byte AS number in dotted notation:2-byte user-defined number, for example, 0.0:3 or 0.1:0. A 4-byte AS number in dotted notation is in the format of x.y, where x and y are integers that range from 0 to 65535. A user-defined number also ranges from 0 to 65535. * IPv4 address:2-byte user-defined number, for example, 192.168.122.15:1. The IP address ranges from 0.0.0.0 to 255.255.255.255, and the user-defined number is an integer ranging from 0 to 65535. |
| **1** | Displays intra-AS I-PMSI A-D routes. | - |
| **2** | Displays inter-AS I-PMSI A-D routes. | - |
| **3** | Displays S-PMSI A-D routes. | - |
| *leaf-s-pmsi* | Displays A-D routes. | * If route-key-type is set to 1, the value of leaf-s-pmsi is in the format of X.X.X.X:Y.Y.Y.Y.   X.X.X.X indicates the multicast source address in an (S, G) entry, in dotted decimal notation.  Y. Y. Y. Y indicates the address of a multicast group in an (S, G) entry. The value is in dotted decimal notation and ranges from 224.0. 0.0 to 239.255. 255.255.   * If route-key-type is set to 2, the value is in the format of source AS number:source device IP address. Source AS number: The value is an integer ranging from 1 to 4294967295. IP address of the source device: The value is in dotted decimal notation. * If route-key-type is set to 3, the value of leaf-s-pmsi is in the format of X.X.X.X:Y.Y.Y.Y:Z.Z.Z.Z:L.L.L.L.   X.X.X.X indicates the multicast source address in an (S, G) entry, in dotted decimal notation.  Y. Y. Y. Y indicates the address of a multicast group in an (S, G) entry. The value is in dotted decimal notation and ranges from 224.0. 0.0 to 239.255. 255.255.  Z. Z. Z. Z indicates the IP address of the source device, in dotted decimal notation.  L. L. L. L indicates the IP address of the leaf source device, in dotted decimal notation. |
| **vpn-instance** *vpn-instance-name* | Displays the BGP routes of the specified VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **peer** *ipv4-address* | Displays the routes of the specified peer. | The value is in dotted decimal notation. |
| **advertised-routes** | Displays the routes advertised to the specified peer. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To view BGP MVPN routes, run the display bgp mvpn routing-table type 4 route-key-type command. You can specify different parameters to view the specific routing information.When BGP MVPN routing table is displayed, if the length of the destination address mask of an IPv4 route is the same as that of its natural mask, the mask length is not displayed.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about Leaf A-D routes in an MVPN instance.
```
<HUAWEI> display bgp mvpn vpn-instance ng routing-table  type 4 route-key-type 1 10.0.0.2
 BGP local router ID : 10.0.0.4
 Local AS number : 100
 BGP routing table entry information of 10.0.0.2:
 Route Distinguisher: 100:1
 Remote-Cross route
 From: 10.0.0.2 (10.0.0.2) 
 Route Duration: 0d00h00m12s
 Original nexthop: 10.0.0.2
 Qos information : 0x0
 Ext-Community: RT <1 : 1>
 AS-path Nil, origin incomplete, MED 0, localpref 100, pref-val 0, valid, internal, best, select, pre 255
 Route Type: 1 (Intra-AS I-PMSI AD Route)
 Originator IP: 10.0.0.2
 PMSI: Flags 0x0,RSVP-TE P2MP LSP, Label 0:0:0(0), P2MP ID: 0x63000002, Tunnel ID: 49153, Extended tunnel ID: 10.0.0.2
 Not advertised to any peer yet

```

# Display information about Leaf A-D routes(IPv6) in an MVPN instance.
```
<HUAWEI> display bgp mvpn vpn-instance vrf1 routing-table type 4  route-key-type 1  2001:db8:1::3-2001:db8:1::1


 BGP local router ID : 1.1.1.1
 Local AS number : 100
 BGP routing table entry information of 2001:db8:1::3-2001:db8:1::1:
 Route Distinguisher: 1:1
 Imported route.
 From: 0.0.0.0 (0.0.0.0) 
 Route Duration: 0d01h20m10s
 Original nexthop: 127.0.0.1
 Qos information : 0x0
 IPv6 Ext-Community: RT <2001:db8:1::3 . 0>
 AS-path Nil, origin incomplete, MED 0, pref-val 0, valid, local, best, select, pre 255
 Route Type: 4 (Leaf AD Route)
 Originator IP: 2001:db8:1::3, LeafOriIP : 2001:db8:1::1
 PMSI: Flags 0x0, Label 0:0:0(0), subdomain ID: 0, BFR ID: 2, BFR prefix: 2001:db8:1::1
 Not advertised to any peer yet

```

**Table 1** Description of the **display bgp mvpn routing-table type 4 route-key-type** command output
| Item | Description |
| --- | --- |
| BGP local router ID | ID of the local BGP device. The format is the same as the IPv4 address. |
| BGP routing table entry information of | The following information is about the route X.X.X.X. |
| Local AS number | Local AS number. |
| Route Distinguisher | Route distinguisher. |
| Route Duration | Duration of routes. |
| Route Type | Route type. |
| Original nexthop | Original next hop IP address. |
| Qos information | Qos information. |
| AS-path Nil | AS\_Path attribute, with Nil indicating that the attribute value is null. |
| MED | Multi\_Exit discriminator. |
| pre 255 | The priority of the BGP route is 255. |
| Originator IP | Original IP address. |
| IPv6 Ext-Community | Displays the IPv6 ext-community list of the route. |
| From | IP address of the router that sends the route. |
| best | Optimal route. |
| select | Selected route. |
| PMSI | Provider Multicast Service Interface (PMSI) tunnel information. |
| Ext-Community | BGP EVPN extended community attribute. |
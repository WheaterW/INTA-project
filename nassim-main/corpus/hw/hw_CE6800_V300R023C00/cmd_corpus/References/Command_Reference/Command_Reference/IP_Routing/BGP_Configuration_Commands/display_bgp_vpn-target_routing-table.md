display bgp vpn-target routing-table
====================================

display bgp vpn-target routing-table

Function
--------



The **display bgp vpn-target routing-table** command displays information about routes in the BGP-VPN-Target address family.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display bgp vpn-target routing-table** [ **peer** { *ipv4-address* | *ipv6-address* } { **advertised-routes** | **received-routes** } ] [ **origin-as** *origin-as-num* ] *vpn-target*

For CE6885-LL (low latency mode):

**display bgp vpn-target routing-table** [ **peer** *ipv4-address* { **advertised-routes** | **received-routes** } ] [ **origin-as** *origin-as-num* ] *vpn-target*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **peer** *ipv4-address* | Specifies an IPv4 address. | It is in dotted decimal notation. |
| *ipv6-address* | Specifies an IPv6 peer address.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| **advertised-routes** | Displays information about routes advertised to a specified peer. | - |
| **received-routes** | Displays information about the routes received from the specified peer. | - |
| **origin-as** *origin-as-num* | Displays information about RT routes with the specified origin AS number. | The value is an integer ranging from 0 to 4294967295. |
| *vpn-target* | Displays information about a specified VPN target. | The format of a VPN target can be as follows:   * 2-byte AS number:4-byte user-defined number, for example, 1:3. An AS number is an integer ranging from 0 to 65535, and a user-defined number is an integer ranging from 0 to 4294967295. The AS and user-defined numbers cannot be both 0s. This means that a VPN target cannot be 0:0. * Integral 4-byte AS number:2-byte user-defined number, for example, 65537:3. An AS number is an integer ranging from 65536 to 4294967295, and a user-defined number is an integer ranging from 0 to 65535. * 4-byte AS number in dotted notation:2-byte user-defined number, for example, 0.0:3 or 0.1:0. A 4-byte AS number in dotted notation is in the format of x.y, where x and y are integers ranging from 0 to 65535. A user-defined number is an integer ranging from 0 to 65535. The AS and user-defined numbers cannot be both 0s. This means that a VPN target cannot be 0.0:0. * 32-bit IP address:2-byte user-defined number. For example, 192.168.122.15:1. An IP address ranges from 0.0.0.0 to 255.255.255.255, and a user-defined number is an integer ranging from 0 to 65535. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The display bgp vpn-target routing-table command displays information about routes in the BGP-VPN-Target address family.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about routes with the specified VPN target.
```
<HUAWEI> display bgp vpn-target routing-table 1:1
 
 BGP local router ID:2.2.2.2
 Local AS number:

 Origin AS:100
 BGP routing table entry information of RT<1:1>/96:
 RR-client route.
 FROM:1.1.1.1(10.1.1.1)
 Route Duration:00h37m05s
 Relay IP Nexthop:10.1.1.1
 Relay IP Out-Interface:Ethernet1/0/1
 Original nexthop:1.1.1.1
 Qos information:0x0
 AS-path Nil,origin incomplete,MED 0,localpref 100,pref-val 0,valid,internal,best,select,pre 255,IGP cost 10
 Advertised to such 2 peers:
 Update-Group 1:
  10.1.1.2
 Update-Group 0:
  1.1.1.1

```

# Display information about the VPN-Target routes that have the prefix 1:1 and are received from the peer with IP address 2.2.2.2.
```
<HUAWEI> display bgp vpn-target routing-table peer 2.2.2.2 received-routes 1:1
 BGP local router ID:1.1.1.1
 Local AS number:100

 Origin AS:100

 BGP routing table entry information of RT<1:1>/96:
 FROM:2.2.2.2(2.2.2.2)
 Route Duration:18h14m07s
 Relay IP Nexthop:10.21.2.1
 Relay IP Out-Interface:Ethernet1/0/1
 Original nexthop:2.2.2.2
 Qos information:0x0
 AS-path Nil,origin incomplete,MED 0,localpref 100,pref-val 0,valid,internal,best,select,pre 255,IGP cost 1,not preferred for route type
 Not advertised to any peer yet

```

# Display information about the VPN-Target routes that have the prefix 1:1 and origin AS number 100 and are received from the peer with IP address 2.2.2.2.
```
<HUAWEI> display bgp vpn-target routing-table peer 2.2.2.2 received-routes origin-as 100 1:1
 BGP local router ID:1.1.1.1
 Local AS number:100

 Origin AS:100
 BGP routing table entry information of RT<1:1>/96:
 FROM:2.2.2.2(2.2.2.2)
 Route Duration:18h20m42s
 Relay IP Nexthop:10.21.2.1
 Relay IP Out-Interface:Ethernet1/0/1
 Original nexthop:2.2.2.2
 Qos information:0x0
 AS-path Nil,origin incomplete,MED 0,localpref 100,pref-val 0,valid,internal,best,select,pre 255,IGP cost 1,not preferred for route type
 Not advertised to any peer yet

```

**Table 1** Description of the **display bgp vpn-target routing-table** command output
| Item | Description |
| --- | --- |
| BGP local router ID | Router ID of the local device, in the format of an IPv4 address. |
| BGP routing table entry information of RT<1:1>/96 | The following information is about a specified RT route. |
| Local AS number | Local AS number. |
| Origin AS | Origin AS number of the route. |
| Origin | Origin attribute of the BGP route. There are three types: 1. IGP: For example, the Origin attribute of the routes imported to the BGP routing table using the network command is IGP. 2. EGP: indicates that the Origin attribute of the routes obtained through EGP is EGP. 3. Incomplete: The origin of the route cannot be determined. For example, the Origin attribute of the routes imported by BGP using the import-route command is Incomplete. |
| Route Duration | Duration for route advertisement. |
| Relay IP Nexthop | IP recursive next hop. |
| Relay IP Out-Interface | Outbound interface obtained when the route recurses to another route. |
| Original nexthop | Original next hop IP address. |
| Qos information | Qos information. |
| AS-path | AS\_Path attribute (Nil indicates that the attribute value is null.). |
| Advertised to such 2 peers | Peer to which a route is advertised. |
| Not advertised to any peer yet | The route has not been advertised to any peer yet. |
| FROM | IP address of the device that sends the route. |
| MED | Multi-exit discriminator (MED), which is used to determine the optimal route when traffic enters an AS. During route selection, the route with the smallest MED value is selected as the optimal route if all other attributes are the same. |
| localpref | Local\_Pref of the RT route. |
| pref-val | Preferred value. |
| internal | The route is internal. |
| pre | The priority of the route. |
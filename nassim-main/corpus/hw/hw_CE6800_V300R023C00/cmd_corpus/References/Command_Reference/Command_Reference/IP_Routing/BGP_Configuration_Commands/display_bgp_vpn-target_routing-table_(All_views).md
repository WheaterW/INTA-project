display bgp vpn-target routing-table (All views)
================================================

display bgp vpn-target routing-table (All views)

Function
--------



The **display bgp vpn-target routing-table** command displays information about routes in the BGP-VPN-Target address family.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display bgp vpn-target routing-table** { [ **peer** { *ipv4-address* | *ipv6-address* } **received-routes** ] | [ **origin-as** *origin-as-num* ] }

For CE6885-LL (low latency mode):

**display bgp vpn-target routing-table** { [ **peer** *ipv4-address* **received-routes** ] | [ **origin-as** *origin-as-num* ] }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **peer** *ipv6-address* | Specifies an IPv6 peer address.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| **peer** *ipv4-address* | Specifies an IPv4 address. | It is in dotted decimal notation. |
| **received-routes** | Displays information about the routes received from the specified peer. | - |
| **origin-as** *origin-as-num* | Displays information about RT routes with the specified origin AS number. | The value is an integer that ranges from 0 to 4294967295. |



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


# Display information about routes that have the prefix 1:1 and are received from the peer with IP address 2.2.2.2 in the BGP-VPN-Target address family.
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

# Display information about routes received from the peer with IP address 2.2.2.2 in the BGP-VPN-Target address family.
```
<HUAWEI> display bgp vpn-target routing-table peer 2.2.2.2 received-routes
 Received routes total: 2


 BGP Local router ID is 10.2.1.2
 Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
               Origin : i - IGP, e - EGP, ? - incomplete


 Origin AS: 100
        Network            NextHop        MED        LocPrf    PrefVal Path/Ogn
 *>i    RT<1:1>            2.2.2.2        0          100        0        ?
 *>i    RT<0.1:1>          2.2.2.2        0          100        0        ?

```

**Table 1** Description of the **display bgp vpn-target routing-table (All views)** command output
| Item | Description |
| --- | --- |
| BGP local router ID | Router ID of the local device, in the format of an IPv4 address. |
| BGP routing table entry information of RT<1:1>/96 | The following information is about a specified RT route. |
| Local AS number | Local AS number. |
| Origin AS | Origin AS number of the route. |
| Origin | Origin attribute:   * IGP: indicates that the route is added to the BGP routing table using the network command. * EGP: indicates that the route is learned through the EGP. * Incomplete: indicates that the origin of the route cannot be identified. For example, if a route is imported using the import-route command, its origin is Incomplete. |
| Route Duration | Duration of the route. |
| Relay IP Nexthop | Next hop to which the route recurses. |
| Relay IP Out-Interface | Outbound interface obtained when the route recurses to another route. |
| Original nexthop | Original next-hop IP address. |
| Qos information | QoS information. |
| AS-path | AS\_Path attribute. Nil indicates that the attribute value is null. |
| Not advertised to any peer yet | The route has not been advertised to any peer yet. |
| Received routes total | Number of routes received from a specified peer. |
| MED | Multi-exit discriminator (MED), which is used to determine the optimal route when traffic enters an AS. During route selection, the route with the smallest MED value is selected as the optimal route if all other attributes are the same. |
| LocPrf | Local\_Pref of the RT route. |
| FROM | IP address of the device that advertised the route. |
| pref-val | PrefVal of the route. |
| internal | The route is internal. |
| pre | The priority of the BGP route. |
display bgp routing-table verbose
=================================

display bgp routing-table verbose

Function
--------



The **display bgp routing-table verbose** command displays detailed information about BGP routes.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**display bgp routing-table verbose**

**display bgp vpnv4** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **verbose**

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display bgp ipv6 routing-table verbose**

**display bgp vpnv6** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **verbose**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpnv4** | Indicates the VPNv4 address family. | - |
| **all** | Specifies all VPN instances. | - |
| **vpn-instance** *vpn-instance-name* | Specifies a VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. In addition, the VPN instance name must not be \_public\_. The character string can contain spaces if it is enclosed in double quotation marks (""). |
| **ipv6** | Indicates the IPv6 unicast address family.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **vpnv6** | Indicates the VPNv6 address family.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**



To check detailed information about all BGP IPv4 public network routes, run the **display bgp routing-table verbose** command.

To check detailed information about all BGP IPv6 public network routes, run the **display bgp ipv6 routing-table verbose** command.

To check detailed information about routes in the BGP-VPNv4 address family, run the **display bgp vpnv4 all routing-table verbose** command.

To check detailed information about routes in the BGP-VPNv6 address family, run the **display bgp vpnv6 all routing-table verbose** command.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display detailed information about BGP IPv4 public network routes.
```
<HUAWEI> display bgp routing-table verbose

 Total Number of Routes: 1
 
 BGP local router ID : 10.0.12.2
 Local AS number : 100
 Paths:   1 available, 1 best, 1 select, 0 best-external, 0 add-path
 BGP routing table entry information of 10.0.3.0/24:
 Label information (Received/Applied): 48130/48122
 From: 10.0.23.3 (10.0.23.3)  
 Route Duration: 0d00h13m31s
 Direct Out-interface:  Eth-trunk1
 Relay Tunnel Out-Interface:  Eth-trunk1
 Original nexthop: 10.0.23.3
 Qos information : 0x0
 AS-path 200, origin igp, MED 0, pref-val 1, valid, external, best, select, pre 255
 Advertised to such 1 peers:
    10.1.1.1

```

# Display detailed information about all VPN routes in the BGP-VPNv6 address family.
```
<HUAWEI> display bgp vpnv6 all routing-table verbose
 
 Total number of routes from all PE: 4
 
 BGP local router ID : 10.0.12.2
 Local AS number : 100
 
 Total routes of Route Distinguisher(1:100): 1
 BGP routing table entry information of 2001:DB8:2003::/64:
 Label information (Received/Applied): 48122/48127
 From: 10.0.23.3 (10.0.23.3)  
 Route Duration: 0d00h13m32s
 Direct Out-interface:  Eth-trunk1
 Relay Tunnel Out-Interface:  Eth-trunk1
 Original nexthop: ::FFFF:10.0.23.3
 Qos information : 0x0
 Ext-Community: RT <1 : 1>
 AS-path 200, origin igp, MED 0, pref-val 1, valid, external, best, select, pre 255
 Advertised to such 1 peers:
    10.1.1.1
 
 Total routes of Route Distinguisher(2:200): 3
 BGP routing table entry information of 2001:DB8:2003::/64:
 Label information (Received/Applied): 48123/48128
 From: 10.0.23.3 (10.0.23.3)  
 Route Duration: 0d00h13m32s
 Direct Out-interface:  Eth-trunk1
 Relay Tunnel Out-Interface:  Eth-trunk1
 Original nexthop: ::FFFF:10.0.23.3
 Qos information : 0x0
 Ext-Community: RT <2 : 2>
 AS-path 200, origin igp, MED 0, pref-val 1, valid, external, best, select, pre 255
 Advertised to such 1 peers:
    10.1.1.1

 BGP routing table entry information of 2001:DB8:2222::/64:
 Label information (Received/Applied): 48124/48129
 From: 10.0.23.3 (10.0.23.3)  
 Route Duration: 0d00h13m32s
 Direct Out-interface:  Eth-trunk1
 Relay Tunnel Out-Interface:  Eth-trunk1
 Original nexthop: ::FFFF:10.0.23.3
 Qos information : 0x0
 Ext-Community: RT <2 : 2>
 AS-path 200, origin igp, MED 0, pref-val 1, valid, external, best, select, pre 255
 Advertised to such 1 peers:
    10.1.1.1

 BGP routing table entry information of 2001:DB8:2223::/64:
 Label information (Received/Applied): 48125/48130
 From: 10.0.23.3 (10.0.23.3)  
 Route Duration: 0d00h13m32s
 Direct Out-interface:  Eth-trunk1
 Relay Tunnel Out-Interface:  Eth-trunk1
 Original nexthop: ::FFFF:10.0.23.3
 Qos information : 0x0
 Ext-Community: RT <2 : 2>
 AS-path 200, origin igp, MED 0, pref-val 1, valid, external, best, select, pre 255
 Advertised to such 1 peers:
    10.1.1.1

 VPN-Instance 1, Router ID 10.0.12.2:

 Total Number of Routes: 1
 BGP routing table entry information of 2001:DB8:2003::/64:
 Route Distinguisher: 1:100
 Remote-Cross route
 Label information (Received/Applied): 48122/NULL
 From: 10.0.23.3 (10.0.23.3)  
 Route Duration: 0d00h13m32s
 Relay Tunnel Out-Interface:  Eth-trunk1
 Original nexthop: ::FFFF:10.0.23.3
 Qos information : 0x0
 Ext-Community: RT <1 : 1>
 AS-path 200, origin igp, MED 0, pref-val 1, valid, external, best, select, pre 255
 Not advertised to any peer yet

 VPN-Instance 2, Router ID 10.0.12.2:

 Total Number of Routes: 3
 BGP routing table entry information of 2001:DB8:2003::/64:
 Route Distinguisher: 2:200
 Remote-Cross route
 Label information (Received/Applied): 48123/NULL
 From: 10.0.23.3 (10.0.23.3)  
 Route Duration: 0d00h13m32s
 Relay Tunnel Out-Interface:  Eth-trunk1
 Original nexthop: ::FFFF:10.0.23.3
 Qos information : 0x0
 Ext-Community: RT <2 : 2>
 AS-path 200, origin igp, MED 0, pref-val 1, valid, external, best, select, pre 255
 Not advertised to any peer yet

 BGP routing table entry information of 2001:DB8:2222::/64:
 Route Distinguisher: 2:200
 Remote-Cross route
 Label information (Received/Applied): 48124/NULL
 From: 10.0.23.3 (10.0.23.3)  
 Route Duration: 0d00h13m32s
 Relay Tunnel Out-Interface:  Eth-trunk1
 Original nexthop: ::FFFF:10.0.23.3
 Qos information : 0x0
 Ext-Community: RT <2 : 2>
 AS-path 200, origin igp, MED 0, pref-val 1, valid, external, best, select, pre 255
 Not advertised to any peer yet

 BGP routing table entry information of 2001:DB8:2223::/64:
 Route Distinguisher: 2:200
 Remote-Cross route
 Label information (Received/Applied): 48125/NULL
 From: 10.0.23.3 (10.0.23.3)  
 Route Duration: 0d00h13m32s
 Relay Tunnel Out-Interface:  Eth-trunk1
 Original nexthop: ::FFFF:10.0.23.3
 Qos information : 0x0
 Ext-Community: RT <2 : 2>
 AS-path 200, origin igp, MED 0, pref-val 1, valid, external, best, select, pre 255
 Not advertised to any peer yet

```

# Display detailed information about all routes in the BGP-VPNv6 address family of a specified VPN instance.
```
<HUAWEI> display bgp vpnv6 vpn-instance 1 routing-table verbose

 VPN-Instance 1, Router ID 10.0.12.2:

 Total Number of Routes: 1
 
 BGP local router ID : 10.0.12.2
 Local AS number : 100
 Paths:   1 available, 1 best, 1 select, 0 best-external, 0 add-path
 BGP routing table entry information of 2001:DB8:2003::/64:
 Route Distinguisher: 1:100
 Remote-Cross route
 Label information (Received/Applied): 48122/NULL
 From: 10.0.23.3 (10.0.23.3)  
 Route Duration: 0d00h13m31s
 Relay Tunnel Out-Interface:  Eth-trunk1
 Original nexthop: ::FFFF:10.0.23.3
 Qos information : 0x0
 Ext-Community: RT <1 : 1>
 AS-path 200, origin igp, MED 0, pref-val 1, valid, external, best, select, pre 255
 Not advertised to any peer yet

```

# Display detailed information about all VPN routes in the BGP-VPNv4 address family.
```
<HUAWEI> display bgp vpnv4 all routing-table verbose
 
 Total number of routes from all PE: 4
 
 BGP local router ID : 10.0.12.2
 Local AS number : 100
 
 Total routes of Route Distinguisher(1:100): 1
 BGP routing table entry information of 10.0.3.0/24:
 Label information (Received/Applied): 48126/48123
 From: 10.0.23.3 (10.0.23.3)  
 Route Duration: 0d00h13m31s
 Direct Out-interface:  Eth-trunk1
 Relay Tunnel Out-Interface:  Eth-trunk1
 Original nexthop: 10.0.23.3
 Qos information : 0x0
 Ext-Community: RT <1 : 1>
 AS-path 200, origin igp, MED 0, pref-val 1, valid, external, best, select, pre 255
 Advertised to such 1 peers:
    10.1.1.1
 
 Total routes of Route Distinguisher(2:200): 3
 BGP routing table entry information of 10.0.3.0/24:
 Label information (Received/Applied): 48127/48124
 From: 10.0.23.3 (10.0.23.3)  
 Route Duration: 0d00h13m31s
 Direct Out-interface:  Eth-trunk1
 Relay Tunnel Out-Interface:  Eth-trunk1
 Original nexthop: 10.0.23.3
 Qos information : 0x0
 Ext-Community: RT <2 : 2>
 AS-path 200, origin igp, MED 0, pref-val 1, valid, external, best, select, pre 255
 Advertised to such 1 peers:
    10.1.1.1

 BGP routing table entry information of 10.22.22.0/24:
 Label information (Received/Applied): 48128/48125
 From: 10.0.23.3 (10.0.23.3)  
 Route Duration: 0d00h13m31s
 Direct Out-interface:  Eth-trunk1
 Relay Tunnel Out-Interface:  Eth-trunk1
 Original nexthop: 10.0.23.3
 Qos information : 0x0
 Ext-Community: RT <2 : 2>
 AS-path 200, origin igp, MED 0, pref-val 1, valid, external, best, select, pre 255
 Advertised to such 1 peers:
    10.1.1.1

 BGP routing table entry information of 10.23.23.0/24:
 Label information (Received/Applied): 48129/48126
 From: 10.0.23.3 (10.0.23.3)  
 Route Duration: 0d00h13m31s
 Direct Out-interface:  Eth-trunk1
 Relay Tunnel Out-Interface:  Eth-trunk1
 Original nexthop: 10.0.23.3
 Qos information : 0x0
 Ext-Community: RT <2 : 2>
 AS-path 200, origin igp, MED 0, pref-val 1, valid, external, best, select, pre 255
 Advertised to such 1 peers:
    10.1.1.1

 VPN-Instance 1, Router ID 10.0.12.2:

 Total Number of Routes: 1
 BGP routing table entry information of 10.0.3.0/24:
 Route Distinguisher: 1:100
 Remote-Cross route
 Label information (Received/Applied): 48126/NULL
 From: 10.0.23.3 (10.0.23.3)  
 Route Duration: 0d00h13m31s
 Relay Tunnel Out-Interface:  Eth-trunk1
 Original nexthop: 10.0.23.3
 Qos information : 0x0
 Ext-Community: RT <1 : 1>
 AS-path 200, origin igp, MED 0, pref-val 1, valid, external, best, select, pre 255
 Not advertised to any peer yet

 VPN-Instance 2, Router ID 10.0.12.2:

 Total Number of Routes: 3
 BGP routing table entry information of 10.0.3.0/24:
 Route Distinguisher: 2:200
 Remote-Cross route
 Label information (Received/Applied): 48127/NULL
 From: 10.0.23.3 (10.0.23.3)  
 Route Duration: 0d00h13m31s
 Relay Tunnel Out-Interface:  Eth-trunk1
 Original nexthop: 10.0.23.3
 Qos information : 0x0
 Ext-Community: RT <2 : 2>
 AS-path 200, origin igp, MED 0, pref-val 1, valid, external, best, select, pre 255
 Not advertised to any peer yet

 BGP routing table entry information of 10.22.22.0/24:
 Route Distinguisher: 2:200
 Remote-Cross route
 Label information (Received/Applied): 48128/NULL
 From: 10.0.23.3 (10.0.23.3)  
 Route Duration: 0d00h13m31s
 Relay Tunnel Out-Interface:  Eth-trunk1
 Original nexthop: 10.0.23.3
 Qos information : 0x0
 Ext-Community: RT <2 : 2>
 AS-path 200, origin igp, MED 0, pref-val 1, valid, external, best, select, pre 255
 Not advertised to any peer yet

 BGP routing table entry information of 10.23.23.0/24:
 Route Distinguisher: 2:200
 Remote-Cross route
 Label information (Received/Applied): 48129/NULL
 From: 10.0.23.3 (10.0.23.3)  
 Route Duration: 0d00h13m31s
 Relay Tunnel Out-Interface:  Eth-trunk1
 Original nexthop: 10.0.23.3
 Qos information : 0x0
 Ext-Community: RT <2 : 2>
 AS-path 200, origin igp, MED 0, pref-val 1, valid, external, best, select, pre 255
 Not advertised to any peer yet

```

# Display detailed information about all routes in the BGP-VPNv4 address family of a specified VPN instance.
```
<HUAWEI> display bgp vpnv4 vpn-instance 1 routing-table verbose

 VPN-Instance 1, Router ID 10.0.12.2:

 Total Number of Routes: 1
 
 BGP local router ID : 10.0.12.2
 Local AS number : 100
 Paths:   1 available, 1 best, 1 select, 0 best-external, 0 add-path
 BGP routing table entry information of 10.0.3.0/24:
 Route Distinguisher: 1:100
 Remote-Cross route
 Label information (Received/Applied): 48126/NULL
 From: 10.0.23.3 (10.0.23.3)  
 Route Duration: 0d00h13m31s
 Relay Tunnel Out-Interface:  Eth-trunk1
 Original nexthop: 10.0.23.3
 Qos information : 0x0
 Ext-Community: RT <1 : 1>
 AS-path 200, origin igp, MED 0, pref-val 1, valid, external, best, select, pre 255
 Not advertised to any peer yet

```

# Display detailed information about all BGP IPv6 public network routes.
```
<HUAWEI> display bgp ipv6 routing-table verbose

 Total Number of Routes: 2
 
 BGP local router ID : 10.0.12.2
 Local AS number : 100
 Paths:   1 available, 1 best, 1 select, 0 best-external, 0 add-path
 BGP routing table entry information of 2001:DB8:2003::/64:
 From: 2001:DB8:2023::3 (10.0.23.3)  
 Route Duration: 0d00h13m30s
 Direct Out-interface:  Eth-trunk1
 Original nexthop: 2001:DB8:2023::3
 Qos information : 0x0
 AS-path 200, origin igp, MED 0, pref-val 1, valid, external, best, select, pre 255
 Not advertised to any peer yet
 
 BGP local router ID : 10.0.12.2
 Local AS number : 100
 Paths:   1 available, 1 best, 1 select, 0 best-external, 0 add-path
 BGP routing table entry information of 2001:DB8:2005::/64:
 From: 2001:DB8:2023::3 (10.0.23.3)  
 Route Duration: 0d00h13m30s
 Direct Out-interface:  Eth-trunk1
 Original nexthop: 2001:DB8:2023::3
 Qos information : 0x0
 AS-path 200, origin igp, MED 0, pref-val 1, valid, external, best, select, pre 255
 Not advertised to any peer yet

```

**Table 1** Description of the **display bgp routing-table verbose** command output
| Item | Description |
| --- | --- |
| Total Number of Routes | Total number of routes in the routing table. |
| Total number of routes from all PE | Total number of current routes. |
| BGP local router ID | Router ID of the local BGP device. |
| BGP routing table entry information of | Routing entry information. |
| Local AS number | Local AS number. |
| Label information (Received/Applied) | Information about labels, including received and sent labels. |
| Route Duration | Route duration. |
| Route Distinguisher | Route distinguisher. |
| Relay Tunnel Out-Interface | Recursive tunnel outbound interface. |
| Original nexthop | Original next hop ddress used to forward packets. |
| Qos information | Qos information. |
| AS-path | Number of the AS that the route passes through. |
| MED | MED. |
| pref-val | PrefVal of a route. |
| pre | EXP value. |
| Advertised to such 1 peers | Information about the device that sends the peer information. |
| Remote-Cross route | Remotely leaked route. |
| Not advertised to any peer yet | Not advertised to any peer yet. |
| Ext-Community | Extended community attribute contained in a route. |
| Origin | Origin attribute of a BGP route It is classified into the following types:   * IGP: If a route is added to the BGP routing table using the network command, its origin is IGP. * EGP: The Origin attribute of the route obtained through EGP is EGP. * Incomplete: The origin of the route cannot be identified. For example, the Origin attribute of the routes imported by BGP through the import-route command is Incomplete. |
| select | Preferred route. |
| best | Optimal route. |
| valid | Valid route. |
| From | Origin of the route. |
| Paths | Route selection result. |
display bgp mvpn routing-table
==============================

display bgp mvpn routing-table

Function
--------



The **display bgp mvpn routing-table** command displays BGP Multicast Virtual Private Network (MVPN) routes.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp mvpn** { **all** | **route-distinguisher** *route-distinguisher* } **routing-table** **all-type**

**display bgp mvpn** { **all** | **route-distinguisher** *route-distinguisher* } **routing-table** **type** { **1** | **2** | **3** | **4** | **5** | **6** | **7** }

**display bgp mvpn vpn-instance** *vpn-instance-name* **routing-table** **all-type**

**display bgp mvpn vpn-instance** *vpn-instance-name* **routing-table** **type** { **1** | **2** | **3** | **4** | **5** | **6** | **7** }

**display bgp mvpn all routing-table peer** *ipv4-address* { **advertised-routes** | **received-routes** } **all-type**

**display bgp mvpn all routing-table peer** *ipv4-address* { **advertised-routes** | **received-routes** } **type** { **1** | **2** | **3** | **4** | **5** | **6** | **7** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Displays statistics about all BGP MVPN routes. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. The VPN instance name cannot be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **route-distinguisher** *route-distinguisher* | Displays statistics about BGP routes with the specified Route Distinguisher (RD). | The RD can be in any of the following formats:   * 2-byte AS number:4-byte user-defined number, for example, 101:3. The AS number ranges from 0 to 65535, and the user-defined number ranges from 0 to 4294967295. If both the AS number and user-defined number are 0, that is, the RD is 0:0, the MVPN instance is a public network MVPN instance. * 4-byte AS number in integer format:2-byte user-defined number, for example, 65537:3. An AS number ranges from 65536 to 4294967295, and a user-defined number ranges from 0 to 65535. * 4-byte AS number in dotted notation:2-byte user-defined number, for example, 0.0:3 or 0.1:0. A 4-byte AS number in dotted notation is in the format of x.y, where x and y are integers that range from 0 to 65535. A user-defined number also ranges from 0 to 65535. * IPv4 address:2-byte user-defined number, for example, 192.168.122.15:1. The IP address ranges from 0.0.0.0 to 255.255.255.255, and the user-defined number is an integer ranging from 0 to 65535. |
| **all-type** | Displays all types of MVPN routes. | The value is in the dotted decimal format. |
| **type** **1** | Displays intra-AS I-PMSI A-D routes. | - |
| **2** | Displays S-PMSI A-D routes. | - |
| **3** | Displays inter-AS I-PMSI A-D routes. | - |
| **4** | Displays Leaf A-D routes. | - |
| **5** | Displays Source Active A-D routes. | - |
| **6** | Displays Shared Tree Join C-multicast routes. | - |
| **7** | Displays Source Tree Join C-multicast routes. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **vpn-instance** *vpn-instance-name* | Displays statistics about the BGP routes with the specified VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. The VPN instance name cannot be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **peer** *ipv4-address* | Displays the routes of the specified BGP peer. | The value is in dotted decimal notation. |
| **advertised-routes** | Displays the routes advertised to the specified peer. | - |
| **received-routes** | Displays the routes received from the specified peer. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can specify different parameters to view the specific routing information.When you view the BGP MVPN routing table, if the mask length of the destination address of an IPv4 route is equal to the natural mask length, the mask length is not displayed.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display all types of MVPN routes.
```
<HUAWEI> display bgp mvpn all routing-table all-type
 BGP Local router ID is 1.2.3.4
 Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
               Origin : i - IGP, e - EGP, ? - incomplete
 RPKI validation codes: V - valid, I - invalid, N - not-found



 Total number of routes from all PE: 5
    Number of Intra-AS I-PMSI A-D Routes: 3

 Route Distinguisher: 200:1
        Network(Originator IP Addr)                             NextHop
 *>     2.2.2.2                                                 0.0.0.0

 Route Distinguisher: 300:1
        Network(Originator IP Addr)                             NextHop
 *>i    3.3.3.3                                                 3.3.3.3

 Route Distinguisher: 400:1
        Network(Originator IP Addr)                             NextHop
 *>i    4.4.4.4                                                 4.4.4.4
    Number of Source Tree Join Routes: 2
 Route Distinguisher: 300:1
        Network(AS Number:(C-S):(C-G))                                    NextHop
 *>i    100:1.1.1.1:225.1.1.1                                   3.3.3.3

 Route Distinguisher: 400:1
        Network(AS Number:C-S:C-G)                              NextHop
 *>i    100:1.1.1.1:224.1.1.1                                   4.4.4.4

 Total number of routes of IPv4-MVPN-family for vpn-instance VPNA: 5
    Number of Intra-AS I-PMSI A-D Routes: 3
        Network(Originator IP Addr)                                       NextHop
 *>     2.2.2.2                                                 0.0.0.0
 *>i    3.3.3.3                                                 3.3.3.3
 *>i    4.4.4.4                                                 4.4.4.4
    Number of Source Tree Join Routes: 2
        Network(AS Number:(C-S):(C-G))                                    NextHop
 *>i    100:1.1.1.1:224.1.1.1                                   4.4.4.4
 *>i    100:1.1.1.1:225.1.1.1                                   3.3.3.3

```

# Display all types of MVPN routes (including IPv6 routes).
```
<HUAWEI> display bgp mvpn all routing-table all-type
 
 BGP Local router ID is 1.1.1.1
 Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
               Origin : i - IGP, e - EGP, ? - incomplete


 Total Number of Routes: 12

    Number of Intra-AS I-PMSI A-D Routes: 3

 Route Distinguisher: 1:1
        Network(Originator IP Addr)                                       NextHop
 *>     10.1.1.1                                                           0.0.0.0         
 *>     2001:db8:1::1                                                              0.0.0.0         
 *>i    2001:db8:1::3                                                              2001:db8:1::3                                   

    Number of S-PMSI A-D Routes: 2

 Route Distinguisher: 1:1
        Network((C-S)-(C-G)-Originator IP Addr)                           NextHop
 *>i    10.1.1.1-225.0.0.1-2001:db8:1::3                                          2001:db8:1::3                                   
 *>i    10.1.1.2-225.0.0.1-2001:db8:1::3                                          2001:db8:1::3                                   

    Number of Leaf A-D Routes: 3

 Route Distinguisher: 1:1
        Network([OriIP|AsNum|(C-S)-(C-G)-OriIP]-LeafOriIP)                NextHop
 *>     2001:db8:1::3-2001:db8:1::1                                                         0.0.0.0         
 *>     10.1.1.1-225.0.0.1-2001:db8:1::3-2001:db8:1::1                                     0.0.0.0         
 *>     10.1.1.2-225.0.0.1-2001:db8:1::3-2001:db8:1::1                                     0.0.0.0         

    Number of Source Active A-D Routes: 1

 Route Distinguisher: 1:1
        Network((C-S):(C-G))                                              NextHop
 *>i    10.1.1.2:225.0.0.1                                               10.3.3.3         

    Number of Shared Tree Join Routes: 1

 Route Distinguisher: 1:1
        Network(AS Number:(C-S):(C-G))                                    NextHop
 *>     10:200.1.1.1:225.0.0.2                                           0.0.0.0         

    Number of Source Tree Join Routes: 2

 Route Distinguisher: 1:1
        Network(AS Number:(C-S):(C-G))                                    NextHop
 *>     10:200.1.1.1:225.0.0.1                                           0.0.0.0         
 *>     10:200.1.1.2:225.0.0.1                                           0.0.0.0         

 Total number of routes of IPv4-MVPN-family for vpn-instance vrf1: 12

    Number of Intra-AS I-PMSI A-D Routes: 3
        Network(Originator IP Addr)                                       NextHop
 *>     10.1.1.1                                                           0.0.0.0         
 *>     2001:db8:1::1                                                              0.0.0.0         
 *>i    2001:db8:1::3                                                              2001:db8:1::3                                   

    Number of S-PMSI A-D Routes: 2
        Network((C-S)-(C-G)-Originator IP Addr)                           NextHop
 *>i    10.1.1.1-225.0.0.1-2001:db8:1::3                                          2001:db8:1::3                                   
 *>i    10.1.1.2-225.0.0.1-2001:db8:1::3                                          2001:db8:1::3                                   

    Number of Leaf A-D Routes: 3
        Network([OriIP|AsNum|(C-S)-(C-G)-OriIP]-LeafOriIP)                NextHop
 *>     2001:db8:1::3-2001:db8:1::1                                                         0.0.0.0         
 *>     10.1.1.1-225.0.0.1-2001:db8:1::3-2001:db8:1::1                                     0.0.0.0         
 *>     10.1.1.2-225.0.0.1-2001:db8:1::3-2001:db8:1::1                                     0.0.0.0         

    Number of Source Active A-D Routes: 1
        Network((C-S):(C-G))                                              NextHop
 *>i    10.1.1.2:225.0.0.1                                               10.3.3.3         

    Number of Shared Tree Join Routes: 1
        Network(AS Number:(C-S):(C-G))                                    NextHop
 *>     10:200.1.1.1:225.0.0.2                                           0.0.0.0         

    Number of Source Tree Join Routes: 2
        Network(AS Number:(C-S):(C-G))                                    NextHop
 *>     10:200.1.1.1:225.0.0.1                                           0.0.0.0         
 *>     10:200.1.1.2:225.0.0.1                                           0.0.0.0

```

**Table 1** Description of the **display bgp mvpn routing-table** command output
| Item | Description |
| --- | --- |
| BGP Local router ID is | ID of the local BGP device. The format is the same as the IPv4 address. |
| best | Optimal route. |
| Total number of routes from all PE | Number of routes from all PEs. |
| Total Number of Routes | Route statistics. |
| Number of Shared Tree Join Routes | Number of Shared Tree Join routes. |
| Number of Source Tree Join Routes | Number of the Source Tree Join routes. |
| Route Distinguisher | Route distinguisher. |
| NextHop | Next hop address of a packet. |
| Network | Network address in the BGP routing table or AS number. |
| valid | Valid route. |
| Originator IP | Original IP address. |
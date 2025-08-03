display bgp instance vpnv4 routing-table large-community
========================================================

display bgp instance vpnv4 routing-table large-community

Function
--------



The **display bgp instance vpnv4 routing-table large-community** command displays information about BGP VPNv4 routes matched with large communities.

The **display bgp instance vpnv4 routing-table statistics large-community** command displays statistics about BGP VPNv4 routes matched with large communities.




Format
------

**display bgp instance** *instance-name* **vpnv4** **route-distinguisher** *route-distinguisher* **routing-table** **large-community** [ *aa:bb:cc* ] &<1-33>

**display bgp instance** *instance-name* **vpnv4** **route-distinguisher** *route-distinguisher* **routing-table** **statistics** **large-community** [ *aa:bb:cc* ] &<1-33>

**display bgp instance** *instance-name* **vpnv4** **route-distinguisher** *route-distinguisher* **routing-table** **large-community** [ *aa:bb:cc* ] &<1-33> **whole-match**

**display bgp instance** *instance-name* **vpnv4** **route-distinguisher** *route-distinguisher* **routing-table** **statistics** **large-community** [ *aa:bb:cc* ] &<1-33> **whole-match**

**display bgp instance** *instance-name* **vpnv4** **route-distinguisher** *route-distinguisher* **routing-table** **large-community-filter** *large-community-filter-name*

**display bgp instance** *instance-name* **vpnv4** **route-distinguisher** *route-distinguisher* **routing-table** **statistics** **large-community-filter** *large-community-filter-name*

**display bgp instance** *instance-name* **vpnv4** **route-distinguisher** *route-distinguisher* **routing-table** **large-community-filter** *large-community-filter-name* **whole-match**

**display bgp instance** *instance-name* **vpnv4** **route-distinguisher** *route-distinguisher* **routing-table** **statistics** **large-community-filter** *large-community-filter-name* **whole-match**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **route-distinguisher** *route-distinguisher* | Displays statistics about the BGP routes with a specified RD. | The value is a string of 3 to 21 case-sensitive characters, spaces not supported. |
| **large-community** *aa:bb:cc* | Specifies a value of the Large-Community attribute. | The value is a string of 5 to 32 case-sensitive characters, spaces not supported. |
| **instance** *instance-name* | Specifies a BGP instance. | The value is a string of 1 to 31 case-sensitive characters without spaces. When double quotation marks are used around the string, spaces are allowed in the string. |
| **statistics** | Displays statistics about routes advertised to or received from a specified peer. | - |
| **whole-match** | Indicates exact matching. | - |
| **large-community-filter** *large-community-filter-name* | Displays detailed configurations of a Large-Community filter with a specified name. | The value is a string of 1 to 51 case-sensitive characters, spaces not supported. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



The **display bgp instance vpnv4 routing-table large-community** command displays information about BGP VPNv4 routes matched with large communities.The **display bgp instance vpnv4 routing-table statistics large-community** command displays statistics about BGP VPNv4 routes matched with large communities.



**Precautions**



If a routing loop occurs, some routes may have not converged. Therefore, the route statistics displayed using the command may be different from the actual number.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display BGP routes with large-community attributes.
```
<HUAWEI> display bgp instance a vpnv4 route-distinguisher 11:11 routing-table large-community
 
 BGP Local router ID is 10.1.123.1
 Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
               Origin : i - IGP, e - EGP, ? - incomplete
 RPKI validation codes: V - valid, I - invalid, N - not-found


 Route Distinguisher: 11:11

 Total Number of Routes: 3
        Network            NextHop                       MED        LocPrf    PrefVal LargeCommunity

 *>     10.1.1.11/32        127.0.0.1                      0                     0      <1:1:1>
 *>     10.2.2.22/32        10.3.123.2                     0                     0      <1:1:1>, <2:2:2>
 *>     10.3.3.33/32        10.3.123.3                     0                     0      <1:1:1>, <3:3:3>
    
 VPN-Instance vpna, Router ID 10.1.123.1:

 Total Number of Routes: 3
        Network            NextHop                       MED        LocPrf    PrefVal LargeCommunity

 *>     10.1.1.11/32        0.0.0.0                        0                     0      <1:1:1>
 *>     10.2.2.22/32        10.3.123.2                     0                     0      <1:1:1>, <2:2:2>
 *>     10.3.3.33/32        10.3.123.3                     0                     0      <1:1:1>, <3:3:3>

```

**Table 1** Description of the **display bgp instance vpnv4 routing-table large-community** command output
| Item | Description |
| --- | --- |
| LargeCommunity | Large-community attribute of a route. |
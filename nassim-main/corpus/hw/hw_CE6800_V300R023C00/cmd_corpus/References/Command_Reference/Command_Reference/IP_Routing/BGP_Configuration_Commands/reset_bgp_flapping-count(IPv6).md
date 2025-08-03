reset bgp flapping-count(IPv6)
==============================

reset bgp flapping-count(IPv6)

Function
--------



The **reset bgp flapping-count** command clears the flapping count of a specified BGP IPv6 peer.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset bgp** { **ipv6** | [ **instance** *bgpName* ] **vpn-instance** *vpn-instance-name* **ipv6-family** } *ipv6-address* **flapping-count**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ipv6** | Clears the flapping count of a specified BGP IPv6 peer. | - |
| **instance** *bgpName* | Displays BGP routes of a specified BGP multi-instance. | The value is a string of 1 to 31 case-sensitive characters without any spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **vpn-instance** *vpn-instance-name* | Specifies the name of VPN instance enabled with an IPv6 address family. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name cannot be \_public\_. If the string is enclosed in double quotation marks (" "), the string can contain spaces.. |
| **ipv6-family** | Indicates the IPv6 address family. | - |
| *ipv6-address* | Specifies the IPv6 address of a BGP peer. | The format is X:X:X:X:X:X:X:X. |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

BGP peer flapping affects the stability of a BGP network and BGP route convergence.The **reset bgp flapping-count** command can be used to clear the flapping account of a BGP peer. This allows the device to re-collect the flapping statistics of a peer to locate BGP network problems.

**Configuration Impact**

After the **reset bgp flapping-count** command is run, the flapping statistics of BGP peers are reset and cannot be displayed.

**Follow-up Procedure**

After the **reset bgp flapping-count** command is used to clear the statistics count of a specified BGP peer, run the **display bgp peer** command to display the flapping count of BGP peers and locate BGP network problems.


Example
-------

# Clear the flapping count of a specified BGP peer.
```
<HUAWEI> reset bgp ipv6 2001:DB8:1::1 flapping-count

```
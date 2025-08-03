reset bgp flapping-count
========================

reset bgp flapping-count

Function
--------



The **reset bgp flapping-count** command resets the flapping count of a specified BGP peer.




Format
------

**reset bgp** { *ipv4-address* | [ **instance** *bgpName* ] **vpn-instance** *vpn-instance-name* **ipv4-family** *ipv4-address* } **flapping-count**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **instance** *bgpName* | Specifies the BGP multi-instance name. | The value is a string of 1 to 31 case-sensitive characters without spaces. When double quotation marks are used around the string, spaces are allowed in the string. |
| **vpn-instance** *vpn-instance-name* | Specifies the name of VPN instance enabled with an IPv4 address family. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name cannot be \_public\_. If the string is enclosed in double quotation marks (" "), the string can contain spaces.. |
| **ipv4-family** *ipv4-address* | Specifies the IPv4 address of a BGP peer. | The value is in dotted decimal notation. |



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
<HUAWEI> reset bgp 10.1.1.1 flapping-count

```
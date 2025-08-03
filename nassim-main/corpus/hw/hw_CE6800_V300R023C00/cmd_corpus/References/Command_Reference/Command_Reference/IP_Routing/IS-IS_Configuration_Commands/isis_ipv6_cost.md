isis ipv6 cost
==============

isis ipv6 cost

Function
--------



The **isis ipv6 cost** command configures a link cost in an IPv6 topology.

The **undo isis ipv6 cost** command restores the default value.



By default, the link cost value in an IPv6 topology is 10.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**isis ipv6 cost** *cost-value* [ **level-1** | **level-2** ]

**undo isis ipv6 cost** [ *cost-value* ] [ **level-1** | **level-2** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *cost-value* | Specifies IPv6 link cost. | The value is an integer and varies with the cost type.   * When the cost type is wide or wide-compatible, the value ranges from 1 to 16777214. * For other cost types, the value ranges from 1 to 63.   The default value is 10.  The maximum parameter can be configured only when the cost-style of IS-IS is wide or wide-compatible. The neighbor TLV generated after the cost of an interface is set to 16777215 is used for TE information transmission, not for route calculation.  The cost type can be configured using the cost-style command. |
| **level-1** | Configures a link cost for Level-1 links. | - |
| **level-2** | Configures a link cost for Level-2 links.  If no IPv6 link level is specified, an IPv6 link cost is set for both Level-1 and Level-2 interfaces. | - |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On a large-scale network, there are multiple valid routes destined for the same destination in most cases. IS-IS calculates an optimal route based on the SPF algorithm and transmits traffic over it. This feature may cause the following problems:

* All traffic is transmitted over the optimal route, causing load imbalance.
* If the optimal route fails, traffic transmitted over it will be discarded.To address this problem, run the **isis ipv6 cost** command to configure different link costs for different interfaces so that traffic can be transmitted over different physical links.

**Configuration Impact**



If the link cost is changed, routes of the entire network are recalculated, and the traffic forwarding path changes accordingly.



**Precautions**



The **isis ipv6 cost** command takes effect only when links are active and an IPv6 topology is enabled.If the IPv6 topology type is compatible or standard, the IPv6 link cost is the same as the IPv4 link cost. When an IPv6 topology type is compatible enable-mt-spf or ipv6, IPv6 and IPv4 link costs need to be configured separately.If the isis ipv6 cost and ipv6 circuit-cost commands are both run, the value set using the isis ipv6 cost takes effect.




Example
-------

# Set the IPv6 link cost value of 100GE1/0/1 to 50.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] ipv6 enable
[*HUAWEI-isis-1] quit
[*HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] isis ipv6 enable 1
[*HUAWEI-100GE1/0/1] isis ipv6 cost 50

```
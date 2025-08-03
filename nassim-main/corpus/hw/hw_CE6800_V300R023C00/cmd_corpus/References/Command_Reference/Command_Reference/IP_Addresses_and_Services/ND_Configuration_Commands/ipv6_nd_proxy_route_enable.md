ipv6 nd proxy route enable
==========================

ipv6 nd proxy route enable

Function
--------



The **ipv6 nd proxy route enable** command enables the routed proxy ND function.

The **undo ipv6 nd proxy route enable** command disables the routed proxy ND function.



By default, the routed proxy ND function is not enabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd proxy route enable** [ **prune** ]

**undo ipv6 nd proxy route enable** [ **prune** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **prune** | Enables routed proxy source pruning. | - |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When two hosts are on the same network segment and are isolated into different physical networks by gateways with different addresses, the hosts cannot communicate with each other. You can run the **ipv6 nd proxy route enable** command to enable routed proxy ND on a gateway that connects two hosts. The gateway replies with an NA message using its own MAC address and the IPv6 address of the destination host. That is, the gateway replies with an NA message on behalf of the destination host. In this way, hosts on the same network segment but on different physical networks can communicate with each other (gateways connected to the hosts have different gateway addresses). If the source pruning function is enabled using the **ipv6 nd proxy route enable prune** command, the received NS message whose destination IP address is not a local IP address matches the network segment route of the local host, and the Layer 3 interface to which the message is sent is the same as the next hop interface of the route, the proxy function is not performed.

**Prerequisites**

The IPv6 function has been enabled using the **ipv6 enable** command.

**Precautions**

* Proxy ND cannot be enabled on an interface configured with a CGA address. Otherwise, the NA packets carrying the CGA/RSA option returned by the proxy device may be directly discarded by users.
* You can configure multiple types of proxy ND in the interface view. The priorities of proxy ND configured in descending order are as follows: proxy ND anyway, intra-VLAN proxy ND, inter-VLAN proxy ND, and routed proxy ND.
* The device does not perform proxy ND for the following packets:NS packets whose target address is the link-local address.DAD NS packets with an all-0 source address.NS packets whose target address is the local host.The ipv6 nd proxy route enable and ipv6 nd multicast-suppress commands are mutually exclusive.


Example
-------

# Enable the routed proxy ND function on a 100GE1/0/1 interface.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ipv6 nd proxy route enable

```

# Enable routed proxy ND and source pruning on Vlanif1.
```
<HUAWEI> system-view
[~HUAWEI] interface Vlanif 1
[*HUAWEI-Vlanif1] ipv6 enable
[*HUAWEI-Vlanif1] ipv6 nd proxy route enable prune

```
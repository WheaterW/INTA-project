ipv6 nd proxy anyway enable
===========================

ipv6 nd proxy anyway enable

Function
--------



The **ipv6 nd proxy anyway enable** command enables any proxy ND function.

The **undo ipv6 nd proxy anyway enable** command disables the any proxy ND function.



By default, the any proxy ND function is not enabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd proxy anyway enable**

**undo ipv6 nd proxy anyway enable**


Parameters
----------

None

Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In scenarios where servers are partitioned into VMs, to allow flexible deployment and migration of VMs on multiple servers or gateways, the common solution is to configure Layer 2 interworking between multiple gateways. However, this approach may lead to larger Layer 2 domains on the network and risks of broadcast storms. To resolve this problem, a common way is to enable any proxy ND on a VM gateway so that the gateway sends its own MAC address to the source VM and the traffic sent from the source VM to other VMs is transmitted over routes.

**Prerequisites**

The IPv6 function has been enabled using the **ipv6 enable** command.

**Precautions**

* Proxy ND cannot be enabled on an interface configured with a CGA address. Otherwise, the NA packets carrying the CGA/RSA option returned by the proxy device may be directly discarded by users.
* You can configure multiple types of proxy ND in the interface view. The priorities of proxy ND configured in descending order are as follows: proxy ND anyway, intra-VLAN proxy ND, inter-VLAN proxy ND, local proxy ND, and routed proxy ND.
* The device does not perform proxy ND for the following packets:NS packets whose target address is the link-local address.DAD NS packets with an all-0 source address.NS packets whose target address is the local host.

Example
-------

# Enable the any proxy ND function on the 100GE1/0/1 interface.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ipv6 nd proxy anyway enable

```
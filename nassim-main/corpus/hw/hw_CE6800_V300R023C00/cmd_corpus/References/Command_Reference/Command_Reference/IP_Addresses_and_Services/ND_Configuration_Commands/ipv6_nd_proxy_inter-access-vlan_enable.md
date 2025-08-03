ipv6 nd proxy inter-access-vlan enable
======================================

ipv6 nd proxy inter-access-vlan enable

Function
--------



The **ipv6 nd proxy inter-access-vlan enable** command enables the inter-VLAN proxy ND function.

The **undo ipv6 nd proxy inter-access-vlan enable** command disables the inter-VLAN proxy ND function.



By default, the inter-VLAN proxy ND function is not enabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd proxy inter-access-vlan enable**

**undo ipv6 nd proxy inter-access-vlan enable**


Parameters
----------

None

Views
-----

100ge sub-interface view,10GE sub-interface view,200GE sub-interface view,25GE sub-interface view,400GE sub-interface view,50GE sub-interface view,Eth-Trunk sub-interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

By using VLANs, you can divide a network into different subnets and a large broadcast domain into several small ones. This implements user isolation between different VLANs, effectively reducing the impact scope for broadcast packets and improving network security.In the following scenarios, the inter-VLAN proxy ND function needs to be enabled to allow communication between hosts:

* The inter-VLAN proxy ND function needs to be enabled on the interfaces of two hosts in different VLANs.
* In a VLAN aggregation scenario, if the hosts in sub-VLANs need to communicate with each other, the inter-VLAN proxy ND function needs to be enabled on the VLANIF interfaces in a super-VLAN.

**Prerequisites**

The IPv6 function has been enabled using the **ipv6 enable** command.

**Precautions**

* The IPv6 address configured for a proxy ND-enabled interface must be on the same network segment as the IPv6 address of the host connected to the interface.
* ND proxy cannot be enabled on an interface configured with a CGA address. Otherwise, the NA packets carrying the CGA/RSA option returned by the proxy device may be directly discarded by users.
* You can configure multiple types of proxy ND in the interface view. The priorities of proxy ND configured in descending order are as follows: proxy ND anyway, intra-VLAN proxy ND, inter-VLAN proxy ND, and routed proxy ND.
* If a device does not support VLAN segments, ND proxy between VLANs is not supported.
* The device does not perform proxy ND for the following packets:NS packets whose target address is the link-local address.DAD NS packets with an all-0 source address.NS packets whose target address is not on the same network segment as the local interface address.NS packets whose target address is the local host.

Example
-------

# Enable the inter-VLAN proxy ND function on VLANIF 20.
```
<HUAWEI> system-view
[~HUAWEI] vlan 20
[*HUAWEI-vlan20] quit
[*HUAWEI] interface vlanif 20
[*HUAWEI-Vlanif20] ipv6 enable
[*HUAWEI-Vlanif20] ipv6 nd proxy inter-access-vlan enable

```
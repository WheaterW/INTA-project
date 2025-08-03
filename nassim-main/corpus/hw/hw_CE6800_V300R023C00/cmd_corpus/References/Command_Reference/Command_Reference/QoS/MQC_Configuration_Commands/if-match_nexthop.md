if-match nexthop
================

if-match nexthop

Function
--------



The **if-match nexthop** command configures a matching rule based on the next hop IP address and outbound interface in a traffic classifier.

The **undo if-match nexthop** command deletes a matching rule based on the next hop IP address and outbound interface in a traffic classifier.

The **if-match ipv6 nexthop** command configures a matching rule based on the next hop ipv6 IP address and outbound interface in a traffic classifier.

The **undo if-match ipv6 nexthop** command deletes a matching rule based on the next hop ipv6 IP address and outbound interface in a traffic classifier.



By?default,?a?matching?rule?based?on?the?next?hop?IP?address?and?outbound?interface?is?not?configured?in?a?traffic?classifier.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**if-match** { **nexthop** *ip-address* | **ipv6** **nexthop** *ipv6-address* } **interface** { *interface-type* *interface-number* | *interface-name* }

**undo if-match** { **nexthop** *ip-address* | **ipv6** **nexthop** *ipv6-address* } **interface** { *interface-type* *interface-number* | *interface-name* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specify the IP nexthop address of the flow. | The value is in dotted decimal notation. |
| **ipv6** | Specifies the matching rule based on the next hop IPv6 address. | - |
| *ipv6-address* | Specify the IPv6 nexthop address of the flow. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| **interface** *interface-type* *interface-number* | Displays packet statistics on an interface to which a traffic policy has been applied.   * interface-type specifies the interface type. * interface-number specifies the interface number. | - |
| *interface-name* | Displays packet statistics on a specified interface to which a traffic policy has been applied. | - |



Views
-----

Traffic classifier view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run the **if-match nexthop** command to classify packets based on the next hop IP address and outbound interface so that the device processes packets with the same next hop IP address and outbound interface in the same manner.

**Precautions**

* The outbound interface must be a Layer 3 Ethernet interface or VLANIF interface.
* If the destination IP address of packets and the matched next hop IP address are on the same network segment, the traffic policy does not take effect.

Example
-------

# Configure a matching rule based on the next hop IP address of 192.168.1.1 and outbound interface of VLANIF 100 in the traffic classifier c1.
```
<HUAWEI> system-view
[~HUAWEI] vlan 100
[*HUAWEI] interface Vlanif 100
[*HUAWEI-Vlanif100] q
[*HUAWEI] traffic classifier c1
[*HUAWEI-classifier-c1] if-match nexthop 192.168.1.1 interface Vlanif 100

```
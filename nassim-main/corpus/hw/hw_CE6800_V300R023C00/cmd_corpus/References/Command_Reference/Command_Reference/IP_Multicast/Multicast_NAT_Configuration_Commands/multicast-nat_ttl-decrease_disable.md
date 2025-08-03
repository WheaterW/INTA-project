multicast-nat ttl-decrease disable
==================================

multicast-nat ttl-decrease disable

Function
--------



The **multicast-nat ttl-decrease disable** command disables the function of reducing the TTL value of multicast packets so that the TTL value of multicast packets does not decrease by 1 when the packets pass through the device.

The **undo multicast-nat ttl-decrease disable** command enables the function of reducing the TTL value of multicast packets. When a multicast packet passes through the device, the TTL value of the packet is reduced by 1.



By default, the function of reducing the TTL value of multicast packets is enabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**multicast-nat ttl-decrease disable**

**undo multicast-nat ttl-decrease disable**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In multicast NAT, input and output multicast streams are sent through different interfaces. In normal situations, the TTL value of a multicast stream decreases by 1 after the stream is sent through an outbound interface. If you do not want the TTL value of a multicast packet to decrease when the multicast packet is sent, run the multicast ttl-reduce disable command to disable the TTL value reduction function for multicast packets.

**Prerequisites**

Multicast NAT has been globally enabled using the **multicast-nat enable** command.


Example
-------

# Disable a device from reducing the TTL value of multicast packets.
```
<HUAWEI> system-view
[~HUAWEI] multicast-nat enable
[*HUAWEI] multicast-nat ttl-decrease disable

```
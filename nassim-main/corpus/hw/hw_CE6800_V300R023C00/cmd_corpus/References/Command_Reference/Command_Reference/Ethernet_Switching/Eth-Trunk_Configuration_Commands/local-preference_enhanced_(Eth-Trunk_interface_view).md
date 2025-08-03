local-preference enhanced (Eth-Trunk interface view)
====================================================

local-preference enhanced (Eth-Trunk interface view)

Function
--------



The **local-preference enhanced** command enables a chip to preferentially forward local traffic on an Eth-Trunk interface.

The **undo local-preference enhanced** command disables a chip from preferentially forwarding local traffic on an Eth-Trunk interface.



By default, a chip is disabled from preferentially forwarding local traffic on an Eth-Trunk interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H and CE6881H-K.



Format
------

**local-preference enhanced**

**undo local-preference enhanced**


Parameters
----------

None

Views
-----

Eth-Trunk interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When a chip is configured to preferentially forward local traffic through Eth-trunk member interfaces, the traffic arriving at an interface corresponding to the chip is preferentially forwarded through an Eth-Trunk member interface of the chip, without passing through the interconnection links between chips inside the local device. This avoids packet loss due to low bandwidth of the interconnection links.Preferential forwarding of local traffic on an Eth-Trunk must be enabled on a device before a chip is configured to preferentially forward local traffic on an Eth-Trunk interface. If the chip has an outbound interface, traffic is preferentially forwarded through the outbound interface of the chip. If the chip does not have an outbound interface, traffic is preferentially forwarded through an outbound interface of the local device.

**Precautions**

The function of configuring a chip to preferentially forward local traffic takes effect only for known unicast packets, and does not take effect for broadcast, multicast, and unknown unicast packets.


Example
-------

# Enable a chip to preferentially forward local traffic on an Eth-Trunk interface.
```
<HUAWEI> system-view
[~HUAWEI] interface Eth-Trunk 10
[~HUAWEI-Eth-Trunk10] local-preference enhanced

```
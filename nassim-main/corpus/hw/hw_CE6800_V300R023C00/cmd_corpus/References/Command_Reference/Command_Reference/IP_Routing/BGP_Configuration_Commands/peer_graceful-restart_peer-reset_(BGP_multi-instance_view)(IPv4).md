peer graceful-restart peer-reset (BGP multi-instance view)(IPv4)
================================================================

peer graceful-restart peer-reset (BGP multi-instance view)(IPv4)

Function
--------



The **peer graceful-restart peer-reset** command enables a device to reset the BGP connection with a specified peer in graceful restart (GR) mode.

The **undo peer graceful-restart peer-reset** command restores the default configuration.

The **peer graceful-restart peer-reset disable** command disables a peer from inheriting from a peer group the configuration of resetting the BGP connection with a specified peer in GR mode.

The **undo peer graceful-restart peer-reset disable** command restores the default configuration.



By default, a device is not enabled to reset the BGP connection with a specified peer in GR mode.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**peer** { *ipv4-address* | *ipv6-address* } **graceful-restart** **peer-reset**

**peer** { *ipv4-address* | *ipv6-address* } **graceful-restart** **peer-reset** **disable**

**undo peer** { *ipv4-address* | *ipv6-address* } **graceful-restart** **peer-reset**

**undo peer** { *ipv4-address* | *ipv6-address* } **graceful-restart** **peer-reset** **disable**

For CE6885-LL (low latency mode):

**peer** *ipv4-address* **graceful-restart** **peer-reset**

**peer** *ipv4-address* **graceful-restart** **peer-reset** **disable**

**undo peer** *ipv4-address* **graceful-restart** **peer-reset**

**undo peer** *ipv4-address* **graceful-restart** **peer-reset** **disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **peer** *ipv4-address* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |
| **peer** *ipv6-address* | Specifies an IPv6 peer address.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |



Views
-----

BGP multi-instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Currently, BGP does not support dynamic capability negotiation. Therefore, BGP capability changes cause peer relationships to be re-established and routing entries to be deleted, interrupting services. To solve this problem, run the **peer graceful-restart peer-reset** command to reset the BGP connection with a specified peer in GR mode after GR is enabled on the BGP peer.After the function of resetting the BGP connection with a specified peer in GR mode is configured, if a BGP peer relationship in another address family is established based on the BGP IPv4 unicast peer session, BGP starts to reset the BGP connection with the specified peer in GR mode and renegotiates capabilities. During this process, the BGP IPv4 unicast peer session is re-established, but the original routing entries are not deleted. The forwarding module can still forward packets based on the routing information, ensuring uninterrupted IPv4 services.

**Prerequisites**

The GR function has been enabled on a peer using the **peer capability-advertise graceful-restart** command. If GR is enabled on a peer for the first time, all sessions and instances are deleted and re-established, causing service interruptions.

**Precautions**

If the **peer capability-advertise graceful-restart** command is run but the **peer graceful-restart peer-reset** command is not run, the peer relationship reestablishment triggered by the reset bgp command or dynamic capability negotiation will not reset the BGP connection in GR mode. The peer relationship reestablishment triggered by the reset bgp command or dynamic capability negotiation resets the BGP connection in GR mode only after both the peer capability-advertise graceful-restart and **peer graceful-restart peer-reset** commands are run.


Example
-------

# Enable a device to use the GR mode to reset the BGP connection with a specified peer.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100 instance dd
[*HUAWEI-bgp-instance-dd] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp-instance-dd] peer 10.1.1.1 capability-advertise graceful-restart
[*HUAWEI-bgp-instance-dd] peer 10.1.1.1 graceful-restart peer-reset

```
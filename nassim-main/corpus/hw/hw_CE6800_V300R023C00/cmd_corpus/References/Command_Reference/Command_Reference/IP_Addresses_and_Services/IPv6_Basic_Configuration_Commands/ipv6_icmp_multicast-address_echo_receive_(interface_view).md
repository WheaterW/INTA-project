ipv6 icmp multicast-address echo receive (interface view)
=========================================================

ipv6 icmp multicast-address echo receive (interface view)

Function
--------



The **ipv6 icmp multicast-address echo receive** command enables a device to respond or disables a device from responding to ICMPv6 multicast Echo messages received on an interface.

The **undo ipv6 icmp multicast-address echo receive** command restores the default configuration in the interface view.



By default, if a device is not disabled from responding to received ICMPv6 multicast Echo messages in the system view, it responds to ICMPv6 multicast Echo messages received on an interface; if a device is disabled from responding to received ICMPv6 multicast Echo messages in the system view, it does not respond to ICMPv6 multicast Echo messages received on an interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 icmp multicast-address echo receive** { **disable** | **enable** }

**undo ipv6 icmp multicast-address echo receive** [ **disable** | **enable** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **disable** | Disables a device from responding to ICMPv6 multicast Echo messages received on an interface. | - |
| **enable** | Enables a device to respond to ICMPv6 multicast Echo messages received on an interface. | - |



Views
-----

100ge sub-interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If a routing device or an interface receives a large number of ICMPv6 multicast Echo messages, responding to these messages consumes performance. To disable a device from responding to ICMPv6 multicast Echo messages received on a specified interface, run the **ipv6 icmp multicast-address echo receive disable** command. To disable a device from responding to ICMPv6 multicast Echo messages received globally and enable a device to respond to ICMPv6 multicast Echo messages received on a specified interface, run the **ipv6 icmp multicast-address echo receive disable** command in the system view and the **ipv6 icmp multicast-address echo receive enable** command in the interface view. In this way, the performance consumption caused by responding to the messages can be reduced.

**Precautions**

Priority of enabling an interface to respond or disabling an interface from responding to received ICMPv6 multicast Echo messages:The configuration in the interface view takes precedence over the configuration in the system view.


Example
-------

# Disable a device from responding to ICMPv6 multicast Echo messages received on an interface.
```
<HUAWEI> system-view
[~HUAWEI] interface Eth-Trunk 1
[~HUAWEI-Eth-Trunk1] undo portswitch
[*HUAWEI-Eth-Trunk1] ipv6 enable
[*HUAWEI-Eth-Trunk1] ipv6 icmp multicast-address echo receive disable

```
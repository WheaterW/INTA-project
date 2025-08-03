igmp snooping send-query source-address (vlan)
==============================================

igmp snooping send-query source-address (vlan)

Function
--------



The **igmp snooping send-query source-address** command sets a source IP address for the IGMP Query messages sent by a device.

The **undo igmp snooping send-query source-address** command restores the default source IP address (192.168.0.1) of the IGMP Query messages sent by a device.



By default, the source IP address is not configured in VLAN.


Format
------

**igmp snooping send-query source-address** *ip-source-address*

**undo igmp snooping send-query source-address**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-source-address* | Specifies the source IP address contained in an IGMP Query message. | This value is in dotted decimal notation. |



Views
-----

VLAN range view,VLAN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After IGMP snooping proxy or querier is enabled on a device in a Layer 2 broadcast domain, the device sends IGMP Query messages on behalf of the upstream Layer 3 router in the Layer 2 broadcast domain to collect user information. By default, the source IP address of the IGMP Query messages sent by the device is 192.168.0.1. In some scenarios, the IP address may be used by another device, or users require that the source IP address of IGMP Query messages be on the same network segment as the IP address of the local device. In this case, you can run the igmp-snooping send-query source-address command to set a source IP address for the IGMP Query messages sent by the device.

**Precautions**



If source IP addresses are set for the Query messages both in a VLAN and globally, the configuration in the VLAN takes effect preferentially.If no source IP address is configured in a VLAN, the global configuration is used.The user VLAN inherits the relevant configuration of the multicast VLAN.




Example
-------

# Set the source IP address to 1.1.1.1 for the IGMP Query messages sent by the device in VLAN 100.
```
<HUAWEI> system-view
[~HUAWEI] igmp snooping enable
[*HUAWEI] vlan 100
[*HUAWEI-vlan100] igmp snooping send-query source-address 1.1.1.1

```
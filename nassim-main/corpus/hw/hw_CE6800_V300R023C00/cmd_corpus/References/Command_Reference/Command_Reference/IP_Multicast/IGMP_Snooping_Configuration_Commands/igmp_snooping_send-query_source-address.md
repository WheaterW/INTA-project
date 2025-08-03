igmp snooping send-query source-address
=======================================

igmp snooping send-query source-address

Function
--------



The **igmp snooping send-query source-address** command sets a source address contained in an IGMP Query message sent by a device.

The **undo igmp snooping send-query source-address** command restores the default configuration.



By default, the source IP address contained in IGMP Query messages is 192.168.0.1.


Format
------

**igmp snooping send-query source-address** *ip-source-address*

**undo igmp snooping send-query source-address**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-source-address* | Specifies a source IP address contained in an IGMP Query message. | This value is in dotted decimal notation. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

After the topology of a Layer 2 ring network changes, interfaces in a relevant VLAN will receive a link change event. After the igmp snooping send-query source-address command is run on a device on the ring network, the device will send IGMP Query messages to all non-router ports in the VLAN so that the other devices can quickly update router port information.If 192.168.0.1 has been used by other devices, the igmp snooping send-query source-address command can be used to set a new source IP address contained in IGMP Query messages sent by the IGMP snooping module.


Example
-------

# Set the source IP address contained in IGMP Query messages used to respond to Layer 2 network topology changes to 192.168.10.1.
```
<HUAWEI> system-view
[~HUAWEI] igmp snooping enable
[*HUAWEI] igmp snooping send-query source-address 192.168.10.1

```
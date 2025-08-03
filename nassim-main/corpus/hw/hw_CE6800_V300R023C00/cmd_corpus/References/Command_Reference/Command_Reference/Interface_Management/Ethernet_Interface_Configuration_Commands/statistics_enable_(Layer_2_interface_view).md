statistics enable (Layer 2 interface view)
==========================================

statistics enable (Layer 2 interface view)

Function
--------

The **statistics enable** command enables IPv4 or IPv6 traffic statistics collection on a Layer 2 physical interface.

The **undo statistics enable** command disables IPv4 or IPv6 traffic statistics collection on a Layer 2 physical interface.

By default, IPv4 or IPv6 packet statistics collection is disabled on a Layer 2 physical interface.



Format
------

**statistics** { **ipv4** | **ipv6** } **enable** [ **inbound** | **outbound** ]

**undo statistics** { **ipv4** | **ipv6** } **enable** [ **inbound** | **outbound** ]



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ipv4** | Collects statistics on IPv4 packets. | - |
| **ipv6** | Collects statistics on IPv6 packets. | - |
| **inbound** | Enables traffic statistics collection in the inbound direction of an interface. | - |
| **outbound** | Enables traffic statistics collection in the outbound direction of an interface. | - |




Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

By default, traffic statistics collection is enabled on a Layer 2 physical interface, and statistics on all the packets of the interface are collected. To collect statistics on IPv4 or IPv6 packets on a Layer 2 physical interface respectively, run this command. You can enable IPv4 traffic statistics collection and IPv6 traffic statistics collection together.

You can run the
**display interface** command or run the
**display this interface** command in the interface view to check the collected statistics.

**Precautions**

* Enabling traffic statistics collection on a Layer 2 physical interface may affect the forwarding performance, for example, some interfaces may fail to forward packets at the line rate when all interfaces provide line-rate forwarding. Use this function if required.
* Traffic statistics collection on a Layer 2 physical interface needs to occupy ACL resources of the system. If traffic statistics collection is enabled on too many Layer 2 physical interfaces, other services may fail to obtain ACL resources.
* The switch cannot collect statistics on unicast and multicast packets, respectively.


Example
-------

# Enable IPv4 and IPv6 traffic statistics collection on a Layer 2 interface.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] portswitch
[*HUAWEI-100GE1/0/1] statistics ipv4 enable
[*HUAWEI-100GE1/0/1] statistics ipv6 enable

```
statistics enable (Layer 3 main interface view)
===============================================

statistics enable (Layer 3 main interface view)

Function
--------

The **statistics enable** command enables IPv4 and IPv6 traffic statistics collection on a Layer 3 main interface.

The **undo statistics enable** command disables IPv4 and IPv6 traffic statistics collection on a Layer 3 main interface.

By default, traffic statistics collection is disabled on a Layer 3 main interface.



Format
------

**statistics** { **ipv4** | **ipv6** } **enable** [ **inbound** | **outbound** ]

**undo statistics** { **ipv4** | **ipv6** } **enable** [ **inbound** | **outbound** ]



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ipv4** | Enables traffic statistics collection of IPv4 packets. | - |
| **ipv6** | Enables traffic statistics collection of IPv6 packets. | - |
| **inbound** | Enables traffic statistics collection in the inbound direction of an interface. | - |
| **outbound** | Enables traffic statistics collection in the outbound direction of an interface. | - |




Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

To check the network status or locate network faults, you can enable traffic statistics collection on Layer 3 main interfaces, so that statistics on incoming and outgoing traffic on Layer 3 main interfaces are collected.

You can run the
**display interface** command or run the
**display this interface** command in the interface view to check the collected statistics.After you run the
**undo statistics enable** command to disable traffic statistics collection on a Layer 3 main interface, the system also clears traffic statistics on the Layer 3 main interface.

**Prerequisites**

The interface has been switched to a Layer 3 main interface using the **undo portswitch** command.

**Precautions**

* If the inbound and outbound parameters are not specified, traffic statistics collection is enabled in the inbound and outbound directions of a Layer 3 main interface.
* Enabling traffic statistics collection on a Layer 3 main interface may affect the forwarding performance, for example, some interfaces may fail to forward packets at the line rate when all interfaces provide line-rate forwarding. Use this function if required.
* Traffic statistics collection on a Layer 3 main interface needs to occupy ACL resources of the system. If traffic statistics collection is enabled on too many Layer 3 main interfaces, other services may fail to obtain ACL resources.
* For Layer 3 main interfaces, error packet statistics collection is not supported, unicast and broadcast packet statistics cannot be collected separately, and bandwidth usage statistics collection is not supported.



Example
-------

# Enable IPv4 and IPv6 traffic statistics collection on a Layer 3 main interface.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] statistics ipv4 enable
[*HUAWEI-100GE1/0/1] statistics ipv6 enable

```
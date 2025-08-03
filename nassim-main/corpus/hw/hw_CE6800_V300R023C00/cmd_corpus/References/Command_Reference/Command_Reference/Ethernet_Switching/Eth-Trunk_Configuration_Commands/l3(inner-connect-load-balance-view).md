l3(inner-connect-load-balance-view)
===================================

l3(inner-connect-load-balance-view)

Function
--------



The **l3** command configures a load balancing mode for Layer 3 packets.

The **undo l3** command deletes the specified load balancing mode of Layer 3 packets or restores the default load balancing mode of Layer 3 packets.



By default, Layer 3 packets on internal communication interfaces are load balanced based on sbsp, src-ip, dst-ip, src-port, and dst-port.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H and CE6881H-K.



Format
------

**l3** { **sbsp** | **outer-vlan** | **inner-vlan** | **src-ip** | **dst-ip** | **protocol** | **src-port** | **dst-port** } \*

**undo l3** [ **sbsp** | **outer-vlan** | **inner-vlan** | **src-ip** | **dst-ip** | **protocol** | **src-port** | **dst-port** ] \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **sbsp** | Performs load balancing based on the source port of the source card. | - |
| **outer-vlan** | Performs load balancing based on the outer VLAN ID. | - |
| **inner-vlan** | Performs load balancing based on the inner VLAN ID. | - |
| **src-ip** | Performs load balancing based on the source IP address. | - |
| **dst-ip** | Performs load balancing based on the destination IP address. | - |
| **protocol** | Performs load balancing based on the protocol number. | - |
| **src-port** | Performs load balancing based on the source port. | - |
| **dst-port** | Performs load balancing based on the destination port. | - |



Views
-----

inner-connect load balance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The device consists of two forwarding chips, which communicate with each other through internal communication interfaces. To change the load balancing mode of internal communication interfaces, run this command.The **undo l3** command with no parameter specified restores the default load balancing mode. The **undo l3** command with a parameter specified deletes the specified load balancing mode.


Example
-------

# Set the load balancing mode of Layer 3 packets to sbsp, src-ip, dst-ip, and dst-port in the load balancing profile for internal communication interfaces.
```
<HUAWEI> system-view
[~HUAWEI] load-balance inner-connect
[~HUAWEI-inner-connect] l3 sbsp src-ip dst-ip dst-port

```
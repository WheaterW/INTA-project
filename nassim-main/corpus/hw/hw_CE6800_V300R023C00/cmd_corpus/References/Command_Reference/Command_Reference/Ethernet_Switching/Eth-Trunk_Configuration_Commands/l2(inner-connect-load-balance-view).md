l2(inner-connect-load-balance-view)
===================================

l2(inner-connect-load-balance-view)

Function
--------



The **l2** command configures a load balancing mode for Layer 2 packets.

The **undo l2** command deletes the specified load balancing mode of Layer 2 packets or restores the default load balancing mode of Layer 2 packets.



By default, Layer 2 packets on internal communication interfaces are load balanced based on sbsp, dst-mac, and src-mac.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H and CE6881H-K.



Format
------

**l2** { **sbsp** | **dst-mac** | **src-mac** | **eth-type** | **outer-vlan** | **inner-vlan** } \*

**undo l2** [ **sbsp** | **dst-mac** | **src-mac** | **eth-type** | **outer-vlan** | **inner-vlan** ] \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **sbsp** | Performs load balancing based on the source port of the source card. | - |
| **dst-mac** | Performs load balancing based on the destination MAC address. | - |
| **src-mac** | Performs load balancing based on the source MAC address. | - |
| **eth-type** | Performs load balancing based on the protocol. | - |
| **outer-vlan** | Performs load balancing based on the outer VLAN ID. | - |
| **inner-vlan** | Performs load balancing based on the inner VLAN ID. | - |



Views
-----

inner-connect load balance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The device consists of two forwarding chips, which communicate with each other through internal communication interfaces. To change the load balancing mode of internal communication interfaces, run this command.The **undo l2** command with no parameter specified restores the default load balancing mode. The **undo l2** command with a parameter specified deletes the specified load balancing mode.


Example
-------

# Set the load balancing mode of Layer 2 packets to sbsp, dst-mac, src-mac, and eth-type in the load balancing profile for internal communication interfaces.
```
<HUAWEI> system-view
[~HUAWEI] load-balance inner-connect
[~HUAWEI-inner-connect] l2 sbsp dst-mac src-mac eth-type

```
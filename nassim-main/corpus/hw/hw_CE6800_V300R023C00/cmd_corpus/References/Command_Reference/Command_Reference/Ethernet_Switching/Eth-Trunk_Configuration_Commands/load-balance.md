load-balance
============

load-balance

Function
--------



The **load-balance** command sets a load balancing mode of an Eth-Trunk.

The **undo load-balance** command restores the default load balancing mode of an Eth-Trunk.



By default, the load balancing mode is enhanced mode.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**load-balance** { **dst-ip** | **src-ip** | **src-dst-ip** | **dst-mac** | **src-mac** | **src-dst-mac** | **round-robin** | **enhanced** **profile** *profile-name* }

**undo load-balance** [ **dst-ip** | **src-ip** | **src-dst-ip** | **dst-mac** | **src-mac** | **src-dst-mac** | **round-robin** | **enhanced** **profile** *profile-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **dst-ip** | Indicates load balancing based on dst-ip mode. | - |
| **src-ip** | Indicates load balancing based on src-ip mode. | - |
| **src-dst-ip** | Indicates load balancing based on src-dst-ip mode. | - |
| **dst-mac** | Indicates load balancing based on dst-mac mode. | - |
| **src-mac** | Indicates load balancing based on src-mac mode. | - |
| **src-dst-mac** | Indicates load balancing based on src-dst-mac mode. | - |
| **round-robin** | Indicates the load balancing based on round-robin mode. | - |
| **enhanced** | Indicates load balancing based on enhanced mode. | - |
| **profile** *profile-name* | Indicates the profile name. | The value is a string of 1 to 31 case-sensitive characters. The string cannot contain the following characters: | > $. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

Eth-Trunk interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To ensure proper load balancing between physical links of an Eth-Trunk and avoid link congestion, use the **load-balance** command to set the load balancing mode of the Eth-Trunk.

Load balancing is valid only for outgoing traffic; therefore, the load balancing modes for the interfaces at both ends of the link can be different and do not affect each other.

You can set the load balancing mode based on traffic models. When a parameter of traffic changes frequently, you can set the load balancing mode based on this parameter to ensure that the traffic is load balanced evenly. For example, if IP addresses in packets change frequently, use the load balancing mode based on dst-ip, src-ip, or src-dst-ip so that traffic can be properly load balanced among physical links. If MAC addresses in packets change frequently and IP addresses are fixed, use the load balancing mode based on dst-mac, src-mac, or src-dst-mac so that traffic can be properly load balanced among physical links.

The device supports the following load balancing modes:

* dst-ip: load balancing based on destination IP address. In this mode, the system obtains the destination IP address in incomimg packets to perform the Exclusive-OR calculation, and then selects the outgoing interface from the Eth-Trunk table according to the calculation result.
* dst-mac: load balancing based on destination MAC address. In this mode, the system obtains the destination MAC address in incomimg packets to perform the Exclusive-OR calculation, and then selects the outgoing interface from the Eth-Trunk table according to the calculation result.
* src-ip: load balancing based on source IP address. In this mode, the system obtains the source IP address in incoming packets to perform the Exclusive-OR calculation, and then selects the outgoing interface from the Eth-Trunk table according to the calculation result.
* src-mac: load balancing based on source MAC address. In this mode, the system obtains the source MAC address in incomimg packets to perform the Exclusive-OR calculation, and then selects the outgoing interface from the Eth-Trunk table according to the calculation result.
* src-dst-ip: load balancing based on the Exclusive-OR result of the source IP address and the destination IP address. In this mode, the system obtains the source IP address and destination IP address in incomimg packets to perform the Exclusive-OR calculation, and then selects the outgoing interface from the Eth-Trunk table according to the calculation result.
* src-dst-mac: load balancing based on the Exclusive-OR result of the source MAC address and the destination MAC address. In this mode, the system obtains the source MAC address and the destination MAC address in incomimg packets to perform the Exclusive-OR calculation, and then selects the outgoing interface from the Eth-Trunk table according to the calculation result.
* round-robin: Each Eth-Trunk member interface forwards traffic in turn. For known unicast traffic, if packets have approximate lengths, configure this load balancing mode to achieve even load balancing. This mode may cause the mis-sequencing problem. Ensure that the receive device or terminal supports assembly of mis-sequenced packets.
* enhanced load balancing: The devices select interfaces to forward packets according to the load balancing mode defined for different packets by the enhanced load balancing profile.

**Prerequisites**



Ensure that the **load-balance profile profile-name** command has been executed to create a load balancing profile before you run the load-balance enhanced profile profile-name command.



**Precautions**

If you run the **load-balance** command multiple times, only the latest configuration takes effect.


Example
-------

# Set the load balancing mode of Eth-Trunk 1 to src-dst-ip.
```
<HUAWEI> system-view
[~HUAWEI] interface Eth-Trunk 1
[*HUAWEI-Eth-Trunk1] load-balance src-dst-ip

```
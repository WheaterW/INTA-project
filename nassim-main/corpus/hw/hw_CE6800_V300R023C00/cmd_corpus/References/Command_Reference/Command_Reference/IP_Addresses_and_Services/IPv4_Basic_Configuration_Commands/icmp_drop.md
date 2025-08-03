icmp drop
=========

icmp drop

Function
--------



The **icmp drop** command enables boards to discard specifies the ICMP packets.

The **undo icmp drop** command disables boards from discarding specifies ICMP packets.



By default, interface boards do not discard ICMP packets with a TTL value of 0 or 1, and the system does not discard ICMP packets with options.


Format
------

**icmp** { **with-options** | **ttl-exceeded** } **drop** **slot** *slot-id*

**icmp** { **with-options** | **ttl-exceeded** } **drop** **all**

**undo icmp** { **with-options** | **ttl-exceeded** } **drop** **slot** *slot-id*

**undo icmp** { **with-options** | **ttl-exceeded** } **drop** **all**

**undo icmp** { **with-options** | **ttl-exceeded** } **drop** **slot** *undo-slotid*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **with-options** | enables interface boards to discard ICMP packets with options. | - |
| **ttl-exceeded** | Enables boards to discard ICMP packets with a TTL value of 0 or 1. | - |
| **slot** *slot-id* | Specifies an existing valid slot ID. | - |
| **slot** *undo-slotid* | Specifies a slot ID, which can be specified randomly and is not restricted by the current slot status. | - |
| **all** | Indicates all boards. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



If a device receives an IP datagram whose destination address is not a local address and the TTL value is 1 or 0, the device sends an ICMP TTL Exceeded packet. When a device receives a large number of ICMP packets with TTL of 1 or 0, usually sent by an attacker, device performance deteriorates because the device processes these packets. To address this issue, run the **icmp ttl-exceeded drop** command to configure the device to discard ICMP packets with TTL of 1 or 0. This improves network performance and security.When a device receives a large number of ICMP packets carrying route options, network loads increase and device performance deteriorates.To address this issue, run the **icmp with-options drop** command to configure the device to discard ICMP packets carrying route options. This improves network performance and security.




Example
-------

# Enable the system to discard ICMP packets with options.
```
<HUAWEI> system-view
[~HUAWEI] icmp with-options drop all

```

# Enable all interface boards to discard ICMP packets with a TTL value of 0 or 1.
```
<HUAWEI> system-view
[~HUAWEI] icmp ttl-exceeded drop all

```
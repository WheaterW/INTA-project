vrrp6 na interval
=================

vrrp6 na interval

Function
--------



The **vrrp6 na interval** command configures an interval at which the master router in a Virtual Router Redundancy Protocol for IPv6 (VRRP6) backup group sends NA packets.

The **vrrp6 na interval disable** command disables the master router in a Virtual Router Redundancy Protocol for IPv6 (VRRP6) backup group from periodically sending NA packets.

The **undo vrrp6 na interval** command restores the default interval.



By default, the master router sends an NA packet every 120 seconds.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**vrrp6 na interval** *interval*

**vrrp6 na interval disable**

**undo vrrp6 na interval**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies an interval at which the master router in a VRRP6 backup group sends NA packets. | The value is an integer ranging from 30 to 1200, in seconds. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After a VRRP6 backup group performs a master/backup switchover, the new master router periodically sends NA packets to update the destination MAC address and outbound interface on its connected downstream device.To configure an interval at which the master router in a VRRP6 backup group sends NA packets, run the **vrrp6 na interval** command.To ensure that the destination MAC address and outbound interface on a downstream device connected to the master router in a VRRP6 backup group are updated in real time, the master router sends NA packets to the downstream device at a specified interval. Because the NA protocol is simple and does not provide any security mechanisms, attackers can send spoofed NA packets to attack networks. To prevent security risks caused by NA attacks, run the **vrrp6 na interval disable** command to disable the master router in a VRRP6 backup group from periodically sending NA packets.

**Configuration Impact**

After the **vrrp6 na interval disable** command is run, the master routers in all VRRP6 backup groups no longer periodically send NA packets. An NA packet is sent to a downstream device only when a backup router switches to the Master state. To enable the master router in a VRRP6 backup group to periodically send NA packets and set an interval between sending NA packets, run the **vrrp6 na interval** command.


Example
-------

# Set the interval at which the master router in a VRRP6 backup group sends NA packets to 600 seconds.
```
<HUAWEI> system-view
[~HUAWEI] vrrp6 na interval 600

```

# Disable the master router in a VRRP6 backup group from periodically sending NA packets.
```
<HUAWEI> system-view
[~HUAWEI] vrrp6 na interval disable

```
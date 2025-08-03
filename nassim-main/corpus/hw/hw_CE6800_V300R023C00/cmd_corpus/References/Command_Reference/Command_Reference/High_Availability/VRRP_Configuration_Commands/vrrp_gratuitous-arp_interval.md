vrrp gratuitous-arp interval
============================

vrrp gratuitous-arp interval

Function
--------



The **vrrp gratuitous-arp interval** command sets the interval at which the master device sends a gratuitous ARP packet.

The **undo vrrp gratuitous-arp interval** command restores the default value.

The **vrrp gratuitous-arp interval disable** command disables the master device from sending a gratuitous ARP packet at intervals.



By default, the master device sends a gratuitous ARP or ND packet every 120 seconds.


Format
------

**vrrp gratuitous-arp interval** *interval*

**vrrp gratuitous-arp interval disable**

**undo vrrp gratuitous-arp interval**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies the interval at which the master device sends a gratuitous ARP packet. | The value is an integer ranging from 30 to 1200, in seconds. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The master device in a VRRP backup group periodically sends gratuitous ARP packets to downstream devices to update the destination MAC addresses and outbound interface information. You can run the vrrp gratuitous-arp interval command to set the interval at which the master device sends a gratuitous ARP packet according to the networking requirements. The interval must be less than the MAC address aging time on the downstream switches.

**Configuration Impact**

After the master device is disabled from sending gratuitous ARP packets at intervals, all VRRP groups in the Master state no longer send gratuitous ARP packets at intervals. A gratuitous ARP packet is sent to downstream devices only when a backup device becomes the master device. You can run the vrrp gratuitous-arp interval command to reenable the master device to send gratuitous ARP packets at a specified interval.

**Precautions**

After the interval at which the master device sends gratuitous ARP packets is set, running the **vrrp gratuitous-arp interval disable** command disables the master device from periodically sending gratuitous ARP packets and ND packets.Exercise caution when running the **vrrp gratuitous-arp interval disable** command.


Example
-------

# Set the interval at which the master device sends a gratuitous ARP packet to 600 seconds.
```
<HUAWEI> system-view
[~HUAWEI] vrrp gratuitous-arp interval 600

```

# Disable the master device from sending a gratuitous ARP packet at intervals.
```
<HUAWEI> system-view
[~HUAWEI] vrrp gratuitous-arp interval disable

```
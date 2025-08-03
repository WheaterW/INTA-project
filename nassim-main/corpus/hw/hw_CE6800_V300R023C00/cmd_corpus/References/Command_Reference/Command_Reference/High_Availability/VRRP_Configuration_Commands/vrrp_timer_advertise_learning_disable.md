vrrp timer advertise learning disable
=====================================

vrrp timer advertise learning disable

Function
--------



The **vrrp timer advertise learning disable** command disables a device from learning the interval at which a VRRP Advertisement packet is sent.

The **undo vrrp timer advertise learning disable** command enables a device to learn the interval at which a VRRP Advertisement packet is sent.



By default, a device is enabled to learn the interval at which a VRRP Advertisement packet is sent.


Format
------

**vrrp timer advertise learning disable**

**undo vrrp timer advertise learning disable**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The master device in a VRRP group periodically sends VRRP Advertisement packets to the backup devices in the group to notify them of its status. After receiving the VRRP Advertisement packet, each backup device compares the interval between sending VRRP Advertisement packets in the packet with the local configured interval.

* If the two intervals are the same, the backup device discards the packet, resets the Adver\_Timer, and continues monitoring the master device.
* If the two intervals are different, the backup device discards the packet but does not reset the Adver\_Timer. After the Adver\_Timer expires, the backup device switches to the Master state. As a result, two master devices coexist. To prevent this situation, run the **undo vrrp timer advertise learning disable** command to enable the backup device to learn the interval at which a VRRP Advertisement packet is sent. After the command is run, the backup device synchronizes its Adver\_Timer with the master device to ensure proper VRRP group negotiation.

**Precautions**

* If the **vrrp timer advertise learning disable** command is run to disable a device from sending VRRP Advertisement packets, the **vrrp vrid timer advertise** command must be run on devices in the same VRRP group to set the same interval at which VRRP Advertisement packets are sent. If the intervals are different on devices in a VRRP group, VRRP negotiation fails and two master devices coexist.
* After the **undo vrrp timer advertise learning disable** command is run to disable a device from learning the interval at which a VRRP Advertisement packet is sent, GR is disabled.

Example
-------

# Disable a device from learning the interval at which a VRRP Advertisement packet is sent.
```
<HUAWEI> system-view
[~HUAWEI] vrrp timer advertise learning disable

```
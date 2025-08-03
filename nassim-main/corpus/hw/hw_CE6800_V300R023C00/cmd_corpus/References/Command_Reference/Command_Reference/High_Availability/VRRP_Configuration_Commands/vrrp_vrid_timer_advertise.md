vrrp vrid timer advertise
=========================

vrrp vrid timer advertise

Function
--------



The **vrrp vrid timer advertise** command sets an interval at which the master device sends a VRRP Advertisement packet.

The **undo vrrp vrid timer advertise** command restores the default interval.



By default, the master device sends VRRP Advertisement packets at an interval of 1 second.


Format
------

**vrrp vrid** *virtual-router-id* **timer** **advertise** *advertise-interval*

**undo vrrp vrid** *virtual-router-id* **timer** **advertise**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **advertise** *advertise-interval* | Specifies the interval at which the master device sends a VRRP Advertisement packet. | The value is an integer ranging from 1 to 255, in seconds. |
| **vrid** *virtual-router-id* | Specifies the ID of a VRRP group. | The value is an integer ranging from 1 to 255. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The master device in a VRRP group periodically sends VRRP Advertisement packets to the backup devices in the group to notify them of its status. You can run the vrrp vrid timer advertise command to set an interval at which the master device in the VRRP group sends a VRRP Advertisement packet.If a backup device does not receive a VRRP Advertisement packet from the master device within a period three times the interval (As defined in relevant standards protocols: Interval specified by master-down-interval= (256 - priority)/256 + 3 x timer. According to the formula, the default interval specified by master-down-interval is about three times the interval specified by advertise-interval.) between sending VRRP Advertisement packets, the backup device considers the master device Down and preempts the Master state. If a backup device does not receive a VRRP Advertisement packet within a specified timeout period due to heavy network traffic or timer differences, a master/backup VRRP switchover is performed. To prevent this situation, configure a large interval at which the master device sends VRRP Advertisement packets.

**Prerequisites**

A VRRP group has been configured using the **vrrp vrid** command.

**Configuration Impact**

After the vrrp vrid timer advertise command is run, the master device in the specified VRRP group on a specified interface sends a VRRP Advertisement packet at a specified interval.When you configure more than 1K VRRP groups on a device, set the interval at which VRRP Advertisement packets are sent to 3 or more seconds to ensure VRRP stability.

**Precautions**



If the **vrrp timer advertise learning disable** command has been run to disable a device from learning the interval at which VRRP Advertisement packets are sent, ensure that the devices in the VRRP group have the same time for learning the interval. An interval inconsistency causes a VRRP negotiation failure. As a result, two master devices coexist.




Example
-------

# Set the interval at which the master device in VRRP group 1 sends a VRRP Advertisement packet to 5 seconds.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ip address 10.1.1.1 24
[*HUAWEI-100GE1/0/1] vrrp vrid 1 virtual-ip 10.1.1.111
[*HUAWEI-100GE1/0/1] vrrp vrid 1 timer advertise 5

```
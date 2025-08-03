carrier
=======

carrier

Function
--------



The **carrier** command configures the delay in reporting an interface status change event.

The **undo carrier** command restores the default delay in reporting an interface status change event.



By default, the delay in reporting an interface Up event and delay in reporting an interface Down event are both 0 milliseconds.


Format
------

**carrier** { **down-hold-time** *hold-down* | **up-hold-time** *hold-up* }

**undo carrier up-hold-time** [ *hold-up* ]

**undo carrier down-hold-time** [ *hold-down* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **down-hold-time** *hold-down* | Specifies the delay in reporting an interface Down event. | The value is an integer that ranges from 0 to 3600000, in milliseconds. |
| **up-hold-time** *hold-up* | Specifies the delay in reporting an interface Up event. | The value is an integer that ranges from 0 to 3600000, in milliseconds. |



Views
-----

Layer 2 100GE interface view,100GE interface view,Layer 2 10GE interface view,10GE interface view,Layer 2 200GE interface view,200GE interface view,25GE-L2 view,25GE interface view,400GE-L2 view,400GE interface view,Layer 2 50GE interface view,50GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

An Ethernet interface can be physically up or down. When the physical status of an interface changes, the device where the interface resides notifies upper-layer protocol modules, such as the routing and forwarding modules, of the change to guide packet receiving and forwarding. In addition, the device automatically generates traps and logs to remind users to perform the corresponding operations on physical links.After you configure a delay in reporting changes in interfaces' physical status, the device will not detect physical status changes during that delay. After the delay, if the physical status has not resumed its original status, the physical status changes are reported to the device.You can configure the delay in reporting physical status changes based on the network connection status.

* Set the delay in reporting status changes to a large value.For example, in some scenarios, the convergence time of the upper-layer protocol may be longer than the interface Up/Down time. If the upper-layer protocol does not converge but the interface goes Up, packet loss may occur. You need to set a long delay in reporting status changes to prevent packet loss caused by the convergence time of the upper-layer protocol longer than the interface Up/Down time.
* Set the delay in reporting status changes to a small value.For example, two links work in primary/backup mode. When the physical status of the interface on the primary link changes from up to down, the system needs to immediately instruct the upper-layer service forwarding protocol to send service packets from the interface on the backup link. In this case, you need to set a short delay for reporting status changes to ensure real-time service switchover.

**Precautions**

If you run this command multiple times on the same interface, only the latest configuration takes effect.After the **carrier down-hold-time** command is run, the system automatically adjusts the delay for an interface to go Down based on the physical layer status because the time required for an interface to go Up varies according to the interface attribute. In this manner, the interface does not go Down when signals are intermittently interrupted.


Example
-------

# Set the delay in reporting an interface Up event to 1000 milliseconds on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] carrier up-hold-time 1000

```
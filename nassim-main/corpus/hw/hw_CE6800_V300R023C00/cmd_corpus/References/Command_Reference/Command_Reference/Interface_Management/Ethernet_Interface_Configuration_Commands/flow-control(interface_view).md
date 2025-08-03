flow-control(interface view)
============================

flow-control(interface view)

Function
--------



The **flow-control** command enables flow control on an Ethernet interface.

The **undo flow-control** command disables flow control on an Ethernet interface.



By default, flow control is disabled on an Ethernet interface.


Format
------

**flow-control**

**flow-control input**

**flow-control output**

**undo flow-control**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **input** | Enables flow control in the inbound direction of an Ethernet interface. | - |
| **output** | Enables flow control in the outbound direction of an Ethernet interface. | - |



Views
-----

Layer 2 100GE interface view,100GE interface view,Layer 2 10GE interface view,10GE interface view,Layer 2 200GE interface view,200GE interface view,25GE-L2 view,25GE interface view,400GE-L2 view,400GE interface view,Layer 2 50GE interface view,50GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Network congestion causes packet loss. Flow control is a method of avoiding packet loss. If network congestion occurs on the local device after flow control is configured on both ends of the link, the local device sends a message to the peer device, instructing the peer device to reduce the packet sending rate. After receiving the message, the peer device stops sending packets to the local device no matter whether its packet sending rate is high or low, which prevents congestion.You can enable flow control in both the inbound and outbound directions of an interface or enable the function in either direction based on actual requirements. For example, if flow control is enabled in the inbound direction of an interface, the interface is controlled by the remote interface and stops sending data packets after receiving a Pause frame from the remote interface. If flow control is enabled in the outbound direction of an interface, the interface only sends a Pause frame to the remote interface, instructing the remote interface to stop sending packets. If the inbound and outbound directions are not specified, flow control is enabled in both directions.

**Precautions**

* The flow control function must also be enabled on the interface of the peer device to implement flow control.
* Flow control is not supported for broadcast packets, multicast packets, and unknown unicast packets.
* If input and output are not specified, flow control is enabled in both the inbound and outbound directions.
* When enabling flow control, ensure that no loop exists on the traffic path. Otherwise, traffic may fail to be forwarded.
* When a hwFlowControlDeadLockAlarm alarm is generated, the device automatically disables flow control in the inbound direction of the interface. When the hwFlowControlDeadLockAlarm is cleared, the device automatically restores flow control in the inbound direction of the interface.
* On the CE6866, CE6866K, CE6860-SAN, CE6860-HAM, CE8851-32CQ8DQ-P, CE8851K, CE8850-SAN, and CE8850-HAM, flow control can be configured only in the input direction.


Example
-------

# Enable flow control in the inbound direction of 10GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 10ge 1/0/1
[~HUAWEI-10GE1/0/1] flow-control input

```
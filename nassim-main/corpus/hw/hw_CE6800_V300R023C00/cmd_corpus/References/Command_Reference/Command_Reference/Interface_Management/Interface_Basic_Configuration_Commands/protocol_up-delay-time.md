protocol up-delay-time
======================

protocol up-delay-time

Function
--------



The **protocol up-delay-time** command configures a delay period (in seconds) after which the protocol status of a Layer 3 interface goes Up.

The **undo protocol up-delay-time** command restores the default configuration.



By default, the delay period is 0s, indicating the delay Up function is disabled.


Format
------

**protocol up-delay-time** *time*

**undo protocol up-delay-time**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *time* | Specifies a delay period (in seconds) after which the protocol status of a Layer 3 interface goes Up. | The value is an integer, in seconds. The range of the value and the default value vary with the interface type. The VLANIF interface number ranges from 0 to 7200. The default value is 1. For other interfaces, the value ranges from 0 to 60. The default value is 0. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view,Sub-interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



In a scenario where active and standby links are configured, if the active link is faulty, the standby link will take over traffic from the faulty active link. After the active link restores, traffic is switched back to the active link. Once the protocol status of the active link interface goes Up on a device, Layer 3 protocols, such as routing protocols and VRRP begin to send protocol packets to renegotiate with a remote device. However, if the link Layer of the local interface or remote interface is not ready for forwarding packets, the protocol packets will be discarded, causing the Layer 3 protocol negotiation to fail and burdening the device with extra costs. To address this problem, run the **protocol up-delay-time** command to configure a delay period (in seconds) after which the protocol status of a Layer 3 interface goes Up.For example, two devices are connected using an active link with the same rate interfaces whose protocol status has gone Up, but the physical status of the remote interface is blocked by STP. In this situation, when the local device sends a routing packet to the remote device, the remote device cannot respond to the packet. To address this problem, run the **protocol up-delay-time** command which allows the protocol status of a Layer 3 interface to go Up after the physical status of a link Layer restores to Up.



**Prerequisites**

The **protocol up-delay-time** command can be configured only on a Layer 3 interface.

**Precautions**

The **protocol up-delay-time time** and **shutdown network-layer** commands cannot be configured together.


Example
-------

# Configure the delay period after which the protocol status of 100GE1/0/1 goes Up to 20s.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] protocol up-delay-time 20

```
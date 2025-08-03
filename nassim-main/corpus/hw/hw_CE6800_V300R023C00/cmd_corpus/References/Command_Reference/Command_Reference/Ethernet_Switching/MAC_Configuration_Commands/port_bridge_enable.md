port bridge enable
==================

port bridge enable

Function
--------



The **port bridge enable** command enables the port bridge function. This function forwards packets with the same source and destination addresses on a port.

The **undo port bridge enable** command disables the port bridge function.



By default, the port bridge function is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**port bridge enable**

**undo port bridge enable**


Parameters
----------

None

Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

By default, an interface does not forward packets whose source and destination MAC addresses are the same. Generally, when a port receives such a packet, the switching device determines that the packet is invalid and discards it. As a result, communication between devices is affected. In this case, you can run the **port bridge enable** command to enable the port bridge function. When a port receives a packet with the same source and destination addresses, the port forwards the packet if the MAC address table on the device contains an entry corresponding to the destination MAC address of the packet. The port bridge function of a switching device applies to the following scenarios:

* A switching device is connected to devices that do not support Layer 2 forwarding. When users connected to these devices need to communicate with each other, these devices directly send packets to the switching device, and the switching device forwards these packets. In this scenario, the port bridge function must be enabled.
* A switching device is connected to multiple servers. Multiple VMs are enabled on a server, and data needs to be exchanged between the VMs. To improve the data transmission rate and server performance, enable the port bridge function on the interfaces connected to the servers so that the switching device forwards data packets between the VMs.


Example
-------

# Enable the port bridge function on 100GE 1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] port bridge enable

```
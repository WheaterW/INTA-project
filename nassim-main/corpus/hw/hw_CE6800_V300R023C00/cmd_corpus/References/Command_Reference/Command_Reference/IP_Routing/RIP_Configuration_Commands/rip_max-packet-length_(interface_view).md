rip max-packet-length (interface view)
======================================

rip max-packet-length (interface view)

Function
--------



The **rip max-packet-length** command sets the maximum length of RIP packets.

The **undo rip max-packet-length** command restores the default length.



By default, the maximum length of RIP packets is 512 bytes.


Format
------

**rip max-packet-length** *value*

**rip max-packet-length mtu**

**undo rip max-packet-length**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *value* | Specifies the maximum length of a RIP packet. | The value is an integer ranging from 32 to 65535, in bytes. |
| **mtu** | Indicates that the maximum length of a RIP packet is determined by the interface Maximum Transmission Unit (MTU). | - |



Views
-----

100GE interface view,10GE sub-interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To set the maximum length of RIP packets, run the **rip max-packet-length** command, which improves link bandwidth utilization.

**Implementation Procedure**

If the set maximum length of RIP packets is greater than the interface MTU, the interface MTU is used as the actual length of RIP packets.

**Precautions**

The maximum length of RIP packets varies with the vendor. Therefore, exercise caution when running the **rip max-packet-length** command.


Example
-------

# Configure the maximum length of RIP packets on 100GE 1/0/1 to be determined by the interface MTU.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] rip max-packet-length mtu

```
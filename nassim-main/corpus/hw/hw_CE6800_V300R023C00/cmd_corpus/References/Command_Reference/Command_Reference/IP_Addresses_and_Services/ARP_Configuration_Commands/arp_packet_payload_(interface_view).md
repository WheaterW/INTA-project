arp packet payload (interface view)
===================================

arp packet payload (interface view)

Function
--------



The **arp packet payload** command sets the payload length of ARP packets on an interface.

The **undo arp packet payload** command restores the default payload length of ARP packets on an interface.



By default, the payload length of ARP packets is 24 bytes.


Format
------

**arp packet payload** *payloadLen*

**undo arp packet payload**

**undo arp packet payload** *payloadLen*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *payloadLen* | Specifies the payload length of an ARP packet. | The value is an integer that ranges from 0 to 32, in bytes. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,1200ge sub-interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view,Interface group view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

ARP packets are encapsulated into data link frames and are called ARP frames. The length of an ARP frame is 28 bytes. An Ethernet data frame (which may be referred to as a payload, payload) has at least 46 bytes, and therefore, a padding byte (PAD) needs to be padded behind an ARP frame to meet a length requirement of the Ethernet data frame.When different products are interconnected, the payload lengths of different products are different. As a result, ARP negotiation between different devices fails and ARP learning fails. To prevent this problem, you can set the payload length of ARP packets on the device to be the same as that on the peer device.


Example
-------

# Set the payload length of ARP packets to be sent to 18 bytes.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] arp packet payload 18

```
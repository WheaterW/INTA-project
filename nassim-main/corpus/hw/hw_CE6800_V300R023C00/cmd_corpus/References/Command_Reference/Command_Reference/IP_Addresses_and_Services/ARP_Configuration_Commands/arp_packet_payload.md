arp packet payload
==================

arp packet payload

Function
--------



The **arp packet payload** command configures the payload length of ARP packets to be sent.

The **undo arp packet payload** command configures the default configuration.



By default, the payload length of ARP packets is 24 bytes.


Format
------

**arp packet payload** *payloadLen*

**undo arp packet payload** [ *payloadLen* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *payloadLen* | Specifies the payload length of ARP packets to be sent. | The value is an integer ranging from 0 to 32, in bytes. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



ARP packets are encapsulated into data link frames and are called ARP frames. The length of an ARP frame is 28 bytes. An Ethernet data frame (which may be referred to as a payload, payload) has at least 46 bytes, and therefore, a padding byte (PAD) needs to be padded behind an ARP frame to meet a length requirement of the Ethernet data frame.When different devices are interconnected, the payload lengths of ARP packets to be sent are different on these devices. As a result, ARP negotiation fails and in turn ARP entries cannot be learned. To prevent this issue, you can configure the same payload length for ARP packets to be sent on the interconnected devices.




Example
-------

# Set the payload length of ARP packets to be sent to 18 bytes.
```
<HUAWEI> system-view
[~HUAWEI] arp packet payload 18

```
jumboframe enable
=================

jumboframe enable

Function
--------



The **jumboframe enable** command configures the maximum length of a jumbo frame allowed by an interface.

The **undo jumboframe enable** command restores the default maximum length of a jumbo frame allowed by an interface.



By default, the maximum length of a jumbo frame and the maximum length of a non-jumbo frame allowed by an Ethernet interface are 9216 bytes and 1518 bytes, respectively. A frame whose length is less than or equal to 1518 bytes is a non-jumbo frame.


Format
------

**jumboframe enable** *value*

**undo jumboframe enable** [ *value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *value* | Specifies the maximum frame length allowed by an Ethernet interface. A frame whose length exceeds value is discarded. | For CE6866, CE6866K, CE6860-SAN, CE6860-HAM, CE8851-32CQ8DQ-P, CE8851K, CE8850-SAN, CE8850-HAM, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL, CE6885-T and CE6863E-48S8CQ:  The value is an integer that ranges from 1518 to 9500.  For CE6820H, CE6820S, CE6820H-K, CE6863H, CE6863H-K, CE6881H-48S6CQ and CE6881H-48S6CQ-K:  The value is an integer that ranges from 1518 to 15360.  For CE6881H-48T6CQ and CE6881H-48T6CQ-K:  The value is an integer that ranges from 1518 to 10240. |



Views
-----

Layer 2 100GE interface view,100GE interface view,Layer 2 10GE interface view,10GE interface view,Layer 2 200GE interface view,200GE interface view,25GE-L2 view,25GE interface view,400GE-L2 view,400GE interface view,Layer 2 50GE interface view,50GE interface view,Eth-Trunk interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When exchanging a large amount of data (for example, transmitting files), Ethernet interfaces may receive Jumbo frames whose length exceeds that of common packets. If the length of the received Jumbo frames exceeds the default data frame length that can be processed, the device directly discards the Jumbo frames. You can set the Jumbo frame length allowed on an interface.After the Jumbo frame length allowed on an interface is adjusted, packet forwarding becomes flexible. If multiple common Ethernet frames are used to transmit a data packet, redundant information such as inter-packet gaps (IPGs) and headers is also transmitted. If Jumbo frames are used to transmit a data packet of the same length, there are fewer frames without unnecessary IPGs and headers to transmit, improving bandwidth utilization.

For jumbo frame configurations in the Eth-Trunk interface view:

* The configurations take effect for all member interfaces. When an interface is added to the Eth-Trunk, the interface inherits jumbo frame configurations on the Eth-Trunk. When a member interface is removed from the Eth-Trunk, default jumbo frame configurations of the interface are restored.
* Jumbo frames cannot be configured on Eth-Trunk member interfaces.

**Precautions**

An interface checks whether the length of a packet exceeds the maximum frame length only in the inbound direction. An interface does not check the packet length in the outbound direction. After an interface receives protocol packets such as VXLAN packets, the chip encapsulates packet headers containing certain bytes to the packets. As a result, the length of the outgoing packets will exceed that of the incoming packets. Therefore, you need to consider the packet header length when configuring the maximum frame length allowed by an interface, preventing packets from being discarded because the packet length exceeds the maximum frame length.


Example
-------

# Set the maximum frame length allowed by 100GE1/0/1 to 5000 bytes.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] jumboframe enable 5000

```
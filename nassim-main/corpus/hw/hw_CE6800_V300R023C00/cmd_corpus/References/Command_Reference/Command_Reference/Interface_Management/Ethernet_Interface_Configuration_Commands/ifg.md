ifg
===

ifg

Function
--------



The **ifg** command configures the inter-frame gap (IFG).

The **undo ifg** command restores the default IFG.



By default, the IFG is 12 bytes.


Format
------

**ifg** *ifg-value*

**undo ifg** [ *ifg-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ifg-value* | Specifies the IFG. | The value is an integer that ranges from 8 to 16, in bytes. |



Views
-----

Layer 2 100GE interface view,100GE interface view,Layer 2 10GE interface view,10GE interface view,Layer 2 200GE interface view,200GE interface view,25GE-L2 view,25GE interface view,400GE-L2 view,400GE interface view,Layer 2 50GE interface view,50GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The IFG is used to differentiate two data packets. You can run the **ifg** command to configure the IFG to improve data packet forwarding efficiency.The packet forwarding rate, also called throughput, refers to the data forwarding capability on an interface, in pps. The packet forwarding rate is calculated based on the number of 64-byte data packets in a certain period. The payload of the preamble and IFG affects the packet forwarding rate.The default IFG is 12 bytes and is recommended. If you set the IFG to a small value, the device may not have enough time to receive the next frame after receiving one data frame. The packets then cannot be processed in real time, which results in packet loss. Similarly, if the length of a sent data frame exceeds 8000 bytes, it is recommended that you change the IFG to 16 bytes.


Example
-------

# Set the IFG of 100GE1/0/1 to 10 bytes.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] ifg 10

```
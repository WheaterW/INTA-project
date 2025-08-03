traffic-analysis udp identification block
=========================================

traffic-analysis udp identification block

Function
--------



The **traffic-analysis udp identification block** command configures the number of blocks in a UDP flow to be intelligently analyzed.

The **undo traffic-analysis udp identification block** command restores the default configuration.



By default, a UDP flow is divided into 256 blocks for intelligent traffic analysis.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**traffic-analysis udp identification block** *number*

**undo traffic-analysis udp identification block** [ *number* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *number* | Specifies the number of blocks in a UDP flow to be intelligently analyzed. | The options are as follows:   * 4 * 8 * 16 * 32 * 64 * 128 * 256   The default value is 256. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

Intelligent traffic analysis for UDP flows is performed based on the block granularity. Each UDP flow has multiple UDP packets. Each time a UDP packet is sent, the Identification field in the packet is incremented by 1, which determines the sequence number of the UDP packet. Since the Identification field is 16 bits long, the sequence numbers of UDP packets in a UDP flow range from 0 to 65535.UDP packets in a UDP flow are grouped into multiple blocks based on the sequence numbers of packets. For example, when the number of blocks is set to 128, UDP packets numbered from 0 to 511 belong to the first block. The TAP creates a flow table for a received UDP block and analyzes all UDP packets in this block.


Example
-------

# Set the number of blocks in a UDP flow to be intelligently analyzed to 128.
```
<HUAWEI> system-view
[~HUAWEI] traffic-analysis udp identification block 128

```
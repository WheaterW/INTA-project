traffic-analysis tcp one-way
============================

traffic-analysis tcp one-way

Function
--------



The **traffic-analysis tcp one-way** command enables intelligent traffic analysis for unidirectional TCP flows.

The **undo traffic-analysis tcp one-way** command restores the default configuration.



By default, intelligent traffic analysis for unidirectional TCP flows is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**traffic-analysis tcp one-way sequence** *sequence-value* *sequence-mask*

**undo traffic-analysis tcp one-way** [ **sequence** *sequence-value* *sequence-mask* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *sequence-value* | Specifies a sequence number or acknowledgment number. | The value must be a hexadecimal number and start with 0x. The length ranges from 3 to 10 digits. |
| *sequence-mask* | Specifies the mask of the sequence number or acknowledgment number. This mask is similar to the subnet mask of IP addresses. F indicates that the bit is matched, and 0 indicates that the bit is not matched. This helps determine the range of sequence numbers or acknowledgment numbers of TCP packets. | The value must be a hexadecimal number and start with 0x. The length ranges from 3 to 10 digits. |
| **sequence** | Matches TCP packets with a specified sequence number range or acknowledgment number range. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

In scenarios such as M-LAG and ECMP, packets of a specified TCP flow may be sent and received along different paths. In this case, you can enable intelligent traffic analysis for the unidirectional TCP flow. After this command is executed, the TAP checks whether the sequence numbers or acknowledgment numbers of received TCP packets are within the specified range. If so, the TAP creates a flow table that contains unidirectional TCP flow information for the TCP packets. The TAP then sends the flow table to the FabricInsight collector in real time, without waiting for the flow table to meet aging conditions. The FabricInsight collector then summarizes and sends characteristics of the TCP flow to the FabricInsight analyzer for graphical display.


Example
-------

# Enable intelligent traffic analysis for unidirectional TCP packets with sequence numbers or acknowledgment numbers of 0xXXXXXX0A (X indicates any hexadecimal number) so that the TAP can create a unidirectional flow table for these TCP packets.
```
<HUAWEI> system-view
[~HUAWEI] traffic-analysis tcp one-way sequence 0x0000000A 0x000000FF

```
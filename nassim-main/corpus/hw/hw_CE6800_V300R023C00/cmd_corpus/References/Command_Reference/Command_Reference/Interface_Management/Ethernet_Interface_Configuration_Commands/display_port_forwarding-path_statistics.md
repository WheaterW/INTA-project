display port forwarding-path statistics
=======================================

display port forwarding-path statistics

Function
--------



The **display port forwarding-path statistics** command displays statistics on packets that contain specified 5-tuple information.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display port forwarding-path path-id** *pathnum* **statistics**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **path-id** *pathnum* | Specifies the path ID. | The value is an integer that ranges from 1 to 128 . |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

The 5-tuple information includes the source and destination IP addresses, source and destination port numbers, and protocol type. Traffic transmitted on each device interface contains different 5-tuple information. If the outbound interface is an Eth-Trunk or packets have multiple ECMP next hops, you can use this command to check statistics on packets containing specified 5-tuple information (including the outbound interface), facilitating fault locating and traffic forwarding path identification.

**Precautions**



The outbound interface information is displayed in the display port forwarding-path statistics command output if traffic flows through the interface after the port forwarding-path statistics command is executed.During the port splitting or combination, the outbound interface may fail to be queried. After the port splitting or combination is completed, the outbound interface can be queried properly.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Check the statistics of the packets containing specified 5-tuple information.
```
<HUAWEI> display port forwarding-path path-id 2 statistics
Interface: 100GE1/0/1
--------------------------------------------------------------------------
Direction                              Packets                       Bytes
--------------------------------------------------------------------------
Inbound                             13,800,000               1,766,400,000
Outbound                                     0                           0
-------------------------------------------------------------------------- 

Interface: 100GE1/0/2
--------------------------------------------------------------------------
Direction                              Packets                       Bytes
--------------------------------------------------------------------------
Inbound                             13,800,000               1,766,400,000
Outbound                                     0                           0
--------------------------------------------------------------------------

```

**Table 1** Description of the **display port forwarding-path statistics** command output
| Item | Description |
| --- | --- |
| Direction | Packet direction.   * Inbound. * Outbound. |
| Packets | Number of packets. |
| Bytes | Bytes. |
| Interface | Interface that packets traverse. |
display dcb pfc buffer
======================

display dcb pfc buffer

Function
--------



The **display dcb pfc buffer** command displays information about PFC parameters.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display dcb pfc buffer** [ **interface** { *interface-name* | *interface-type* *interface-num* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-num* | Displays PFC parameter settings on a specified interface.   * interface-type specifies the type of an interface. * interface-number specifies the number of an interface.   If this parameter is not specified, PFC parameter settings of priority queues that have taken effect on all interfaces are displayed. | - |
| **interface** *interface-name* | Displays PFC parameter settings on a specified interface.   * interface-name specifies the name of an interface.   If this parameter is not specified, PFC parameter settings of priority queues that have taken effect on all interfaces are displayed. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

After PFC parameters are configured and the PFC function is enabled for queues with specified priorities, you can run the **display dcb pfc buffer** command to check information about PFC parameters in the queues with the specified priorities on the interface.

**Precautions**



For the CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL, CE6885-T, and CE6863E-48S8CQ:The buffer space is divided by fixed small blocks. Therefore, the actually effective buffer thresholds and the thresholds for triggering and stopping PFC frames are integer multiples of the fixed small block value rounded up. For the CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL (standard forwarding mode), CE6885-T, and CE6863E-48S8CQ, the fixed small block size is 320 bytes. For the CE6885-LL (low-latency mode), the fixed small block size is 96 bytes. The values in the **display dcb pfc buffer** command output are the actually effective ones.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display PFC parameter settings on all interfaces. (CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, and CE8850-HAM)
```
<HUAWEI> display dcb pfc buffer
Xon:        PFC backpressure stop threshold
Xoff:       PFC backpressure threshold
K:kilobytes   D:dynamic alpha
--------------------------------------------------
Interface      Queue            Xon           Xoff
--------------------------------------------------
100GE1/0/1         3           3(K)           4(K)
--------------------------------------------------

```

# Display PFC parameter settings on all interfaces. (CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-T, CE6885-LL (standard forwarding mode), and CE6863E-48S8CQ)
```
<HUAWEI> display dcb pfc buffer
Xon:        PFC backpressure stop threshold
Xoff:       PFC backpressure threshold
Hdrm:       Headroom buffer threshold
Guaranteed: PFC guaranteed buffer threshold
B:bytes   	K:kilobytes   	D:dynamic alpha
The actual PFC backpressure stop threshold is the higher value between the value of
xon-lowest and the difference between the value of xoff and the value of xon-offset. 
------------------------------------------------------------------------------------
Interface      Queue    Guaranteed     Xon-Lowest  Xon-Offset       Xoff        Hdrm
------------------------------------------------------------------------------------
100GE1/0/1         3       1600(B)         640(B)        6(K)       5(D)       40(K)
------------------------------------------------------------------------------------

```

# Display PFC parameter settings on all interfaces. (CE6885-LL (low-latency mode))
```
<HUAWEI> display dcb pfc buffer
Xon:        PFC backpressure stop threshold
Xoff:       PFC backpressure threshold
Hdrm:       Headroom buffer threshold
Guaranteed: PFC guaranteed buffer threshold
B:bytes   	K:kilobytes   	D:dynamic alpha
The actual PFC backpressure stop threshold is the higher value between the value of
xon-lowest and the difference between the value of xoff and the value of xon-offset. 
------------------------------------------------------------------------------------
Interface      Queue    Guaranteed     Xon-Lowest  Xon-Offset       Xoff        Hdrm
------------------------------------------------------------------------------------
100GE1/0/1         3       1632(B)         192(B)        6(K)       5(D)       40(K)
------------------------------------------------------------------------------------

```

**Table 1** Description of the **display dcb pfc buffer** command output
| Item | Description |
| --- | --- |
| K:kilobytes | The value is expressed in kilobytes. |
| Interface | Name of an interface. |
| Queue | Queue index. |
| Xon | Threshold for stopping PFC frames. |
| Xoff | Threshold for triggering PFC frames. |
| D:dynamic alpha | The value is expressed in alpha. |
| B:bytes | The unit is expressed in bytes. |
| Guaranteed | Guaranteed buffer threshold for a PFC queue in the inbound direction. |
| Xon-Lowest | Xon (threshold for stopping PFC frames) protection value. |
| Xon-Offset | Offset between the Xon value and the Xoff value. |
| Hdrm | Headroom buffer threshold for a PFC queue in the inbound direction. |
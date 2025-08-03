display ai-ecn calculated state
===============================

display ai-ecn calculated state

Function
--------



The **display ai-ecn calculated state** command displays whether the AI ECN threshold function is enabled for lossless queues and the calculated ECN thresholds.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ai-ecn calculated state** [ **interface** { *interface-name* | *interface-type* *interface-number* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** | Displays whether the AI ECN threshold function is enabled and the calculated ECN thresholds on a specified interface. | - |
| *interface-name* | Specifies an interface name. | - |
| *interface-type* | Specifies an interface type. | - |
| *interface-number* | Specifies an interface number. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run this command to display whether the AI ECN threshold function is enabled for lossless queues and the calculated ECN thresholds. Additionally, you can run the **display qos ecn threshold** command to check whether the calculated ECN thresholds take effect.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display whether the AI ECN threshold function is enabled for lossless queues and the calculated ECN thresholds.
```
<HUAWEI> display ai-ecn calculated state
AI-ECN Model Version : 1.0.1
Mode : NN - Model inference    BBR - Heuristic inference    STATIC - Static threshold
-----------------------------------------------------------------------------------------------------------------------------
Interface       Queue   Low-Threshold   High-Threshold   Probability   Mode                Active model       Actived time
                               (Byte)           (Byte)           (%)
-----------------------------------------------------------------------------------------------------------------------------
100GE1/0/1          4          204800           614400             5    BBR   AI_ECN_DistributedStorage   2022-01-10 09:09:23
100GE1/0/2          4          204800           614400             5    BBR   AI_ECN_DistributedStorage   2022-01-10 09:09:23
-----------------------------------------------------------------------------------------------------------------------------

```

**Table 1** Description of the **display ai-ecn calculated state** command output
| Item | Description |
| --- | --- |
| Mode | AI ECN inference mode:   * NN: model inference mode. * BBR: heuristic inference mode. * STATIC: static threshold mode.   A hyphen (-) is displayed when the function is abnormal. |
| Interface | Interface type and number. |
| Queue | Queue index. |
| Active model | Embedded AI system model invoked by the AI ECN function:   * AI\_ECN\_DistributedStorage: distributed storage model. * AI\_ECN\_CentralizedStorage: centralized storage model. * AI\_ECN\_HPC: high-performance computing model. * AI\_ECN\_DistributedFileStorage: distributed file storage model. |
| Actived time | Time when the AI ECN model is activated. |
| Low-Threshold(Byte) | Lower ECN threshold, in bytes. A hyphen (-) is displayed when the function is abnormal. |
| High-Threshold(Byte) | Upper ECN threshold, in bytes. A hyphen (-) is displayed when the function is abnormal. |
| Probability(%) | Maximum drop probability of ECN. A hyphen (-) is displayed when the function is abnormal. |
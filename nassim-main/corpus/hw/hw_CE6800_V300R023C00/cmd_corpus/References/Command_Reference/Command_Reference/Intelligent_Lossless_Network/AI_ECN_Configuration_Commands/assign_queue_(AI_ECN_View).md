assign queue (AI ECN View)
==========================

assign queue (AI ECN View)

Function
--------



The **assign queue** command specifies a lossless queue for which the AI ECN function is enabled.

The **undo assign queue** command disables the AI ECN function for a specified queue.



By default, no lossless queue is specified for enabling the AI ECN function.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**assign queue** *queue-id* [ **model** { **ai\_ecn\_centralizedstorage** | **ai\_ecn\_hpc** | **ai\_ecn\_distributedfilestorage** } ]

**undo assign queue** *queue-id* [ **model** { **ai\_ecn\_centralizedstorage** | **ai\_ecn\_hpc** | **ai\_ecn\_distributedfilestorage** } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *queue-id* | Specifies a lossless queue for which the AI ECN function is enabled. | For the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 0 to 7.  For the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM:The value is an integer ranging from 0 to 5. |
| **model** | Specifies the name of the model to be loaded. | - |
| **ai\_ecn\_centralizedstorage** | Specifies the centralized storage model. | - |
| **ai\_ecn\_hpc** | Specifies the high-performance computing model. | - |
| **ai\_ecn\_distributedfilestorage** | Specifies the distributed file storage model. | - |



Views
-----

AI ECN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run this command to specify a lossless queue for which AI ECN is enabled and specify the model file to be loaded to the lossless queue.If no model is specified using the **assign queue queue-id** command, the distributed storage model ai\_ecn\_distributedstorage is loaded by default.If no model is specified using the **undo assign queue queue-id** command, the loaded model is disabled.

**Precautions**

For the CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL, CE6885-T, and CE6863E-48S8CQ:

* The AI ECN function can be enabled for a maximum of two queues.
* AI ECN and static ECN can be enabled for a combined total of four queues. To enable static ECN for a specified queue, run the **qos queue ecn** command.
* When the AI ECN function is enabled for two or more queues on an interface, the performance can be improved only when both the distributed storage model and high-performance computing model are loaded.

For the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, and CE8850-HAM:

* The AI ECN function can be enabled for a maximum of two queues.
* When the AI ECN function is enabled for two queues on an interface, the performance can be improved only when the distributed storage model and high-performance computing model are loaded for the two queues respectively.
* If the AI ECN function has been enabled for two queues and the device is downgraded to a version that supports AI ECN enabled for only one queue, some of the configuration is lost and only one queue with AI ECN enabled is retained.
* If the AI ECN function has been enabled for one queue and the device is downgraded to a version that supports AI ECN enabled for only one queue, the configuration is retained. That is, the queue for which AI ECN has been enabled still takes effect.


Example
-------

# Enable the AI ECN function for queue 3. If no model is specified, the distributed storage model is loaded by default.
```
<HUAWEI> system-view
[~HUAWEI] ai-service
[*HUAWEI-ai-service] ai-ecn
[*HUAWEI-ai-service-ai-ecn] assign queue 3

```

# Enable AI ECN for queue 3 and load the centralized storage model.
```
<HUAWEI> system-view
[~HUAWEI] ai-service
[*HUAWEI-ai-service] ai-ecn
[*HUAWEI-ai-service-ai-ecn] assign queue 3 model ai_ecn_centralizedstorage

```

# Enable AI ECN for queue 3 and load the distributed storage model. Enable AI ECN for queue 4 and load the high-performance computing model.
```
<HUAWEI> system-view
[~HUAWEI] ai-service
[*HUAWEI-ai-service] ai-ecn
[*HUAWEI-ai-service-ai-ecn] assign queue 3
[*HUAWEI-ai-service-ai-ecn] assign queue 4 model ai_ecn_hpc

```

# Enable AI ECN for queue 3 and load the distributed file storage model.
```
<HUAWEI> system-view
[~HUAWEI] ai-service
[*HUAWEI-ai-service] ai-ecn
[*HUAWEI-ai-service-ai-ecn] assign queue 3 model ai_ecn_distributedfilestorage

```
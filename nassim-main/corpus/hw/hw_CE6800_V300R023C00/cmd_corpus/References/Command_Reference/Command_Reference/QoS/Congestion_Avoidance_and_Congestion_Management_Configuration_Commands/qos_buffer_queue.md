qos buffer queue
================

qos buffer queue

Function
--------



The **qos buffer queue** command configures service buffer thresholds for queues.

The **undo qos buffer queue** command cancels the configuration.



By default, the service buffer thresholds for queues are not configured.


Format
------

For CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode):

**qos buffer queue** *queue-index* **shared-threshold** { **static** *bytes-value* { **bytes** | **kbytes** | **mbytes** } | **dynamic** *dynamic-value* }

**undo qos buffer queue** *queue-index* [ **shared-threshold** [ **static** [ *bytes-value* { **bytes** | **kbytes** | **mbytes** } ] | **dynamic** [ *dynamic-value* ] ] ]

For CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K:

**qos buffer queue** *queue-index* **shared-threshold** **dynamic** *dynamic-value*

**undo qos buffer queue** *queue-index* **shared-threshold** **dynamic**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *queue-index* | Specifies the index of a queue. | The value is an integer ranging from 0 to 7. |
| **shared-threshold** | Specifies the queue-level service buffer size. | - |
| **static** *bytes-value* | Specifies the queue-level service buffer in static mode.   * bytes: The unit is byte. * kbytes: The unit is kbyte. * mbytes: The unit is mbyte.   NOTE:  This parameter is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | For the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer that ranges from 0 to 34078720, in bytes.  For the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM:The value is an integer that ranges from 0 to 31457280, in bytes.  For the CE6885-LL (low latency mode):The value is an integer that ranges from 0 to 10223616, in bytes. |
| **bytes** | Indicates that the queue-level service buffer specified in static mode is expressed in bytes.  NOTE:  This parameter is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **kbytes** | Indicates that the queue-level service buffer specified in static mode is expressed in kbytes.  NOTE:  This parameter is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **mbytes** | Indicates that the queue-level service buffer specified in static mode is expressed in mbytes.  NOTE:  This parameter is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **dynamic** *dynamic-value* | Specifies the dynamic service buffer threshold for queues. | For the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 12.  For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S:The value is an integer ranging from 0 to 10. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run the **qos buffer queue** command to manually set the buffer threshold for queues.

**Prerequisites**



Before running this command, ensure that the qos burst-mode (system view) command is not configured in the system view and the qos burst-mode (interface view) command is not configured in the interface view.



**Precautions**

* The **qos buffer queue** command sets the queue-level service buffer for outbound queues.
* The buffer space is divided by fixed small block. When the queue-level service buffer size is statically specified, the actual buffer size is an integer multiple of the fixed small block size, which is slightly different from the configured value.


Example
-------

# Set the depth of buffer threshold for queue 1 on 100GE1/0/1 to 2000 bytes.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] qos buffer queue 1 shared-threshold static 2000 bytes

```

# Set the dynamic service buffer threshold for queue 1 on 100GE1/0/1 to 5.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] qos buffer queue 1 shared-threshold dynamic 5

```
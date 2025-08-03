npcc mode
=========

npcc mode

Function
--------



The **npcc mode** command configures the NPCC function to work in high throughput mode or low-latency mode.

The **undo npcc mode** command restores the mode of the NPCC function to the default setting.



By default, the NPCC function works in high throughput mode.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**npcc mode** { **high-throughput** | **low-latency** }

**undo npcc mode** { **high-throughput** | **low-latency** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **high-throughput** | Specifies the high-throughput mode. | - |
| **low-latency** | Specifies the low-latency mode. | - |



Views
-----

NPCC view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

You can run this command to configure the NPCC function to work in high-throughput mode or low-latency mode. In high-throughput mode, the device focuses on improving the throughput of RoCEv2 traffic. In low-latency mode, the device aims to reduce the latency of RoCEv2 traffic. Generally, the high-throughput mode is recommended for storage scenarios.


Example
-------

# Configure the NPCC function to work in low-latency mode.
```
<HUAWEI> system-view
[~HUAWEI] ai-service
[*HUAWEI-ai-service] npcc
[*HUAWEI-ai-service-npcc] npcc mode low-latency

```
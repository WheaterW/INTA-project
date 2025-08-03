buffer optimization mode
========================

buffer optimization mode

Function
--------



The **buffer optimization mode** command configures the plane buffer optimization mode and enables the plane buffer optimization function.

The **undo buffer optimization mode** command disables the plane buffer optimization function.



By default, the plane buffer optimization function is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

For CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE8850-SAN, CE8851-32CQ8DQ-P, CE8850-HAM, CE8851K:

**buffer optimization mode long-distance**

**undo buffer optimization mode long-distance**

For CE6860-SAN, CE8850-SAN:

**buffer optimization mode enhanced-long-distance**

**undo buffer optimization mode enhanced-long-distance**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **long-distance** | Specifies the plane buffer optimization mode to long-distance mode. | - |
| **enhanced-long-distance** | Specifies the plane buffer optimization mode to enhanced long-distance mode.  NOTE:  This parameter is supported only on the CE6860-SAN and CE8850-SAN. | - |



Views
-----

AI Service view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Plane buffer optimization can intelligently allocate buffer spaces for different planes based on the service mode of the live network, reducing the buffer space of the plane where interfaces with low usage reside and ensuring that the interfaces where lossless queues reside can obtain sufficient buffer space. This function can be configured when lossless services on the live network have a long communication distance, for example, storage services deployed across multiple data centers.

**Precautions**

* After the plane buffer optimization mode is modified and takes effect, the configurations related to the buffer threshold, such as the WRED/ECN/PFC queue buffer configuration, may be affected.
* The **buffer optimization mode** command and the **qos burst-mode** command are mutually exclusive.
* The new plane buffer optimization mode takes effect after the device restarts.

Example
-------

# Set the plane buffer optimization mode to long-distance mode.
```
<HUAWEI> system-view
[~HUAWEI] ai-service
[~HUAWEI-ai-service] buffer optimization mode long-distance

```
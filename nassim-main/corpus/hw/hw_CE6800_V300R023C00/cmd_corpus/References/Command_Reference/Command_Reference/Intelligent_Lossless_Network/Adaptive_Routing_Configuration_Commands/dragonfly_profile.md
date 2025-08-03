dragonfly profile
=================

dragonfly profile

Function
--------



The **dragonfly profile** command displays the dragonfly profile view.

The **undo dragonfly profile** command deletes a dragonfly profile.



By default, a dragonfly profile exists.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**dragonfly profile default**

**undo dragonfly profile default**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **default** | Specifies the default dragonfly profile. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Currently, the device supports only the default dragonfly profile. You can run the **dragonfly profile** command to enter the default dragonfly profile view and configure adaptive routing parameters, including the threshold of the bandwidth utilization level, threshold of the queue depth level, and interval for sending ARN messages about congestion.

**Precautions**

Currently, only the default dragonfly profile is supported and cannot be deleted.


Example
-------

# Enter the default dragonfly profile view.
```
<HUAWEI> system-view
[~HUAWEI] dragonfly profile default

```
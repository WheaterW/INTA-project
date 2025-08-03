assign queue (iQCN View)
========================

assign queue (iQCN View)

Function
--------



The **assign queue** command specifies a lossless queue for which the iQCN function is enabled.

The **undo assign queue** command disables the iQCN function for a specified queue.



By default, no lossless queue is specified for enabling the iQCN function.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**assign queue** *queueid*

**undo assign queue** *queueid*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *queueid* | Specifies a lossless queue for which the iQCN function is enabled. | The value is an integer ranging from 0 to 5. |



Views
-----

iQCN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

You can run this command to specify a lossless queue for which the iQCN function is enabled.


Example
-------

# Specify queue 3 for which the iQCN function is enabled.
```
<HUAWEI> system-view
[~HUAWEI] ai-service
[*HUAWEI-ai-service] iqcn
[*HUAWEI-ai-service-iqcn] assign queue 3

```
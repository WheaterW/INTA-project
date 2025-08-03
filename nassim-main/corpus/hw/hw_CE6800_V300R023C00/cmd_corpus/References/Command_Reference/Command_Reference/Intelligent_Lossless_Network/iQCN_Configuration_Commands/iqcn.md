iqcn
====

iqcn

Function
--------



The **iqcn** command displays the iQCN view.

The **undo iqcn** command deletes all configurations in the iQCN view and disables iQCN.



By default, the iQCN is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**iqcn**

**undo iqcn**


Parameters
----------

None

Views
-----

AI Service view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run this command to enter the iQCN view and configure the iQCN function. In this way, the device can intelligently determine the congestion status on the network and proactively send CNP packets to the NIC of the source host, ensuring that the NIC reduces the packet sending rate in a timely manner.

**Precautions**

NPCC and iQCN cannot be enabled at the same time in the AI service view.


Example
-------

# In the AI service view, enter the iQCN view.
```
<HUAWEI> system-view
[~HUAWEI] ai-service
[*HUAWEI-ai-service] iqcn
[*HUAWEI-ai-service-iqcn]

```
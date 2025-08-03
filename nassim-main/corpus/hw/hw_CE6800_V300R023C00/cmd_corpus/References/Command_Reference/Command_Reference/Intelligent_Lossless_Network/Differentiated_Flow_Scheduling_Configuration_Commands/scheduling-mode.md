scheduling-mode
===============

scheduling-mode

Function
--------



The **scheduling-mode** command configures a scheduling mode.

The **undo scheduling-mode** command cancels the scheduling mode.



By default, no scheduling mode is configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**scheduling-mode hybrid**

**undo scheduling-mode hybrid**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **hybrid** | Specifies the hybrid scheduling mode. | - |



Views
-----

mice-elephant-flow view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

You can run this command to configure a scheduling mode. The hybrid mode is used to optimize performance in hybrid scheduling scenarios. For example, the hybrid mode can optimize performance in NVMe over TCP scenarios where TCP and UDP are used together.


Example
-------

# Set the scheduling mode to hybrid.
```
<HUAWEI> system-view
[~HUAWEI] ai-service
[*HUAWEI-ai-service] mice-elephant-flow
[*HUAWEI-ai-service-mice-elephant-flow] scheduling-mode hybrid

```
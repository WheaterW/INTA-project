assign forward mode
===================

assign forward mode

Function
--------



The **assign forward mode** command configures the packet forwarding mode.

The **undo assign forward mode** command restores the default packet forwarding mode.



By default, the packet forwarding mode is store-and-forward mode.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**assign forward mode** { **cut-through** | **store-and-forward** }

**undo assign forward mode** [ **cut-through** | **store-and-forward** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **cut-through** | Sets the packet forwarding mode to cut-through. | - |
| **store-and-forward** | Sets the packet forwarding mode to store-and-forward. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When low packet delay is required, run the assign forward mode command to set the packet forwarding mode to cut-through to speed up packet forwarding.

**Precautions**

* In cut-through mode, CRC error packets are also forwarded but not discarded. - In cut-through mode, if network congestion occurs, the system forwards packets in store-and-forward mode. After network congestion is eliminated, the system forwards packets in cut-through mode.

Example
-------

# Set the packet forwarding mode to cut-through.
```
<HUAWEI> system-view
[~HUAWEI] assign forward mode cut-through

```
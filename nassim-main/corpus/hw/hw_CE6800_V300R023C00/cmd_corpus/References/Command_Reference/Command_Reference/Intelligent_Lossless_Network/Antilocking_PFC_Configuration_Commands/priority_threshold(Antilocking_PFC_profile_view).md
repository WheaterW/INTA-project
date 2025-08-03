priority threshold(Antilocking PFC profile view)
================================================

priority threshold(Antilocking PFC profile view)

Function
--------



The **priority threshold** command sets the buffer threshold for antilocking PFC to take effect.

The **undo priority threshold** command restores the default buffer threshold for antilocking PFC to take effect.



By default, the buffer threshold for antilocking PFC to take effect is 0.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6885-SAN.



Format
------

**priority** *priority* **threshold** *threshold-value*

**undo priority** *priority* **threshold** [ *threshold-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *priority* | Specifies the priority. | The value is an integer ranging from 0 to 7. |
| *threshold-value* | Specifies the buffer threshold for antilocking PFC to take effect. | The value is an integer that ranges from 0 to 512. The unit is KB and the default value is 0. |



Views
-----

Antilocking PFC profile view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run this command to configure the buffer threshold for antilocking PFC to take effect based on priority queues.

**Prerequisites**

The **priority** command has been run to specify the priority queue for which antilocking PFC is enabled.


Example
-------

# Set the buffer threshold for antilocking PFC to take effect in priority queue 3 to 1 KB.
```
<HUAWEI> system-view
[~HUAWEI] abs-pfc profile myabspfc
[~HUAWEI-abs-pfc-myabspfc] priority 3
[*HUAWEI-abs-pfc-myabspfc] priority 3 threshold 1

```
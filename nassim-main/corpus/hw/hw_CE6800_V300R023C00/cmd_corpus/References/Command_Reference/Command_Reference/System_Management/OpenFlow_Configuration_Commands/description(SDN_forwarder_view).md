description(SDN forwarder view)
===============================

description(SDN forwarder view)

Function
--------



The **description** command configures a description for an OpenFlow-compatible device.

The **undo description** command deletes the description of an OpenFlow-compatible device.



By default, no description is configured for an OpenFlow-compatible device.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**description** *text*

**undo description**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *text* | Specifies the description of an OpenFlow-compatible device. | The value is a string of 1 to 63 characters, spaces supported. |



Views
-----

SDN forwarder view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

You can configure the description of an OpenFlow-compatible device to identify device features, facilitating memorization and management.


Example
-------

# Set the description of an OpenFlow-compatible device to Huawei.
```
<HUAWEI> system-view
[~HUAWEI] sdn agent
[*HUAWEI-sdn-agent] description Huawei

```
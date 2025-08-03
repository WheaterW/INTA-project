aggregation service-port
========================

aggregation service-port

Function
--------



The **aggregation service-port** command configures an aggregation service port number.

The **undo aggregation service-port** command cancels the aggregation service port number configuration.



By default, no aggregation service port number is configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**aggregation service-port** { *port-id1* [ **to** *port-id2* ] }

**undo aggregation service-port** { *port-id1* [ **to** *port-id2* ] }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *port-id1* | Specify start port number. | The value is an integer ranging from 0 to 65535. |
| **to** *port-id2* | Specify end port number. | The value is an integer ranging from 0 to 65535. |



Views
-----

any-flow view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After the flow aggregation function is enabled, you need to specify the aggregation service port number. The device aggregates only the service traffic with the specified service port number.

**Precautions**

If aggregation flow statistics export is configured, the device does not report original flow statistics. Set a proper service port number range.


Example
-------

# Configure the device to aggregate only flows destined for port 1500.
```
<HUAWEI> system-view
[~HUAWEI] any-flow
[*HUAWEI-any-flow] aggregation service-port 1500

```
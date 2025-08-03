traffic-analysis tcp export template timeout-rate
=================================================

traffic-analysis tcp export template timeout-rate

Function
--------



The **traffic-analysis tcp export template timeout-rate** command sets the delivery interval of the template for exporting packets carrying the TCP flow analysis results of intelligent traffic analysis.

The **undo traffic-analysis tcp export template timeout-rate** command restores the default configuration.



By default, the delivery interval of the template for exporting packets carrying the TCP flow analysis results of intelligent traffic analysis is 1 minute.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**traffic-analysis tcp export template timeout-rate** *timeout-interval*

**undo traffic-analysis tcp export template timeout-rate** [ *timeout-interval* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *timeout-interval* | Specifies the interval at which the template is delivered. | The value is an integer that ranges from 1 to 60. in minute. The default value is 1. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

When intelligent traffic analysis results of TCP flows are exported, the corresponding data template must also be exported to the TDA for parsing packets. You can run this command to configure the interval at which the template is delivered.If network traffic is heavy, the template delivery interval should be set to a small value. However, more traffic will be generated for sending the template. Similarly, if the template delivery interval is set to a large value, less traffic is generated for sending the template. Therefore, you need to set a proper template delivery interval based on actual requirements. The default interval is recommended if you do not have special requirements.


Example
-------

# Set the delivery interval of the template for exporting packets carrying the flow analysis results of TCP packets to 15 minutes.
```
<HUAWEI> system-view
[~HUAWEI] traffic-analysis tcp export template timeout-rate 15

```
raps-mel
========

raps-mel

Function
--------



The **raps-mel** command sets the value of the maintenance entity group level (MEL) field in R-APS PDUs.

The **undo raps-mel** command restores the default value of the MEL field.



By default, the value of the MEL field in R-APS PDUs is 7.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE8855, CE8851-32CQ4BQ, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**raps-mel** *level-id*

**undo raps-mel**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *level-id* | Specifies the value of the MEL field in R-APS PDUs. | The value is an integer ranging from 0 to 7. The default is 7. |



Views
-----

ERPS ring view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



On a Layer 2 network where ERPS is running, if another fault detection protocol is enabled, the MEL field in R-APS PDUs determines whether the R-APS PDUs can be forwarded. If the MEL value in an ERPS ring is smaller than the MEL value of the fault detection protocol, the R-APS PDUs have a lower priority and are discarded. If the MEL value in an ERPS ring is larger than the MEL value of the fault detection protocol, the R-APS PDUs can be forwarded. You can run the **raps-mel** command to set the value of the MEL field in R-APS PDUs.In addition, the MEL value can also be used for interworking with other vendors' devices in an ERPS ring. The same MEL value ensures smooth communication between devices.




Example
-------

# Specify the value of the MEL field of R-APS PDUs to 5 in ERPS ring 1.
```
<HUAWEI> system-view
[~HUAWEI] erps ring 1
[*HUAWEI-erps-ring1] raps-mel 5

```
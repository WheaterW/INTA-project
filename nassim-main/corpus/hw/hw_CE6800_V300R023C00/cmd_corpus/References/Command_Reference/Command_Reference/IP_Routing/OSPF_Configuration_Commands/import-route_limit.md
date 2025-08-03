import-route limit
==================

import-route limit

Function
--------



The **import-route limit** command sets a limit on the number of LSAs generated when an OSPF or OSPFv3 process imports routes.

The **undo import-route limit** command cancels the limit on the number of LSAs generated when an OSPF or OSPFv3 process imports routes.



By default, the number of LSAs generated when an OSPF or OSPFv3 process imports external routes is not limited.


Format
------

**import-route limit** *limit-number* [ **threshold-alarm** { **upper-limit** *upper-limit-value* | **lower-limit** *lower-limit-value* } \* ]

**undo import-route limit** [ *limit-number* ] [ **threshold-alarm** [ **upper-limit** *upper-limit-value* | **lower-limit** *lower-limit-value* ] \* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *limit-number* | Specifies a limit on the number of LSAs generated when an OSPF or OSPFv3 process imports external routes. | The value is an integer ranging from 1 to 4294967295. |
| **threshold-alarm** | Indicates an alarm threshold. | - |
| **upper-limit** *upper-limit-value* | Specifies the upper alarm threshold, in percentage. | The value is an integer ranging from 1 to 100. The default value is 80. |
| **lower-limit** *lower-limit-value* | Specifies the lower alarm threshold, in percentage. | The value is an integer ranging from 1 to 100. The default value is 70. |



Views
-----

OSPFv3 view,OSPF view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When OSPF imports a large number of external routes and advertises them to a device with a small route capacity, the number of routes learned by the device exceeds the route capacity. As a result, the device restarts unexpectedly. To prevent this problem, set a limit on the number of LSAs generated when an OSPF process imports external routes to ensure stable device operation. You can run the **display ospf brief** command to view the Current status field in the command output.

* Normal: The lower alarm threshold is not exceeded.
* Approach limit: The upper alarm threshold is about to be reached. The upper alarm threshold has reached 90% of the upper alarm threshold.
* Exceed limit: The number has reached or exceeded the maximum.upper-limit-value must be greater than or equal to lower-limit-value.When the number of LSAs generated when an OSPF process imports external routes reaches the alarm threshold, the device generates the following alarms:
* The system generates the OSPF\_1.3.6.1.4.1.2011.5.25.155.31.7 hwOspfv2ImportAseRouteThreshold alarm if the number of ASE LSAs generated when an OSPF process imports external routes exceeds the upper alarm threshold (in percentage) multiplied by the maximum number allowed.The system generates the OSPF\_1.3.6.1.4.1.2011.5.25.155.31.8 hwOspfv2ImportAseRouteThresholdClear alarm if the number falls to or below the lower alarm threshold (in percentage) multiplied by the maximum number allowed.
* The system generates the OSPF\_1.3.6.1.4.1.2011.5.25.155.31.9 hwOspfv2ImportAseRouteExceed alarm if the number of ASE LSAs generated when an OSPF process imports external routes is greater than or equal to the maximum number allowed.
* The system generates the OSPF\_1.3.6.1.4.1.2011.5.25.155.31.10 hwOspfv2ImportAseRouteExceedClear alarm if the number of ASE LSAs generated when an OSPF process imports external routes falls below 90% of the maximum number allowed.
* The system generates the OSPF\_1.3.6.1.4.1.2011.5.25.155.31.11 hwOspfv2ImportNssaRouteThreshold alarm if the number of NSSA LSAs generated when an OSPF process imports external routes exceeds the upper alarm threshold (in percentage) multiplied by the maximum number allowed.
* The system generates the OSPF\_1.3.6.1.4.1.2011.5.25.155.31.12 hwOspfv2ImportNssaRouteThresholdClear alarm if the number falls to or below the lower alarm threshold (in percentage) multiplied by the maximum number allowed.
* The system generates the OSPF\_1.3.6.1.4.1.2011.5.25.155.31.13 hwOspfv2ImportNssaRouteExceed alarm if the number of NSSA-LSAs generated when an OSPF process imports external routes is greater than or equal to the maximum number allowed.
* The system generates the OSPF\_1.3.6.1.4.1.2011.5.25.155.31.14 hwOspfv2ImportNssaRouteExceedClear alarm if the number of NSSA-LSAs generated when an OSPF process imports external routes falls below 90% of the maximum number allowed.When OSPFv3 imports a large number of external routes and advertises them to a device with a small route capacity, the number of routes learned by the device exceeds the route capacity. As a result, the device restarts unexpectedly. To prevent this problem, set a limit on the number of imported external routes to be advertised by OSPFv3 to ensure stable device running.upper-limit-value must be greater than or equal to lower-limit-value.The system generates the following alarms:
* The system generates the OSPFV3\_1.3.6.1.4.1.2011.5.25.147.0.19 hwOspfv3ImportAseRouteExceed alarm when the number of AS-external LSAs generated when an OSPFv3 process imports external routes is greater than or equal to the maximum number allowed.
* The system generates the OSPFV3\_1.3.6.1.4.1.2011.5.25.147.0.20 hwOspfv3ImportAseRouteExceedClear alarm when the number of AS-external LSAs generated when an OSPFv3 process imports external routes falls below 90% of the maximum number allowed.
* The system generates the OSPFV3\_1.3.6.1.4.1.2011.5.25.147.0.17 hwOspfv3ImportAseRouteThreshold alarm when the number of AS-external LSAs generated when an OSPFv3 process imports external routes exceeds limit-numberÃupper-limit-value/100.
* The system generates the OSPFV3\_1.3.6.1.4.1.2011.5.25.147.0.18 hwOspfv3ImportAseRouteThresholdClear alarm when the number of AS-external-LSAs generated when an OSPFv3 process imports external routes falls below limit-numberÃlower-limit-value/100 or below.

**Precautions**

The **import-route limit** command limits the number of LSAs generated when a device imports routes. If a large number of routes are imported, and this command is deleted, a large number of LSAs may be generated.


Example
-------

# Set the limit on the number of LSAs generated when an OSPF process imports external routes, the upper alarm threshold, and lower alarm threshold to 3000, 85%, and 75%, respectively.
```
<HUAWEI> system-view
[~HUAWEI] ospf 100
[*HUAWEI-ospf-100] import-route limit 3000 threshold-alarm upper-limit 85 lower-limit 75

```

# Set the limit on the number of LSAs generated when an OSPFv3 process imports external routes, the upper alarm threshold, and lower alarm threshold to 3000, 85%, and 75%, respectively.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 100
[*HUAWEI-ospfv3-100] import-route limit 3000 threshold-alarm upper-limit 85 lower-limit 75

```
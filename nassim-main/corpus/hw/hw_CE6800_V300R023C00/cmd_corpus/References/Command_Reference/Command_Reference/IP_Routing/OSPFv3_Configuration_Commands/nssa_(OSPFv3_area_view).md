nssa (OSPFv3 area view)
=======================

nssa (OSPFv3 area view)

Function
--------



The **nssa** command configures an NSSA.

The **undo nssa** command restores an OSPFv3 NSSA to a common OSPFv3 area.



By default, no OSPFv3 area is configured as an NSSA.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**nssa** [ { **default-route-advertise** [ **backbone-peer-ignore** | **cost** *cost-value* | **tag** *tag-value* | **type** *type-value* ] \* } | **no-import-route** | **no-summary** | **set-n-bit** | **translator-always** | **translator-interval** *interval-value* | **suppress-forwarding-address** ] \*

**undo nssa**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **default-route-advertise** | Generates default Type-7 LSAs on the ASBR and then advertises them to the NSSA.  The ABR generates a default NSSA LSA (Type7 LSA) automatically and advertises it in the NSSA. | - |
| **backbone-peer-ignore** | Prevents an ABR from checking the neighbor status in the backbone area. Specifically, the ABR generates default Type 7 LSAs and advertises them to the NSSA as long as an interface is up in the backbone area. | - |
| **cost** *cost-value* | Specifies the default cost of Type 7 LSAs. | The value is an integer ranging from 0 to 16777214. The default value is 1. |
| **tag** *tag-value* | Specifies the tag value of the OSPFv3 route imported to an NSSA. | The value is an integer ranging from 0 to 4294967295. The default value is 0. |
| **type** *type-value* | Specifies the default type of Type 5 LSAs. | The value is 1 or 2.   * 1: Type 1 external route * 2: Type 2 external route   The default value is 2. |
| **no-import-route** | Indicates that no external routes are imported to NSSAs. | - |
| **no-summary** | Disables ABRs from sending summary LSAs to NSSAs. | - |
| **set-n-bit** | Indicates that the N-bit is set in DD packets. | - |
| **translator-always** | Specifies the ABR in an NSSA as the translator. Multiple ABRs in an NSSA can be configured as translators. | - |
| **translator-interval** *interval-value* | Specifies the timeout period of a translator. | The value is an integer ranging from 1 to 120, in seconds. The default value is 40 seconds. |
| **suppress-forwarding-address** | Indicates that no forwarding address (FA) is set for Type 5 LSAs that are converted from Type 7 LSAs. | - |



Views
-----

OSPFv3 area view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

An NSSA is configured in the scenario where AS external routes are to be imported but not forwarded to save system resources. AS external routes can be imported to an NSSA and transmitted to the entire NSSA.All devices in the NSSA must be configured with NSSA attributes using the **nssa** command. The **nssa** command is applicable to the following scenarios:

* The keyword default-route-advertise is used to generate default Type 7 LSAs. Regardless of whether there is route ::/0 in the routing table on an ABR, a Type 7 LSA default route is generated. A Type 7 LSA default route can be generated only when there is route ::/0 in the routing table on an ASBR.
* If an ASBR also functions as an ABR, setting no-import-route prevents external routes imported using the **import-route** command from being advertised to the NSSA.
* To reduce the number of LSAs that are transmitted to the NSSA, set no-summary on an ABR to prevent the ABR from transmitting Type 3 LSAs to the NSSA.
* If set-n-bit is set, the DD packets sent by the device carry the N-bit being 1.
* If multiple ABRs are deployed in the NSSA, the system automatically selects an ABR (generally the device with the largest router ID) as a translator to convert Type 7 LSAs into Type 5 LSAs. You can also set translator-always on an ABR to specify the ABR as an all-the-time translator. To specify two ABRs for load balancing, configure translator-always on two ABRs to specify the ABRs as all-the-time translators. You can use this command to pre-configure a fixed translator to prevent LSA flooding caused by translator role changes.
* translator-interval is used to ensure uninterrupted services when translator roles change. The value must be greater than the flooding period.

**Configuration Impact**



Configuring or deleting NSSA attributes may trigger routing updates in the area. A second configuration of NSSA attributes can be implemented or canceled only after a routing update is complete.



**Precautions**

When the last ordinary area (other than a stub area or NSSA) in an OSPFv3 process is deleted, useless Type 5 LSAs originated by the local device in the area will be deleted immediately. The local device still reserves useless Type 5 LSAs received from other devices. These useless Type 5 LSAs will not be deleted until the aging time reaches 3600s.


Example
-------

# Configure area 1 as an NSSA.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] area 1
[*HUAWEI-ospfv3-1-area-0.0.0.1] nssa

```
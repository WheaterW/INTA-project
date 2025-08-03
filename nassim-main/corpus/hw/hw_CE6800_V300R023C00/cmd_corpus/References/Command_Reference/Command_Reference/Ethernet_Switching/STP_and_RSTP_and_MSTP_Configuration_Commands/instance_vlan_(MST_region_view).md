instance vlan (MST region view)
===============================

instance vlan (MST region view)

Function
--------



The **instance vlan** command maps a VLAN or VLAN range to a Multiple Spanning Tree Instance (MSTI).

The **undo instance vlan** command deletes the mapping between a VLAN or VLAN range and an MSTI.



By default, all VLANs are mapped to Common and Internal Spanning Tree (CIST), namely, instance 0.


Format
------

**instance** *instance-id* **vlan** { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10>

**undo instance** *instance-id* [ **vlan** { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10> ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *instance-id* | Specifies the ID of an MSTI. | The value is an integer ranging from 0 to 4094, Value 0 indicates CIST.  <instance-id> specified in the undo instance command cannot be 0, that is, instance 0 cannot be deleted. |
| *vlan-id1* | Specifies the start VLAN ID to be mapped to an MSTI. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **to** *vlan-id2* | Specifies the end VLAN ID to be mapped to an MSTI. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094. <vlanIdEnd> must be greater than <vlanIdBegin>.  For the CE6885-LL (low latency mode):The value is an integer that ranging from 1 to 1023. The value must be greater than vlanIdBegin. |



Views
-----

MST region view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

MSTP divides a switching network into multiple regions, each of which has independent Multiple Spanning Trees. Each spanning tree is called an MSTI, and each region is called a Multiple Spanning Tree (MST) region. Two devices belong to the same MST region only when their following configurations are the same:

* MST region name
* Mappings between MSTIs and VLANs
* MST region revision levelTo map a VLAN or VLAN range to an MSTI, run the instance command.

**Configuration Impact**

When using the **undo instance** command, note the following points:

* After the mapping between specified VLANs and a specified MSTI is deleted, these VLANs will be mapped to CIST, namely, instance 0.
* If no VLAN is specified, all VLANs that have established mappings with an MSTI are mapped to CIST.If the instance command is run more than once, all configurations take effect.

**Precautions**

A VLAN cannot be mapped to different MSTIs. If the instance command is run more than once, the latest configuration overrides the previous one.


Example
-------

# Map VLAN 2 to MSTI 1.
```
<HUAWEI> system-view
[~HUAWEI] stp region-configuration
[~HUAWEI-mst-region] instance 1 vlan 2

```
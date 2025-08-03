vlan batch
==========

vlan batch

Function
--------



The **vlan batch** command creates VLANs in batches.

The **undo vlan batch** command is used to delete VLANs in batches.



By default, VLAN 1 exists.


Format
------

**vlan batch** { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10>

**undo vlan batch** { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10>


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **to** *vlan-id2* | Specifies the end ID of a VLAN. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **batch** *vlan-id1* | Specifies the start VLAN ID. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **vlan batch** command creates multiple VLANs at one time, simplifying VLAN configuration.

**Precautions**

The **vlan batch** command creates VLANs in batches. If a VLAN has been created, using this command does not create the same VLAN or modify the VLAN configuration. If you run the **vlan batch** command more than once, all the created VLANs take effect.


Example
-------

# Create VLAN 6, VLAN 7, and VLAN 16 through VLAN 20 in a batch.
```
<HUAWEI> system-view
[~HUAWEI] vlan batch 6 7 16 to 20

```
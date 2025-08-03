instance vlan (VLAN instance view)
==================================

instance vlan (VLAN instance view)

Function
--------



The **instance vlan** command maps a VLAN or VLAN range to an instance.

The **undo instance vlan** command deletes the mapping between a VLAN or VLAN range and an instance.



By default, all VLANs are mapped to instance 0.


Format
------

**instance** *instance-id* **vlan** { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10>

**undo instance** *instance-id* [ **vlan** { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10> ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *instance-id* | Specifies the ID of a Layer 2 ring protocol instance. | The value is an integer ranging from 0 to 65535. Value 0 indicates CIST. |
| *vlan-id1* | Specifies the start VLAN ID. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **to** *vlan-id2* | Specifies the ID of an end VLAN.  <vlan-id2> and <vlan-id1> specify a VLAN range. If to <vlan-id2> is not specified, only the VLAN specified by <vlan-id1> is mapped to an instance.  The value of <vlan-id2> must be greater than or equal to that of <vlan-id1>. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |



Views
-----

VLAN instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When you configure a Layer 2 ring protocol, run the **instance vlan** command in the VLAN instance view to configure mappings between a Layer 2 ring protocol instance and VLANs. This command applies to all ring protocols, facilitating configurations.

**Configuration Impact**



After you run the **undo instance vlan** command to delete mappings between a specified instance and VLANs, these VLANs will be remapped to instance 0.If the **instance vlan** command is run more than once, all configurations take effect.




Example
-------

# Map VLAN 2 to instance 1.
```
<HUAWEI> system-view
[~HUAWEI] vlan instance
[~HUAWEI-vlan-instance] instance 1 vlan 2

```
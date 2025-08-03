binding bridge-domain profile
=============================

binding bridge-domain profile

Function
--------



The **binding bridge-domain profile** command binds a BD profile to a BD.

The **undo binding bridge-domain profile** command unbinds a BD profile from a BD.



By default, no BD profile is created.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**binding bridge-domain profile** *profileId*

**undo binding bridge-domain profile** *profileId*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *profileId* | Specifies the ID of the profile to be bound to a BD. | The value is a string of 1 to 16 characters. |



Views
-----

bd-range view,Bridge domain view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When replacing a TRILL network with a VXLAN network, you need to bind VLANs and VNIs to BDs and configure EVPN-related commands in BDs. If there are a large number of BDs, the configuration workload is heavy. To address this issue, a BD profile is introduced to automatically bind VLANs and VNIs to BDs and automatically generate RDs and RTs for EVPN instances. The preceding configurations can be automatically generated for a BD after the BD is bound to the BD profile.

**Precautions**

1. A profile can be bound to a maximum of 500 BDs.
2. A BD can be automatically bound to VLANs ranging from 1 to 4094. Therefore, only BDs with IDs ranging from 1 to 4094 can be bound to a profile.
3. The profile bound to a BD cannot be modified. It can only be deleted and then added.
4. After a BD is bound to a profile, the commands configured in the profile cannot be configured in the BD. If the commands in the profile have been configured in the BD, the BD cannot be bound to the profile.

Example
-------

# Create profile 10 and bind it to BD 10.
```
<HUAWEI> system-view
[~HUAWEI] bridge-domain 10
[~HUAWEI-bd10] binding bridge-domain profile 10

```
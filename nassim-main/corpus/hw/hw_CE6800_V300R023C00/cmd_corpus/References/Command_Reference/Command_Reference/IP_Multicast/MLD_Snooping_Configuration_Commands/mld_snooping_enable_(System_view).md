mld snooping enable (System view)
=================================

mld snooping enable (System view)

Function
--------



The **mld snooping enable vlan** command enables MLD snooping for VLANs.

The **undo mld snooping enable vlan** command disables MLD snooping for VLANs.

The **mld snooping enable** command enables MLD snooping.

The **undo mld snooping enable** command disables MLD snooping.



By default, MLD snooping is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mld snooping enable**

**mld snooping enable vlan** { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10>

**undo mld snooping enable**

**undo mld snooping enable vlan** { **all** | { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10> }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vlan** *vlan-id1* **to** *vlan-id2* | Specifies a VLAN or VLAN range for which MLD snooping is to be enabled. vlan-id1 and to vlan-id2 specify a VLAN range.   * vlan-id1 specifies the start VLAN ID. * to vlan-id2 specifies the end VLAN ID. If to vlan-id2 is not specified, MLD snooping is enabled only for the VLAN specified by vlan-id1. | The value is an integer ranging from 1 to 4094.  vlan-id2 must be greater than vlan-id1. |
| **all** | Disables MLD snooping for all VLANs. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

MLD snooping runs on a Layer 2 device between a Layer 3 multicast device and user hosts. MLD snooping listens on multicast protocol messages exchanged between the Layer 3 device and user hosts to maintain forwarding entries of multicast packets. MLD snooping manages and controls forwarding of multicast data packets. Enabling MLD snooping is the prerequisite for implementing Layer 2 multicast. You can run this command to enable MLD snooping globally and in a VLAN.

**Precautions**

* Running the **mld snooping enable** command in the system view enables MLD snooping globally. If you run the **undo mld snooping enable** command in the system view, MLD snooping is disabled on the entire device.
* Running this command in the VLAN view enables or disables MLD snooping in the VLAN. MLD snooping can be enabled in a VLAN only after MLD snooping is enabled globally. After MLD snooping is enabled in the system view, MLD snooping is still disabled in a VLAN by default.
* The **mld snooping enable** command and the **virtual peer-link** command are mutually exclusive.


Example
-------

# Enable MLD snooping for multiple VLANs.
```
<HUAWEI> system-view
[~HUAWEI] mld snooping enable
[*HUAWEI] vlan batch 2 to 10
[*HUAWEI] mld snooping enable vlan 2 to 10

```

# Enable MLD snooping globally.
```
<HUAWEI> system-view
[~HUAWEI] mld snooping enable

```
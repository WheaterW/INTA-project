vxlan vni auto
==============

vxlan vni auto

Function
--------



The **vxlan vni auto** command configures automatic binding between a BD and a VXLAN VNI in a BD profile.

The **undo vxlan vni auto** command disables automatic binding between a BD and a VXLAN VNI in a BD profile.



By default, a BD is not automatically bound to a VXLAN VNI in a BD profile.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**vxlan vni auto**

**undo vxlan vni auto**


Parameters
----------

None

Views
-----

bd-profile view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

A virtual network (VN) is a broadcast domain on a VXLAN network. When configuring VXLAN in simplified mode, you can run the **vxlan vni auto** command to configure a BD profile for automatically binding a VXLAN VNI. When the profile is bound to a BD, the BD is then automatically bound to the VXLAN VNI.


Example
-------

# Configure automatic binding between a BD and a VXLAN VNI in a BD profile.
```
<HUAWEI> system-view
[~HUAWEI] bridge-domain profile 1
[*HUAWEI-bd-profile1] vxlan vni auto

```
vni reserved for m-lag
======================

vni reserved for m-lag

Function
--------



The **vni reserved for m-lag** command reserves 4096 VNIs for virtual peering M-LAG.

The **undo vni reserved for m-lag** command cancels the VNI reservation for virtual peering M-LAG.



By default, no VNI is reserved for virtual peering M-LAG.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**vni** *vni-id* **reserved** **for** **m-lag**

**undo vni** *vni-id* **reserved** **for** **m-lag**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vni-id* | Specifies the start value of reserved VNIs. | The value is an integer ranging from 1 to 16773120. |



Views
-----

NVE interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

In a virtual peering M-LAG scenario, VLAN traffic between M-LAG devices needs to be forwarded through the virtual peer-link. VLANs need to be translated into VNIs and forwarded through the bypass VXLAN tunnel. In this case, you need to reserve 4096 VNIs to map VLANs to the reserved VNIs.


Example
-------

# Reserve VNIs 1â4096 for virtual peering M-LAG.
```
<HUAWEI> system-view
[~HUAWEI] interface Nve 1
[*HUAWEI-Nve1] vni 1 reserved for m-lag

```
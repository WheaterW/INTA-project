evpn ( bd-evpn-instance view )
==============================

evpn ( bd-evpn-instance view )

Function
--------



The **evpn** command creates an EVPN instance for a VXLAN.

The **undo evpn** command deletes an EVPN instance of a VXLAN.



By default, no EVPN instance is created for VXLANs.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**evpn**

**undo evpn**


Parameters
----------

None

Views
-----

BD-EVPN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The created EVPN instance can store EVPN routes sent from peer VTEPs.

**Prerequisites**

The following tasks have been performed:

* EVPN has been configured to serve as the VXLAN control plane using the **evpn-overlay enable** command.
* A VNI has been created using the **vxlan vni** command and associated with a broadcast domain (BD).

**Configuration Impact**

If you run **undo evpn** command to delete an EVPN instance, all configurations in the EVPN instance are deleted.


Example
-------

# Create an EVPN instance.
```
<HUAWEI> system-view
[~HUAWEI] evpn-overlay enable
[*HUAWEI] bridge-domain 100
[*HUAWEI-bd100] vxlan vni 200
[*HUAWEI-bd100] evpn

```
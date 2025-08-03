evpn(extend-bdprofile-evpn view)
================================

evpn(extend-bdprofile-evpn view)

Function
--------



The **evpn** command creates an EVPN profile in VXLAN mode.

The **undo evpn** command deletes an EVPN profile in VXLAN mode.



By default, no EVPN profile in VXLAN mode is created.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**evpn**

**undo evpn**


Parameters
----------

None

Views
-----

extend-bdprofile-evpn view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To simplify EVPN configuration, run the evpn vpn-profile command to create an EVPN profile, so that the profile can be bound to a BD.

**Prerequisites**

The following tasks have been performed:EVPN has been configured to serve as the VXLAN control plane using the **evpn-overlay enable** command.An auto VNI has been created and associated with a BD profile using the **vxlan vni auto** command.

**Implementation Procedure**

After an EVPN profile is deleted using the **undo evpn** command, all configurations of the EVPN instance bound to the BD profile are deleted.


Example
-------

# Create an EVPN profile.
```
<HUAWEI> system-view
[~HUAWEI] evpn-overlay enable
[*HUAWEI] bridge-domain profile 1
[*HUAWEI-bd-profile1] vxlan vni auto
[*HUAWEI-bd-profile1] evpn

```
bridge-domain profile
=====================

bridge-domain profile

Function
--------



The **bridge-domain profile** command creates a BD profile and displays the BD profile view.

The **undo bridge-domain profile** command deletes a BD profile.



By default, no BD profile is created.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**bridge-domain profile** *profileId*

**undo bridge-domain profile** *profileId*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *profileId* | Specifies the ID of a BD profile. | The value is a string of 1 to 16 characters. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When a TRILL network is replaced with a VXLAN network, the VXLAN configuration workload is heavy. You need to bind VLANs and VNIs to BDs and configure EVPN-related commands in BDs. If there are a large number of BDs, the configuration workload is heavy. To solve this problem, the BD profile function is introduced. You can configure a BD to automatically bind VLANs and VNIs and automatically generate EVPN RD and RT commands in the BD profile. You only need to bind each BD to the profile to complete the preceding configurations.

**Precautions**

A maximum of 16 BD profiles can be configured, and a BD profile can be bound to a maximum of 500 BDs.


Example
-------

# Create BD profile 2 and display the BD profile view.
```
<HUAWEI> system-view
[~HUAWEI] bridge-domain profile 2

```
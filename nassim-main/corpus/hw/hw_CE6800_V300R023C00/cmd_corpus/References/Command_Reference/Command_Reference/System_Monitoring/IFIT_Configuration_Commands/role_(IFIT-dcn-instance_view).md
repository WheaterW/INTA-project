role (IFIT-dcn-instance view)
=============================

role (IFIT-dcn-instance view)

Function
--------



The **role** command configures the NE role for IFIT.

The **undo role** command restores the default NE role for IFIT.



By default, an IFIT NE is configured as a transit node.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**role** { **ingress-egress** | **transit** }

**undo role** { **ingress-egress** | **transit** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ingress-egress** | Ingress and egress nodes deployed on the same server. | - |
| **transit** | Transit node (default role). | - |



Views
-----

IFIT dcn-instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Before configuring IFIT, you can run this command to configure an NE role. If the role is set to ingress-egress, the IFIT header is removed from the traffic on all egress ports of the device. If the role is set to transit, the IFIT header is retained on all egress ports of the device.

**Prerequisites**

IFIT has been enabled.

**Precautions**

The NE role configuration takes effect on the entire system. The priority of the NE role is lower than that of the port role.


Example
-------

# Set the NE role to ingress-egress.
```
<HUAWEI> system-view
[~HUAWEI] ifit
[*HUAWEI-ifit] dcn-instance
[*HUAWEI-ifit-dcn-instance] role ingress-egress

```
mac-route no-advertise
======================

mac-route no-advertise

Function
--------



The **mac-route no-advertise** command disables local MAC routes from being advertised.

The **undo mac-route no-advertise** command cancels the configuration.



By default, local MAC routes can be advertised.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mac-route no-advertise**

**undo mac-route no-advertise**


Parameters
----------

None

Views
-----

EVPN instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In VXLAN Layer 3 gateway scenarios where Layer 2 unicast traffic forwarding is not involved, to disable local MAC routes from being advertised, run the **mac-route no-advertise** command. This configuration prevents an EVPN peer gateway from receiving MAC routes, therefore saving memory resources.

**Precautions**

The **mac-route no-advertise** command disables MAC routes learned within BDs from being advertised based on VXLAN Network Identifiers (VNIs).


Example
-------

# Disable local MAC routes from being advertised.
```
<HUAWEI> system-view
[~HUAWEI] bridge-domain 10
[*HUAWEI-bd10] vxlan vni 20
[*HUAWEI-bd10] evpn
[*HUAWEI-bd10-evpn] mac-route no-advertise

```
mac rib-only
============

mac rib-only

Function
--------



The **mac rib-only** command disables a device from delivering a MAC entry for a remote MAC route.

The **undo mac rib-only** command restores the default configuration.



By default, a device delivers MAC entries for remote MAC routes.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mac rib-only**

**undo mac rib-only**


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

In a VXLAN Layer 3 gateway scenario, if Layer 2 unicast traffic forwarding is not involved, run the **mac rib-only** command to disable a device from delivering a MAC entry to its local MAC address table after it receives a VNI-based MAC route from the EVPN peer. This configuration saves forwarding entry resources.


Example
-------

# Disable a device from delivering a local MAC entry for a received remote MAC route.
```
<HUAWEI> system-view
[~HUAWEI] bridge-domain 10
[*HUAWEI-bd10] evpn
[*HUAWEI-bd10-evpn] mac rib-only

```
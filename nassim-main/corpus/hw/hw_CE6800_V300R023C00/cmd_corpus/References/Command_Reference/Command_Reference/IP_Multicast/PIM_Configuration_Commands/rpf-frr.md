rpf-frr
=======

rpf-frr

Function
--------



The **rpf-frr** command enables PIM FRR.

The **undo rpf-frr** command disables PIM FRR.



By default, PIM FRR is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**rpf-frr**

**rpf-frr policy** { **acl-name** *acl-name* | *acl-number* }

**undo rpf-frr**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **policy** | Configure a policy which uses ACL rules to specify the routing table entries that the FRR function takes effect on. | - |
| **acl-name** *acl-name* | Specifies an ACL by its name. | The value is a string of 1 to 64 case-sensitive characters without spaces. The value must start with a letter (a to z or A to Z, case sensitive). |
| *acl-number* | Specifies an ACL by its number. | The value is an integer ranging from 2000 to 3999. |



Views
-----

VPN instance PIM view,PIM view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If a multicast link fails, services are interrupted before unicast routes are converged. Route convergence generally takes a long time, which is unacceptable by multicast services that have high requirements on real-time data transmission. To resolve this problem, configure PIM FRR. After PIM FRR is configured, PIM sets up primary and backup MDTs based on unicast backup FRR routes, allowing multicast traffic transmission through both the primary and backup links. The device's forwarding plane permits the multicast traffic on the primary link and discards that on the backup link. However, the forwarding plane permits the multicast traffic on the backup link immediately after the primary link fails, thus minimizing traffic loss.You can specify an ACL to enable PIM FRR for the specified entry.

**Precautions**

This command is mutually exclusive with the multicast load-splitting { balance-ucmp | stable-preferred } command. If FRR is enabled, load balancing cannot be configured, and vice versa.rpf-frr and pim dm are mutually exclusive.If a device has a board that does not support PIM FRR, the **rpf-frr** command cannot be run in the PIM view.After PIM FRR is enabled on a device, if a board that does not support PIM FRR is installed on the device, the board cannot register.If this command is run multiple times, the latest configuration overrides the previous one.This command is under license control. When the license is invalid or does not exist:

1. An error is reported during configuration delivery.
2. The configuration is lost when the device is restarted using the configuration file.

Example
-------

# Enable PIM FRR for a specified multicast routing entry in the public network instance.
```
<HUAWEI> system-view
[~HUAWEI] acl name frracl
[*HUAWEI-acl4-advance-frracl] rule permit ip source 10.0.0.1 0 destination 226.0.0.1 0
[*HUAWEI-acl4-advance-frracl] commit
[~HUAWEI-acl4-advance-frracl] quit
[~HUAWEI] multicast routing-enable
[~HUAWEI] pim
[*HUAWEI-pim] rpf-frr policy acl-name frracl

```

# Enable PIM FRR for the public network instance.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] pim
[*HUAWEI-pim] rpf-frr

```
register-suppression-timeout (IPv6)
===================================

register-suppression-timeout (IPv6)

Function
--------



The **register-suppression-timeout** command sets a timeout period during which the device remains in the Register suppression state.

The **undo register-suppression-timeout** command restores the default value.



By default, the timeout period during which the device remains in the Register suppression state is 60 seconds.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**register-suppression-timeout** *interval*

**undo register-suppression-timeout**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies a timeout period during which the device remains in the Register suppression state. | The value is an integer ranging from 11 to 3600, in seconds. |
| **register-suppression-timeout** | Specifies a timeout period during which the device remains in the Register suppression state. | - |



Views
-----

IPv6 PIM view,VPN instance IPv6 PIM view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

After receiving a Register-Stop message from the rendezvous point (RP), a device immediately stops sending Register messages and enters the register suppression state. To set a timeout period during which the device remains in the register suppression state, run the register-suppression-timeout command.If the configured timeout period is too short, the RP frequently receives burst multicast data. If the configured timeout period is too long, the delay for a new receiver to join a multicast group is long when an (S, G) entry times out on the RP.


Example
-------

# In the public network instance, specify 70 seconds as the timeout period during which the device remains in the Register suppression state.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] pim ipv6
[*HUAWEI-pim6] register-suppression-timeout 70

```
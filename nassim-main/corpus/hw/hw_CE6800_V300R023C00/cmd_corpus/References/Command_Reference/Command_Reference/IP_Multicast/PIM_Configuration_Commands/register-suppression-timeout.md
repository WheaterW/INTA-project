register-suppression-timeout
============================

register-suppression-timeout

Function
--------



The **register-suppression-timeout** command sets a timeout period during which the device remains in the Register suppression state.

The **undo register-suppression-timeout** command restores the default value.



By default, the timeout period during which the device remains in the Register suppression state is 60 seconds.


Format
------

**register-suppression-timeout** *interval*

**undo register-suppression-timeout**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies a timeout period during which the device remains in the Register suppression state. | The value is an integer that ranges from 11 to 3600, in seconds. |



Views
-----

VPN instance PIM view,PIM view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After receiving a Register-Stop message from the rendezvous point (RP), a device immediately stops sending Register messages and enters the register suppression state. To set a timeout period during which the device remains in the register suppression state, run the register-suppression-timeout command.If the configured timeout period is too short, the RP frequently receives burst multicast data. If the configured timeout period is too long, the delay for a new receiver to join a multicast group is long when an (S, G) entry times out on the RP.

**Prerequisites**

The multicast routing function has been enabled using the **multicast routing-enable** command in the public network instance view or VPN instance view.

**Configuration Impact**

If the register-suppression-timeout command is run more than once, the latest configuration overrides the previous one.


Example
-------

# In the public network instance, specify 70 seconds as the timeout period during which the device remains in the Register suppression state.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] pim
[*HUAWEI-pim] register-suppression-timeout 70

```
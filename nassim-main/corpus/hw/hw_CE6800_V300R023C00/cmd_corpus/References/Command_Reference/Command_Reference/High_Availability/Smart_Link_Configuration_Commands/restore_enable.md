restore enable
==============

restore enable

Function
--------



The **restore enable** command enables the switchback function for a Smart Link group.

The **undo restore enable** command disables the function.



By default, the switchback function is disabled for a Smart Link group.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE8855, CE8851-32CQ4BQ, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**restore enable**

**undo restore enable**


Parameters
----------

None

Views
-----

Smart Link group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If the primary link in a Smart Link group fails, traffic automatically switches to the secondary link. The primary link remains blocked after it recovers to ensure uninterrupted traffic forwarding. To switch traffic back to the primary link, run the restore enable command to enable the switchback function for the Smart Link group. Traffic automatically switches back to the primary link after the switchback delay expires.

**Prerequisites**

A Smart Link group has been created using the **smart-link group** command.Both member interfaces in the group are Up.

**Follow-up Procedure**

Run the **timer wtr** command to set the switchback delay. By default, the switchback delay is 60s.

**Precautions**

The master and slave interfaces must both be Up in the Smart Link group.The switchback function cannot be disabled during the traffic switchback; otherwise, the traffic switchback fails.


Example
-------

# Enable the switchback function for Smart Link group 1.
```
<HUAWEI> system-view
[~HUAWEI] smart-link group 1
[*HUAWEI-smlk-group1] restore enable

```
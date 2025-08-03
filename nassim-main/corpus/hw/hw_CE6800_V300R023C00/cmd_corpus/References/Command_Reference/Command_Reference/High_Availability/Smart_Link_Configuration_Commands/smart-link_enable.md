smart-link enable
=================

smart-link enable

Function
--------



The **smart-link enable** command enables a Smart Link group.

The **undo smart-link enable** command disables a Smart Link group.



By default, a Smart Link group is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE8855, CE8851-32CQ4BQ, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**smart-link enable**

**undo smart-link enable**


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

To enable a Smart Link group, run the smart-link enable command. Smart Link takes effect only after a Smart Link group is enabled. When a Smart Link group is enabled, the slave interface in the group is blocked. If a Smart Link group is disabled, the slave interface in the group is unblocked.After creating a Smart Link group and adding interfaces to the group, you need to enable the Smart Link group for it to take effect.

**Prerequisites**

A Smart Link group has been created using the smart-link group command, and the master and slave interfaces have been configured in the Smart Link group using the **port** command.

**Precautions**

The slave interface in a Smart Link group is blocked only when the master and slave interfaces are both Up and the Smart Link group is enabled.


Example
-------

# Enable Smart Link group 1.
```
<HUAWEI> system-view
[~HUAWEI] smart-link group 1
[*HUAWEI-smlk-group1] smart-link enable

```
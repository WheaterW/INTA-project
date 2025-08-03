lacp force-down
===============

lacp force-down

Function
--------



The **lacp force-down** command enables the function of forcibly setting Eth-Trunk interfaces that are added to an M-LAG to down.

The **undo lacp force-down** command disables this function.



By default, the function of forcibly setting Eth-Trunk interfaces that are added to an M-LAG to down is disabled.


Format
------

**lacp force-down**

**undo lacp force-down**


Parameters
----------

None

Views
-----

maintenance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In an M-LAG dual-homing access scenario where a maintenance mode upgrade is performed, you can run the **lacp force-down** command on the local device, so that the member interfaces of the local static/dynamic Eth-Trunk interfaces that are added to an M-LAG immediately send LACP Dying Gasp packets to the peer device. After receiving the packets, the peer device sets the member interfaces of Eth-Trunk interfaces to down, directing the server to switch upstream traffic to the standby link. After the upgrade is complete, you can run the **undo lacp force-down** command to switch the upstream traffic back to the original link.

**Precautions**

This command is used only in an M-LAG dual-homing access scenario where a maintenance mode upgrade is performed. After the **lacp force-down** command is run, the static/dynamic Eth-Trunk interfaces added to an M-LAG go down, which may affect traffic forwarding.


Example
-------

# Enable the function of forcibly setting Eth-Trunk interfaces that are added to an M-LAG to down.
```
<HUAWEI> system-view
[~HUAWEI] maintenance
[~HUAWEI-maintenance] lacp force-down

```
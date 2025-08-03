smart-link
==========

smart-link

Function
--------



The **smart-link** command enables a Smart Link group to lock traffic on a specified interface.

The **undo smart-link** command disables the function.



By default, traffic is not locked in the Smart Link group.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE8855, CE8851-32CQ4BQ, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**smart-link** { **lock** | **force** }

**undo smart-link** { **lock** | **force** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **lock** | Locks traffic on the master interface. | - |
| **force** | Locks traffic on the slave interface. | - |



Views
-----

Smart Link group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To lock traffic on the master or slave interface in a Smart Link group, run the smart-link command. The command allows the traffic to be transmitted only along the primary or secondary link. For example, if you want to have the primary link in a Smart Link group inspected during maintenance, run the smart-link force command to lock traffic on the slave interface of the secondary link before the inspection to prevent a service interruption, and run the undo smart-link force command after the inspection. Then, traffic automatically switches back to the primary link if the switchback function is enabled.

**Prerequisites**

The Smart Link group has been enabled using the **smart-link enable** command.

**Precautions**

* If traffic is locked on one of the interfaces in a Smart Link group, the link on which the interface resides is considered active, and traffic cannot be automatically switched to the other link even if the link fails.
* Lock and force are mutually exclusive, and only one of them can be configured. lock has a higher priority than force. If you configure force and then lock, lock takes effect (traffic is locked on the master interface.) If you configure lock first, force cannot be configured.
* Traffic locking by a Smart Link group may cause a data flow to be interrupted intermittently.

Example
-------

# Enable Smart Link group 1 to lock traffic on the slave interface.
```
<HUAWEI> system-view
[~HUAWEI] smart-link group 1
[*HUAWEI-smlk-group1] smart-link force

```
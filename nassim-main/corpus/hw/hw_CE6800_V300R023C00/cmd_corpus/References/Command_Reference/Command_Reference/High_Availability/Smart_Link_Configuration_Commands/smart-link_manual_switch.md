smart-link manual switch
========================

smart-link manual switch

Function
--------



The **smart-link manual switch** command performs a manual primary/secondary link switchover in Smart Link group.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE8855, CE8851-32CQ4BQ, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**smart-link manual switch**


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

When the active link in a Smart Link group fails, traffic is automatically switched to the standby link. After the original active link recovers, it remains in the blocked state and does not preempt the active link to ensure stable traffic transmission. Generally, a more stable link needs to be used as the active link. Therefore, after the original active link recovers, you can use either of the following methods to restore the original active link:Run the **restore enable** command to enable the revertive switching function of the Smart Link group. After the revertive switching timer expires, the Smart Link group automatically switches to the active link. You can run the **timer wtr** command to set the WTR time of a Smart Link group.Run the **smart-link manual switch** command to complete the switchover between the active and standby links in the Smart Link group immediately.

**Prerequisites**

The following conditions must be met for a successful traffic switchover:

* The master and slave interfaces must both be Up in the Smart Link group.
* Traffic is not locked by using the smart-link { force | lock } command.
* The Smart Link group has been enabled using the smart-link enable command.

**Precautions**

When traffic is switched between the primary and secondary links, packets are lost within milliseconds.


Example
-------

# Perform a primary/secondary link switchover in Smart Link group 1 manually.
```
<HUAWEI> system-view
[~HUAWEI] smart-link group 1
[*HUAWEI-smlk-group1] smart-link manual switch

```
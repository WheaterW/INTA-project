monitor-link disable
====================

monitor-link disable

Function
--------



The **monitor-link disable** command disables association between uplink and downlink interfaces in a Monitor Link group.

The **undo monitor-link disable** command restores the association between uplink and downlink interfaces in a Monitor Link group.



By default, association is enabled between uplink and downlink interfaces in a Monitor Link group.


Format
------

**monitor-link disable**

**undo monitor-link disable**


Parameters
----------

None

Views
-----

Monitor link group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



In normal situations, Monitor Link monitors the uplink interface in a Monitor Link group and sets the downlink interface status according to uplink interface status. Monitor Link triggers a Layer 2 protocol on downstream devices to perform a link switchover when the downlink interface status changes. In some situations, for example, an optical module needs to be replaced, you may want to change the uplink status temporarily without affecting the downlink status. To meet this requirement, you have to cancel the configurations of downlink interfaces one by one. You may have the trouble in recovering the configurations in future if needed. To save the trouble, run the monitor-link disable command. After this command is configured, Monitor Link does not change the downlink status based on the uplink status. In addition, the command configuration does not affect the uplink or downlink interface configurations.




Example
-------

# Disable association between uplink and downlink interfaces in a Monitor Link group.
```
<HUAWEI> system-view
[~HUAWEI] monitor-link group 2
[*HUAWEI-mtlk-group2] monitor-link disable

```
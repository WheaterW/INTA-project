lacp lag-mib admin-key change-to-lagid (System view)
====================================================

lacp lag-mib admin-key change-to-lagid (System view)

Function
--------



The **lacp lag-mib admin-key change-to-lagid** command sets the values of the dot3adAggActorAdminKey and dot3adAggPortActorAdminKey objects in the LAG-MIB each to be the same as an Eth-Trunk ID.

The **undo lacp lag-mib admin-key change-to-lagid** command restores the default configuration.



By default, the values of the dot3adAggActorAdminKey and dot3adAggPortActorAdminKey objects in the LAG-MIB are each the same as an Eth-Trunk ID plus 1.


Format
------

**lacp lag-mib admin-key change-to-lagid**

**undo lacp lag-mib admin-key change-to-lagid**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



By default, the values of the dot3adAggActorAdminKey object in dot3adAggTable and the 3adAggPortActorAdminKey object in dot3adAggPortTable in the LAG-MIB are each the same as an Eth-Trunk ID plus 1. When an Eth-Trunk ID is 65535, the values of the two objects are each 65536, exceeding the permitted value range. To resolve this issue, run the lacp lag-mib admin-key change-to-lagid command to set the values of the two objects each to be the same as an Eth-Trunk ID.




Example
-------

# Set the values of the dot3adAggActorAdminKey and dot3adAggPortActorAdminKey objects in the LAG-MIB each to be the same as an Eth-Trunk ID.
```
<HUAWEI> system-view
[~HUAWEI] lacp lag-mib admin-key change-to-lagid

```
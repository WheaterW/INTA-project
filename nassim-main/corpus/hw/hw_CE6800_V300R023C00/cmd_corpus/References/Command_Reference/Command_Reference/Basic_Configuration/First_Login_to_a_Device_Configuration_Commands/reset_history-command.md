reset history-command
=====================

reset history-command

Function
--------



The **reset history-command** command deletes the historical commands of the current user.

The reset history-command all-users command deletes the historical commands of all users in the system.




Format
------

**reset history-command**


Parameters
----------

None

Views
-----

User view


Default Level
-------------

0: Visit level


Usage Guidelines
----------------

**Usage Scenario**

To delete the historical commands of the current user, run the **reset history-command** command.The reset history-command all-users command clears the query result of the display history-command all-users command, without affecting the query result of the **display history-command** command.


Example
-------

# Delete the historical commands of the current user.
```
<HUAWEI> reset history-command

```
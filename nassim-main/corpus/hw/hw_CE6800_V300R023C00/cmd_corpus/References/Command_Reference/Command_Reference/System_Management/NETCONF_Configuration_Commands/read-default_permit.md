read-default permit
===================

read-default permit

Function
--------



The **read-default permit** command enables users to perform query operations.

The **undo read-default permit** command disables users from performing query operations.



By default, the NACM function is disabled.


Format
------

**read-default permit**

**undo read-default permit**


Parameters
----------

None

Views
-----

NACM view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To enable users to perform query operations, run the **read-default permit** command.Supported query operations include get and get-config.


Example
-------

# Enable users to perform query operations.
```
<HUAWEI> system-view
[~HUAWEI] netconf
[~HUAWEI-netconf] nacm
[~HUAWEI-netconf-nacm] read-default permit

```
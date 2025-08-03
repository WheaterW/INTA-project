write-default permit
====================

write-default permit

Function
--------



The **write-default permit** command enables users to perform configuration operations.

The **undo write-default permit** command disables users from performing configuration operations.



By default, users' permission to perform configuration operations is disabled.


Format
------

**write-default permit**

**undo write-default permit**


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

To enable users to perform configuration operations, run the **write-default permit** command.Currently, the supported configuration operation is edit-config.


Example
-------

# Enable users to perform configuration operations.
```
<HUAWEI> system-view
[~HUAWEI] netconf
[~HUAWEI-netconf] nacm
[~HUAWEI-netconf-nacm] write-default permit

```
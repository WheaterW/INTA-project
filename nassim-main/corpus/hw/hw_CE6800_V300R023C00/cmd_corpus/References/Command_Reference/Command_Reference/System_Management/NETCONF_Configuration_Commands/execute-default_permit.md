execute-default permit
======================

execute-default permit

Function
--------



The **execute-default permit** command enables users to have the default execution permission for RPC operations.

The **undo execute-default permit** command disables users from having the default execution permission for RPC operations.



By default, users have the default execution permission for RPC operations.


Format
------

**execute-default permit**

**undo execute-default permit**


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

To enable users to have the default execution permission for RPC operations, run the execute-default permit command.The YANG file-defined RPC operations include get, get-config, edit-config, copy-config, delete-config, lock, unlock, commit, close-session, and kill-session.


Example
-------

# Enable users to have the default execution permission for RPC operations.
```
<HUAWEI> system-view
[~HUAWEI] netconf
[~HUAWEI-netconf] nacm
[~HUAWEI-netconf-nacm] execute-default permit

```
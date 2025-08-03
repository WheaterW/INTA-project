rpc-message log protocol-operation get
======================================

rpc-message log protocol-operation get

Function
--------



The **rpc-message log protocol-operation get** command enables NETCONF operation log query.

The **undo rpc-message log protocol-operation get** command disables NETCONF operation log query.



By default, NETCONF operation log query is disabled.


Format
------

**rpc-message log protocol-operation get**

**undo rpc-message log protocol-operation get**


Parameters
----------

None

Views
-----

NETCONF user interface view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To query NETCONF operation logs, run the **rpc-message log protocol-operation get** command to enable NETCONF operation log query. The operation logs for this command is in log.log format.

**Prerequisites**

To enable the NETCONF component, you need to execute the **snetconf server enable** or **protocol inbound ssh port 830** command.


Example
-------

# Enable NETCONF operation log query.
```
<HUAWEI> system-view
[~HUAWEI] snetconf server enable
[*HUAWEI] netconf
[*HUAWEI-netconf] rpc-message log protocol-operation get

```
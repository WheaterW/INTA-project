uplink-port enable
==================

uplink-port enable

Function
--------



The **uplink-port enable** command configures an interface as an uplink interface.

The **undo uplink-port enable** command cancels the uplink interface configuration.



By default, an interface is not an uplink interface.


Format
------

**uplink-port enable**

**undo uplink-port enable**


Parameters
----------

None

Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

This command configures an interface as an uplink interface.

**Precautions**

An interface cannot be configured as an uplink interface and a peer-link interface at the same time.An interface cannot be configured as an uplink interface and an Eth-Trunk member interface at the same time.An interface cannot be configured as an uplink interface and an M-LAG member interface at the same time.The uplink-port enable and **dfs-group port-group** commands are mutually exclusive on an interface.


Example
-------

# Configure 100GE1/0/1 as an uplink interface.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] uplink-port enable

```
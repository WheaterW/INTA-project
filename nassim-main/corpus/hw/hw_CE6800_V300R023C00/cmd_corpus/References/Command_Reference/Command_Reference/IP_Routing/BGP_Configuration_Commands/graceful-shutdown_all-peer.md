graceful-shutdown all-peer
==========================

graceful-shutdown all-peer

Function
--------



The **graceful-shutdown all-peer** command enables the g-shut feature globally.

The **undo graceful-shutdown all-peer** command restores the default configuration.



By default, the g-shut feature is not enabled globally.


Format
------

**graceful-shutdown all-peer**

**undo graceful-shutdown all-peer**


Parameters
----------

None

Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To enable the g-shut feature for all peers, run this command.




Example
-------

# Enable the g-shut feature globally.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] graceful-shutdown all-peer

```
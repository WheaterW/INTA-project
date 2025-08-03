graceful-shutdown manual-activate
=================================

graceful-shutdown manual-activate

Function
--------



The **graceful-shutdown manual-activate** command activates the g-shut feature globally.

The **undo graceful-shutdown manual-activate** command restores the default configuration.



By default, the g-shut feature is not activated globally.


Format
------

**graceful-shutdown manual-activate**

**undo graceful-shutdown manual-activate**


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



To activate the g-shut feature for all peers, run this command.




Example
-------

# Activate the g-shut feature globally.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] graceful-shutdown manual-activate

```
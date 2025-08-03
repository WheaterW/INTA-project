load-balance enhanced resilient
===============================

load-balance enhanced resilient

Function
--------



The **load-balance enhanced resilient** command configures resilient hashing on an Eth-Trunk interface.

The **undo load-balance enhanced resilient** command restores the default resilient hashing configuration on an Eth-Trunk interface.



By default, resilient hashing is disabled on an Eth-Trunk interface.


Format
------

**load-balance enhanced resilient**

**undo load-balance enhanced resilient**


Parameters
----------

None

Views
-----

Eth-Trunk interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

Resilient hashing reduces the chances of traffic switching to other links when member links are added to or deleted from an Eth-Trunk. For example, an Eth-Trunk consists of three member links and forwards traffic based on the hash key value. If one link fails, all traffic is reallocated and load balanced over the other two links if resilient hashing is not configured. If resilient hashing is configured, the traffic that has been allocated to the other two links is still transmitted over them, and the traffic on the faulty link is evenly distributed to these links, minimizing the impact on services. After the faulty link recovers, some traffic is switched from the other two links to the recovered link, but the traffic volume on each is not the same as that before the link fault.


Example
-------

# Configure resilient hashing on Eth-Trunk 1.
```
<HUAWEI> system-view
[~HUAWEI] interface Eth-Trunk 1
[*HUAWEI-Eth-Trunk1] load-balance enhanced resilient

```
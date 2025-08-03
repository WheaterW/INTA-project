load-balance ecmp stateful enhanced enable
==========================================

load-balance ecmp stateful enhanced enable

Function
--------



The **load-balance ecmp stateful enhanced enable** command enables the ECMP load balancing consistency enhancement function.

The **undo load-balance ecmp stateful enhanced enable** command disables the ECMP load balancing consistency enhancement function.



By default, ECMP load balancing consistency enhancement is disabled.


Format
------

**load-balance ecmp stateful enhanced enable**

**undo load-balance ecmp stateful enhanced enable**


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

When an ECMP member link fails, the ECMP load balancing consistency function ensures that the forwarding path of a normal link remains unchanged. However, if a faulty member link recovers or a new link is added, traffic is forwarded along another path. The ECMP load balancing consistency function cannot ensure that the original forwarding path remains unchanged. After ECMP load balancing consistency enhancement is enabled using the **load-balance ecmp stateful enhanced enable** command, if a faulty link is removed, only traffic on the faulty link is hashed again. If a new link is added, not all traffic is hashed again.

**Prerequisites**

Before running the **load-balance ecmp stateful enhanced enable** command to enable the ECMP load balancing consistency enhancement function, run the **load-balance ecmp stateful enable** command in the system view to enable the ECMP load balancing consistency function.

**Precautions**

* Before applying ECMP consistency enhancement, ensure that routes are symmetrically deployed. Specifically, multiple equal-cost paths to different destination addresses are either all the same or all different.
* After ECMP consistency enhancement is enabled, you cannot change the configured load balancing hash algorithm, hash algorithm offset, or load balancing mode. Otherwise, this function may not take effect.
* When the outbound interfaces of equal-cost links are intermittently disconnected, the ECMP load balancing consistency enhancement function may not take effect.
* ECMP consistency enhancement may not take effect if outbound interfaces of equal-cost links are intermittently disconnected.
* If ECMP members include IP tunnels, VXLAN tunnels, and VBDIF interfaces (next hops), the hash consistency function is not supported.
* After ECMP consistency enhancement is configured, traffic will not be evenly hashed if the number of paths to the next hop is not a power of 2.

Example
-------

# Enable load balancing consistency enhancement.
```
<HUAWEI> system-view
[~HUAWEI] load-balance ecmp stateful enable
[*HUAWEI] load-balance ecmp stateful enhanced enable

```
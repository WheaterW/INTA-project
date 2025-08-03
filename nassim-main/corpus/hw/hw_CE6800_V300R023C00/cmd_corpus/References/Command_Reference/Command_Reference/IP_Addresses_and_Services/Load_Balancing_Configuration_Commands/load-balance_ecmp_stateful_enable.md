load-balance ecmp stateful enable
=================================

load-balance ecmp stateful enable

Function
--------



The **load-balance ecmp stateful enable** command enables the ECMP load balancing consistency function.

The **undo load-balance ecmp stateful enable** command disables the ECMP load balancing consistency function.



By default, the ECMP load balancing consistency function is disabled.


Format
------

**load-balance ecmp stateful enable**

**undo load-balance ecmp stateful enable**


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

When a switch that participates in traffic load balancing becomes faulty, the number of equal-cost routes reduces, and so all traffic needs to be load balanced again using the hash algorithm. As a result, traffic forwarding paths may change. Requests of the same user may be sent to different servers, greatly affecting the services in which sessions need to be maintained. To prevent this problem, run the **load-balance ecmp stateful enable** command. This command enables the ECMP load balancing consistency function so that hash calculation is performed only for traffic on the faulty link, without affecting traffic on other normal links.

**Prerequisites**

* When using the ECMP load balancing consistency function, ensure that routes are symmetrically deployed. Multiple equal-cost paths to different destination addresses are either all the same or all different.
* If the hash consistency enhancement command has been run, run the **undo load-balance ecmp stateful enhanced enable** command in the system view to disable hash consistency enhancement before canceling load-balance ecmp stateful enable.

**Configuration Impact**

After enabling the ECMP load balancing consistency function, do not change the configured load balancing hash algorithm, hash algorithm offset, or load balancing mode. Otherwise, this function may be unable to take effect.This function may be unable to take effect when outbound interfaces of equal-cost links are intermittently disconnected.The ECMP load balancing consistency function takes effect only for common IP traffic, but not for traffic transmitted over tunnels.After the ECMP load balancing consistency function is enabled, if the number of next-hop paths is not a power of 2, traffic cannot be evenly load balanced.

**Precautions**

* This command and the **load-balancing ucmp** command are mutually exclusive.
* On the CE6863H, CE6863H-K, CE6881H, and CE6881H-K models, this command and the **local-preference enhanced** command are mutually exclusive.
* On the CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, and CE8851K, this command and the **load-balancing adaptive-routing** command are mutually exclusive.
* On the CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, and CE8851K, this command and the **adaptive-routing enable** command are mutually exclusive.


Example
-------

# Enable the ECMP load balancing consistency function.
```
<HUAWEI> system-view
[~HUAWEI] load-balance ecmp stateful enable

```
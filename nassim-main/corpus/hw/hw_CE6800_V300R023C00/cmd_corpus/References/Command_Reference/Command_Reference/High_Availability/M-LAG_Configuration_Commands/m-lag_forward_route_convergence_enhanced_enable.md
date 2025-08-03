m-lag forward route convergence enhanced enable
===============================================

m-lag forward route convergence enhanced enable

Function
--------



The **m-lag forward route convergence enhanced enable** command enables enhanced M-LAG route convergence in IPv4 and IPv6 scenarios.

The **undo m-lag forward route convergence enhanced enable** command disables enhanced M-LAG route convergence in IPv4 and IPv6 scenarios.



By default, enhanced M-LAG route convergence is disabled in IPv4 and IPv6 scenarios.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**m-lag forward route convergence enhanced enable**

**undo m-lag forward route convergence enhanced enable**


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

After enhanced M-LAG route convergence is enabled in an IPv4 or IPv6 scenario, backup FRR resources are requested for all routing entries with M-LAG member interfaces as outbound interfaces. The outbound interfaces can be changed to peer-link interfaces, and active and standby paths are established and delivered. If the system detects that an M-LAG member interface fails, dual-homing networking is changed to single-homing networking. The next hop in the corresponding routing entry is changed from the M-LAG member interface to the peer-link interface. This improves the switchover performance when faults occur.

**Precautions**

* Before enabling enhanced M-LAG route convergence, run the m-lag forward layer-3 enhanced enable command to enable enhanced M-LAG Layer 3 functions. Before disabling enhanced M-LAG Layer 3 functions, run the undo m-lag forward route convergence enhanced enable command to disable enhanced M-LAG route convergence.
* After enhanced M-LAG route convergence is enabled, the active and standby paths may fail to be delivered due to increased next-hop resource consumption. As a result, packet loss occurs.
* The enhanced M-LAG route convergence function takes effect only for routes with a single next hop and an M-LAG outbound interface.
* After enhanced M-LAG route convergence is enabled, you can disable this function only after 300s. After enhanced M-LAG route convergence is disabled, you can enable this function only after 300s.
* After enhanced M-LAG route convergence is enabled, the MAC addresses of VLANIF interfaces and VBDIF interfaces on the two M-LAG member devices must be the same.
* In an M-LAG scenario where devices in the M-LAG are upgraded and replaced with devices of different models, if enhanced M-LAG route convergence has been enabled before the upgrade, disable enhanced M-LAG route convergence and enhanced M-LAG Layer 3 functions, and then perform the upgrade and replacement operations.
* For routes with a single next hop and M-LAG outbound interfaces in active/standby mode, FRR is delivered by default and is not controlled by the enhanced M-LAG route convergence command.

Example
-------

# The command disables enhanced M-LAG route convergence
```
<HUAWEI> system-view
[~HUAWEI] undo m-lag forward route convergence enhanced enable

```

# The command enables enhanced M-LAG route convergence
```
<HUAWEI> system-view
[~HUAWEI] m-lag for layer-3 enhanced enable
[*HUAWEI] m-lag forward route convergence enhanced enable

```
m-lag forward layer-2 overlay enhanced enable
=============================================

m-lag forward layer-2 overlay enhanced enable

Function
--------



The **m-lag forward layer-2 overlay enhanced enable** command enables enhanced M-LAG Layer 2 forwarding in an overlay scenario.

The **undo m-lag forward layer-2 overlay enhanced enable** command disables enhanced M-LAG Layer 2 forwarding in an overlay scenario.



By default, enhanced M-LAG Layer 2 forwarding is disabled in an overlay scenario.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H and CE6881H-K.



Format
------

**m-lag forward layer-2 overlay enhanced enable**

**undo m-lag forward layer-2 overlay enhanced enable**


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

To speed up convergence when an M-LAG member interface fails in an overlay scenario, you can enable enhanced M-LAG Layer 2 forwarding. Backup FRR resources are requested for all MAC address entries whose outbound interfaces are M-LAG member interfaces. The outbound interfaces can be changed to peer-link interfaces to establish active and standby paths for traffic forwarding. Once an M-LAG member interface fault is detected, traffic is quickly switched to a peer-link interface, improving the switching performance in fault scenarios.

**Precautions**



This function is supported only in overlay scenarios.




Example
-------

# Enable enhanced M-LAG Layer 2 forwarding.
```
<HUAWEI> system-view
[~HUAWEI] m-lag forward layer-2 overlay enhanced enable

```
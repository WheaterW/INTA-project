m-lag forward layer-3 enhanced
==============================

m-lag forward layer-3 enhanced

Function
--------



For the CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, and CE6881H-K:

The **m-lag forward layer-3 enhanced enable** command enables enhanced M-LAG Layer 3 forwarding.

The **undo m-lag forward layer-3 enhanced enable** command disables enhanced M-LAG Layer 3 forwarding.

For the CE6866, CE6860-SAN, CE6860-HAM, CE6866K, CE8851-32CQ8DQ-P, CE8850-SAN, CE8850-HAM, CE8851K, CE8865, CE8865-SAN, CE8875, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, and CE6885-LL (low latency mode):

The **m-lag forward layer-3 enhanced disable** command disables enhanced M-LAG Layer 3 forwarding.

The **undo m-lag forward layer-3 enhanced disable** command enables enhanced M-LAG Layer 3 forwarding.



For the CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, and CE6881H-K:

By default, enhanced M-LAG Layer 3 forwarding is disabled.

For the CE6866, CE6860-SAN, CE6860-HAM, CE6866K, CE8851-32CQ8DQ-P, CE8850-SAN, CE8865, CE8865-SAN, CE8875, CE8850-HAM, CE8851K, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, and CE6885-LL (low latency mode):

By default, enhanced M-LAG Layer 3 forwarding is enabled.




Format
------

For CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K:

**m-lag forward layer-3 enhanced enable**

**undo m-lag forward layer-3 enhanced enable**

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**m-lag forward layer-3 enhanced disable**

**undo m-lag forward layer-3 enhanced disable**


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

After enhanced M-LAG Layer 3 forwarding is enabled, backup FRR resources are requested for all ARP/ND entries with M-LAG member interfaces as outbound interfaces. The outbound interfaces can be changed to peer-link interfaces to establish active and standby paths for traffic forwarding. If the system detects that an M-LAG member interface fails, dual-homing networking is changed to single-homing networking. The next hop in the corresponding ARP/ND entry is changed from the M-LAG member interface to the peer-link interface. This improves the switchover performance when faults occur.

**Precautions**

For the CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, and CE6881H-K:

* When devices in an M-LAG are upgraded and replaced with devices of different models, if the enhanced Layer 3 forwarding function has been enabled before the upgrade, run the corresponding command for disabling this function, and then perform the upgrade and replacement operations.
* Before enabling enhanced M-LAG route convergence, run the **m-lag forward layer-3 enhanced enable** command to enable enhanced M-LAG Layer 3 forwarding. Before disabling enhanced M-LAG Layer 3 forwarding, run the **undo m-lag forward route convergence enhanced enable** command to disable enhanced M-LAG route convergence.
* After enhanced M-LAG Layer 3 forwarding is enabled, the active and standby paths may fail to be delivered due to increased next-hop resource consumption. As a result, packet loss occurs.
* After enhanced M-LAG Layer 3 forwarding is enabled, you need to configure an interface to clear all the learned ARP and ND entries when it is added to or removed from an Eth-Trunk interface that functions as an M-LAG member interface. This prevents FRR resources from being wasted because the upper-layer protocol module does not detect M-LAG member interface changes.
* After enhanced M-LAG Layer 3 forwarding is enabled, you can disable this function only after 300s. After enhanced M-LAG Layer 3 forwarding is disabled, you can enable this function only after 300s.
* In a VXLAN scenario, to use enhanced M-LAG Layer 3 forwarding in an IPv4 scenario, you also need to configure the **arp broadcast-detect enable** command.
* After enhanced Layer 3 forwarding is enabled, the MAC addresses of VLANIF interfaces and VBDIF interfaces on the two member devices in an M-LAG must be the same.
* When enabling enhanced M-LAG Layer 3 forwarding, enable the function on the two member devices in an M-LAG.
* When the outbound interfaces of ARP/ND entries are M-LAG interfaces in active/standby mode, FRR is delivered by default and is not controlled by the enhanced M-LAG Layer 3 forwarding command.

For the CE6866, CE6860-SAN, CE6860-HAM, CE6866K, CE8851-32CQ8DQ-P, CE8850-SAN, CE8850-HAM, CE8851K, CE8865, CE8865-SAN, CE8875, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, and CE6885-LL (low latency mode):

* After enhanced M-LAG Layer 3 forwarding is enabled, the active and standby paths may fail to be delivered due to increased next-hop resource consumption. As a result, packet loss occurs.
* After enhanced M-LAG Layer 3 forwarding is enabled, you need to configure an interface to clear all the learned ARP and ND entries when it is added to or removed from an Eth-Trunk interface that functions as an M-LAG member interface. This prevents FRR resources from being wasted because the upper-layer protocol module does not detect M-LAG member interface changes.
* After enhanced M-LAG Layer 3 forwarding is enabled, you can disable this function only after 300s. After enhanced M-LAG Layer 3 forwarding is disabled, you can enable this function only after 300s.
* In a VXLAN scenario, to use enhanced M-LAG Layer 3 forwarding in an IPv4 scenario, you also need to configure the **arp broadcast-detect enable** command.
* After enhanced Layer 3 forwarding is enabled, the MAC addresses of VLANIF interfaces and VBDIF interfaces on the two member devices in an M-LAG must be the same.
* When enabling enhanced M-LAG Layer 3 forwarding, enable the function on the two member devices in an M-LAG.
* When the outbound interfaces of ARP/ND entries are M-LAG interfaces in active/standby mode, FRR is delivered by default and is not controlled by the enhanced M-LAG Layer 3 forwarding command.


Example
-------

# Enable enhanced M-LAG Layer 3 forwarding for the CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, and CE6881H-K.
```
<HUAWEI> system-view
[~HUAWEI] m-lag forward layer-3 enhanced enable

```

# Enable enhanced M-LAG Layer 3 forwarding for the CE6866, CE6860-SAN, CE6860-HAM, CE6866K, CE8851-32CQ8DQ-P, CE8850-SAN, CE8850-HAM, CE8851K, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6885-SAN, and CE6885-LL (low latency mode).
```
<HUAWEI> system-view
[~HUAWEI] undo m-lag forward layer-3 enhanced disable

```
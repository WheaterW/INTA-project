direct-route degrade-delay
==========================

direct-route degrade-delay

Function
--------



The **direct-route degrade-delay** command enables the cost recovery delay function for IPv4 direct routes on an interface after the interface changes from Down to Up.

The **undo direct-route degrade-delay** command disables a cost recovery delay for IPv4 direct routes on an interface.



By default, there is no such function on the interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**direct-route degrade-delay** *delay-time* **degrade-cost** *cost*

**undo direct-route degrade-delay**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *delay-time* | Specifies the delay after which the original cost of the IPv4 direct route is restored on a specified interface. | The value is an integer ranging from 1 to 3600, in seconds. |
| **degrade-cost** *cost* | Specifies the cost of the IPv4 direct route on a specified interface. | The value is an integer ranging from 1 to 4294967295. |



Views
-----

Eth-Trunk sub-interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



In an M-LAG dual-active scenario, a CE is dual-homed to PE1 and PE2 through an Eth-Trunk interface working in LACP mode, and traffic is load-balanced. If either PE1 or PE2 fails and restarts, a traffic switchback is triggered. For example, PE1 restarts. After that, the Eth-Trunk member interface on PE1 detects the link Up state. In this case, PE1 successfully negotiates with the CE on LACP. The Eth-Trunk interface becomes Up, and the Eth-Trunk sub-interface entries are delivered. Since the entry information is huge, the delivery is time consuming. As a result, traffic sent from the network side to PE1 and the CE is dropped because the delivery of PE1's Eth-Trunk sub-interface entries is not complete.To address the preceding problem, run the **direct-route degrade-delay** command to increase the route cost. After the **direct-route degrade-delay** command is run, the cost of the direct IPv4 route on PE1 increases first. The route advertised by PE1 is no longer preferentially selected, and network-to-user traffic passes through PE2 through the backup link. After a specified delay time, the original cost of the direct IPv4 route on PE1 is restored. The route advertised by PE1 is preferentially selected again. Since PE1 has learned the MAC address of the base station, a network-to-user traffic switchback does not result in traffic loss.



**Precautions**



The direct-route degrade-delay, and **direct-route track vrrp** commands cannot all be configured simultaneously. If you run the commands, the latest configuration overrides the previous one.




Example
-------

# Set degrade-cost cost to 50 and delay-time to 10s on Eth-Trunk1.1.
```
<HUAWEI> system-view
[~HUAWEI] interface Eth-Trunk 1
[~HUAWEI-Eth-Trunk1] undo portswitch
[*HUAWEI-Eth-Trunk1] quit
[*HUAWEI] interface Eth-Trunk 1.1
[*HUAWEI-Eth-Trunk1.1] direct-route degrade-delay 20 degrade-cost 50

```
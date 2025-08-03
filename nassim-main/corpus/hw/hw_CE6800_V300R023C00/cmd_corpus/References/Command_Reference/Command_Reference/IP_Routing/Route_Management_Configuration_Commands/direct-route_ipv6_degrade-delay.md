direct-route ipv6 degrade-delay
===============================

direct-route ipv6 degrade-delay

Function
--------



The **direct-route ipv6 degrade-delay** command enables the cost recovery delay function for IPv6 direct routes on an interface after the interface changes from Down to Up.

The **undo direct-route ipv6 degrade-delay** command disables a cost recovery delay for IPv6 direct routes on an interface.



By default, there is no such configuration on the interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**direct-route ipv6 degrade-delay** *delay-time* **degrade-cost** *cost*

**undo direct-route ipv6 degrade-delay**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *delay-time* | Specifies the delay after which the original cost of the IPv6 direct route is restored on a specified interface. | The value is an integer ranging from 1 to 3600, in seconds. |
| **degrade-cost** *cost* | Specifies the cost of the IPv6 direct route on a specified interface. | The value is an integer ranging from 1 to 4294967295. |



Views
-----

Eth-Trunk sub-interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

After the **direct-route ipv6 degrade-delay** command is configured on an interface and the interface changes from Down to Up, the cost of the IPv6 direct route changes to the configured value. After the configuration of delay-time times out, the cost of the IPv6 direct route is restored to the default value 0.


Example
-------

# Set the cost of the IPv6 direct route on Eth-Trunk10.1 to 30 and the delay to restore the default cost of 0 to 10 seconds.
```
<HUAWEI> system-view
[~HUAWEI] interface eth-trunk 10
[~HUAWEI-Eth-Trunk10] undo portswitch
[*HUAWEI-Eth-Trunk10] quit
[*HUAWEI] interface eth-trunk 10.1
[*HUAWEI-Eth-Trunk10.1] ipv6 enable
[*HUAWEI-Eth-Trunk10.1] direct-route ipv6 degrade-delay 10 degrade-cost 30

```
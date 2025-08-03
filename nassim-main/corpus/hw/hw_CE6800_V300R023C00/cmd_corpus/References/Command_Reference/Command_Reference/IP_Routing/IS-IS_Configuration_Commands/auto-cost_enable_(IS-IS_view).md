auto-cost enable (IS-IS view)
=============================

auto-cost enable (IS-IS view)

Function
--------



The **auto-cost enable** command enables IS-IS to automatically calculate the link cost of interfaces according to the interface bandwidth.

The **auto-cost enable compatible** command enables IS-IS to automatically calculate the link cost of interfaces according to the interface bandwidth in compatible.

The **undo auto-cost enable** command disables the function.

The **ipv6 auto-cost enable** command enables IS-IS to automatically calculate the IPv6 link cost of interfaces according to the interface bandwidth.

The **ipv6 auto-cost enable compatible** command enables IS-IS to automatically calculate the link cost of interfaces according to the interface bandwidth in compatible.

The **undo ipv6 auto-cost enable** command disables the function.



By default, automatic interface cost calculation is disabled.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**auto-cost enable** [ **compatible** ]

**undo auto-cost enable**

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**ipv6 auto-cost enable** [ **compatible** ]

**undo ipv6 auto-cost enable**


Parameters
----------

None

Views
-----

IS-IS view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can configure a link cost for interfaces or run the **auto-cost enable** command to enable automatic interface cost calculation.You can configure an IPv6 link cost for interfaces or run the **auto-cost enable** command to enable automatic interface cost calculation.

**Prerequisites**



No interface cost has been set in the interface view, and no global cost has been configured in the IS-IS view.



**Configuration Impact**

After automatic interface cost calculation is enabled, the system automatically calculates the interface cost.If the cost style of the system is wide or wide-compatible:When **auto-cost enable** command is configured, Interface cost = (Bandwidth-reference/Interface bandwidth) x 10.When **auto-cost enable compatible** command is configured, Interface cost = (Bandwidth-reference/Interface bandwidth).If the cost type is narrow, narrow-compatible, or compatible, the cost of each interface is based on:

* Interface bandwidth â¤ 10 Mbit/s, cost = 60
* 10 Mbit/s < interface bandwidth â¤ 100 Mbit/s, cost = 50
* 10 Mbit/s < interface bandwidth â¤ 155 Mbit/s, cost = 40
* 155 Mbit/s < interface bandwidth â¤ 622 Mbit/s, Cost = 30
* 622 Mbit/s < Interface bandwidth â¤ 2.5 Gbit/s, cost = 20
* 2.5 Gbit/s < interface bandwidth, Cost = 10After automatic interface cost calculation is enabled, the system automatically calculates the interface cost.If the cost style of the system is wide or wide-compatible:When **ipv6 auto-cost enable** command is configured, Interface cost = (Bandwidth-reference/Interface bandwidth) x 10.When **ipv6 auto-cost enable compatible** command is configured, Interface cost = (Bandwidth-reference/Interface bandwidth).If the cost type is narrow, narrow-compatible, or compatible, the IPv6 link cost of each interface is calculated based on:
* Interface bandwidth â¤ 10 Mbit/s, cost = 60
* 10 Mbit/s < interface bandwidth â¤ 100 Mbit/s, cost = 50
* 10 Mbit/s < interface bandwidth â¤ 155 Mbit/s, cost = 40
* 155 Mbit/s < interface bandwidth â¤ 622 Mbit/s, Cost = 30
* 622 Mbit/s < Interface bandwidth â¤ 2.5 Gbit/s, cost = 20
* 2.5 Gbit/s < interface bandwidth, Cost = 10

**Precautions**



The **auto-cost enable** command cannot change the cost of a loopback interface.The **auto-cost enable** command can be run on Eth-Trunk interfaces as well as on physical interfaces. If the command is run on an Eth-Trunk interface, the bandwidth of the Eth-Trunk interface is equal to the total bandwidth of all its member interfaces.




Example
-------

# Enable automatic IPv6 cost calculation on an IS-IS interface.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] ipv6 enable
[*HUAWEI-isis-1] ipv6 auto-cost enable

```

# Enable automatic cost calculation on IS-IS interfaces.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] auto-cost enable

```
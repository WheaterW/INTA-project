nexthop recursive-lookup delay (BGP multi-instance VPN instance IPv4 address family view)
=========================================================================================

nexthop recursive-lookup delay (BGP multi-instance VPN instance IPv4 address family view)

Function
--------



The **nexthop recursive-lookup delay** command configures a delay in responding to next hop recursion changes.

The **undo nexthop recursive-lookup delay** command cancels the configuration of the delay in responding to next hop recursion changes.

The **nexthop recursive-lookup non-critical-event delay** command configures a delay in responding to non-critical next hop recursion changes.

The **undo nexthop recursive-lookup non-critical-event delay** command cancels the configuration of the delay in responding to non-critical next hop recursion changes.



By default, the delay in responding to non-critical next hop recursion changes is 10s, and the device does not delay responding to critical next hop recursion changes.


Format
------

**nexthop recursive-lookup delay** [ *delay-time* ]

**nexthop recursive-lookup non-critical-event delay** [ *nonCrit-delay-time* ]

**undo nexthop recursive-lookup delay**

**undo nexthop recursive-lookup non-critical-event delay**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *delay-time* | Specifies the delay in responding to recursion changes. | The value is an integer that ranges from 1 to 100, in seconds. The default value is 5 seconds. |
| *nonCrit-delay-time* | Indicates the delay in responding to non-critical recursion changes. | The value is an integer ranging from 0 to 100, in seconds. The default value is 10. |



Views
-----

BGP multi-instance VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If the recursion result of BGP routes changes frequently, you can run the **nexthop recursive-lookup delay** command to configure BGP to respond to the recursion result change after a specified period of time. This reduces unnecessary route re-selection and re-advertisement. However, this affects network convergence. Therefore, recursion result changes are classified into two types:

* Critical recursion result change: When the recursion result of the next hop changes, the reachability also changes. For example, if a fault occurs on the network, BGP routes cannot find the next hop route or tunnel to which BGP routes can be recursed. As a result, traffic is interrupted.
* Non-critical recursion result change: The recursion result of the next hop changes, but the reachability does not change. For example, the interface or type of the tunnel to which the next hop of a BGP route is recursed changes. That is, the tunnel to which the next hop of a BGP route is recursed changes from tunnel A to tunnel B, but traffic is not interrupted. Only the tunnel to which the next hop of a BGP route is recursed changes.

**Configuration Impact**

The rules for configuring a delay in response to next hop recursion changes and configuring a dedicated delay in response to non-critical recursion changes are as follows:

* nexthop recursive-lookup delay //Configure the device to delay for 5s in response to critical recursion changes and delay for 10s in response to non-critical recursion changes.
* nexthop recursive-lookup non-critical-event delay //Configure the device not to delay the responses to critical recursion changes but to delay for 10s in response to non-critical recursion changes.
* nexthop recursive-lookup delay 3 //Configure the device to delay for 3s in response to critical recursion changes and delay for 10s in response to non-critical recursion changes.
* nexthop recursive-lookup non-critical-event delay 6 //Configure the device not to delay the responses to critical recursion changes but to delay for 6s in response to non-critical recursion changes.
* nexthop recursive-lookup delaynexthop recursive-lookup non-critical-event delay 0 //Configure the device to delay for 5s in response to both critical and non-critical recursion changes.
* nexthop recursive-lookup delaynexthop recursive-lookup non-critical-event delay //Configure the device to delay for 5s in response to critical recursion changes and delay for 10s in response to non-critical recursion changes.
* nexthop recursive-lookup delay 3nexthop recursive-lookup non-critical-event delay //Configure the device to delay for 3s in response to critical recursion changes and delay for 10s in response to non-critical recursion changes.
* nexthop recursive-lookup delay 3nexthop recursive-lookup non-critical-event delay 6 //Configure the device to delay for 3s in response to critical recursion changes and delay for 6s in response to non-critical recursion changes.
* nexthop recursive-lookup delaynexthop recursive-lookup non-critical-event delay 6 //Configure the device to delay for 5s in response to critical recursion changes and delay for 6s in response to non-critical recursion changes.

**Precautions**



Delayed response to BGP next hop recursion changes applies only to scenarios where multiple links exist between the downstream device and the same destination. If there is only one link between the downstream device and the destination, configuring delayed response to BGP next hop recursion changes may cause heavier traffic loss when the link fails because link switching is impossible.After the **nexthop recursive-lookup delay** command is run, if the delay in response to non-critical recursion changes is set to 0 using the **nexthop recursive-lookup non-critical-event delay** command, the actual delay in response to non-critical recursion changes is the same as the delay in response to next hop recursion changes specified in the **nexthop recursive-lookup delay** command.




Example
-------

# Set the delay in responding to non-critical recursion changes to 20 seconds.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv4-family
[*HUAWEI-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
[*HUAWEI-vpn-instance-vpna-af-ipv4] quit
[*HUAWEI-instance-vpna] quit
[*HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] ipv4-family vpn-instance vpna
[*HUAWEI-bgp-instance-a-vpna] nexthop recursive-lookup non-critical-event delay 20

```
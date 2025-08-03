nexthop (ICMP Ping test instance)
=================================

nexthop (ICMP Ping test instance)

Function
--------



The **nexthop** command configures a next-hop IP address for an NQA ping test instance.

The **undo nexthop** command deletes the configured next-hop IP address.



By default, a device searches the routing table for the next-hop IP address during packet sending.


Format
------

**nexthop ipv4** *ipv4Address*

**nexthop ipv6** *ipv6Address*

**undo nexthop**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ipv6** *ipv6Address* | Specifies a next hop IPv6 address on an ingress. | The address is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **ipv4** *ipv4Address* | Specifies a next hop IP address on an ingress. | The value is in dotted decimal notation. |



Views
-----

NQA view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In a scenario where NQA is associated with static routes, if a link is faulty, the NQA ICMP test fails, and the associated static route goes Down. As the device needs to search the routing table when sending ICMP test packets, the ICMP test still fails even if the link fault is rectified. In addition, the associated static route keeps being Down, and service traffic cannot be switched back to the original link.To resolve this problem, specify a next-hop IP address for the ICMP test packets so that the packets can be properly sent after the link fault is rectified. This configuration also causes the test to succeed and the associated static route to go Up.

**Configuration Impact**

After a next-hop IP address is specified, test packets are directly sent based on the IP address, freeing the device from searching the routing table for packet sending.

**Precautions**

When specifying a next-hop IP address, run the **source-interface** command to specify an outbound interface. In this situation, the test must meet the following conditions. Otherwise, the test fails.

* The specified next-hop IP address and outbound interface match each other.
* The specified outbound interface cannot be a member interface of a logical interface.No VPN is specified when you specify a next-hop IP address.No simulated inbound interface is specified when you specify a next-hop IP address.

Example
-------

# Specify a next-hop IP address.
```
<HUAWEI> system-view
[~HUAWEI] nqa test-instance user test
[*HUAWEI-nqa-user-test] test-type icmp
[*HUAWEI-nqa-user-test] nexthop ipv4 10.1.1.1

```
peer timer connect-retry (BGP multi-instance view)
==================================================

peer timer connect-retry (BGP multi-instance view)

Function
--------



The **peer timer connect-retry** command sets a ConnectRetry interval for a peer.

The **undo peer timer connect-retry** command restores the default setting.



By default, the ConnectRetry interval is 32s.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**peer** { *ipv4-address* | *ipv6-address* } **timer** **connect-retry** *connect-retry-time*

**undo peer** { *ipv4-address* | *ipv6-address* } **timer** **connect-retry**

For CE6885-LL (low latency mode):

**peer** *ipv4-address* **timer** **connect-retry** *connect-retry-time*

**undo peer** *ipv4-address* **timer** **connect-retry**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *connect-retry-time* | Specifies a ConnectRetry interval. | The value ranges from 1 to 65535, in seconds. |
| **peer** *ipv4-address* | Specifies the IPv4 address of a peer. | The value is in dotted decimal notation. |
| **peer** *ipv6-address* | Specifies an IPv6 peer address.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |



Views
-----

BGP multi-instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When BGP initiates a TCP connection, the ConnectRetry timer is stopped if the TCP connection is established successfully. If the attempt to establish a TCP connection fails, BGP tries again to establish the TCP connection after the ConnectRetry timer expires. The ConnectRetry interval can be adjusted as needed.

* The ConnectRetry interval can be reduced in order to lessen the time BGP waits to retry establishing a TCP connection after the first attempt fails.
* To suppress route flapping caused by constant peer flapping, the ConnectRetry interval can be increased to accelerate route convergence.

**Prerequisites**

The **peer as-number** command has been used to create a peer.

**Precautions**

A ConnectRetry interval can be configured globally, or on a particular peer. A ConnectRetry interval configured on a specific peer or peer group takes precedence over a global ConnectRetry interval.

* If both the peer ipv4-address timer connect-retry connect-retry-time command and the peer group-name timer connect-retry connect-retry-time command are run on a device, the configuration of the peer ipv4-address timer connect-retry connect-retry-time command takes effect, but the configuration of the peer group-name timer connect-retry connect-retry-time command does not.
* If both the peer { group-name | ipv4-address } timer connect-retry connect-retry-time command and the timer connect-retry connect-retry-time command are run on a device, the configuration of the peer { group-name | ipv4-address } timer connect-retry connect-retry-time command takes effect, but the configuration of the timer connect-retry connect-retry-time command does not.

Example
-------

# Set the ConnectRetry interval to 60s for peer.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] peer 10.2.2.2 as-number 200
[*HUAWEI-bgp-instance-a] peer 10.2.2.2 timer connect-retry 60

```
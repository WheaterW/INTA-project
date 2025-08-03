peer timer connect-retry (BGP-VPN instance view) (group)
========================================================

peer timer connect-retry (BGP-VPN instance view) (group)

Function
--------



The **peer timer connect-retry** command sets a ConnectRetry interval for a peer group.

The **undo peer timer connect-retry** command restores the default setting.



By default, the ConnectRetry interval is 32s.


Format
------

**peer** *group-name* **timer** **connect-retry** *connect-retry-time*

**undo peer** *group-name* **timer** **connect-retry**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The value is a string of 1 to 47 case-sensitive characters and cannot contain spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| *connect-retry-time* | Specifies a ConnectRetry interval. | The value ranges from 1 to 65535, in seconds. |



Views
-----

BGP-VPN instance view,BGP multi-instance VPN instance session view


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

The **peer as-number** command has been run to create BGP peers or BGP peer groups.

**Precautions**

A ConnectRetry interval can be configured globally, or on a particular peer. A ConnectRetry interval configured on a specific peer or peer group takes precedence over a global ConnectRetry interval.

* If both the peer { ipv4-address| ipv6-address } timer connect-retry connect-retry-time command and the peer group-name timer connect-retry connect-retry-time command are run on a device, the configuration of the peer { ipv4-address| ipv6-address } timer connect-retry connect-retry-time command takes effect, but the configuration of the peer group-name timer connect-retry connect-retry-time command does not.
* If both the peer { group-name | ipv4-address| ipv6-address } timer connect-retry connect-retry-time command and the timer connect-retry connect-retry-time command are run on a device, the configuration of the peer { group-name | ipv4-address| ipv6-address } timer connect-retry connect-retry-time command takes effect, but the configuration of the timer connect-retry connect-retry-time command does not.

Example
-------

# Set the ConnectRetry interval to 60s for peer group.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] vpn-instance vpn1
[*HUAWEI-bgp-instance-vpn1] group test
[*HUAWEI-bgp-instance-vpn1] peer test timer connect-retry 60

```
peer graceful-restart timer restart (BGP multi-instance VPN instance IPv4 address family view)(IPv4)
====================================================================================================

peer graceful-restart timer restart (BGP multi-instance VPN instance IPv4 address family view)(IPv4)

Function
--------



The **peer graceful-restart timer restart** command sets the maximum duration on a device for a specified peer to wait for its BGP peer relationship to be reestablished with the device. After the command is run, the device will advertise the maximum duration to the specified peer.

The **undo peer graceful-restart timer restart** command deletes the configured duration.



By default, a peer specified on a device waits for its BGP peer relationship to be reestablished with the device for a maximum of 150s.


Format
------

**peer** *ipv4-address* **graceful-restart** **timer** **restart** *time-value*

**undo peer** *ipv4-address* **graceful-restart** **timer** **restart**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specify an IPv4 peer address. | The value is in dotted decimal notation. |
| *time-value* | Specifies the maximum duration on a device for a peer to wait for its BGP peer relationship to be reestablished with the device. | The value is an integer ranging from 3 to 3600, in seconds. |



Views
-----

BGP multi-instance VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



If a device and a BGP peer specified on the device both support GR, you can run the peer graceful-restart timer restart command to set the maximum duration on the device for the peer to wait for its BGP peer relationship to be reestablished with the device. After this command is run, if the peer detects that the device is down, the BGP session on the peer enters the GR process. If the peer relationship fails to be reestablished within the specified duration, the BGP session exits from the GR process and the peer selects the optimal route from current reachable routes.



**Configuration Impact**



If this command is run, the BGP peer relationship is disconnected and re-established. Therefore, exercise caution when running this command.




Example
-------

# Set the maximum duration to 100s on a device for a specified peer to wait for its BGP peer relationship to be reestablished with the device.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv4-family
[*HUAWEI-vpn-instance-vpn1-af-ipv4] bgp 100 instance a
[*HUAWEI-bgp-instance-a] ipv4-family vpn-instance vpn1
[*HUAWEI-bgp-instance-a-vpn1] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp-instance-a-vpn1] peer 10.1.1.1 graceful-restart timer restart 100

```
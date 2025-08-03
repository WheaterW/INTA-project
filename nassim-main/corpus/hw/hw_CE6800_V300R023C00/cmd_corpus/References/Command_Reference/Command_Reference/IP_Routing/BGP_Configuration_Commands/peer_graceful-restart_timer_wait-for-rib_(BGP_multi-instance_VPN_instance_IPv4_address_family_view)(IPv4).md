peer graceful-restart timer wait-for-rib (BGP multi-instance VPN instance IPv4 address family view)(IPv4)
=========================================================================================================

peer graceful-restart timer wait-for-rib (BGP multi-instance VPN instance IPv4 address family view)(IPv4)

Function
--------



The **peer graceful-restart timer wait-for-rib** command sets the maximum duration for a BGP restarter to wait for the End-of-RIB flag from a specified peer.

The **undo peer graceful-restart timer wait-for-rib** command deletes the configured duration.



By default, a BGP restarter waits for the End-of-RIB flag from a specified peer for a maximum of 600s.


Format
------

**peer** *ipv4-address* **graceful-restart** **timer** **wait-for-rib** *time-value*

**undo peer** *ipv4-address* **graceful-restart** **timer** **wait-for-rib**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |
| *time-value* | Specifies the maximum duration for a BGP restarter to wait for the End-of-RIB flag. | The value is an integer ranging from 3 to 3000, in seconds. |



Views
-----

BGP multi-instance VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



After the local device reestablishes a BGP session with a specified peer, the local device should receive the End-Of-RIB flag from the specified peer within the period specified by this command. If the local device does not receive the End-Of-RIB flag within the period specified by this command, the local device exits the GR process and selects the optimal route from the existing routes.



**Configuration Impact**



If the command is run more than once, the latest configuration overrides the previous one.




Example
-------

# Set the maximum duration during which a BGP restarter waits for the End-of-RIB flag from a specified peer to 100s.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna] bgp 100 instance dd
[*HUAWEI-bgp-instance-dd] ipv4-family vpn-instance vpna
[*HUAWEI-bgp-instance-dd-vpna] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp-instance-dd-vpna] peer 10.1.1.1 graceful-restart timer wait-for-rib 100

```
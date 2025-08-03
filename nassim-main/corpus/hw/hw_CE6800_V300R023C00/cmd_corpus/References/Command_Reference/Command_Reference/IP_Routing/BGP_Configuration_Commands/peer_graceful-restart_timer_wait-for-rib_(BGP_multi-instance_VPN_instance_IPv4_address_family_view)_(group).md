peer graceful-restart timer wait-for-rib (BGP multi-instance VPN instance IPv4 address family view) (group)
===========================================================================================================

peer graceful-restart timer wait-for-rib (BGP multi-instance VPN instance IPv4 address family view) (group)

Function
--------



The **peer graceful-restart timer wait-for-rib** command sets the maximum duration for a BGP restarter to wait for the End-of-RIB flag from each peer in a specified group.

The **undo peer graceful-restart timer wait-for-rib** command deletes the configured duration.



By default, a BGP restarter waits for the End-of-RIB flag from each peer in a specified group for a maximum of 600s.


Format
------

**peer** *group-name* **graceful-restart** **timer** **wait-for-rib** *time-value*

**undo peer** *group-name* **graceful-restart** **timer** **wait-for-rib**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The value is a string of 1 to 47 case-sensitive characters. If spaces are used, the string must start and end with double quotation marks ("). |
| *time-value* | Specifies the maximum duration for waiting for the End-Of-RIB flag. | The value is an integer ranging from 3 to 3000, in seconds. |



Views
-----

BGP multi-instance VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



After the local device re-establishes a BGP session with a specified peer group, the local device should receive the End-Of-RIB flag from the specified peer group within the period specified by this command. If the local device does not receive the End-Of-RIB flag within the period specified by this command, the local device exits the GR process and selects the optimal route from the existing routes.



**Configuration Impact**



If the peer graceful-restart timer wait-for-rib command is run more than once, the latest configuration overrides the previous one.




Example
-------

# Set the maximum duration during which a BGP restarter waits for the End-of-RIB flag from each peer in a specified group to 100s.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna] bgp 100 instance dd
[*HUAWEI-bgp-instance-dd] ipv4-family vpn-instance vpna
[*HUAWEI-bgp-instance-dd-vpna] group aaa
[*HUAWEI-bgp-instance-dd-vpna] peer aaa graceful-restart timer wait-for-rib 100

```
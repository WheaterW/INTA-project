monitor all-vpn-instance
========================

monitor all-vpn-instance

Function
--------



The **monitor all-vpn-instance** command displays the BMP-Monitor view and allows the BGP running status of BGP peers in all VPN instance address families to be monitored.

The **undo monitor all-vpn-instance** command restores the default configuration.



By default, the BGP running status of BGP peers is not monitored.


Format
------

**monitor all-vpn-instance**

**undo monitor all-vpn-instance**


Parameters
----------

None

Views
-----

BMP session view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



BMP is used to monitor BGP running status of devices in real time, such as the establishment and termination status of BGP peer relationships and route update status. To allow the BGP running status of BGP peers in all VPN instance address families to be monitored, run the monitor all-vpn-instance command. After a TCP connection is established between the device and the monitoring server, the device reports BGP running status to the monitoring server, improving network monitoring efficiency.



**Follow-up Procedure**

Perform either of the following operations as required:

* Run the route-mode { { ipv4-family | ipv6-family } unicast } adj-rib-in { pre-policy | post-policy } command to set the type of RIB-in route (received from all peers in a specified address family of a specified VPN instance) whose statistics are to be sent by the device to the monitoring server.
* Run the route-mode { { ipv4-family | ipv6-family } unicast } adj-rib-out { pre-policy | post-policy } command to set the type of RIB-out route (to be advertised or already advertised to all peers in a specified address family of a specified VPN instance) whose statistics are to be sent by the device to the monitoring server.
* Run the route-mode { { ipv4-family | ipv6-family } unicast } local-rib [ add-path ] command to configure the device to send statistics about Local-RIB routes of all BGP peers in a specified address family of the VPN instance to the monitoring server.


Example
-------

# Display the BMP-Monitor view and allow the BGP running status of all BGP peers in all VPN instance address families to be monitored.
```
<HUAWEI> system-view
[~HUAWEI] bmp
[*HUAWEI-bmp] bmp-session 10.1.1.1 alias a
[*HUAWEI-bmp-session-10.1.1.1-a] monitor all-vpn-instance

```
monitor public
==============

monitor public

Function
--------



The **monitor public** command displays the BMP-Monitor view and allows the BGP running status of all BGP peers in the public network address family to be monitored.

The **undo monitor public** command restores the default configuration.



By default, the BGP running status of BGP peers is not monitored.


Format
------

**monitor public**

**undo monitor public**


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



BMP is used to monitor BGP running status of devices in real time, such as the establishment and termination status of BGP peer relationships and route update status. To allow the BGP running status of all BGP peers in the public network address family to be monitored, run the monitor public command. After a TCP connection is established between a device and a monitoring server, the device reports BGP running status to the monitoring server, improving network monitoring efficiency.



**Follow-up Procedure**

Perform either of the following operations as required:

* Run the route-mode { { { ipv4-family | ipv6-family } unicast } | ipv4-family vpnv4 | ipv6-family vpnv6 } adj-rib-in { pre-policy | post-policy } command to set the type of RIB-in route (received from all peers in a specified public network address family) whose statistics are to be sent by the device to the monitoring server.
* Run the route-mode { { { ipv4-family | ipv6-family } unicast } | ipv4-family vpnv4 | ipv6-family vpnv6 } adj-rib-out { pre-policy | post-policy } command to set the type of RIB-out route (to be advertised or already advertised to all peers in a specified public network address family) whose statistics are to be sent by the device to the monitoring server.
* Run the route-mode { { { ipv4-family | ipv6-family } unicast } | ipv4-family vpnv4 | ipv6-family vpnv6 } local-rib [ add-path ] command to configure the device to send statistics about Local-RIB routes of all BGP peers in the specified public network address family to the monitoring server.


Example
-------

# Display the BMP-Monitor view and allow the BGP running status of all BGP peers in the public network address family to be monitored.
```
<HUAWEI> system-view
[~HUAWEI] bmp
[*HUAWEI-bmp] bmp-session 10.1.1.1 alias a
[*HUAWEI-bmp-session-10.1.1.1-a] monitor public

```
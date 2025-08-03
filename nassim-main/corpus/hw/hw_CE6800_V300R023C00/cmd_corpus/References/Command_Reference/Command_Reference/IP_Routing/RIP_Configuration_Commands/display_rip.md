display rip
===========

display rip

Function
--------



The **display rip** command displays the operating status and configurations of a RIP process.

The **display ripng** command displays the current operating status and configurations of a RIPng process.

The **display default-parameter rip** command displays the default values of all the configurable parameters of RIP.

The **display default-parameter ripng** command displays default RIPng configurations.




Format
------

**display rip** [ *process-id* | **vpn-instance** *vpn-instance-name* ]

**display default-parameter rip**

**display ripng** [ *process-id* | **vpn-instance** *vpn-instance-name* ]

**display default-parameter ripng**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies the ID of a process. | The value is an integer ranging from 1 to 4294967295. |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

To check the running status and configurations of RIP processes on a local device, run the **display rip** command.After basic RIPng functions are configured, you can run this command to view the configured information.You can run the **display default-parameter rip** command either in a process or on an interface.Even if the default RIPng configurations have been changed, this command displays the original default RIPng configurations.You can run the **display default-parameter ripng** command either in a process or on an interface.

**Precautions**



If no process ID is specified, running the display ripng command displays the parameters of all configured RIPng processes.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the operating status of the RIP process and the configuration.
```
<HUAWEI> display rip
Public VPN-instance
RIP process : 1
RIP version   : 1
Preference    : 100
Check zero    : Enabled
Default cost  : 1
Summary       : Enabled
Host route    : Enabled
Maximum number of balanced paths : 6
Update time   : 30 sec             Age time  : 180 sec
Suppress time : 0 sec   Garbage-collect time : 120 sec
Graceful restart  : Disabled
BFD               : Enabled
Transmit-Interval : 102 ms
Receive-Interval  : 101 ms
Detect-Multiplier : 5
Silent interfaces : None
Default route : Route Policy
       Default route Route-Policy : abcd
       Default Route Cost : 0
Verify source : Enabled
Networks :
10.1.0.0   10.2.0.0
Configured peers             : None
Number of routes in database : 1
Number of interfaces enabled : 0
Number of VRRP interfaces    : 0
Triggered updates sent       : 0
Number of route changes      : 0
Number of replies to queries : 0
Total count for 1 process :
Number of routes in database : 1
Number of interfaces enabled : 0
Number of VRRP interfaces    : 0
Number of routes sendable in a periodic update : 0
Number of routes sent in last periodic update : 0

```

# View the default RIP configuration.
```
<HUAWEI> display default-parameter rip
--------------------------------------------
 Protocol Level Default Configurations
--------------------------------------------
       RIP version   : 1
       Preference    : 100
       Checkzero     : Enabled
       Default-cost  : 0
       Auto Summary  : Enabled
       Host-route    : Enabled
       Maximum Balanced Paths : 64
       Update time   : 30 sec     Age time : 180 sec
       Suppress time : 0 sec      Garbage-collect time : 120 sec
       Default-route : Disabled
       Verify-source : Enabled
       Graceful restart  : Disabled
--------------------------------------------
 Interface Level Default Configurations
--------------------------------------------
  Metricin                : 0
  Metricout               : 1
  Input Packet Processing : Enabled
  Output Packet Processing: Enabled
  Poison Reverse          : Disabled
  Replay Protect          : Disabled
  Split Horizon
   For Broadcast and P2P Interfaces :  Enabled
   For NBMA Interfaces              :  Disabled
  Packet Transmit Interval          :  200 msecs
  Packet Transmit Number            :  50
  RIP Protocol Version              :  RIPv1 Compatible (Non-Standard)

```

# Display the current operating status and configurations of the RIPng process.
```
<HUAWEI> display ripng 100
Public vpn-instance name :
RIPng process : 100
Preference : 100
Checkzero : Enabled
Default Cost : 0
Maximum number of balanced paths : 6
Update time   : 30 sec   Age time  : 180 sec
Suppress time : 0 sec    Garbage-Collect time : 120 sec
Number of periodic updates sent : 0
Number of trigger updates sent : 1
Number of routes in database : 1
Number of interfaces enabled : 1

```

# Display default RIPng configurations.
```
<HUAWEI> display default-parameter ripng
-------------------------------------------------- 
 Protocol Level Default Configurations
-------------------------------------------------- 
       Preference    : 100
       Checkzero     : Enabled
       Default-cost  : 0
       Maximum Balanced Paths : 64
       Update time   : 30 sec     Age time             : 180 sec
       Suppress time : 0 sec      Garbage-collect time : 120 sec
-------------------------------------------------- 
 Interface Level Default Configurations
-------------------------------------------------- 
    Metricin          : 0
    Metricout         : 1
    Input Packet Processing : Enabled
    Output Packet Processing: Enabled
    Poison Reverse    : Disabled
    Split Horizon
     For Broadcast and P2P Interfaces     :  Enabled
     For NBMA Interfaces and LoopBack     :  Disabled
    Default-route                         :  Disabled
    Packet Transmit Interval              :  200 msecs
    Packet Transmit Number                :  30

```

**Table 1** Description of the **display rip** command output
| Item | Description |
| --- | --- |
| RIP version | RIP version: 1 or 2. |
| RIP Protocol Version | RIP version:   * RIPv1 Compatible (Non-Standard): Supports both RIPv1 and RIPv2. * RIP-1. * RIP-2. |
| RIP process | RIP process ID. |
| Preference | Priority of the process. |
| Checkzero | MBZ field check. |
| Default-cost | Default cost. |
| Summary | Whether route summarization is enabled. |
| Host-route | Whether host routes are enabled. |
| Maximum Balanced Paths | Maximum number of equal-cost routes. |
| Maximum number of balanced paths | Maximum number of equal-cost routes. |
| Update time | Interval at which Update packets are sent. |
| Age time | Aging time. |
| Suppress time | Suppression period of routes. |
| Garbage-collect time | Interval at which garbage routes are collected. |
| Graceful restart | Whether GR is enabled. |
| BFD | Whether BFD is enabled. |
| Transmit-Interval | Minimum interval at which BFD packets are sent. |
| Receive-Interval | Minimum interval at which BFD packets are received. |
| Detect-Multiplier | Local BFD detection multiplier. |
| Default-route | Default route, which is used when route entries cannot be found in the routing table to forward packets. |
| Default Route | Default route. |
| Default Cost | Default cost. |
| Default Route Cost | Cost of the originated default route. |
| Default route | Default route generation information:   * Enabled: indicates that default route generation is enabled. * Originate Always: indicates that default routes are generated unconditionally. * Match Default: indicates that the default routes generated by other routing protocols or RIP processes exist in the routing table. * Route Policy: indicates that the routes matching the route-policy exist in the routing table. * Disabled: indicates that default route generation is disabled. |
| Default route Route-Policy | Name of the route-policy used by the RIP process to originate the default route. |
| Verify-source | Whether source authentication is enabled. |
| Networks | Network address. |
| Configured peers | Configured neighbors. |
| Number of periodic updates sent | Number of RIPng Update packets sent periodically. |
| Number of trigger updates sent | Number of triggered RIPng Update packets. |
| Number of routes in database | Number of routes in the database. |
| Number of interfaces enabled | Number of the interfaces on which is enabled. |
| Number of VRRP interfaces | Number of VRRP-capable interfaces. |
| Number of replies to queries | Number of response packets to RIP queries. |
| Number of routes sendable in a periodic update | Number of routes that can be sent in each update. |
| Number of routes sent in last periodic update | Number of routes that were sent in the last update. |
| Number of route changes | Statistics on the routes that have been changed in the database. |
| Triggered updates sent | Number of sent triggered updates. |
| Total count for 1 process | Number of routes in RIP process 1. |
| Check zero | Whether Zero field check is enabled. |
| Host route | Whether the host route is enabled. |
| Silent interfaces | Number of interfaces that do not send periodic update packets. |
| Verify source | Source verification. |
| Protocol Level Default Configurations | Protocol-level default information. |
| Auto Summary | Whether route summarization is enabled. |
| Interface Level Default Configurations | Interface-level default configuration. |
| Metricin | Metric that is added to the route when the interface receives a packet. |
| Metricout | Metric that is added to the route when the interface sends a packet. |
| Input Packet Processing | Whether the processing of incoming packets is enabled. |
| Packet Transmit Number | Number of transmitted packets. |
| Packet Transmit Interval | Interval at which packets are transmitted, in milliseconds. |
| Output Packet Processing | Whether the processing of outgoing packets is enabled. |
| Poison Reverse | Whether poison reverse is enabled on the interface. |
| Replay Protect | Replay attack protection. |
| Split Horizon | Whether split horizon is enabled on the interface:   * For Broadcast and P2P Interfaces: whether split horizon is enabled on broadcast and P2P interfaces. * For NBMA Interfaces: whether split horizon is enabled on an NBMA interface. * For NBMA Interfaces and LoopBack: whether split horizon is enabled on the NBMA interface and loopback interface. |
| RIPng process | RIPng process ID. |
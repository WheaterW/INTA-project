display pim interface
=====================

display pim interface

Function
--------



The **display pim interface** command displays information about PIM interfaces.




Format
------

**display pim interface** [ *interface-name* | *interface-type* *interface-number* | **up** | **down** ] [ **verbose** ]

**display pim** { **vpn-instance** *vpn-instance-name* | **all-instance** } **interface** [ *interface-name* | *interface-type* *interface-number* | **up** | **down** ] [ **verbose** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Specifies an interface name. | - |
| *interface-type* | Specifies the type of an interface. | If this parameter is not specified, the command displays information about all PIM interfaces in a specified or all instances. |
| *interface-number* | Specifies the number of an interface. | If this parameter is not specified, the command displays information about all PIM interfaces in a specified or all instances. |
| **up** | Displays information about PIM interfaces of which the IP protocol state is Up. | - |
| **down** | Displays information about PIM interfaces of which the IP protocol state is Down. | - |
| **verbose** | Displays detailed information about PIM interfaces. | - |
| **vpn-instance** *vpn-instance-name* | Specifies a VPN instance name. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **all-instance** | Indicates all instances. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

To check information about PIM interfaces (referring to those on which PIM is enabled), run the **display pim interface** command. The command output includes the number of PIM neighbor relationships that a PIM interface has established, interval at which Hello messages are sent, designated router (DR) priority, and DR address.

**Precautions**

If neither vpn-instance nor all-instance is specified, the command displays information about PIM interfaces in the public network instance.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about PIM interfaces in the public network instance.
```
<HUAWEI> display pim interface
VPN-Instance: public net
 Interface      State   NbrCnt   HelloInt   DR-Pri     DR-Address                ECMP-Pri
 100GE1/0/1        up       1         30          1       10.1.1.2                  -
 100GE1/0/2        up       0         30          1       1.1.1.2        (local)    -
 100GE1/0/3        up       1         30          1       10.1.1.3                  -
 Loopback0         up       0         30          1       1.1.1.1        (local)    -

```

# Display detailed information about the PIM-SM interface 100GE 1/0/1.
```
<HUAWEI> display pim interface 100GE1/0/1 verbose
VPN-Instance: public net
 Interface: 100GE1/0/1, 10.1.1.1
     PIM version: 2
     PIM mode: Sparse
     PIM state: up
     PIM DR: 10.1.1.2
     PIM DR Priority (configured): 1
     PIM neighbor count: 1
     PIM hello interval: 30 s
     PIM LAN delay (negotiated): 500 ms
     PIM LAN delay (configured): 500 ms
     PIM hello override interval (negotiated): 2500 ms
     PIM hello override interval (configured): 2500 ms 
     PIM Silent: disabled 
     PIM neighbor tracking (negotiated): disabled
     PIM neighbor tracking (configured): disabled
     PIM generation ID: 0XF5712241 
     PIM require-GenID: disabled   
     PIM hello hold interval: 105 s
     PIM assert hold interval: 180 s
     PIM triggered hello delay: 5 s
     PIM J/P interval: 60 s
     PIM J/P hold interval: 210 s 
     PIM BSR domain border: disabled
     PIM BFD: enabled
     PIM BFD min-tx-interval: 10 ms
     PIM BFD min-rx-interval: 10 ms
     PIM BFD detect-multiplier: 3
     PIM dr-switch-delay timer: 20 s
     PIM offer-interval: 1 s
     PIM election-robust-count: 5
     PIM backoff-interval: 1 s
     Number of routers on link not using DR priority: 0
     Number of routers on link not using LAN delay: 0
     Number of routers on link not using neighbor tracking: 2
     ACL of PIM neighbor policy: -
     ACL of PIM ASM join policy: -
     ACL of PIM SSM join policy: - 
     ACL of PIM join policy: -
     PIM ignore assert: disabled
     PIM ecmp-priority : -

```

# Display detailed information about the PIM-DM interface 100GE 1/0/1.
```
<HUAWEI> display pim interface 100GE1/0/1 verbose
 VPN-Instance: public net
 Interface: 100GE1/0/1, 10.1.1.1
     PIM version: 2
     PIM mode: Dense
     PIM state: up
     PIM DR: 10.1.1.2 (local)
     PIM DR Priority (configured): 1
     PIM neighbor count: 1
     PIM hello interval: 30 s
     PIM LAN delay (negotiated): 500 ms
     PIM LAN delay (configured): 500 ms
     PIM hello override interval (negotiated): 2500 ms
     PIM hello override interval (configured): 2500 ms
     PIM Silent: disabled
     PIM neighbor tracking (negotiated): disabled
     PIM neighbor tracking (configured): disabled
     PIM generation ID: 0x4E2679FE
     PIM require-GenID: disabled
     PIM hello hold interval: 105 s
     PIM assert hold interval: 180 s
     PIM triggered hello delay: 5 s
     PIM J/P interval: 60 s
     PIM J/P hold interval: 210 s
     PIM state-refresh processing: enabled
     PIM state-refresh interval: 60 s
     PIM graft retry interval: 3 s
     PIM state-refresh capability on link: capable
     PIM BSR domain border: disabled
     PIM BFD: disabled
     PIM dr-switch-delay timer: not configured
     Number of routers on link not using DR priority: 0
     Number of routers on link not using LAN delay: 0
     Number of routers on link not using neighbor tracking: 2
     ACL of PIM neighbor policy: -
     ACL of PIM ASM join policy: -
     ACL of PIM SSM join policy: -
     ACL of PIM join policy: -
     PIM ecmp-priority : -

```

**Table 1** Description of the **display pim interface** command output
| Item | Description |
| --- | --- |
| PIM version | PIM version running on the interface. |
| PIM mode | PIM mode in use.  The value Sparse indicates PIM-SM. |
| PIM DR | DR address of the interface. |
| PIM DR Priority (configured) | DR priority configured for the interface. |
| PIM neighbor count | Number of PIM neighbor relationships that the interface has established. |
| PIM hello interval | Interval at which PIM Hello messages. |
| PIM LAN delay (negotiated) | Negotiated delay in transmitting messages on the interface. |
| PIM LAN delay (configured) | Configured delay in transmitting messages on the interface. |
| PIM hello override interval (negotiated) | Negotiated overriding interval on the interface. |
| PIM hello override interval (configured) | Configured overriding interval on the interface. |
| PIM Silent | Whether PIM silent is enabled on the interface. |
| PIM neighbor tracking (negotiated) | Whether the PIM neighbor tracking function is enabled on the interface after negotiation. |
| PIM neighbor tracking (configured) | Whether the PIM neighbor tracking function is configured on the interface. |
| PIM generation ID | Generation ID of the interface. |
| PIM require-GenID | Whether the interface is configured to deny Hello messages that do not carry generation IDs. |
| PIM hello hold interval | Interval for the receiver of Hello messages to keep its neighbor reachable. |
| PIM assert hold interval | Interval at which Assert messages are sent. |
| PIM triggered hello delay | Maximum random delay for triggering Hello messages. |
| PIM J/P interval | Interval at which the interface sends Join/Prune messages. |
| PIM J/P hold interval | Period for holding the Join/Prune state on the interface. |
| PIM state-refresh processing | Whether State-Refresh is enabled on the interface. |
| PIM state-refresh interval | Interval at which the PIM state is refreshed. |
| PIM graft retry interval | Interval at which Prune messages are retransmitted. |
| PIM state-refresh capability on link | Whether State-Refresh is enabled on the network segment where the interface resides. |
| PIM BSR domain border | Whether a bootstrap device (BSR) domain border is configured on the interface. |
| PIM BFD | Whether PIM BFD is enabled on the interface. |
| PIM BFD min-tx-interval | Minimum interval at which PIM BFD messages are sent. |
| PIM BFD min-rx-interval | Minimum interval at which PIM BFD messages are received. |
| PIM BFD detect-multiplier | PIM BFD detection multiplier. |
| PIM dr-switch-delay timer | DR switching delay. |
| PIM state | Interface state:   * up: The interface is Up. * down: The physical link of the interface is faulty.   If PIM state is down, run the display interface command to check whether the physical state and link state of the interface are both Up.   * If the physical state is not Up, troubleshoot faults to resolve the physical state Down problem. * If the link state is not Up, troubleshoot faults to resolve the link state Down problem. |
| PIM offer-interval | Interval at which Bidirectional Protocol Independent Multicast (BIDIR-PIM) Offer messages are sent on the interface. |
| PIM election-robust-count | Designated forwarder (DF) election robustness variable of the interface. |
| PIM backoff-interval | Interval at which backoff messages are sent. |
| PIM ignore assert | Enable/disable the function of ignoring the ASSERT state of PIM. |
| PIM ecmp-priority | ECMP priority. |
| Number of routers on link not using DR priority | Number of devices that do not have DR priorities on the network segment where the interface resides. |
| Number of routers on link not using LAN delay | Number of devices that do not delay message transmission on the network segment where the interface resides. |
| Number of routers on link not using neighbor tracking | Number of devices that do not have neighbor tracking enabled on the network segment where the interface resides. |
| ACL of PIM neighbor policy | Neighbor filtering policy configured on the interface. |
| ACL of PIM join policy | Join message filtering policy configured on the interface. |
| ACL of PIM ASM join policy | Any-source multicast (ASM) Join message filtering policy configured on the interface. |
| ACL of PIM SSM join policy | Source-specific multicast (SSM) Join message filtering policy configured on the interface. |
| Interface | Interface name. |
| State | Interface state:   * up: The interface is Up. * down: The physical link of the interface is faulty. |
| NbrCnt | Number of PIM neighbor relationships that the interface has established. |
| HelloInt | Interval at which Hello messages are sent on the interface. |
| DR-Pri | DR priority. |
| DR-Address | DR address. |
| ECMP-Pri | ECMP priority. |
| VPN-Instance | Instance to which the PIM interface belongs. |
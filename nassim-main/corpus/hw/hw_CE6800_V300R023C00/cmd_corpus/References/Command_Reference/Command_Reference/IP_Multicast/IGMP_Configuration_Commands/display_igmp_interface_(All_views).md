display igmp interface (All views)
==================================

display igmp interface (All views)

Function
--------



The **display igmp interface** command displays IGMP configurations and state information on interfaces.




Format
------

**display igmp interface** { **up** | **down** } [ **verbose** ]

**display igmp** { **vpn-instance** *vpn-instance-name* | **all-instance** } **interface** { **up** | **down** } [ **verbose** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **up** | Displays IGMP configurations and state information on interfaces with the IP protocol status being Up and the IGMP protocol status being active. | - |
| **down** | Displays IGMP configurations and state information on interfaces with the IP protocol status being Down and the IGMP protocol status being inactive. | - |
| **verbose** | Displays detailed IGMP configurations and state information. | - |
| **vpn-instance** *vpn-instance-name* | Displays IGMP configurations and state information in a specified VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **all-instance** | Displays IGMP configurations and state information in all instances. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

To check IGMP interface's status or locate faults in IGMP interfaces, run the **display igmp interface** command to view IGMP configurations and state information on interfaces.

**Precautions**

Before using the **display igmp interface** command, note the following:If neither vpn-instance nor all-instance is specified, the command displays IGMP configurations and state information in the public network instance.If up is specified, the command displays IGMP configurations and state information on all interfaces on which the IGMP protocol status is active.If down is specified, the command displays IGMP configurations and state information on all interfaces on which the IGMP protocol status is inactive.If verbose is specified, the command displays detailed IGMP configurations and state information.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display detailed IGMP configurations and state information on interfaces in the public network instance.
```
<HUAWEI> display igmp interface verbose
Interface information of VPN instance: public net
 Vlanif10(10.1.10.1):
   IGMP is enabled
   Current IGMP version is 3
   IGMP state: up
   IGMP group policy: none
   IGMP limit: -
   Query interval for IGMP (negotiated): 120 s
   Query interval for IGMP (configured): 120 s
   Other querier timeout for IGMP: 0 s
   Maximum query response time for IGMP: 10 s
   Last member query time: 3 s
   Last member query interval: 1 s
   Startup query interval: 30 s
   Startup query count: 3
   General query timer expiry (hours:minutes:seconds): 00:01:31
   Querier for IGMP: 10.1.10.1 (this router)
   IGMP activity: 2905 joins, 0 leaves
   Robustness (negotiated): 3
   Robustness (configured): 3
   Require Router Alert: disabled
   Send Router Alert: enabled
   Ip-source-policy: disabled
   Query Ip-source-policy: disabled
   Prompt Leave: disabled
   SSM-Mapping: disabled
   Explicit-tracking: enabled
   Startup query timer expiry: off
   Other querier present timer expiry: off
  Total 1 IGMP Group reported

```

**Table 1** Description of the **display igmp interface (All views)** command output
| Item | Description |
| --- | --- |
| Interface information of VPN instance | VPN instance to which the interface information belongs. |
| IGMP is enabled | Indicates that IGMP has been enabled on an interface using the igmp enable command. |
| IGMP state | IGMP state on an interface.  up: IGMP is in the active state.  down: IGMP is in the inactive state. |
| IGMP group policy | Number of an ACL used in an IGMP group policy to control the number of groups that an interface can join.  The ACL is applied to the IGMP group policy using the igmp group-policy command.  If the displayed value in the IGMP group policy field is not none, the groups that the hosts can join have been specified, and IGMP filters Report messages of hosts according to the ACL. If the multicast group G is not included in the groups specified in the ACL, modify or delete the ACL to ensure that members of G can be served. |
| IGMP limit | Maximum number of IGMP entries. |
| IGMP activity | Statistics about active group memberships on an interface.  joins: indicates the number of IGMP groups that the interface has joined. When the interface joins a new group, the value increases by 1. When the interface leaves a group, the value remains unchanged.  leaves: indicates the number of groups that the interface leaves. When the interface leaves a group, the value increases by 1. |
| Current IGMP version | IGMP version configured using the igmp version command. |
| Query Ip-source-policy | Source address-based filtering policy for received IGMP Query messages.  The policy is configured using the igmp query ip-source-policy command. |
| Query interval for IGMP (negotiated) | Interval negotiated by non-queriers for sending Query messages, in seconds The negotiated value is supported by IGMPv3 only. |
| Query interval for IGMP (configured) | Configured interval at which an interface sends IGMP Query messages, in seconds. The value is specified using the igmp timer query command. |
| Other querier timeout for IGMP | Keepalive time of other IGMP queriers.  The value decreases by one per second. The timeout period is specified using the igmp timer other-querier-present command. The value of this item is 0 on the interface that acts as a querier. |
| Other querier present timer expiry | Status of the timer that controls when an existing querier expires and an interface participates in querier election.  off: indicates that an interface considers itself as a querier and no other queriers exist.  on: indicates that an interface does function as a querier and other queriers exist. |
| Maximum query response time for IGMP | Maximum response time carried by an IGMP Query message, in seconds.  The value is specified using the igmp max-response-time command. After a host receives an IGMP Query message for a group, the host starts a timer for the group that it joins. The value of the timer ranges from 0 to the maximum response time. When the timer expires, the host sends Report messages. |
| Last member query time | Last-member query time.  Last-member query time = Interval for sending last-member query messages x Robustness variable. The last-member query time is not defined in IGMPv1. |
| Last member query interval | Interval for sending last-member query messages, in seconds.  The interval for sending last-member query messages is not defined in IGMPv1. |
| Startup query interval | Interval for an interface to send Query messages when it functions as a querier after startup, in seconds.  The value is specified using the igmp timer query command. The startup query interval is used to quickly elect a querier. The value is 1/4 of the interval at which IGMP general query messages are sent. In IGMPv1, the startup query interval is not defined. |
| Startup query count | Number of times that an interface that starts as a querier sends Query messages.  The value is specified using the igmp robust-count command. The startup query count is not defined in IGMPv1. |
| Startup query timer expiry | Status of the timer used to control the interval at which an interface that starts as the querier sends Query messages:  off: indicates that the interface sends Query messages immediately after startup.  on: indicates that the interface does not send Query messages immediately after startup. |
| General query timer expiry (hours:minutes:seconds) | Timeout period of a general query timer. The value is specified using the igmp timer query command. |
| Querier for IGMP | IGMP querier In IGMPv1, a querier is selected based on the multicast routing protocol; in IGMPv2, the router with the lowest IP address acts as the querier on a shared network segment. |
| Robustness (negotiated) | Robustness variable negotiated by non-queriers.  The negotiated value is supported by IGMPv3 only. |
| Robustness (configured) | Robustness variable configured on an interface.  The value is specified using the igmp robust-count command. |
| Require Router Alert | Whether to discard IGMP messages that do not carry the Router-Alert option.  The function is configured using the igmp require-router-alert command. |
| Send Router Alert | Whether to add the Router-Alert option in IGMP packets to be sent.  The function is configured using the igmp send-router-alert command. |
| Prompt Leave | Whether prompt leave is enabled. The function is configured using the igmp prompt-leave command. |
| Vlanif10(10.1.10.1) | Type, number, and IP address of an interface. |
| Ip-source-policy | Source address-based filtering policy for received IGMP Report or Leave messages.  The policy is configured using the igmp ip-source-policy command. |
| SSM-Mapping | Whether SSM mapping is enabled. The function is configured using the igmp ssm-mapping enable command. |
display mld interface (All views)
=================================

display mld interface (All views)

Function
--------



The **display mld interface** command displays Multicast Listener Discovery (MLD) parameters set on an interface.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display mld interface** { **up** | **down** } [ **verbose** ]

**display mld** { **vpn-instance** *vpn-instance-name* | **all-instance** } **interface** { **up** | **down** } [ **verbose** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **up** | Displays information about the interface with the IP protocol status being Up and the MLD protocol status being Active. | - |
| **down** | Displays information about the interface with the IP protocol status being Down and the MLD protocol status being Inactive. | - |
| **verbose** | Displays detailed information about all MLD interfaces or a specified MLD interface. | - |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **all-instance** | Specifies all VPN instance. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

When running the **display mld interface** command, note the following points:

* If up is specified, the parameters of all the interfaces with the MLD protocol status being Active are displayed.
* If down is specified, the parameters of all interfaces with the MLD protocol status being Inactive are displayed.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display parameters of all MLD interfaces with MLD in the Active state.
```
<HUAWEI> system-view
[~HUAWEI] display mld interface up verbose
Interface information of VPN-Instance: public net
 100GE1/0/1.1(FE80::3AA3:47FF:FE31:409):
   MLD is enabled
   Current MLD version is 2
   MLD state: up
   MLD group policy: none
   Value of query interval for MLD (negotiated): 125 s
   Value of query interval for MLD (configured): 125 s
   Value of other querier timeout for MLD: 0 s
   Value of maximum query response time for MLD: 10 s
   Value of last listener query time: 2 s
   Value of last listener query interval: 1 s
   Value of startup query interval: 31 s
   Value of startup query count: 2
   General query timer expiry (hours:minutes:seconds): 00:01:16
   Querier for MLD: FE80::3AA3:47FF:FE31:409 (this router)
   MLD activity: 3 joins, 0 dones
   Robustness (negotiated): 2
   Robustness (configured): 2
   Require-router-alert: disabled
   Send-router-alert: enabled
   Ip-source-policy: disabled
   Query Ip-source-policy: disabled
   Prompt-leave: disabled
   SSM-Mapping: disabled
   Startup-query-timer-expiry: off
   Other-querier-present-timer-expiry: off
   MLD ipsec: disabled
  Total 3 MLD Groups reported

```

**Table 1** Description of the **display mld interface (All views)** command output
| Item | Description |
| --- | --- |
| Interface information of VPN-Instance | VPN instance to which the interface whose information is to be displayed belongs. |
| MLD state | Indicates that status of an MLD interface.   * up: indicates that the MLD status is Active. * down: indicates that the MLD status is Inactive. |
| MLD group policy | Indicates the number of an ACL used in an MLD group policy.  If the displayed value in the MLD group policy field is not none, the groups that the hosts can join have been specified, and MLD filters Report messages of hosts according to the ACL. If the multicast group G is not included in the groups specified in the ACL, modify or delete the ACL to ensure that members of G can be served. |
| MLD activity | Indicates the statistics of MLD activity (join or leave). |
| MLD ipsec | Whether IP Security (IPSec) authentication is configured for MLD messages. |
| Current MLD version is 2 | Indicates that the version of MLD running on the current interface is 2. |
| Value of query interval for MLD (negotiated) | Indicates the negotiated interval for sending MLD Query messages, in seconds. |
| Value of query interval for MLD (configured) | Indicates the set interval for sending MLD Query messages, in seconds. |
| Value of other querier timeout for MLD | Indicates the timeout period of an MLD querier, in seconds. |
| Value of maximum query response time for MLD | Indicates the maximum query response time carried by an MLD Query message, in seconds. |
| Value of last listener query time | Indicates the last-listener query time, in seconds. The formula used to calculate the last-listener query time is: Last-member query time = Interval for sending last-member query messages x Robustness variable. |
| Value of last listener query interval | Indicates the interval for sending last-listener query messages (the messages are group-specific query messages), in seconds. |
| Value of startup query interval | Indicates the interval for sending Query messages when a querier starts, in seconds. |
| Value of startup query count | Indicates the number of times for sending Query messages when a querier starts. |
| General query timer expiry | Indicates the timeout period of a general query timer. |
| Querier for MLD | Indicates the link-local address of an MLD querier. |
| Robustness (configured) | Indicates the robustness variable of a querier. |
| Robustness (negotiated) | Robustness variable of the querier that is actually adopted by the system after negotiation. |
| Query Ip-source-policy | Indicates the source address-based filtering policy for received MLD Query messages. The policy can be configured using the mld query ip-source-policy command. |
| 100GE1/0/1.1(FE80::3AA3:47FF:FE31:409) | Link-local address of an interface. |
| Require-router-alert | Indicates whether to discard MLD packets without the Router-Alert option:   * disabled: indicates that MLD packets without the Router-Alert option can be accepted and processed. * enabled: indicates that MLD packets without the Router-Alert option are ignored. |
| Send-router-alert | Indicates whether MLD packets to be sent carry the Router-Alert option. |
| Ip-source-policy | Indicates the source address-based filtering policy for received MLD Report or Done messages. The policy can be configured using the mld ip-source-policy command. |
| Prompt-leave | Indicates whether prompt leave is enabled. |
| SSM-Mapping | Indicates whether Source-Specific Multicast (SSM) mapping is enabled. |
| Startup-query-timer-expiry | Indicates the status of the timer used to control the interval at which an interface starts as the querier sends Query messages:   * off: indicates that the interface sends Query messages immediately after startup. * on: indicates that the interface does not send Query messages immediately after startup. |
| Other-querier-present-timer-expiry | Indicates the status of the timer identifying whether another querier is present:   * off: indicates that an interface considers itself as a querier and that no other queriers exist. * on: indicates that an interface does function as a querier and other queriers exist. |
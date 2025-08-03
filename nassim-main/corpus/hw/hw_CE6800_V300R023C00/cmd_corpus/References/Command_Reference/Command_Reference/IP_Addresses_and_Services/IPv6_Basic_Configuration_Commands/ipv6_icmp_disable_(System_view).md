ipv6 icmp disable (System view)
===============================

ipv6 icmp disable (System view)

Function
--------



The **ipv6 icmp disable** command disables the system from sending or receiving ICMPv6 messages.

The **undo ipv6 icmp disable** command enables the system to send or receive ICMPv6 messages.

The **clear ipv6 icmp** command clears the configuration records of the ipv6 icmp disable and undo ipv6 icmp disable commands.



By default, a device sends or receives well-known ICMPv6 messages not other types of ICMPv6 messages.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 icmp** { **echo-reply** | **echo** | **err-header-field** | **hop-limit-exceeded** | **neighbor-advertisement** | **neighbor-solicitation** | **packet-too-big** | **redirect** | **router-advertisement** | **router-solicitation** | **multicast-listener-report-v2** | **multicast-listener-query** | **multicast-listener-report** | **multicast-listener-done** } { **send** | **receive** } **disable**

**ipv6 icmp** { **frag-time-exceeded** | **host-admin-prohib** | **unknown-next-hdr** } { **send** | **receive** } **disable**

**ipv6 icmp unknown-ipv6-opt** { **send** | **receive** } **disable**

**ipv6 icmp host-unreachable** { **send** | **receive** } **disable**

**ipv6 icmp port-unreachable** { **send** | **receive** } **disable**

**ipv6 icmp** *icmpv6Type* *icmpv6Code* { **send** | **receive** } **disable**

**ipv6 icmp all-famous** { **send** | **receive** } **disable**

**clear ipv6 icmp** { **frag-time-exceeded** | **host-admin-prohib** | **unknown-next-hdr** } { **send** | **receive** }

**clear ipv6 icmp** { **echo-reply** | **echo** | **err-header-field** | **hop-limit-exceeded** | **neighbor-advertisement** | **neighbor-solicitation** | **packet-too-big** | **redirect** | **router-advertisement** | **router-solicitation** | **multicast-listener-report-v2** | **multicast-listener-query** | **multicast-listener-report** | **multicast-listener-done** } { **send** | **receive** }

**clear ipv6 icmp all-famous** { **send** | **receive** }

**clear ipv6 icmp port-unreachable** { **send** | **receive** }

**clear ipv6 icmp host-unreachable** { **send** | **receive** }

**clear ipv6 icmp unknown-ipv6-opt** { **send** | **receive** }

**ipv6 icmp network-unreachable** { **send** | **receive** } **disable**

**clear ipv6 icmp network-unreachable** { **send** | **receive** }

**undo ipv6 icmp** { **echo-reply** | **echo** | **err-header-field** | **hop-limit-exceeded** | **neighbor-advertisement** | **neighbor-solicitation** | **packet-too-big** | **redirect** | **router-advertisement** | **router-solicitation** | **multicast-listener-report-v2** | **multicast-listener-query** | **multicast-listener-report** | **multicast-listener-done** } { **send** | **receive** } **disable**

**undo ipv6 icmp** { **frag-time-exceeded** | **host-admin-prohib** | **unknown-next-hdr** } { **send** | **receive** } **disable**

**undo ipv6 icmp unknown-ipv6-opt** { **send** | **receive** } **disable**

**undo ipv6 icmp host-unreachable** { **send** | **receive** } **disable**

**undo ipv6 icmp port-unreachable** { **send** | **receive** } **disable**

**undo ipv6 icmp** *icmpv6Type* *icmpv6Code* { **send** | **receive** } **disable**

**undo ipv6 icmp all-famous** { **send** | **receive** } **disable**

**undo ipv6 icmp network-unreachable** { **send** | **receive** } **disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **echo-reply** | Indicates an Echo Reply message. | - |
| **echo** | Indicates an Echo message. | - |
| **err-header-field** | Indicates a Parameter Problem message generated in response to an IPv6 packet with erroneous header field. | - |
| **hop-limit-exceeded** | Indicates a Hop Limit Exceeded message. | - |
| **neighbor-advertisement** | Indicates a Neighbor Advertisement message. | - |
| **neighbor-solicitation** | Indicates a Neighbor Solicitation message. | - |
| **packet-too-big** | Indicates a Packet Too Big message. | - |
| **redirect** | Indicates a Redirect message. | - |
| **router-advertisement** | Indicates a Router Advertisement message. | - |
| **router-solicitation** | Indicates a Router Solicitation message. | - |
| **multicast-listener-report-v2** | Indicates a Version 2 Multicast Listener Report message. | - |
| **multicast-listener-query** | Indicates a Multicast Listener Query message. | - |
| **multicast-listener-report** | Indicates a Multicast Listener Report message. | - |
| **multicast-listener-done** | Indicates a Multicast Listener Done message. | - |
| **send** | Indicates the function of sending ICMPv6 packets of a specified type. | - |
| **receive** | Indicates the function of receiving ICMPv6 packets of a specified type. | - |
| **frag-time-exceeded** | Indicates a Fragment Reassembly Time Exceeded message. | - |
| **host-admin-prohib** | Indicates a Destination Host Administratively Prohibited message. | - |
| **unknown-next-hdr** | Indicates a Parameter Problem message generated in response to an IPv6 packet with an unrecognized next header type. | - |
| **unknown-ipv6-opt** | Indicates a Parameter Problem message generated in response to an IPv6 packet with an unrecognized IPv6 option. | - |
| **host-unreachable** | Indicates a Host Unreachable message. | - |
| **port-unreachable** | Indicates a Port Unreachable message. | - |
| *icmpv6Type* | Specifies the type of an ICMPv6 message. | The value is an integer ranging from 0 to 255. |
| *icmpv6Code* | Specifies the code of an ICMPv6 message. | The value is an integer ranging from 0 to 255. |
| **all-famous** | Indicates well-known ICMPv6 messages, including:   * Sent well-known ICMPv6 messages: echo, echo-reply, hop-limit-exceeded, neighbor-advertisement, neighbor-solicitation, network-unreachable, packet-too-big, redirect, router-advertisement, router-solicitation, multicast-listener-done, multicast-listener-query, multicast-listener-report, multicast-listener-report-v2, host-unreachable, and port-unreachable. * Received well-known ICMPv6 messages: echo, echo-reply, hop-limit-exceeded, neighbor-advertisement, neighbor-solicitation, packet-too-big, router-advertisement, router-solicitation, multicast-listener-done, multicast-listener-query, multicast-listener-report, multicast-listener-report-v2, and port-unreachable. | - |
| **network-unreachable** | Indicates a Network Unreachable message. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On a normal network, a device can correctly send or receive ICMPv6 messages; however, when network traffic load is heavy, host unreachable or port unreachable events frequently occur and ME devices need to send a large number of ICMPv6 messages, which burdens the network and degrades the performance of the ME devices. In addition, attackers usually use ICMPv6 error messages to probe the internal network topology illegitimately.To improve network performance and security, run the ipv6 icmp disable command to disable routing devices from sending or receiving ICMPv6 messages of specified types, such as Echo Reply, Host Unreachable, and Port Unreachable messages. If all-famous or ND-related parameters are specified, exercise caution when running this command. Otherwise, IPv6 unicast services may be affected.

* all-famous: disables the system from sending or receiving all well-known ICMPv6 messages.
* ND-related parameters: neighbor-advertisement, neighbor-solicitation, router-advertisement, router-solicitation, and redirect.

**Precautions**



When the network is in good performance, the **undo ipv6 icmp receive disable** command can be used to enable the system to accept ICMPv6 messages.When the network becomes normal again, you can run the **undo ipv6 icmp send disable** command to re-enable the system to process ICMPv6 messages.




Example
-------

# Disable the system from accepting ICMPv6 host-unreachable messages.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 icmp host-unreachable receive disable

```

# Disable the system from sending ICMPv6 Host-Unreachable messages.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 icmp host-unreachable send disable

```

# Enable the system to send ICMPv6 messages.
```
<HUAWEI> system-view
[~HUAWEI] undo ipv6 icmp all-famous send disable

```

# Enable the system to accept all ICMPv6 messages.
```
<HUAWEI> system-view
[~HUAWEI] undo ipv6 icmp all-famous receive disable

```
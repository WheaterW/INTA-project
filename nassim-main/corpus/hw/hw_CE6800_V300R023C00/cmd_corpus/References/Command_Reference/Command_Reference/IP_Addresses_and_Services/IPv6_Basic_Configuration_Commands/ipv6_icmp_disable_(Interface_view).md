ipv6 icmp disable (Interface view)
==================================

ipv6 icmp disable (Interface view)

Function
--------

The **ipv6 icmp send disable** command disables an interface from sending ICMPv6 messages.

The **undo ipv6 icmp send disable** command enables an interface to send ICMPv6 messages.

The **clear ipv6 icmp send disable** command clears the configurations of the ipv6 icmp send disable and undo ipv6 icmp send disable commands.

By default, an interface is enabled to send ICMPv6 messages.

![](../public_sys-resources/note_3.0-en-us.png)
 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.





Format
------

**ipv6 icmp hop-limit-exceeded send disable**

**ipv6 icmp host-unreachable send disable**

**ipv6 icmp port-unreachable send disable**

**clear ipv6 icmp port-unreachable send disable**

**clear ipv6 icmp host-unreachable send disable**

**clear ipv6 icmp hop-limit-exceeded send disable**

**undo ipv6 icmp hop-limit-exceeded send disable**

**undo ipv6 icmp host-unreachable send disable**

**undo ipv6 icmp port-unreachable send disable**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **host-unreachable** | Indicates Host Unreachable messages. | - |
| **port-unreachable** | Indicates a Port Unreachable message. | - |
| **clear** | Deletes statistics. | - |
| **hop-limit-exceeded** | Indicates an ICMPv6 Hop Limit Exceeded message. | - |




Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

On a normal network, a device can correctly send or receive ICMPv6 messages; however, when network traffic load is heavy, host unreachable or port unreachable events frequently occur and devices need to send a large number of ICMPv6 messages, which burdens the network and degrades the performance of the devices. In addition, attackers usually use ICMPv6 error messages to probe the internal network topology illegitimately.

To improve network performance and security, you need to run the
**ipv6 icmp send disable** command to disable an interface from sending ICMPv6 messages.If you want to restore the default configuration and the
**display this** command output does not contain the ipv6 icmp send disable or
**undo ipv6 icmp send disable** command configuration, run the
**clear ipv6 icmp send disable** command.

**Configuration Impact**

After an interface is disabled from sending ICMPv6 messages, the interface counts only the number of discarded messages instead of the number of sent messages.

**Precautions**

When the network becomes normal again, you can run the **undo ipv6 icmp send disable** command to re-enable an interface to process ICMPv6 messages.



Example
-------

# Clear the configuration of sending ICMPv6 Hop Limit Exceeded messages on an interface.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] clear ipv6 icmp hop-limit-exceeded send disable

```

# Disable an interface from sending ICMPv6 Hop Limit Exceeded messages.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ipv6 icmp hop-limit-exceeded send disable

```

# Disable an interface from sending ICMPv6 Host Unreachable messages.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ipv6 icmp host-unreachable send disable

```

# Enable an interface to send ICMPv6 Port Unreachable messages.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] undo ipv6 icmp port-unreachable send disable

```
ipv6 nd ra prefix default no-advertise
======================================

ipv6 nd ra prefix default no-advertise

Function
--------



The **ipv6 nd ra prefix default no-advertise** command configures RA messages not to carry the prefix generated based on an interface IPv6 address.

The **undo ipv6 nd ra prefix default no-advertise** command restores the default configuration.



By default, RA messages contain only the prefix specified through the ipv6 address command.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd ra prefix default no-advertise**

**undo ipv6 nd ra prefix default no-advertise**


Parameters
----------

None

Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If the **ipv6 nd ra prefix** command is run to configure a prefix, the device advertises both the address prefix configured using the **ipv6 nd ra prefix** command and that using the **ipv6 address** command.By default, RA messages do not carry the default prefix generated based on the interface IPv6 address. If a user does not want the RA message to carry the default address prefix, run the **ipv6 nd ra prefix default no-advertise** command.

**Prerequisites**

IPv6 has been enabled on the involved interface using the **ipv6 enable** command.

**Configuration Impact**

After a host receives the RA message with the prefix configured through the **ipv6 nd ra prefix default no-advertise** command, the host updates the local prefix information.

**Precautions**

The prefix configured through the **ipv6 nd ra prefix default no-advertise** command cannot be fe80:: (prefix of a link-local address), ff00:: (prefix of a multicast address), or prefix of an unspecified address. It neither can be the prefix that has been used by another interface (including the interface address prefix and prefix carried in RA messages).


Example
-------

# Configure the 100GE 1/0/1 to not carry the default address prefix in RA messages.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ipv6 nd ra prefix default no-advertise

```
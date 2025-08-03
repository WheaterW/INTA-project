ipv6 enable
===========

ipv6 enable

Function
--------



The **ipv6 enable** command enables the IPv6 capability on an interface.

The **undo ipv6 enable** command disables the IPv6 capability on an interface.



By default, the IPv6 capability is disabled on an interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 enable**

**undo ipv6 enable**


Parameters
----------

None

Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can perform other IPv6 configurations on an interface only when IPv6 is enabled in the interface view.

**Configuration Impact**

After the IPv6 function is disabled on the interface, the IPv6 addresses of the interface are deleted and IPv6-related commands no longer can be configured on the interface.

**Follow-up Procedure**

Perform IPv6-related configurations, including configuring IPv6 addresses and ND-related parameters (M flag, O flag, RA halt flag, interval for sending RA messages, lifetime of RA messages, interval for sending NS messages, DAD times, time period during which the IPv6 neighbor keeps reachable, prefix carried in the RA message, and static ND entries).

**Precautions**

After you disable IPv6 on an interface, IPv6-related configurations are removed. For example, IS-IS IPv6 and RIPng are disabled on the interface, that is, the **isis ipv6 enable** and **ripng enable** commands become ineffective.


Example
-------

# Enable the IPv6 capability on 100GE 1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable

```
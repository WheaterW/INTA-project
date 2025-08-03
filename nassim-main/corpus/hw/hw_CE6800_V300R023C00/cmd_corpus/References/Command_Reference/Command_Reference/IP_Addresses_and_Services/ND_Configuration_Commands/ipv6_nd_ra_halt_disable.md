ipv6 nd ra halt disable
=======================

ipv6 nd ra halt disable

Function
--------



The **ipv6 nd ra halt disable** command enable the router to send RA messages.

The **undo ipv6 nd ra halt disable** command suppresses the router from sending all RA messages.



By default, the router is suppressed from sending all RA messages.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd ra halt disable**

**undo ipv6 nd ra halt disable**


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

When a router is connected to a host, it needs to periodically send RA messages to the host. An RA message carries both the IPv6 prefix and flag of stateful address autoconfiguration. You can run the **ipv6 nd ra halt disable** command to enable a router to send RA messages.When a router is connected to a router, that is, there is no host on the network, sending RA messages is not required. You are then recommended to keep SA message suppression enabled.

**Prerequisites**



IPv6 has been enabled on the involved interface using the **ipv6 enable** command.



**Configuration Impact**



After the **undo ipv6 nd ra halt disable** command is run to suppress a router from sending all RA messages, the router no longer sends all RA messages. In such a case, the hosts on the network cannot receive information about updated IPv6 prefixes periodically.



**Precautions**



By default, sending all RA messages is suppressed. You can run the **display icmpv6 statistics** command to check whether a local router has sent RA messages.




Example
-------

# Suppress a router from sending all RA messages on 100GE 1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] undo ipv6 nd ra halt disable

```
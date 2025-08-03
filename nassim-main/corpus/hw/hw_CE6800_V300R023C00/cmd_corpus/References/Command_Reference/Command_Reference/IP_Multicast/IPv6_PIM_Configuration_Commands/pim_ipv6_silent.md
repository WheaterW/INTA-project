pim ipv6 silent
===============

pim ipv6 silent

Function
--------



The **pim ipv6 silent** command enables the PIM silent function on a specified interface.

The **undo pim ipv6 silent** command disables the PIM silent function on a specified interface.



By default, the PIM silent function is not enabled on an interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**pim ipv6 silent**

**undo pim ipv6 silent**


Parameters
----------

None

Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

At the access layer, if PIM is enabled on a router interface directly connected to a host network segment, the interface can set up PIM neighbor relationships and process various PIM protocol packets. If attackers send a large number of PIM IPv6 Hello messages, the router may be crashed.To address this problem, enable PIM silent on the interface using the **pim ipv6 silent** command. After PIM silent is enabled on an interface, all PIM packets will be discard by this interface, and all PIM neighbors and PIM state machines will be deleted for this interface. The interface automatically becomes a static designated router (DR). MLD functions, however, are not affected on the interface.


Example
-------

# Enable PIM silent on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] pim ipv6 silent

```
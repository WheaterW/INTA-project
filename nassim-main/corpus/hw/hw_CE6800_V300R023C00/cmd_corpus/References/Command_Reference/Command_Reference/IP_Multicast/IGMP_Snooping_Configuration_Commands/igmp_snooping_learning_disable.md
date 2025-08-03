igmp snooping learning disable
==============================

igmp snooping learning disable

Function
--------



The **igmp snooping learning disable** command disables an interface from dynamically learning forwarding entries.

The **undo igmp snooping learning disable** command enables an interface to dynamically learn forwarding entries.



By default, an interface is enabled to dynamically learn forwarding entries.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**igmp snooping learning disable**

**undo igmp snooping learning disable**


Parameters
----------

None

Views
-----

100GE Layer 2 sub-interface view,200GE Layer 2 sub-interface view,400GE Layer 2 sub-interface view,50GE Layer 2 sub-interface view,Eth-Trunk Layer 2 sub-interface view,Layer 2 sub-interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

After you run the igmp snooping learning disable command to enable an interface dynamically to learn forwarding entries, the interface can both be added to a multicast group statically and learn forwarding entries dynamically based on received IGMP Report messages. After the interface is disabled from dynamically learning forwarding entries, you can only add the interface to a multicast group statically.If the igmp snooping learning disable command is run more than once, all configurations take effect.


Example
-------

# Disable Layer 2 sub-interface 100GE 1/0/1.1 in bridge-domain 10 from dynamically learning forwarding entries.
```
<HUAWEI> system-view
[~HUAWEI] igmp snooping enable
[*HUAWEI] bridge-domain 10
[*HUAWEI-bd10] igmp snooping enable
[*HUAWEI-bd10] quit
[*HUAWEI] interface 100GE 1/0/1.1 mode l2
[*HUAWEI-100GE1/0/1.1] portswitch
[*HUAWEI-100GE1/0/1.1] encapsulation dot1q vid 2
[*HUAWEI-100GE1/0/1.1] bridge-domain 10
[*HUAWEI-100GE1/0/1.1] undo igmp snooping learning disable

```
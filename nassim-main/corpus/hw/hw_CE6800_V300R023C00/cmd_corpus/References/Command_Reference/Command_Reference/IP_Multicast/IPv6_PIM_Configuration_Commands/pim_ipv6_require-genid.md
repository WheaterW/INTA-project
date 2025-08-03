pim ipv6 require-genid
======================

pim ipv6 require-genid

Function
--------



The **pim ipv6 require-genid** command configures a PIM interface to reject a Hello message without a generation ID.

The **undo pim ipv6 require-genid** command restores the default configuration.



By default, a PIM interface permits a Hello message without a generation ID.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**pim ipv6 require-genid**

**undo pim ipv6 require-genid**


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

After PIM-SM is enabled on an interface of a Router, the Router generates a random number as the generation ID for Hello messages. Each time the Router status changes, the Router generates a new generation ID.If a Router receives a Hello message that contains a changed generation ID from the same PIM neighbor, the Router considers that the PIM neighbor status has changed. In this manner, the Router can detect status changes of its neighbors. To configure a PIM interface to reject Hello messages without a generation ID, run the pim ipv6 require-genid command, improving communication security.


Example
-------

# Configure 100GE1/0/1 to reject the Hello messages without the Generation ID option.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] pim ipv6 require-genid

```
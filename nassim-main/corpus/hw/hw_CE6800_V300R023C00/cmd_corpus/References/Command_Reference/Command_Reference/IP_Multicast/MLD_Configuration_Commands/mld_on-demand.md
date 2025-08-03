mld on-demand
=============

mld on-demand

Function
--------



The **mld on-demand** command configures the Multicast Listener Discovery (MLD) group that an interface dynamically joins not to time out.

The **undo mld on-demand** command restores the default configuration.



By default, the records about dynamic join to multicast groups on an interface age periodically.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mld on-demand**

**undo mld on-demand**


Parameters
----------

None

Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,Loopback interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

MLD on-demand is used on a multicast device directly connected to an access device, not user hosts. MLD on-demand reduces packet exchanges between the access device and multicast device and reduces the load of these devices.


Example
-------

# Configure the MLD groups that 100GE1/0/1 dynamically joins not to time out.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] mld on-demand

```
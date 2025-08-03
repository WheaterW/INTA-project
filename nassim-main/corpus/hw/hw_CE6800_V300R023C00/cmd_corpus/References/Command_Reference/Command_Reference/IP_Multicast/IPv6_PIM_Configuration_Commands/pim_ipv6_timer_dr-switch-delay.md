pim ipv6 timer dr-switch-delay
==============================

pim ipv6 timer dr-switch-delay

Function
--------



The **pim ipv6 timer dr-switch-delay** command enables the IPv6 PIM designated router (DR) switching delay function and configures a switching delay on an interface.

The **undo pim ipv6 timer dr-switch-delay** command disables IPv6 PIM DR switching delay on an interface.



By default, an IPv6 PIM interface sends Hello messages at an interval of 30 seconds, IPv6 PIM DR switching delay is disabled on an interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**pim ipv6 timer dr-switch-delay** *interval*

**undo pim ipv6 timer dr-switch-delay**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies the IPv6 PIM DR switching delay. | The value is an integer ranging from 10 to 3600, in seconds. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

Without the IPv6 PIM DR switching delay function, when the system triggers a IPv6 PIM DR switchover, the switchover takes effect immediately, and therefore data forwarding will be interrupted during the switchover period. If the network is unstable, frequent switchovers occur, affecting the multicast forwarding performance. To address this issue, run the **pim ipv6 timer dr-switch-delay** command to configure a DR switching delay to implement non-stop service forwarding during the switchover.


Example
-------

# Enable PIM DR switching delay on 100GE1/0/1 and set the delay to 20 seconds.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] pim ipv6 timer dr-switch-delay 20

```
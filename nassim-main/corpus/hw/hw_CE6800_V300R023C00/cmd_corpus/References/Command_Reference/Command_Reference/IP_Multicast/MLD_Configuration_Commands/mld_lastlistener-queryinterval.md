mld lastlistener-queryinterval
==============================

mld lastlistener-queryinterval

Function
--------



The **mld lastlistener-queryinterval** command sets a global interval for sending Multicast Listener Discovery (MLD) last-listener query messages after an MLD querier receives an MLD Done message from a host.

The **undo mld lastlistener-queryinterval** command restores the default value.



By default, the interval for sending MLD last-listener query messages is one second.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mld lastlistener-queryinterval** *interval*

**undo mld lastlistener-queryinterval**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies the interval for sending MLD last-listener query messages. | The value is an integer ranging from 1 to 5, in seconds. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

After receiving an MLD Leave message from a host, the MLD querier immediately starts the Query message timer. If the querier does not receive any Reply message from the host within a specified timer period, the querier determines that the host leaves the MLD group. You can run this command to set a period for the Query message timer.


Example
-------

# Set the interval at which 100GE1/0/1 sends last-listener query messages to 3 seconds.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] mld lastlistener-queryinterval 3

```
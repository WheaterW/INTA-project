lastlistener-queryinterval
==========================

lastlistener-queryinterval

Function
--------



The **lastlistener-queryinterval** command sets a global interval for sending Multicast Listener Discovery (MLD) last-listener query messages after the MLD querier receives an MLD Done message from a host.

The **undo lastlistener-queryinterval** command restores the default value.



By default, the interval for sending MLD last-listener query messages is one second.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**lastlistener-queryinterval** *interval*

**undo lastlistener-queryinterval**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies the interval for sending MLD last-listener query messages. | The value is an integer ranging from 1 to 5, in seconds. |



Views
-----

MLD view,VPN instance MLD view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The function of this command is the same as that of the mld lastlistener-queryinterval command used in the interface view. The system prefers the configuration in the interface view. The configuration in the MLD view is used only when the configuration in the interface view is not done.


Example
-------

# Set the interval for sending MLD last-listener query messages to three seconds.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] mld
[*HUAWEI-mld] lastlistener-queryinterval 3

```
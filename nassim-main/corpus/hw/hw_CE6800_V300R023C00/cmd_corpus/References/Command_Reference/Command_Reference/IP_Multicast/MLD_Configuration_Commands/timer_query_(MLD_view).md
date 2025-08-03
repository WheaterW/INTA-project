timer query (MLD view)
======================

timer query (MLD view)

Function
--------



The **timer query** command sets a global interval for sending Multicast Listener Discovery (MLD) general query messages.

The **undo timer query** command restores the default value.



By default, the interval for sending MLD general query messages is 125 seconds.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**timer query** *interval*

**undo timer query**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Interval for sending MLD general query messages. | The value is an integer that ranges from 1 to 18000, in seconds. |



Views
-----

MLD view,VPN instance MLD view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The function of this command is the same as that of the mld timer query command used in the interface view. The configuration in the MLD view is globally valid, whereas the configuration in the interface view is valid only for the current interface. The system prefers the configuration in the interface view. The configuration in the MLD view is used only when the configuration in the interface view is not done.


Example
-------

# Set the interval for sending MLD general query messages to 200 seconds.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] mld
[*HUAWEI-mld] timer query 200

```
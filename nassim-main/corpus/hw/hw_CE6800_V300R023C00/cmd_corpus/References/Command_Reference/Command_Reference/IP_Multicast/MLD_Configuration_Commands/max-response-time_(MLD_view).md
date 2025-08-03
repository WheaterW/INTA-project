max-response-time (MLD view)
============================

max-response-time (MLD view)

Function
--------



The **max-response-time** command sets a global maximum response time of Multicast Listener Discovery (MLD) Query messages.

The **undo max-response-time** command restores the default value.



By default, the maximum response time for MLD Query messages is 10 seconds.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**max-response-time** *interval*

**undo max-response-time**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies the maximum response time of MLD Query messages. | The value is an integer ranging from 1 to 25, in seconds. |



Views
-----

MLD view,VPN instance MLD view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The function of this command is the same as that of the mld max-response-time command used in the interface view. The system prefers the configuration in the interface view. The configuration in the MLD view is used only when the configuration in the interface view is not done.


Example
-------

# In the MLD view, set the maximum response time of MLD Query messages to 8 seconds.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] mld
[*HUAWEI-mld] max-response-time 8

```
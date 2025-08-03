c-rp advertisement-interval
===========================

c-rp advertisement-interval

Function
--------



The **c-rp advertisement-interval** command sets the interval at which a Candidate-Rendezvous Point (C-RP) sends Advertisement messages.

The **undo c-rp advertisement-interval** command restores the default setting.



By default, a C-RP sends Advertisement messages at an interval of 60s.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**c-rp advertisement-interval** *interval*

**undo c-rp advertisement-interval**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies an interval at which a C-RP sends Advertisement messages. | The value is an integer ranging from 1 to 65535, in seconds. |



Views
-----

IPv6 PIM view,VPN instance IPv6 PIM view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

All C-RPs in a PIM-SM domain send Advertisement messages to the same bootstrap router (BSR). An Advertisement message carries the C-RP address, range of multicast groups that the C-RP serves, and priority of the C-RP. In this manner, the BSR can collect complete RP-set information. To set an interval at which a C-RP sends an Advertisement message, run the c-rp advertisement-interval command.


Example
-------

# In the public network instance, specify 30 seconds as the interval at which a C-RP sends an Advertisement message.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] pim ipv6
[*HUAWEI-pim6] c-rp advertisement-interval 30

```
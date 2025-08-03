c-rp priority
=============

c-rp priority

Function
--------



The **c-rp priority** command globally sets a priority value for candidate-rendezvous points (C-RPs).

The **undo c-rp priority** command restores the default setting.



By default, the global priority value of C-RPs is 192.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**c-rp priority** *priority*

**undo c-rp priority**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *priority* | Specifies a global priority value for C-RPs. A larger value indicates a lower priority. | The value is an integer ranging from 0 to 255. |



Views
-----

IPv6 PIM view,VPN instance IPv6 PIM view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

An RP is elected from C-RPs based on the following rules:

* The C-RP wins if it serves the group address that has the longest mask.
* If group addresses that all C-RPs serve have the same mask length, the C-RP with the highest priority wins (a larger priority value indicates a lower priority).
* If the C-RPs have the same priority, the hash function is started. The C-RP with the greatest calculated value wins.
* If none of the above criteria can determine a winner, the C-RP with the largest address wins.
* To have a C-RP be elected as the RP, run the c-rp priority command to set a lower priority value for the C-RP than those of the other C-RPs.

Example
-------

# In the public network instance, specify 5 as the global priority value for C-RPs.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] pim ipv6
[*HUAWEI-pim6] c-rp priority 5

```
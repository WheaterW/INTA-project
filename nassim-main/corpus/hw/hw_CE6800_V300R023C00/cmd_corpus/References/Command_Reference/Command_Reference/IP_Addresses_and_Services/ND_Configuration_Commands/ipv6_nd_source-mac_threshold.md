ipv6 nd source-mac threshold
============================

ipv6 nd source-mac threshold

Function
--------



The **ipv6 nd source-mac threshold** command sets an attack detection threshold for ND messages with fixed source MAC addresses.

The **undo ipv6 nd source-mac threshold** command restores the default attack detection threshold for ND messages with fixed source MAC addresses.



The default attack detection threshold is 30 for ND messages with fixed source MAC addresses.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd source-mac threshold** *threshold-value*

**undo ipv6 nd source-mac threshold** [ *threshold-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *threshold-value* | Specifies an attack detection threshold for ND messages with fixed source MAC addresses. | The value is an integer ranging from 1 to 5000. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The ND protocol has powerful functions. However, if there is no security mechanism, the ND protocol can be easily used by attackers. The system collects statistics about ND messages sent to the CPU based on the source MAC addresses of the messages. You can run the ipv6 nd source-mac threshold command to set an attack detection threshold for ND messages with fixed source MAC addresses.If the number of ND messages with the same source MAC address received within 5 seconds exceeds a specified threshold, the system considers that an attack occurs and adds the MAC address to an attack entry. Before the attack entry ages out. If a MAC address is added to an ND attack entry, the MAC address is aged out after the aging time expires.


Example
-------

# Set an attack detection threshold for ND messages with fixed source MAC addresses to 50.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 nd source-mac threshold 50

```
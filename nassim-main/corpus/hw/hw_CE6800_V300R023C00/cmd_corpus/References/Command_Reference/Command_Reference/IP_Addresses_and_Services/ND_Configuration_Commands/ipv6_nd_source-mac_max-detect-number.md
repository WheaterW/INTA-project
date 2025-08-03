ipv6 nd source-mac max-detect-number
====================================

ipv6 nd source-mac max-detect-number

Function
--------



The **ipv6 nd source-mac max-detect-number** command sets the maximum number of ND messages with fixed source MAC addresses that can be detected.

The **undo ipv6 nd source-mac max-detect-number** command restores the default maximum number of ND messages with fixed source MAC addresses that can be detected.



By default, a maximum number of 1024 ND messages with fixed source MAC addresses can be detected.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd source-mac max-detect-number** *max-detect-value*

**undo ipv6 nd source-mac max-detect-number** [ *max-detect-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *max-detect-value* | Specifies the maximum number of ND messages with fixed source MAC addresses that can be detected. | The value is an integer ranging from 10 to 2048. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The ND protocol has powerful functions. However, if there is no security mechanism, the ND protocol can be easily used by attackers. The system collects statistics about ND messages sent to the CPU based on the source MAC addresses of the messages. You can run the ipv6 nd source-mac max-detect-number command to set the maximum number of ND messages with fixed source MAC addresses that can be detected, preventing message attacks.


Example
-------

# Set the maximum number of ND messages with fixed source MAC addresses that can be detected to 1500.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 nd source-mac max-detect-number 1500

```
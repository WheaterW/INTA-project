ipv6 nd remote-backup-rate limit
================================

ipv6 nd remote-backup-rate limit

Function
--------



The **ipv6 nd remote-backup-rate limit** command sets the number of neighbor entries synchronized per second through M-LAG.

The **undo ipv6 nd remote-backup-rate limit** command restores the default number of neighbor entries synchronized per second through M-LAG.



By default, the number of neighbor entries that the system can synchronize through M-LAG per second is 2000.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd remote-backup-rate limit** *ratelimit*

**undo ipv6 nd remote-backup-rate limit** *ratelimit*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ratelimit* | Specifies the number of neighbor entries synchronized per second through M-LAG. | It is an integer ranging from 1 to 2000. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

Neighbor entries can be synchronized to the peer device through M-LAG. This command allows you to configure the number of neighbor entries synchronized per second and dynamically adjust the synchronization rate based on the device performance.


Example
-------

# Restore the number of neighbor entries synchronized per second through M-LAG to the default value.
```
<HUAWEI> system-view
[~HUAWEI] undo ipv6 nd remote-backup-rate limit 200

```

# Set the number of neighbor entries synchronized per second through M-LAG.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 nd remote-backup-rate limit 200

```
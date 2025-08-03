arp remote-backup-rate
======================

arp remote-backup-rate

Function
--------



The **arp remote-backup-rate limit** command sets the number of neighbor entries synchronized per second through M-LAG.

The **undo arp remote-backup-rate limit** command restores the default number of neighbor entries synchronized per second through M-LAG.



By default, the number of ARP entries that the system can synchronize through M-LAG per second is 2000.


Format
------

**arp remote-backup-rate limit** *ratelimit*

**undo arp remote-backup-rate limit** [ *ratelimit* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **limit** *ratelimit* | Specifies the number of ARP entries synchronized per second through M-LAG. | The value is an integer ranging from 1 to 2000. The default value is 2000. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

ARP entries can be synchronized to the peer device through M-LAG. This command allows you to configure the number of neighbor entries synchronized per second and dynamically adjust the synchronization rate based on the device performance.

**Precautions**

This operation will modify ARP backup-limit, and may affect CPU usage.


Example
-------

# Set the number of ARP entries per second synchronized through M-LAG.
```
<HUAWEI> system-view
[~HUAWEI] arp remote-backup-rate limit 200

```

# Recovery system can be synchronized by M-LAG by the number of ARP items per second as the default.
```
<HUAWEI> system-view
[~HUAWEI] undo arp remote-backup-rate limit 200

```
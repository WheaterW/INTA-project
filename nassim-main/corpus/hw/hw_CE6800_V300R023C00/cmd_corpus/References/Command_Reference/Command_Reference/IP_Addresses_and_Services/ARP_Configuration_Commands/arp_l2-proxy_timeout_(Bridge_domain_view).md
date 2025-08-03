arp l2-proxy timeout (Bridge domain view)
=========================================

arp l2-proxy timeout (Bridge domain view)

Function
--------



The **arp l2-proxy timeout** command sets the aging time of Address Resolution Protocol (ARP) snooping entries.

The **undo arp l2-proxy timeout** command restores the default aging time of ARP snooping binding entries.



By default, the aging time of ARP snooping binding entries is 900s.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**arp l2-proxy timeout** *expire-time*

**undo arp l2-proxy timeout** [ *expire-time* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *expire-time* | Specifies the aging time of ARP snooping binding entries. | The value is an integer ranging from 1 to 62640, in seconds. |



Views
-----

Bridge domain view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Each ARP snooping binding entry has a life cycle, called aging time. If an ARP snooping binding entry is not updated before its aging time expires, the entry will be deleted.If the device stores a large number of ARP snooping binding entries, the CPU resources are wasted, and ARP snooping binding entries for new users cannot be generated. To resolve this problem, run the **arp l2-proxy timeout** command to set the aging time of ARP snooping binding entries.

**Prerequisites**

Layer 2 proxy ARP has been enabled using the **arp l2-proxy enable** command.


Example
-------

# Set the aging time of BD-based ARP snooping binding entries to 700s.
```
<HUAWEI> system-view
[~HUAWEI] bridge-domain 10
[*HUAWEI-bd10] arp l2-proxy enable
[*HUAWEI-bd10] arp l2-proxy timeout 700

```
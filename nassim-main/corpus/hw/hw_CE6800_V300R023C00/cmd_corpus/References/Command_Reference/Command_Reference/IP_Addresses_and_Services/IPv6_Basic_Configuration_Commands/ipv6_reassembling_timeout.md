ipv6 reassembling timeout
=========================

ipv6 reassembling timeout

Function
--------



The **ipv6 reassembling timeout** command sets a reassembly timeout period for IPv6 fragments.

The **undo ipv6 reassembling timeout** command restores the default reassembly timeout period for IPv6 fragments.



The default reassembly timeout period of IPv6 fragments is 60s.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 reassembling timeout** *interval*

**undo ipv6 reassembling timeout**

**undo ipv6 reassembling timeout** *interval*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | The reassembly timeout period of IPv6 fragments. | The value is an integer ranging from 5 to 120, in seconds. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can set a proper reassembly timeout period for fragments of host packets to be sent to the CPU so that the fragments that have waited for reassembly for a long time are promptly aged. This improves the performance of the routing device and prevents it from being attacked.

**Configuration Impact**

If a long reassembly timeout period is set, a large number of IPv6 fragments are stored on the device, waiting to be reassembled. This consumes resources, reduces device performance, and may cause network attacks. Therefore, you are not recommended to set a long reassembly timeout period


Example
-------

# Set a reassembly timeout period to 20s for IPv6 fragments.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 reassembling timeout 20

```
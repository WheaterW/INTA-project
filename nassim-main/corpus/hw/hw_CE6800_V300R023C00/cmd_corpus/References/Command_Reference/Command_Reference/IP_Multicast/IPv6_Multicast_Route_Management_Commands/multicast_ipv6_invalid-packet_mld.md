multicast ipv6 invalid-packet mld
=================================

multicast ipv6 invalid-packet mld

Function
--------



The **multicast ipv6 invalid-packet mld** command sets the maximum number of invalid IPv6 multicast protocol packets that can be stored on a device.

The **undo multicast ipv6 invalid-packet mld** command deletes the set maximum number of invalid IPv6 multicast protocol packets that can be stored on a device.



By default, a device can save a maximum of 10 invalid packets for each specific multicast protocol.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**multicast ipv6 invalid-packet mld max-count** *max-number*

**undo multicast ipv6 invalid-packet mld**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **max-count** *max-number* | Sets the maximum number of invalid IPv6 multicast protocol packets that can be stored on a device. | The value is an integer ranging from 1 to 100. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If multicast entries fail to be generated or peer relationships fail to be set up, you can enable a device to store invalid IPv6 multicast protocol packets and run related commands to view statistics and details of the invalid IPv6 multicast protocol packets. Based on the command output, you can locate and rectify faults.

**Prerequisites**

You must run the multicast ipv6 routing-enable command to enable the multicast function before using the command.


Example
-------

# Set the maximum number of invalid MLD messages that can be stored on a device to 20.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] multicast ipv6 invalid-packet mld max-count 20

```
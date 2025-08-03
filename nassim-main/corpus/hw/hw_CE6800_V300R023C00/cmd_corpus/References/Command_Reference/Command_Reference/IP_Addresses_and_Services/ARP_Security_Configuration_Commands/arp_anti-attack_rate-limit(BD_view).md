arp anti-attack rate-limit(BD view)
===================================

arp anti-attack rate-limit(BD view)

Function
--------



The **arp anti-attack rate-limit** command sets a rate limit for ARP packets in a specified BD.

The **undo arp anti-attack rate-limit** command restores the default rate limit for ARP packets in a specified BD.



By default, the rate limit for ARP packets in a specified BD is 0. To be specific, the device does not limit the rate of ARP packets in a BD.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**arp anti-attack rate-limit** *limit*

**undo arp anti-attack rate-limit** [ *limit* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *limit* | Specifies a rate limit for ARP packets in a specified BD. | The value is an integer ranging from 0 to 65536, in pps. |



Views
-----

Bridge domain view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If unauthorized users send a large number of ARP packets to a device, many resources are used for processing these ARP packets, and the processing of other services is affected. To resolve this problem, run the arp anti-attack rate-limit command to set the ARP packet rate limit in a BD, enabling the device to discard excessive ARP packets.

**Prerequisites**

Layer 2 proxy ARP has been enabled using the **arp l2-proxy enable** command in the BD view.

**Configuration Impact**

After the rate limit value is set, the device counts the number of received ARP packets. If the number of ARP packets received in a BD in a specified period exceeds the upper limit, the device discards the excess ARP packets.

**Precautions**

If the global rate limit is too low and the login through Telnet fails because the device receives a large number of attack packets, you can log in to the device through the Console port to increase the rate limit.


Example
-------

# Set the rate limit of ARP packets in BD 10 to 100 pps.
```
<HUAWEI> system-view
[~HUAWEI] bridge-domain 10
[*HUAWEI-bd10] arp anti-attack rate-limit 100

```
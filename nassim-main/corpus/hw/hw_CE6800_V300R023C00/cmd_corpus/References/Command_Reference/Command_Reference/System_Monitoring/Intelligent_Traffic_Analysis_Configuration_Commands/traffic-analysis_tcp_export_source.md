traffic-analysis tcp export source
==================================

traffic-analysis tcp export source

Function
--------



The **traffic-analysis tcp export source** command configures the source IP address for the exported packets that carry intelligent traffic analysis results of TCP flows.

The **undo traffic-analysis tcp export source** command deletes the source IP address configured for the exported packets that carry intelligent traffic analysis results of TCP flows.



By default, no source IP address is configured for the exported packets that carry intelligent traffic analysis results of TCP flows.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**traffic-analysis tcp export source** { **ip** *ip-address* | **ipv6** *ipv6-address* }

**undo traffic-analysis tcp export source** { **ip** [ *ip-address* ] | **ipv6** [ *ipv6-address* ] }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ip** *ip-address* | Specifies the source IPv4 address for the exported packets that carry intelligent traffic analysis results of TCP flows. | The value is in dotted decimal notation. |
| **ipv6** *ipv6-address* | Specifies the source IPv6 address for the exported packets that carry intelligent traffic analysis results of TCP flows. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

After intelligent traffic analysis for TCP flows is enabled on the switch, the intelligent traffic analysis flow table that contains the flow analysis results is first stored in the cache of the switch. When the intelligent traffic analysis flow table in the cache meets the aging conditions, the switch sends the flow table in the cache to the specified TDA for further processing and display of flow information. The TDA may need to identify the data source based on the source address in exported packets that carry intelligent traffic analysis results of TCP flows. Therefore, you can run this command to set the source IP address of these exported packets

**Precautions**

If no source IP address is configured for exported packets, packets are not exported. The source IP address must be reachable to the destination address (TDA address) of exported packets. The device can be configured with two source IP addresses (an IPv4 address and an IPv6 address). The two IP addresses are independent of each other.


Example
-------

# Set the source IP address to 10.1.1.1 for the exported packets that carry intelligent traffic analysis results of TCP flows.
```
<HUAWEI> system-view
[~HUAWEI] traffic-analysis tcp export source ip 10.1.1.1

```
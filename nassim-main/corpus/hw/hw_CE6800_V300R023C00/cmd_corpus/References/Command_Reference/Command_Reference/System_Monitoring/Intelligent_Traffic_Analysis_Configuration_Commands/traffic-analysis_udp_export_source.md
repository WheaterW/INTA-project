traffic-analysis udp export source
==================================

traffic-analysis udp export source

Function
--------



The **traffic-analysis udp export source** command configures the source IP address for the exported packets that carry intelligent traffic analysis results of UDP flows.

The **undo traffic-analysis udp export source** command restores the default configuration.



By default, no source IP address is configured for the exported packets that carry intelligent traffic analysis results of UDP flows.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

For CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE8850-SAN, CE8851-32CQ8DQ-P, CE8850-HAM, CE8851K:

**traffic-analysis udp export source** { **ip** *ip-address* | **ipv6** *ipv6-address* }

**undo traffic-analysis udp export source** { **ip** [ *ip-address* ] | **ipv6** [ *ipv6-address* ] }

For CE6885-LL (low latency mode):

**traffic-analysis udp export source ip** *ip-address*

**undo traffic-analysis udp export source ip** [ *ip-address* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ip** *ip-address* | Specifies the source IPv4 address for the exported packets that carry intelligent traffic analysis results of UDP flows. | The value is in dotted decimal notation. |
| **ipv6** *ipv6-address* | Specifies the source IPv6 address for the exported packets that carry intelligent traffic analysis results of UDP flows.  NOTE:  This parameter is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

After intelligent traffic analysis for UDP flows is enabled on a switch, the flow tables that contain UDP flow analysis results are first stored on the switch. When a flow table meets the aging conditions, the switch sends the flow table to the specified TDA for further processing and graphical display of flow information. The TDA may need to identify the data source based on the source IP address in exported packets that carry intelligent traffic analysis results of UDP flows. Therefore, you can run this command to set the source IP address of these exported packets.

**Precautions**



If no source address is configured, packets are not exported. There must be reachable routes between the source address and destination address (TDA address) of the exported packets.Two source IP addresses can be configured simultaneously: one IPv4 address and one IPv6 address. The two addresses are independent of each other. Only an IPv4 address can be specified as the source address for the CE6885-LL in low latency mode.




Example
-------

# Set the source IP address to 10.1.1.1 for the exported packets that carry intelligent traffic analysis results of UDP flows.
```
<HUAWEI> system-view
[~HUAWEI] traffic-analysis udp export source ip 10.1.1.1

```
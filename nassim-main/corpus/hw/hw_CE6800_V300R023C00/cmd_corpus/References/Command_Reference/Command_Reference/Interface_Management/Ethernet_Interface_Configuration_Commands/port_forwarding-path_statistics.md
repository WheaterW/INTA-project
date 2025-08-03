port forwarding-path statistics
===============================

port forwarding-path statistics

Function
--------



The **port forwarding-path statistics** command configures a rule for collecting statistics on packets containing specified 5-tuple information.

The **undo port forwarding-path statistics** command deletes a rule for collecting statistics on packets containing specified 5-tuple information.



By default, no rule for collecting statistics on packets containing specified 5-tuple information is configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**port forwarding-path path-id** *pathnum* { **src-ip** *src-ip-data* [ *srcip-mask-len* ] | **dst-ip** *dst-ip-data* [ *dstip-mask-len* ] | **protocol** { *protocolnum* | **tcp** [ **l4-src-port** *src-port-data* | **l4-dst-port** *dst-port-data* ] \* | **udp** [ **l4-src-port** *src-port-data* | **l4-dst-port** *dst-port-data* ] \* } } \* **statistics** **precedence** *precedencenum*

**undo port forwarding-path path-id** *pathnum* [ { **src-ip** *src-ip-data* [ *srcip-mask-len* ] | **dst-ip** *dst-ip-data* [ *dstip-mask-len* ] | **protocol** { *protocolnum* | **tcp** [ **l4-src-port** *src-port-data* | **l4-dst-port** *dst-port-data* ] \* | **udp** [ **l4-src-port** *src-port-data* | **l4-dst-port** *dst-port-data* ] \* } } \* **statistics** **precedence** *precedencenum* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **src-ip** *src-ip-data* | Specifies a source IPv4 address. | The value is in dotted decimal notation. |
| *srcip-mask-len* | Specifies the mask length of the source IPv4 address. | The value is an integer that ranges from 1 to 32. The default value is 32. |
| **dst-ip** *dst-ip-data* | Specifies a destination IPv4 address. | The value is in dotted decimal notation. |
| *dstip-mask-len* | Specifies the mask length of the destination IPv4 address. | The value is an integer that ranges from 1 to 32. The default value is 32. |
| **protocol** | Specifies the protocol type. | - |
| *protocolnum* | Specifies the protocol number. | The value is an integer that ranges from 0 to 255. The default value is 0. |
| **tcp** | Indicates the TCP protocol type. | - |
| **l4-src-port** *src-port-data* | Specifies the source port number. | The value is an integer that ranges from 0 to 65535. |
| **l4-dst-port** *dst-port-data* | Specifies the destination port number. | The value is an integer that ranges from 0 to 65535. |
| **udp** | Indicates the UDP protocol type. | - |
| **precedence** *precedencenum* | Specifies a priority corresponding to the path ID.  A smaller value of precedencenum indicates a higher priority. | The value is an integer that ranges from 1 to 2000. |
| **path-id** *pathnum* | Specifies the path ID.  A path ID indicates a matching rule. | The value is an integer that ranges from 1 to 128. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The 5-tuple information includes the source and destination IP addresses, source/destination port numbers in TCP or UDP packets, and protocol type. Traffic transmitted on each device interface contains different 5-tuple information. If the outbound interface is an Eth-Trunk or packets have multiple ECMP next hops, you can use the **port forwarding-path statistics** command to configure rules for collecting statistics on the packets containing specified 5-tuple information and the **display port forwarding-path statistics** command to check the statistics (including the outbound interface), facilitating fault locating and traffic forwarding path identification.

**Precautions**

The **port forwarding-path statistics** command can be used to collect statistics only on IPv4 packets.The path ID specified by pathnum and priority specified by precedencenum are globally unique and cannot be overwritten. To change a traffic statistics collection rule, you need to delete the current settings for the rule and then configure a new rule.If a packet matches multiple rules, only the rule with the highest priority takes effect for this packet.For tunnel packets, the system collects statistics on packets by matching 5-tuple information in tunnel-encapsulated outer packets. In addition, the system matches 5-tuple information in tunnel-encapsulated outer packets in both the inbound and outbound directions.Running the **port forwarding-path statistics** command requires a large number of ACL rules to be dynamically delivered, which may exhaust ACL resources. Consequently, an alarm indicating that ACL resource usage exceeds the limit may be generated. Due to insufficient ACL resources, the outbound interface of the traffic may fail to be queried. In this case, you can run the display system tcam fail-record [ slot slot-id ] command in any view to check information on the TCAM delivery failure and determine whether ACL resources are insufficient.


Example
-------

# Configure a rule for collecting statistics on the packets containing specified 5-tuple information.
```
<HUAWEI> system-view
[~HUAWEI] port forwarding-path path-id 2 src-ip 10.1.1.1 32 dst-ip 10.2.2.2 32 statistics precedence 10

```
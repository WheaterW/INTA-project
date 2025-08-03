display port forwarding-path
============================

display port forwarding-path

Function
--------



The **display port forwarding-path** command displays the outbound interface of packets that contain specified 5-tuple information, source MAC address, and destination MAC address.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display port forwarding-path** { **src-ip** *src-ip-data* [ *ip-mask-len* | *source-ip-mask* ] | **dst-ip** *dst-ip-data* [ *ip-mask-len* | *dst-ip-mask* ] | **src-mac** *src-mac-data* | **dst-mac** *dst-mac-data* | **protocol** { *protocol-number* | **gre** | **icmp** | **igmp** | **ip** | **ipinip** | **ospf** | **tcp** [ **l4-src-port** *src-port-data* | **l4-dst-port** *dst-port-data* ] \* | **udp** [ **l4-src-port** *src-port-data* | **l4-dst-port** *dst-port-data* ] \* } } \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **src-ip** *src-ip-data* | Specifies a source IP address. | The value is in dotted decimal notation. |
| *ip-mask-len* | Specifies the mask length. | The value is an integer that ranges from 0 to 32. |
| *source-ip-mask* | Specifies the subnet mask of the source IP address. | The value is in dotted decimal notation. |
| **dst-ip** *dst-ip-data* | Specifies a destination IP address. | The value is in dotted decimal notation. |
| *dst-ip-mask* | Specifies the subnet mask of the destination IP address. | The value is in dotted decimal notation. |
| **src-mac** *src-mac-data* | Specifies a source MAC address. | The value is in H-H-H format. An H is a hexadecimal number of 1 to 4 digits. |
| **dst-mac** *dst-mac-data* | Specifies a destination MAC address. | The value is in H-H-H format. An H is a hexadecimal number of 1 to 4 digits. |
| **protocol** *protocol-number* | Specifies the protocol number or type.  protocol-number specifies the protocol number. | The value is an integer that ranges from 0 to 255.  The protocol type can be:   * GRE * ICMP * IGMP * IP * IPINIP * OSPF * TCP * UDP |
| **l4-src-port** *src-port-data* | Specifies the source port number. | The value is an integer that ranges from 0 to 65535. |
| **l4-dst-port** *dst-port-data* | Specifies the destination port number. | The value is an integer that ranges from 0 to 65535. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

The 5-tuple information contains the source/destination IP addresses, source/destination port numbers, and protocol type. Traffic on each interface often carries different 5-tuple information, source MAC address, and destination MAC address. If the outbound interface of packets is an Eth-Trunk or there are multiple next hops (ECMP), run this command to view the outbound interface in packets that contain specified 5-tuple information, source MAC address, and destination MAC address. The command output helps you locate faults and determine the forwarding path.

**Precautions**

* The query result is displayed only when traffic is transmitted on the outbound interface of packets.
* The outbound interface can be queried only based on 5-tuple information of IPv4 packets.
* Running the **display port forwarding-path** command requires a large number of ACL rules to be dynamically delivered, which may result in ACL resource shortage. Consequently, an alarm indicating that ACL resource usage exceeds the limit may be generated.
* During the port splitting or combination, the outbound interface may fail to be queried. After the port splitting or combination is completed, the outbound interface can be queried properly.
* If both the display port forwarding-path and **port forwarding-path statistics** commands are run on a device, they are delivered to the same ACL group, and only the **port forwarding-path statistics** command with a higher priority takes effect. As a result, the outbound interface may fail to be queried using the **display port forwarding-path** command.
* This command can be used on all service interfaces to query the outbound interface in packets that contain specified 5-tuple information, source MAC address, and destination MAC address. It is recommended that 5-tuple information be specified to query Layer 3 unicast traffic. If the MAC address is specified to query Layer 3 unicast traffic, the query may fail.
* For tunnel packets, the system collects statistics on packets by matching 5-tuple information in tunnel-encapsulated outer packets. In addition, the system matches 5-tuple information in tunnel-encapsulated outer packets in both the inbound and outbound directions.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the outbound interface that contains specified 5-tuple information.
```
<HUAWEI> display port forwarding-path src-ip 10.1.1.1 dst-ip 10.2.2.2
OutInterface: 100GE1/0/1
              100GE1/0/2

```

**Table 1** Description of the **display port forwarding-path** command output
| Item | Description |
| --- | --- |
| OutInterface | Outbound interface of packets that contain specified 5-tuple information. |
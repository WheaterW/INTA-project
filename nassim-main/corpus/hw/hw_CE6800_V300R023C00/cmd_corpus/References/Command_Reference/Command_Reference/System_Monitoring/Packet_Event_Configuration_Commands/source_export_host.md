source export host
==================

source export host

Function
--------



The **source export host** command configures an analyzer address in the collector view.

The **undo source export host** command cancels the configuration of an analyzer address in the collector view.



By default, no analyzer address is configured in the collector view.


Format
------

For CE6820H, CE6820H-K, CE6820S, CE6855-48XS8CQ, CE6860-SAN, CE6863H, CE6863H-K, CE6866, CE6860-HAM, CE6866K, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE8850-SAN, CE8851-32CQ8DQ-P, CE8850-HAM, CE8851K, CE8855, CE8851-32CQ4BQ:

**source** { **ip** *ip-address* | **ipv6** *ipv6-address* } **export** **host** { **ip** *ip-address* | **ipv6** *ipv6-address* } **udp-port** *port-number* [ **vpn-instance** *vpn-instance-name* ]

**undo source** { **ip** *ip-address* | **ipv6** *ipv6-address* } **export** **host** { **ip** *ip-address* | **ipv6** *ipv6-address* } **udp-port** *port-number* [ **vpn-instance** *vpn-instance-name* ]

For CE6885-LL (low latency mode):

**source** { **ip** *ip-address* } **export** **host** { **ip** *ip-address* } **udp-port** *port-number* [ **vpn-instance** *vpn-instance-name* ]

**undo source** { **ip** *ip-address* } **export** **host** { **ip** *ip-address* } **udp-port** *port-number* [ **vpn-instance** *vpn-instance-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ip** *ip-address* | Specify the source / destination IPv4 address of the output packet. | The value is in dotted decimal notation. |
| **ipv6** *ipv6-address* | Specify the source / destination IPv6 address of the output packet.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **udp-port** *port-number* | Specify the destination UDP port number of the output packet. | The value is an integer that ranges from 1 to 65535. |
| **vpn-instance** *vpn-instance-name* | Specify the VPN instance name of the output packet. | The value is a string of 1 to 31 case-sensitive characters. The VPN instance name cannot be \_public\_. The character string can contain spaces if it is enclosed with double quotation marks ("). |



Views
-----

collector view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After the analyzer is configured in the system view, you need to specify the source address, destination address, and UDP port number of the analyzer.

**Prerequisites**

You need to run the **ipv4-family** or **ipv6-family** command in the VPN instance view to configure an IP address family.

**Precautions**

When this command is executed, the IPv4 and IPv6 address families of the VPN instance are automatically verified. If no IP address family is configured for the VPN instance, the configuration will be lost after the upgrade. In this case, reconfigure the IP address family of the VPN instance and then run the command again.The IP addresses of the local and peer devices bound to a VPN instance must be different. In addition, the addresses cannot be set tp unspecified addresses, IPv6 link-local addresses, multicast addresses, or loopback addresses.


Example
-------

# Configure the source IP address of analyzer 1 as 192.168.1.2, the destination IP address as 10.0.0.2, the UDP port as 100, and the VPN instance as vpn1.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI] commit
[~HUAWEI] collector collect 1
[~HUAWEI-collect-1] source ip 192.168.1.2 export host ip 10.0.0.2 udp-port 100 vpn-instance vpn1

```
dns server
==========

dns server

Function
--------



The **dns server** command configures an IP address for a DNS server.

The **undo dns server** command deletes the DNS server IP address.



By default, no DNS server IP address is configured.


Format
------

**dns server** *ip-address* [ **vpn-instance** *vpn-instance-name* ]

**undo dns server** [ *ip-address* [ **vpn-instance** *vpn-instance-name* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies the IP address of a DNS server. | The value is in dotted decimal notation. |
| **vpn-instance** *vpn-instance-name* | Specifies the VPN instance of a DNS server. | The value is a string of 1 to 31 case-sensitive characters. The VPN instance name cannot be \_public\_. The character string can contain spaces if it is enclosed with double quotation marks ("). |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

A maximum of six DNS servers can be specified on the device. During dynamic domain name resolution, the algorithm (configured by the **dns-server-select-algorithm** command) used by the device to select a DNS server determines the DNS server to which the query packet is sent.


Example
-------

# Set the IP address of the DNS server in the VPN named vpn1 to 10.2.0.71.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv4-family
[*HUAWEI-vpn-instance-vpn1-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] dns server 10.2.0.71 vpn-instance vpn1

```

# Assign the IP address 10.2.0.70 to the DNS server.
```
<HUAWEI> system-view
[~HUAWEI] dns server 10.2.0.70

```
display dns server
==================

display dns server

Function
--------



The **display dns server** command displays the configuration and sequence of the current DNS server.




Format
------

**display dns server** [ **vpn-instance** *vpn-instance-name* ] [ **verbose** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters. The VPN instance name cannot be \_public\_. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **verbose** | Displays detailed information about the DNS server. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

After configuring DNS, run the **display dns server** command to view the configuration and sequence of current DNS servers.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display configurations of a DNS server.
```
<HUAWEI> display dns server
Type:
D:Dynamic     S:Static

IPv4 DNS server :
NO. Type Status Used CfgSeq IP Address
0   S    -      Yes  0      10.1.1.1
1   S    -      Yes  1      10.1.1.2

IPv6 DNS servers :
NO. Type Status Used IPv6 Address                            Interface
0   S    -      Yes  FC00:1::1                               -

```

# Display the DNS server address in the VPN named vpn1.
```
<HUAWEI> display dns server vpn-instance vpn1
Type:
D:Dynamic     S:Static

IPv4 DNS server :
NO. Type Status Used CfgSeq IP Address
0   S    -      Yes  0      10.1.2.1
1   S    -      Yes  1      10.1.2.2

IPv6 DNS servers :
NO. Type Status Used IPv6 Address    Interface
0   S    -      Yes  FC00:2::1       -

```

**Table 1** Description of the **display dns server** command output
| Item | Description |
| --- | --- |
| IPv4 DNS server | IPv4 DNS server configuration. |
| NO. | DNS server number, indicating the order in which they were configured. |
| Type | Configuration type of the DNS server IP address, including dynamic and static. |
| Status | DNS server status. |
| Used | Indicates whether the DNS server is used. |
| CfgSeq | Sequence of adding DNS servers to a DNS server group. |
| IP Address | IPv4 address of the DNS server. |
| IPv6 Address | IPv6 address of the DNS server. |
| IPv6 DNS servers | IPv6 DNS server configuration. |
| Interface | Name of the outbound interface communicating with the DNS server. |
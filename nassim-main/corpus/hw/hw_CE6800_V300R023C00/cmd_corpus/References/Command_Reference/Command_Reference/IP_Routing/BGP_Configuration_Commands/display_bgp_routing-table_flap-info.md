display bgp routing-table flap-info
===================================

display bgp routing-table flap-info

Function
--------



The **display bgp routing-table flap-info** command displays statistics about BGP route flapping.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**display bgp** [ **vpnv4** **vpn-instance** *vpn-instance-name* ] **routing-table** **flap-info** [ **as-path-filter** { *as-path-filter-number* | *as-path-filter-name* } | **regular-expression** *as-regular-expression* | *ipv4-address* [ { *mask* | *mask-length* } [ **longer-match** ] ] ]

**display bgp instance** *instance-name* [ **vpnv4** **vpn-instance** *vpn-instance-name* ] **routing-table** **flap-info** [ **as-path-filter** { *as-path-filter-number* | *as-path-filter-name* } | **regular-expression** *as-regular-expression* | *ipv4-address* [ { *mask* | *mask-length* } [ **longer-match** ] ] ]

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display bgp vpnv6 vpn-instance** *vpn-instance-name* **routing-table** **flap-info** [ **as-path-filter** { *as-path-filter-number* | *as-path-filter-name* } | **regular-expression** *as-regular-expression* | *ipv6-address* [ *prefix-length* [ **longer-match** ] ] ]

**display bgp instance** *instance-name* **vpnv6** **vpn-instance** *vpn-instance-name* **routing-table** **flap-info** [ **as-path-filter** { *as-path-filter-number* | *as-path-filter-name* } | **regular-expression** *as-regular-expression* | *ipv6-address* [ *prefix-length* [ **longer-match** ] ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **as-path-filter** *as-path-filter-name* | Specifies an AS\_Path filter name (a string of 1 to 51 characters, which cannot contain only digits.). | The value is a string of 1 to 51 case-sensitive characters. If spaces are used, the string must start and end with double quotation marks ("). |
| **as-path-filter** *as-path-filter-number* | Specifies an AS\_Path filter index. | The value is a decimal integer ranging from 1 to 256. |
| **regular-expression** *as-regular-expression* | Displays the routes that match the regular expression. | The value is a string of 1 to 80 characters. |
| *ipv4-address* | Specify an IPv4 network address. | The value is in dotted decimal notation. |
| *mask* | Specifies an IPv4 network mask. | The value is in dotted decimal notation. |
| *mask-length* | Specifies an IP address prefix length. | The value is an integer ranging from 0 to 32. |
| **longer-match** | Allows match against longer masks. | - |
| **vpnv4** | Indicates the VPNv4 address family. | - |
| **vpn-instance** *vpn-instance-name* | Specifies a VPN instance name. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **instance** *instance-name* | Specifies a BGP instance name. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |
| **vpnv6** | Indicates the VPNv6 address family.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| *ipv6-address* | Specifies an ipv6 network address.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *prefix-length* | Specifies an IPv6 address mask length.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | It is an integer ranging from 0 to 128. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To view statistics about BGP route flapping, run the **display bgp routing-table flap-info** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the flapping statistics of IBGP peers.
```
<HUAWEI> display bgp routing-table flap-info

 BGP Local router ID is 10.20.200.201
 Status codes: * - valid, > - best, d - damped, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
 Origin      : i - IGP, e - EGP, ? - incomplete

 Total Number of Routes: 5
     Network         From            Flaps  Duration     Reuse  Path/Ogn

 di  172.16.1.0       10.20.200.200   5      00:00:36  00:40:47  600i
 di  172.16.2.0       10.20.200.200   5      00:00:36  00:40:47  600i
 di  172.16.3.0       10.20.200.200   5      00:00:36  00:40:47  600i
 di  172.16.4.0       10.20.200.200   5      00:00:36  00:40:47  600i
 di  172.16.5.0       10.20.200.200   5      00:00:36  00:40:47  600i

```

# Display the flapping statistics of EBGP peers.
```
<HUAWEI> display bgp routing-table flap-info

 BGP Local router ID is 10.20.200.201
 Status codes: * - valid, > - best, d - damped, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
 Origin      : i - IGP, e - EGP, ? - incomplete

 Total Number of Routes: 5
     Network         From            Flaps  Duration     Reuse  Path/Ogn

 d  172.16.1.0       10.20.200.200   5      00:00:36  00:40:47  600i
 d  172.16.2.0       10.20.200.200   5      00:00:36  00:40:47  600i
 d  172.16.3.0       10.20.200.200   5      00:00:36  00:40:47  600i
 d  172.16.4.0       10.20.200.200   5      00:00:36  00:40:47  600i
 d  172.16.5.0       10.20.200.200   5      00:00:36  00:40:47  600i

```

**Table 1** Description of the **display bgp routing-table flap-info** command output
| Item | Description |
| --- | --- |
| BGP Local router ID | ID of the local BGP device, in the same format as an IPv4 address. |
| Total Number of Routes | Number of flapping routes. |
| Network | Indicates the network address in the BGP routing table. |
| From | Indicates the IP address of the peer that receives the routes. |
| Flaps | Total number of route flappings. |
| Duration | Total duration of route flapping. |
| Reuse | Reuse value. |
| Path/Ogn | AS\_Path and Origin. |
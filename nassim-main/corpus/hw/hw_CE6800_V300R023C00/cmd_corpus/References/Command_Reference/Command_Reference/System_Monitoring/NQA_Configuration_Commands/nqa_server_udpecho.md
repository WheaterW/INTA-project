nqa server udpecho
==================

nqa server udpecho

Function
--------



The **nqa server udpecho** command configures a UDP server for an NQA test instance.

The **undo nqa server udpecho** command deletes a UDP server for an NQA test instance.



By default, no UDP server is configured for an NQA test.


Format
------

**nqa server udpecho** { *ip-address* | **ipv6** *ipv6-address* } *port-number*

**nqa server udpecho vpn-instance** *vpn-instance-name* { *ip-address* | **ipv6** *ipv6-address* } *port-number*

**undo nqa server udpecho** { *ip-address* | **ipv6** *ipv6-address* } *port-number*

**undo nqa server udpecho vpn-instance** *vpn-instance-name* { *ip-address* | **ipv6** *ipv6-address* } *port-number*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies the IPv4 address of the NQA server for monitoring UDP services. | The value is in dotted decimal notation. |
| **ipv6** *ipv6-address* | Specifies the IPv6 address of the NQA server for monitoring UDP services. | The address is a 32-bit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *port-number* | Specifies the port number of the NQA server for monitoring UDP services. | The value is integer ranging from 1 to 65535. The well-known port number is not recommended. |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance to which the UDP server belongs. | The value is a string of 1 to 31 case-sensitive characters. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To specify an NQA server for a UDP jitter test instance or a UDP test instance, run the nqa-server udpecho command. The UDP server responds to probe packets initiated by an NQA client.

**Configuration Impact**

If no UDP server is configured, the NQA client will receive no response to probe packets within the timeout period. Then, all UDP jitter test instances or UDP test instances will fail.


Example
-------

# Configure a UDP server with ip-address set to 10.10.10.2, vpn-instance set to vpn1, and port-number set to 2000.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] nqa server udpecho vpn-instance vpn1 10.10.10.2 2000

```
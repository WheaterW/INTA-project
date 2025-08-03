reset sdn openflow statistics
=============================

reset sdn openflow statistics

Function
--------



The **reset sdn openflow statistics** command clears statistics about the OpenFlow connection packets.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset sdn openflow statistics** [ **controller** [ **vpn-instance** *vpn-instance-name* ] { *ipv4-address* | *ipv6-address* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **controller** | Controller. | - |
| **vpn-instance** *vpn-instance-name* | Specifies the name of the VPN instance that the controller belongs to. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| *ipv4-address* | Specifies the controller's IP address. | The value is in dotted decimal notation. |
| *ipv6-address* | Specifies the controller's IPv6 address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

To obtain accurate statistics about OpenFlow connection packets, you can run the **reset sdn openflow statistics** command to clear the existing statistics first, and then run the **display sdn openflow statistics** command to view the latest statistics.


Example
-------

# Clear statistics about OpenFlow connection packets.
```
<HUAWEI> reset sdn openflow statistics

```
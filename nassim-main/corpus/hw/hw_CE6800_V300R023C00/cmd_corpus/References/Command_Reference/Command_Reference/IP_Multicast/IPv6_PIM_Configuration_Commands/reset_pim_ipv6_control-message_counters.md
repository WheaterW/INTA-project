reset pim ipv6 control-message counters
=======================================

reset pim ipv6 control-message counters

Function
--------



The **reset pim ipv6 control-message counters** command deletes statistics about IPv6 PIM control messages.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset pim ipv6 control-message counters** [ **interface** { *interface-type* *interface-number* | *interface-name* } ]

**reset pim ipv6** { **vpn-instance** *instance-name* | **all-instance** } **control-message** **counters** [ **interface** { *interface-type* *interface-number* | *interface-name* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* | Deletes statistics about IPv6 PIM control messages on a specified interface type. | - |
| *interface-number* | Deletes statistics about IPv6 PIM control messages on a specified interface number. | - |
| *interface-name* | Specifies the name of an interface. | - |
| **vpn-instance** *instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **all-instance** | Specifies all VPN instance. | - |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To re-collect statistics about IPv6 PIM control messages, run the reset pim ipv6 control-message counters command to delete existing statistics about IPv6 PIM control messages.


Example
-------

# Clear statistics about PIM control messages on 100GE1/0/1.
```
<HUAWEI> reset pim ipv6 control-message counters interface 100GE 1/0/1

```
reset msdp statistics
=====================

reset msdp statistics

Function
--------



The **reset msdp statistics** command clears statistics of one or more source active (SA) peers without resetting the MSDP peer (s).




Format
------

**reset msdp vpn-instance** *vpn-instance-name* **statistics** [ *peer-address* ]

**reset msdp statistics** [ *peer-address* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peer-address* | Specifies the address of an MSDP peer. | The address is in dotted decimal notation. If the peer-address is not specified, the statistics of all MSDP peers are cleared. |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. The VPN instance name "\_public\_" cannot be used. The string can contain spaces if it is enclosed with double quotation marks ("). |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After the **reset msdp statistics** command is used, the statistics of the MSDP peer are cleared automatically. However, the TCP connections among peers are not closed, and MSDP services are not affected.If you want to clear the statistics of an MSDP peer and to rebuild the TCP connections among MSDP peers at the same time, use the **reset msdp peer** command.

**Precautions**

If vpn-instance is not specified, statistics of the MSDP peers in the public network instance are deleted.


Example
-------

# In the public network instance, clear the statistics of MSDP peer 192.168.1.1.
```
<HUAWEI> reset msdp statistics 192.168.1.1

```
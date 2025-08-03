reset msdp all-instance statistics
==================================

reset msdp all-instance statistics

Function
--------



The **reset msdp all-instance statistics** command clears statistics of one or more source active (SA) peers without resetting the MSDP peer (s).




Format
------

**reset msdp all-instance statistics** [ *peer-address* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peer-address* | Specifies IP address of MSDP peer. | The value is in dotted decimal notation. |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

After the **reset msdp all-instance statistics** command is used, the statistics of the MSDP peer are cleared automatically. However, the TCP connections among peers are not closed, and MSDP services are not affected.If you want to clear the statistics of an MSDP peer and to rebuild the TCP connections among MSDP peers at the same time, use the **reset msdp peer** command.


Example
-------

# In the all vpn instance, clear the statistics of MSDP peer 192.168.1.1.
```
<HUAWEI> reset msdp all-instance statistics 192.168.1.1

```
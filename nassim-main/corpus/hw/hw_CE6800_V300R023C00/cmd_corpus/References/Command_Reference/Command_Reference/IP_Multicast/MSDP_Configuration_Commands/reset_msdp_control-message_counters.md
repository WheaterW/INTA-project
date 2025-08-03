reset msdp control-message counters
===================================

reset msdp control-message counters

Function
--------



The **reset msdp control-message counters** command clears the statistics about the received, sent, and discarded Multicast Source Discovery Protocol (MSDP) messages.




Format
------

**reset msdp control-message counters** [ **peer** *peer-address* ]

**reset msdp vpn-instance** *vpn-instance-name* **control-message** **counters** [ **peer** *peer-address* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **peer** *peer-address* | Specifies IP address of MSDP peer. | The value is in dotted decimal notation. |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. The VPN instance name cannot be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

When the **reset msdp control-message counters** command is run:

* If vpn-instance is not specified, only information on the public network instance is cleared.
* If peer peer-address is specified, only the statistics about the MSDP messages received, sent, and discarded with a specified MSDP peer are cleared.

Example
-------

# Clear the statistics about the MSDP messages received, sent, and discarded with the peer 3.3.3.3 in the public network instance.
```
<HUAWEI> reset msdp control-message counters peer 3.3.3.3

```
reset msdp peer
===============

reset msdp peer

Function
--------



The **reset msdp peer** command resets the TCP connection with a specified Multicast Source Discovery Protocol (MSDP) peer, and clears the statistics about the specified MSDP peer.




Format
------

**reset msdp vpn-instance** *vpn-instance-name* **peer** [ *peer-address* ]

**reset msdp peer** [ *peer-address* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peer-address* | Specifies IP address of MSDP peer. | The value is in dotted decimal notation. |
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

When you want to re-configure the TCP connection between MSDP peers or clear statistics about the specified MSDP peer, run the **reset msdp peer** command.Use the **reset msdp statistics** command to clear the statistics about an MSDP peer without resetting the MSDP peer.

**Configuration Impact**

After this command is run, the TCP connection with the specified MSDP peer is torn down and a new TCP is set up again. During this process, MSDP services are interrupted, which may affect multicast services, for example, multicast data transmission fails. Therefore, use this command with caution.

**Precautions**

If vpn-instance is not specified, the TCP connections set up between MSDP peers in the public network instance are reset and the statistics about MSDP peers in the public network instance are cleared.


Example
-------

# Clear the TCP connection and statistics of MSDP peer 192.168.1.1 in the public network instance.
```
<HUAWEI> reset msdp peer 192.168.1.1

```
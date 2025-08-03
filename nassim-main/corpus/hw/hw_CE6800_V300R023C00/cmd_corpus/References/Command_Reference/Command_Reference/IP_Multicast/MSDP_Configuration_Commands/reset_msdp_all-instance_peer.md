reset msdp all-instance peer
============================

reset msdp all-instance peer

Function
--------



The **reset msdp all-instance peer** command resets the TCP connection with a specified Multicast Source Discovery Protocol (MSDP) peer, and clears the statistics about the specified MSDP peer by all vpn instances.




Format
------

**reset msdp all-instance peer** [ *source-address* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *source-address* | Specifies IP address of MSDP peer. | The value is in dotted decimal notation. |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When you want to re-configure the TCP connection between MSDP peers or clear statistics about the specified MSDP peer, run the **reset msdp all-instance peer** command.Use the **reset msdp statistics** command to clear the statistics about an MSDP peer without resetting the MSDP peer.

**Configuration Impact**

After this command is run, the TCP connection with the specified MSDP peer is torn down and a new TCP is set up again. During this process, MSDP services are interrupted, which may affect multicast services, for example, multicast data transmission fails. Therefore, use this command with caution.


Example
-------

# In all vpn instance, reset the TCP connection with MSDP peer 10.10.7.6 and clear the statistics about MSDP peer 10.10.7.6.
```
<HUAWEI> reset msdp all-instance peer 10.10.7.6

```
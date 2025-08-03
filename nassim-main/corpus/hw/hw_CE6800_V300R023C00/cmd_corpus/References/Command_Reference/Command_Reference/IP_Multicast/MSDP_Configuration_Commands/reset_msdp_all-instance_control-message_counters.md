reset msdp all-instance control-message counters
================================================

reset msdp all-instance control-message counters

Function
--------



The **reset msdp all-instance control-message counters** command clears the statistics about the received, sent, and discarded Multicast Source Discovery Protocol (MSDP) messages by all vpn instances.




Format
------

**reset msdp all-instance control-message counters** [ **peer** *peer-address* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **peer** *peer-address* | Specifies IP address of MSDP peer. | The value is in dotted decimal notation. |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When the **reset msdp all-instance control-message counters** command is run,if peer peer-address is specified, only the statistics about the MSDP messages received, sent, and discarded with a specified MSDP peer are cleared.

**Precautions**

When the **reset msdp all-instance control-message counters** command is run:If IP address of MSDP peer is specified, only the statistics about the MSDP messages received, sent, and discarded with a specified MSDP peer are cleared.


Example
-------

# Clear the statistics about the MSDP messages received, sent, and discarded by all vpn instances.
```
<HUAWEI> reset msdp all-instance control-message counters

```
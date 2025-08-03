reset dldp statistics
=====================

reset dldp statistics

Function
--------



The **reset dldp statistics** command clears statistics about DLDPDUs on a specific interface.




Format
------

**reset dldp statistics** [ **interface** { *interface-name* | *interface-type* *interface-number* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-number* | Clears statistics about DLDPDUs on a specific interface.   * If the interface <interface-type interface-number> parameter is not specified, statistics about DLDPDUs on all DLDP-enabled interfaces are cleared. * If the interface <interface-type interface-number> parameter is specified, statistics about DLDPDUs on a specified interface are cleared. | - |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To collect statistics about DLDPDUs within a specific period, run the **reset dldp statistics** command to clear the existing statistics about the DLDPDUs on a specific interface.

**Precautions**

Running the **reset dldp statistics** command can clear statistics about DLDPDUs. Therefore, Exercise caution when running this command.


Example
-------

# Clear statistics about DLDPDUs on all DLDP-enabled interfaces.
```
<HUAWEI> reset dldp statistics

```
reset fwm dldp statistics
=========================

reset fwm dldp statistics

Function
--------



The **reset fwm dldp statistics** command clears statistics about the DLDP module on a specified board.




Format
------

**reset fwm dldp statistics** [ **all** ] **slot** *slot-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Indicates all statistics (including the statistics whose value is 0). | - |
| **slot** *slot-id* | Specifies a slot ID. | The value is a string of case-sensitive characters. It cannot contain spaces. |



Views
-----

All views


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

You can run the **reset fwm dldp statistics** command to clear statistics about the DLDP module on a specified board.


Example
-------

# Clear statistics on the DLDP module in slot 1.
```
<HUAWEI> reset fwm dldp statistics slot 1

```
reset lacp statistics eth-trunk
===============================

reset lacp statistics eth-trunk

Function
--------



The **reset lacp statistics eth-trunk** command clears statistics about LACPDUs on all Eth-Trunk interfaces in static LACP mode, on a specified Eth-Trunk interface in static LACP mode, or on a specified member interface.




Format
------

**reset lacp statistics eth-trunk** [ *trunk-id* [ **interface** { *interface-type* *interface-number* | *interface-name* } ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-number* *interface-name* | Specifies a type,number or name of an interface. | - |
| **eth-trunk** *trunk-id* | Specifies the ID of an Eth-Trunk interface. | The value is an integer in the range from 0 to 1023. |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



Before collecting statistics about LACPDUs on a specific interface within a period, you need to run the reset lacp statistics eth-trunk command to clear the existing statistics about LACPDUs on the interface.When using the reset lacp statistics eth-trunk command, note that:1.If no optional parameter is specified, statistics about LACPDUs on all Eth-Trunk interfaces in static LACP mode are cleared.2.If trunk-id is specified only, statistics about LACPDUs on a specified Eth-Trunk interface in static LACP mode are cleared.3.If both trunk-id and interface portType portNum are specified, statistics about LACPDUs on the specified member interface of the specified Eth-Trunk interface in static LACP mode are cleared.



**Prerequisites**

* Before clearing the statistics about LACPDUs on a specified Eth-Trunk interface, ensure that the Eth-Trunk interface exists and works in static LACP mode.
* Before clearing the statistics about LACPDUs on a specified member interface of an Eth-Trunk interface, ensure that the Eth-Trunk interface and its member interface exist and the Eth-Trunk interface works in static LACP mode.

**Configuration Impact**



The reset lacp statistics eth-trunk command clears the statistics about sent and received LACPDUs on all Eth-Trunk interfaces in static LACP mode, on a specified Eth-Trunk interface in static LACP mode, or on a specified member interface are cleared and cannot be restored. Therefore, exercise caution when you run the command.




Example
-------

# Clear statistics about LACPDUs on the member interface of Eth-Trunk 1 in static LACP mode.
```
<HUAWEI> reset lacp statistics eth-trunk 1 interface 100GE 1/0/1

```

# Clear statistics about LACPDUs on all Eth-Trunk interfaces in static LACP mode.
```
<HUAWEI> reset lacp statistics eth-trunk

```
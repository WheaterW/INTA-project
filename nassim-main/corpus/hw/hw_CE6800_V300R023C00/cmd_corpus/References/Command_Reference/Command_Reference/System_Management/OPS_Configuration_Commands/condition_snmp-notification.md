condition snmp-notification
===========================

condition snmp-notification

Function
--------



The **condition snmp-notification** command configures an SNMP trap OID as the triggering condition of a maintenance assistant.



By default, no triggering condition is configured for a maintenance assistant.


Format
------

**condition snmp-notification oid** *oid-string* [ *optype* *oid-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *optype* | Specifies the type of the comparison between the OID of the generated SNMP trap and the configured SNMP trap OID. | The value can be:   * eq: equal to * ne: not equal to * It: less than * le: less than or equal to * gt: greater than * ge: greater than or equal to |
| *oid-value* | Specifies an OID expressed in numbers. | The value is an integer ranging from -2147483648 to 2147483647. |
| **oid** *oid-string* | Specifies the OID of an SNMP trap. | The value is an integer ranging from 1 to 127. |



Views
-----

Maintenance assistant task view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

After a maintenance assistant is created, a triggering condition must be specified so that the maintenance assistant can be automatically operated as long as the triggering condition is met.An OPS maintenance assistant can be triggered upon an alarm or event. The commands for configuring different triggering conditions for an OPS maintenance assistant vary.To configure an SNMP trap OID as the triggering condition of a maintenance assistant, run the condition snmp-notification command.

**Prerequisites**

The **assistant** command has been run in the system view to create a maintenance assistant.

**Precautions**

A maintenance assistant can be configured with only one triggering condition.


Example
-------

# Configure a maintenance assistant to be triggered based on the OID 1.3.6.1.4.1.2011.5.25.136.1.6.8 expressed in numbers 222.
```
<HUAWEI> system-view
[~HUAWEI] ops
[~HUAWEI-ops] assistant task
[*HUAWEI-ops-assistant-task] condition snmp-notification oid 1.3.6.1.4.1.2011.5.25.136.1.6.8 eq 222

```
snmp-agent packet-priority
==========================

snmp-agent packet-priority

Function
--------



The **snmp-agent packet-priority** command sets the priority of SNMP packets.

The **undo snmp-agent packet-priority** command restores the default priority of SNMP packets.



The default priority of SNMP packets is 6.


Format
------

**snmp-agent packet-priority** { **snmp** *snmpPriority* | **trap** *trapPriority* }

**undo snmp-agent packet-priority snmp**

**undo snmp-agent packet-priority trap**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **snmp** *snmpPriority* | Indicates the priority of the following types of SNMP packets:   * GetResponse PDUs. * SetResponse PDUs. | The value is an integer ranging from 0 to 7. The default value is 6. Value 0 is the lowest priority, and value 7 is the highest priority. |
| **trap** *trapPriority* | Indicates the priority of SNMP notifications. | The value is an integer ranging from 0 to 7. The default value is 6. Value 0 is the lowest priority, and value 7 is the highest priority. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

The snmp-agent packet-priority command is used in the following scenarios:

* Increase the priority of notifications to ensure that the NMS receives these notifications.
* Increase the priority of GetResponse and SetResponse PDUs to facilitate management operations performed in the MIB of a managed device by the NMS.
* Reduce the priority of GetResponse PDUs, SetResponse PDUs, and trap messages, and Inform messages to prevent frequent packet sending in the case of network congestion.

Example
-------

# Set the priority of GetResponse and SetResponse PDUs to 5.
```
<HUAWEI> system-view
[~HUAWEI] snmp-agent packet-priority snmp 5

```
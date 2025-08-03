display snmp-agent proxy statistics
===================================

display snmp-agent proxy statistics

Function
--------



The **display snmp-agent proxy statistics** command displays statistics about SNMP proxy packets.




Format
------

**display snmp-agent proxy statistics**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To view statistics about SNMP proxy packets, run the display snmp-agent proxy statistics command. These statistics provide communication information between the NMS and managed device, helping you diagnose faults.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about SNMP proxy packets.
```
<HUAWEI> display snmp-agent proxy statistics
0 Messages delivered to the SNMP proxy
 0 GetResponse-PDU accepted and processed
 0 Trap-PDU accepted and processed
 0 Inform-PDU accepted and processed
 0 GetRequest-PDU accepted and processed
 0 GetNextRequest-PDU accepted and processed
 0 GetBulkRequest-PDU accepted and processed
 0 SetRequest-PDU accepted and processed
 0 Proxy messages are dropped

```

**Table 1** Description of the **display snmp-agent proxy statistics** command output
| Item | Description |
| --- | --- |
| Messages delivered to the SNMP proxy | Total number of SNMP proxy packets received by the SNMP agent. |
| GetResponse-PDU accepted and processed | Total number of GetResponse PDUs received and processed by the transit node. |
| Trap-PDU accepted and processed | Total number of traps received and processed by the transit node. |
| Inform-PDU accepted and processed | Total number of informs received and processed by the transit node. |
| GetRequest-PDU accepted and processed | Total number of GetRequest PDUs received and processed by the SNMP agent. |
| GetNextRequest-PDU accepted and processed | Total number of GetNextRequest PDUs received and processed by the SNMP agent. |
| GetBulkRequest-PDU accepted and processed | Total number of GetBulkRequest PDUs received and processed by the SNMP agent. |
| SetRequest-PDU accepted and processed | Total number of SetRequest PDUs received and processed by the SNMP agent. |
| Proxy messages are dropped | Total number of SNMP proxy packets dropped by the SNMP agent. |
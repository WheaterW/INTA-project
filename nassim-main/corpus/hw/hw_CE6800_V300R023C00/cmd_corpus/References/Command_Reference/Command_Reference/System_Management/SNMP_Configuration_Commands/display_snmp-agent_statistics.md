display snmp-agent statistics
=============================

display snmp-agent statistics

Function
--------



The **display snmp-agent statistics** command displays SNMP messages statistics.




Format
------

**display snmp-agent statistics**


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

To view statistics about SNMP messages, run the **display snmp-agent statistics** command. The command output contains information about the communication between the SNMP agent and NM station for fault identification.In an SNMP management system, an NM station and an SNMP agent exchange SNMP messages as follows:

* The NM station acts as a manager to send an SNMP Request message to the SNMP agent.
* The SNMP agent searches the MIB on the device for desired information and sends an SNMP Response message to the NM station.
* When the trap triggering conditions are met, the SNMP agent sends a trap message to the NM station to report the event occurring on the device. The network administrator can process the event occurring on the network immediately.NOTE:If a large number of messages are received within a short period, a great number of CPU resources are consumed. The number of received messages depends on the frequency at which the NM station sends the Request messages.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about SNMP messages.
```
<HUAWEI> display snmp-agent statistics
  3158 Messages delivered to the SNMP entity
  0 Messages which were for an unsupported version
  0 Messages which used an SNMP community name not known
  0 Messages which represented an illegal operation for the community supplied
  0 ASN.1 or BER errors in the process of decoding
  3152 Messages passed from the SNMP entity
  0 SNMP PDUs which had badValue error-status
  3 SNMP PDUs which had genErr error-status
  0 SNMP PDUs which had noSuchName error-status
  0 SNMP PDUs which had tooBig error-status
  3135 MIB objects retrieved successfully
  0 MIB objects altered successfully
  0 GetRequest-PDU accepted and processed
  3158 GetNextRequest-PDU accepted and processed
  0 GetBulkRequest-PDU accepted and processed
  3152 GetResponse-PDU sent
  0 SetRequest-PDU accepted and processed
  0 Trap-PDU sent
  0 Inform-PDU sent
  0 Inform-PDU received with no acknowledgement
  0 Inform-PDU received with acknowledgement

```

**Table 1** Description of the **display snmp-agent statistics** command output
| Item | Description |
| --- | --- |
| Messages delivered to the SNMP entity | Total number of received SNMP messages. |
| Messages which were for an unsupported version | Number of messages with incorrect version information. |
| Messages which used an SNMP community name not known | Number of messages with incorrect community names. |
| Messages which represented an illegal operation for the community supplied | Number of messages whose community names have incorrect access rights. |
| Messages passed from the SNMP entity | Total number of sent SNMP messages. |
| SNMP PDUs which had badValue error-status | Number of SNMP messages with a Bad\_values error. A Bad\_values error occurs when data carried in the Set-Request message sent to the SNMP agent is incorrect. |
| SNMP PDUs which had genErr error-status | Number of SNMP packets with a General\_errors error. A General\_errors error is an unknown error. |
| SNMP PDUs which had tooBig error-status | Number of SNMP messages with a Too\_big error. A Too\_big error occurs when the length of the received get-response message exceeds the processing capability of the local device. |
| SNMP PDUs which had noSuchName error-status | Number of SNMP packets with a NoSuchName error. |
| ASN.1 or BER errors in the process of decoding | Number of SNMP messages with incorrect codes. |
| MIB objects retrieved successfully | Number of variables requested by the NMS. |
| MIB objects altered successfully | Number of variables set by the NMS. |
| GetRequest-PDU accepted and processed | Number of received GetRequest messages. |
| GetNextRequest-PDU accepted and processed | Number of received GetNextRequest messages. |
| GetBulkRequest-PDU accepted and processed | Number of received GetBulkRequest messages. |
| GetResponse-PDU sent | Number of sent Get response packets. |
| SetRequest-PDU accepted and processed | Number of received SetRequest messages. |
| Trap-PDU sent | Number of sent trap messages. |
| Inform-PDU sent | Number of sent Inform messages. |
| Inform-PDU received with no acknowledgement | Number of Inform messages without acknowledgement. |
| Inform-PDU received with acknowledgement | Number of Inform messages with acknowledgement. |
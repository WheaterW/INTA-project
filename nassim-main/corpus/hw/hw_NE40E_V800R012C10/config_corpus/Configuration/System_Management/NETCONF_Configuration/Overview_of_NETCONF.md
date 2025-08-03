Overview of NETCONF
===================

NETCONF provides mechanisms to install, maintain, and delete the configuration of devices on distributed networks. For example, device configuration can be restored and new configuration data can be added.

#### Definition

The Network Configuration Protocol (NETCONF) is an extensible markup language (XML) based network configuration and management protocol. NETCONF uses a simple remote procedure call (RPC) mechanism to implement communication between a client and a server.

NETCONF provides a method for a network management system (NMS) to remotely manage and monitor devices.


#### Purpose

As networks grow in scale and complexity, the Simple Network Management Protocol (SNMP) can no longer meet carriers' network management requirements, especially configuration management requirements. XML-based NETCONF was developed to meet the demands.

[Table 1](#EN-US_CONCEPT_0139427563__en-us_concept_0139427193_tab_1) lists the differences between SNMP and NETCONF.

**Table 1** Comparison between SNMP and NETCONF
| Item | SNMP | NETCONF |
| --- | --- | --- |
| Configuration management | SNMP does not provide a lock mechanism to prevent the operations performed by multiple users from conflicting with each other. | NETCONF provides a lock mechanism to prevent the operations performed by multiple users from conflicting with each other. |
| Query | SNMP requires multiple interaction processes to query one or more records in a database table. | NETCONF can directly query system configuration data and supports data filtering. |
| Extensibility | Poor. | Good.  * NETCONF is defined based on multiple layers that are independent of one another. When one layer is expanded, its upper layers are least affected. * XML encoding helps expand NETCONF's management capabilities and compatibility. |
| Security | The International Architecture Board (IAB) released SNMPv2 (enhanced SNMP) in 1996, which still has poor security. SNMPv3, released in 2002, provides important security improvements over the previous two versions but is inextensible. This is because SNMPv3 security parameters are dependent upon the security model. | NETCONF uses existing security protocols to ensure network security and is not specific to any security protocols. NETCONF is more flexible than SNMP in ensuring security. NOTE:  NETCONF prefers Secure Shell (SSH) at the transport layer and uses SSH to transmit XML information. |



#### Benefits

NETCONF offers the following benefits:

* Facilitates configuration data management and interoperability between different vendors' devices using XML encoding to define messages and the RPC mechanism to modify configuration data.
* Reduces network faults caused by manual configuration errors.
* Improves the efficiency of system software upgrade performed using a configuration tool.
* Provides high extensibility, allowing different vendors to define additional NETCONF operations.
* Improves data security using authentication and authorization mechanisms.
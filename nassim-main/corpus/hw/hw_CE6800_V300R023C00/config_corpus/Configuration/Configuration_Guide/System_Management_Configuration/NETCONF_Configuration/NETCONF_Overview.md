NETCONF Overview
================

NETCONF Overview

#### Definition

The Network Configuration Protocol (NETCONF) is an extensible markup language (XML)-based network configuration and management protocol. NETCONF uses a simple remote procedure call (RPC) mechanism to implement communication between a client and a server. NETCONF provides a method for a network management station (client), which is a central computer that runs network management software, to remotely manage and monitor devices.

The NMS uses NETCONF to implement local management and perform operations such as adding, modifying, and deleting configurations of remote devices. This protocol allows a device to provide a complete and formal application programming interface (API). Network management applications can use this API to send and receive complete or partial configuration data sets.


#### Purpose

As networks become larger and more complex, the Simple Network Management Protocol (SNMP) can no longer meet the requirements for managing and configuring networks. This is where NETCONF comes into play.

[Table 1](#EN-US_TOPIC_0000001564122025__en-us_concept_0139427193_tab_1) lists the differences between SNMP and NETCONF.

**Table 1** Comparison between SNMP and NETCONF
| Function | SNMP | NETCONF |
| --- | --- | --- |
| Configuration management | SNMP does not provide a lock mechanism when multiple users perform operations on the same configuration. | NETCONF provides a lock mechanism to ensure that operations performed by multiple users do not conflict with each other. |
| Querying | SNMP can be used to query one or more records in a table, requiring multiple interactions. | NETCONF allows you to directly query the configuration data of the system and supports data filtering. |
| Scalability | Poor. | Good.  * The NETCONF protocol framework adopts a hierarchical structure with four independent layers. Extensions to one layer have little impact on the other layers. * XML encoding helps expand NETCONF's management capabilities and system compatibility. |
| Safety | SNMPv2, released by the International Architecture Board (IAB) in 1996, provides only limited security improvements over SNMPv1. SNMPv3, released in 2002, also has major security problems: no encryption capability and no support for security protocol algorithms at the transport layer. | NETCONF uses existing security protocols to ensure network security and is not specific to any security protocols. NETCONF is therefore more flexible than SNMP in security protection. NOTE:  Secure Shell (SSH) is the preferred transport protocol in NETCONF and is used to transmit XML information. |



#### Benefits

* Facilitates configuration data management and interoperability between different vendors' devices by using XML encoding to define messages and using the RPC mechanism to modify configuration data.
* Reduces network faults caused by manual configuration errors.
* Improves the efficiency of tool-based upgrades to system software.
* Provides high extensibility, allowing different vendors to define additional NETCONF operations.
* Improves data security using authentication and authorization mechanisms.

![](public_sys-resources/note_3.0-en-us.png) 

This document is written according to device information obtained under lab conditions and therefore may not cover all scenarios. Due to factors such as version upgrades and differences in device models, the content provided in this document may differ from the information on user device interfaces. Such information takes precedence over the content provided by this document.
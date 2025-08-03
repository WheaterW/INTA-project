Overview of RESTCONF
====================

Overview of RESTCONF

#### Definition

RESTCONF, an HTTP-based protocol, provides RESTful programming interfaces and allows users to add, delete, modify, as well as query network device data.


#### Purpose

Increasing network scale and complexity are driving the growing demand for automated O&M. The Network Configuration Protocol (NETCONF) provides application programming interfaces (APIs) based on the remote procedure call (RPC) mechanism. However, networks are developing faster than NETCONF, necessitating standard programming interfaces that support web application access and network device operations.

RESTCONF is developed based on both NETCONF and HTTP, and it provides core NETCONF functions using HTTP methods. The programming interface complies with the RESTful style of the IT industry and provides users with the capability of efficiently developing web O&M tools.

[Table 1](#EN-US_CONCEPT_0000001512691646__tab_1) compares RESTCONF and NETCONF based on the YANG data model.

**Table 1** Comparison between RESTCONF and NETCONF
| Item | NETCONF+YANG | RESTCONF+YANG |
| --- | --- | --- |
| Transmission channel (protocol) | NETCONF prefers Secure Shell (SSH) at the transport layer and uses SSH to transmit XML information. | RESTCONF accesses device resources based on HTTP. The programming interfaces provided by RESTCONF comply with the RESTful style of the IT industry. |
| Packet format | XML code | XML or JSON code |
| Operation Characteristics | NETCONF operations are complex. For example:   * NETCONF supports addition, deletion, modification, and query, multiple configuration datastores, as well as configuration rollback. * NETCONF supports two-phase configuration validation, that is, parameters are configured and committed before taking effect. | RESTCONF operations are simple. For example:   * RESTCONF supports addition, deletion, modification, and query operations, and it supports only the <running/> configuration database. * The RESTCONF operations take effect immediately, without the need for two-phase submission. |



#### Benefits

* RESTCONF provides RESTful programming interfaces to support web-based development.
* Standard interfaces are compatible with multi-vendor devices, reducing development and maintenance costs.
* RESTCONF provides high extensibility, allowing various vendors to define additional NETCONF operations.
* No NMS tool is required.
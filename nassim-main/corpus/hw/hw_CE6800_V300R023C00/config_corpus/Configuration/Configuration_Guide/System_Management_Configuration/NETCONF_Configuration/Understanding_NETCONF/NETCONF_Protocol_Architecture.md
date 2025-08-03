NETCONF Protocol Architecture
=============================

NETCONF Protocol Architecture

#### NETCONF Protocol Framework

Like the open systems interconnection (OSI) model, the NETCONF protocol framework also uses a hierarchical structure. Each layer encapsulates certain functions and provides services for its upper layer.

This hierarchical structure enables each layer to focus only on a single aspect of NETCONF and reduces the dependencies between different layers. In this way, the impact that internal implementation imposes on other layers can be minimized.

[Table 1](#EN-US_TOPIC_0000001513041970__table21801748161218) describes the four layers of the NETCONF protocol framework.

**Table 1** NETCONF protocol framework
| Layer | Example | Description |
| --- | --- | --- |
| Layer 1: transport | BEEP, SSH, and SSL | The transport layer provides a communication path for interaction between a NETCONF client and server. NETCONF can be carried over any transport protocol that meets the following basic requirements:  * The transport protocol is connection-oriented and establishes a persistent connection between the NETCONF client and server. This connection provides reliable, sequenced data transmission. * The transport layer provides user authentication, data integrity, and security encryption for NETCONF. * The transport protocol provides a mechanism to distinguish the session type (client or server) for NETCONF.   NOTE:  Currently, the device supports only SSH as the transport layer protocol for NETCONF. |
| Layer 2: message layer | <rpc> and <rpc-reply> | The message layer provides a simple RPC request and response mechanism independent of transport protocols. The client encapsulates RPC request information in the <rpc> element and sends it to the server through a secure and connection-oriented session. The server encapsulates RPC reply information (content at the operation and content layers) in the <rpc-reply> element and sends it to the client.  In normal cases, the <rpc-reply> element encapsulates data required by the client or information about a configuration success. If the client sends an incorrect request or the server fails to process a request from the client, the server encapsulates the <rpc-error> element containing detailed error information in the <rpc-reply> element and sends the <rpc-reply> element to the client. |
| Layer 3: operations | <get-config>, <edit-config>, and <notification> | The operations layer defines a series of basic operations used in RPC. These operations constitute basic capabilities of NETCONF. |
| Layer 4: content | Configuration data | The content layer describes configuration data involved in network management. The configuration data depends on vendors' devices.  To date, only the content layer remains to be standardized for NETCONF. This layer has no standard NETCONF data modeling language or data model. |



#### NETCONF Modeling Language

YANG is a data modeling language developed to design NETCONF-oriented configuration data, status data models, RPC models, and notification mechanisms.

The YANG data model is a machine-oriented model interface, which defines data structures and constraints to provide more flexible and complete data description.


#### Encoding Format

XML encoding is used in NETCONF, allowing complex hierarchical data to be expressed in a text format that can be read, saved, and manipulated with both traditional text tools and XML-specific tools.

XML-based network management uses XML to describe managed data and management operations. In this way, management information forms a database that is understandable to computers, allowing them to efficiently process network management data using enhanced management capabilities.

The format of the file header used in XML encoding is **<?xml version="1.0" encoding="UTF-8"?>**, where:

* **<?**: indicates the start of an instruction.
* **xml**: identifies an XML file.
* version="1.0": The XML1.0 standard version is used.
* **encoding**: indicates the character set encoding format. Only UTF-8 encoding is supported.
* **?>**: indicates the end of an instruction.


#### **Communication Modes**

The NETCONF client and server communicate through the RPC mechanism. To implement the communication, a secure and connection-oriented session must be established. After receiving an RPC request from the client, the server processes the request and sends a response message to the client. The RPC request from the client and the response message from the server are encoded in XML format. The XML-encoded <rpc> and <rpc-reply> elements provide a request and response message framework independent of transport layer protocols. [Table 2](#EN-US_TOPIC_0000001513041970__tab_1) lists some basic RPC elements.

**Table 2** Element description
| Element | Description |
| --- | --- |
| <rpc> | Encapsulates a request that the client sends to the NETCONF server. |
| <rpc-reply> | Encapsulates a response message that the NETCONF server sends in reply to each <rpc> request it receives. |
| <rpc-error> | Notifies a client of an error that occurs during processing of an <rpc> request. The server encapsulates the <rpc-error> element in the <rpc-reply> element and sends the <rpc-reply> element to the client. |
| <ok> | Notifies a client that no errors occur during processing of an <rpc> request. The server encapsulates the <ok> element in the <rpc-reply> element and sends the <rpc-reply> element to the client. |



#### Capability Set

NETCONF defines the syntax and semantics of capabilities. The protocol allows the client and server to notify each other of supported capabilities. The client can send the operation requests only within the capability range supported by the server.

A capability set includes basic and extended functions implemented based on NETCONF. The NETCONF capability set includes a standard capability set defined by the IETF standards organization. In addition, a device can use the capability set to add a protocol operation so that the operation range of the existing configuration object is extended.

Each capability is identified by a unique uniform resource identifier (URI). The URI format of the capability set defined by NETCONF is as follows:

```
urn:ietf:params:xml:ns:netconf:capability:{name}:{version}
```

In addition to the NETCONF-defined capability set, a vendor can define additional capability sets to extend management functions. A module that supports the YANG model needs to add YANG notifications to Hello messages before sending the messages. The message format is as follows:

```
<capability>urn:huawei:yang:huawei-ifm?module=huawei-ifm&amp;revision=2022-03-30</capability>
```

#### Configuration Database

A configuration database is a collection of complete configuration parameters for a device. [Table 3](#EN-US_TOPIC_0000001513041970__tab_2) describes NETCONF-defined configuration databases.

**Table 3** NETCONF-defined configuration databases
| Configuration Database | Description |
| --- | --- |
| <running/> | Stores the device's currently running configuration, status information, and statistics.  If the NETCONF server does not support the candidate capability, this configuration database is the only standard database that is mandatory.  To support modification of the <running/> configuration database, a device must have the writable-running capability. |
| <candidate/> | Stores the configuration data to be run on a device.  An administrator can perform operations on the <candidate/> configuration database. Any change to the <candidate/> database does not directly affect the configurations currently running on the device.  To support the <candidate/> configuration database, a device must have the candidate capability.  NOTE:  The <candidate/> configuration databases supported by devices do not allow inter-session data sharing. Therefore, the configuration of the <candidate/> configuration database does not require additional locking operations. |
| <startup/> | Stores the configuration data loaded during device startup, which is similar to the saved configuration file.  To support the <startup/> configuration database, a device must have the distinct startup capability. |
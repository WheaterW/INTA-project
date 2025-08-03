Understanding SNMPv3
====================

The SNMPv3 architecture embodies the model-oriented design and simplifies the addition and modification of functions. SNMPv3 features the following:

* Strong adaptability: SNMPv3 is applicable to multiple operating systems. It can manage both simple and complex networks.
* Good extensibility: New models can be added as needed.
* High security: SNMPv3 provides multiple security processing models.

SNMPv3 has four models: message processing and control model, local processing model, user security model, and view-based access control model.

Unlike SNMPv1 and SNMPv2, SNMPv3 can implement access control, identity authentication, and data encryption using the local processing model and user security model.

#### Message Processing and Control Model

A message processing and control model is responsible for constructing and analyzing SNMP messages and determining whether the messages can pass through a proxy server. In the message constructing process, the message processing and control model receives a PDU from a dispatcher and then sends it to the user security model to add security parameters to the PDU header. When analyzing the received PDU, the user security model must first process the security parameters in the PDU header and then send the unpacked PDU to the dispatcher for processing.


#### Local Processing Model

A local processing model is primarily used to implement access control, data packaging, and data interruption. Access control is implemented by setting information related to the agent so that the management processes on different workstations can have different access permissions to the agent. This process is implemented through PDU transmission. There are two commonly used access control policies: restricting the workstation from delivering some commands to the agent, and specifying the details in the MIB of the agent that the workstation can access. Access control policies must be predefined. SNMPv3 flexibly defines access control policies using the syntax with various parameters.


#### User Security Model

A user security model provides identity authentication and data encryption services. The two preceding services require that the workstation and agent use a shared key.

* Identity authentication: A process in which the agent (or workstation) confirms whether the received message is from an authorized workstation (or agent) and whether the message is changed during transmission. HMAC is an effective tool that is widely applied on the Internet to generate the message authentication code using the security hash function and shared key.
* Data encryption: The workstation uses the key to calculate the CBC code and then adds a CBC code to the message while the agent uses the same key to decrypt the authentication code and then obtains the actual information. Similar to identity authentication, the encryption requires that the workstation and agent share the same key to encrypt and decrypt the message.

![](public_sys-resources/note_3.0-en-us.png) 

To improve system security, you are advised to configure different authentication and encryption passwords for an SNMP user.



#### View-Based Access Control Model

A view-based access control model is mainly used to restrict the access permissions of user groups to specific views. You must pre-configure a view and specify its permission. When you configure a user or a user group, load this view to implement read/write permission control or the trap function (for SNMPv3).
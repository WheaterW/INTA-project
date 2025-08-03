NETCONF Message Formats
=======================

NETCONF Message Formats

#### Request Message

[Figure 1](#EN-US_TOPIC_0000001513161934__fig_dc_vrp_netconf_feature_001901) shows the structure of a complete NETCONF request message.

**Figure 1** Structure of a NETCONF YANG request message  
![](figure/en-us_image_0000001512683002.png)
A NETCONF request message consists of three layers. [Table 1](#EN-US_TOPIC_0000001513161934__table5321308495) describes the fields in a NETCONF request message.

* Message: The message layer provides a simple and independent mechanism of transmitting frames for RPC messages. The client encapsulates an RPC request into an <rpc> element and sends it to the server, which encapsulates the result of processing this request into the <rpc-reply> element and sends it to the client.
* Operations: The operations layer defines a set of basic NETCONF operations. These operations are invoked by RPC methods that are based on XML encoding parameters.
* Content: The content (managed object) layer defines a configuration data model. Currently, mainstream configuration data models include the YANG model.

**Table 1** Fields in a NETCONF message
| Field | Description |
| --- | --- |
| message-id | Indicates the information code. The value is specified by the client that initiates the RPC request. After receiving the RPC request message, the server saves the message-id attribute, which is used in an <rpc-reply> message to be generated. |
| xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" | Indicates the NETCONF XML namespace. **base** indicates that basic operation types are supported.  base1.0: Indicates that the <running/> configuration database is supported. Basic operations, such as <get-config>, <get>, <edit-config>, <copy-config>, <delete-config>, <lock>, <unlock>, <close-session>, and <kill-session>, are defined. You can set the <error-option> parameter to **stop-on-error**, **continue-on-error**, or **rollback-on-error**.  base1.1: Indicates an upgrade of base1.0, with the following changes:   * The remove operation is added to the operation attribute of <edit-config>. * The well-known error-tag malformed-message is added, and the well-known error-tag partial-operation is obsolete. * The namespace wildcarding mechanism is added for subtree filtering. * The chunked framing mechanism is added to resolve the security issues in the end-of-message (EOM) mechanism.   If you want to perform an operation in base1.1, the client must support base1.1 so that this capability can be advertised during capability set exchange. |
| <edit-config> | Indicates the operation type. |
| <target> | Indicates the target data set to be operated:   * running * candidate * startup |
| <default-operation> | Indicates the default operation type. |
| <error-option> | Indicates the mode for processing subsequent operations if an error occurs during an <edit-config> operation. The options are as follows:   * **stop-on-error**: stops the operation when an error occurs. * **continue-on-error**: records the error information and continues the execution after an error occurs. If an error occurs, the NETCONF server returns an <rpc-reply> message to the client, indicating an operation failure. * **rollback-on-error**: stops the operation after an error occurs and rolls back the configuration to the state before the <edit-config> operation is performed. This operation is supported only when the device supports the rollback-on-error capability. |
| <config> | Indicates a group of hierarchical configuration items defined in the data model. The configuration items must be placed in the specified namespace and meet the constraints of that data model, as defined by its capability set. |
| ]]>]]> | Indicates the end character of an XML message.  NOTE:  When a server exchanges XML packets with a client, the packets must be concluded with the end character **]]>]]>**. Otherwise, the device cannot identify the XML packets and does not respond to them. By default, the end character is automatically added to XML messages sent by a device. The examples provided in this document omit the end character for brevity.  If the capability set in the <hello> elements contains base1.1, the RPC messages in the YANG model support the chunk format. Messages in chunk format can be fragmented. The end character is **\n##\n**. |



#### Response Message

If a request message is successfully executed, the device returns a successful response. Otherwise, the device returns a failed response.

* For a successful response, an <rpc-reply> message carrying the <ok> element is returned.
  ```
  <?xml version="1.0" encoding="utf-8"?>
  <rpc-reply xmlns:nc-ext="urn:huawei:yang:huawei-ietf-netconf-ext"
             xmlns="urn:ietf:params:xml:ns:netconf:base:1.0"
             message-id="10"
             nc-ext:flow-id="33"
             nc-ext:flow-id-time="2022-05-11T10:19:30Z">
    <ok/></rpc-reply>
  ```
* For a failed response, an <rpc-reply> message carrying the <rpc-error> element is returned.
  ```
  <?xml version="1.0" encoding="utf-8"?
  <rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="5">
    <rpc-error>
      <error-type>application</error-type>
      <error-tag>data-exists</error-tag>
      <error-severity>error</error-severity>
      <error-app-tag>43</error-app-tag>
      <error-path xmlns:acl="urn:huawei:yang:huawei-acl">acl:acl/acl:groups/acl:group[acl:identity='2000']</error-path>
      <error-message xml:lang="en">Invalid ACL number:Number can not be the number of an existent ACL.</error-message>
      <error-info xmlns:nc-ext="urn:huawei:yang:huawei-ietf-netconf-ext">
        <nc-ext:error-info-code>8123</nc-ext:error-info-code>
      </error-info>
    </rpc-error>
  </rpc-reply>
  ```
  
  **Table 2** Description of each field in a response message
  | Field | Description |
  | --- | --- |
  | xmlns | Indicates the NETCONF XML namespace. |
  | message-id | Indicates the information code. The value is specified by the client that initiates the RPC request. After receiving the RPC request message, the server saves the message-id attribute, which is used in an <rpc-reply> message to be generated. |
  | flow-id | Indicates the configuration change ID.  NOTE:  The **flow-id** field is carried only in the **running** data set of the <edit-config> operation or in the response packet of the <commit> or <sync-full> operation. |
  | flow-id-time | Indicates the time when the configuration change ID is generated.  NOTE:  The **flow-id-time** field is carried only in the **running** data set of the <edit-config> operation or the response packet of the <commit> operation. |
  | <error-type> | Defines the protocol layer at which an error occurs. The value can be transport, RPC, protocol, or application. |
  | <error-tag> | Indicates the error information. |
  | <error-severity> | Indicates the severity of an error. The value can be error or warning. |
  | <error-app-tag> | Indicates a specific error type. This element is not present if no <error-tag> is associated with the error type. |
  | <error-path> | Indicates the location where the error occurs and the name of the file where the error occurs. |
  | <error-message> | Indicates the description of the error. |
  | <error-info> | Indicates the error information about a specific protocol or data model. This element is not present if the correct <error-info> is not provided. |
  | <error-paras> | Indicates an error parameter list. |
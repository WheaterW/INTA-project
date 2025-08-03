Constructing RESTCONF Packets Based on the YANG Model
=====================================================

RESTCONF packets are classified as request packets and response packets. Request packets are sent by the HTTP client and need to be constructed. Response packets are automatically generated and sent by the HTTP server based on the request packets. In a RESTCONF request packet, the URI and request body need to be constructed.

#### Method of Constructing the URI

An HTTP-based URI is in the following format: http://<host-ip>:<port>/restconf/<node-type>/<path>?<query>.

An HTTPS-based URI is in the following format: https://<host-ip>:<port>/restconf/<node-type>/<path>?<query>.

**Table 1** Parameters in the URI format
| Parameter | Mandatory or Optional | Description |
| --- | --- | --- |
| <host-ip> | Mandatory | IP address of the HTTP server. |
| <port> | Mandatory | Port number used by the HTTP server for HTTP or HTTPS.   * The default port number for HTTP is 80. To specify a port number, run the [**server port**](cmdqueryname=server+port) *port-number* command. * The default port number for HTTPS is 443. To specify a port number, run the [**secure-server port**](cmdqueryname=secure-server+port) *port-number* command. |
| <node-type> | Mandatory | The parameter value varies according to the type of the node in the YANG model.   * If the node is of the RPC type, the <node-type> value is **operations**. * If the node is of other types, the <node-type> value is **data**. |
| <path> | Mandatory | Resource path defined based on the YANG model. |
| ?<query> | Optional | Query parameter. For details, see [Query Parameters](vrp_restconf_cfg_0014.html). |

**The principles for constructing <path> are as follows:**

* The node path based on the YANG model is the XPath. The child node and parent node are separated by a slash (/). For details about the XPaths of nodes in the YANG model, see **Secondary Development** - **YANG API Reference**.
* For the first node or a node that is not in the same YANG model as the parent node, add <module> as the prefix. **module** indicates the namespace, that is, the YANG file module name. If a child node and its parent node belong to the same YANG model, <module> can be omitted for the child node.
* For a list node, you can add =<key> to the end of the list node to specify an instance. If a list node has multiple keys, use commas (,) to separate the keys.

For example, the corresponding XPath of the YANG node for querying the ARP entries learned by VLANIF100 is /ifm:ifm/ifm:interfaces/ifm:interface/arp:arp-entry. In this case, construct <path> based on the XPath.

In the preceding example, ifm:ifm is the first node, and needs to have <module> as the prefix. The YANG module name corresponding to this node is huawei-ifm. The ifm:interfaces and ifm:interface nodes belong to the same YANG model as the ifm:ifm node. Therefore, <module> can be omitted for them. The arp:arp-entry node does not belong to the same YANG model as the ifm:ifm node, and therefore needs to have <module> as the prefix. The YANG module name corresponding to this node is huawei-arp. The ifm:interface node is a list node, its key is a leaf node (name), and the value of name is VLANIF100. In this case, <path> is constructed as follows: huawei-ifm:ifm/interface/interfaces/interface=VLANIF100/huawei-arp:arp-entry.

Some characters in a URI have specific meanings. For example, the slash (/) indicates a separator. If such characters need to be used as common characters, they must be encoded. [Table 2](#EN-US_CONCEPT_0000001667408405__table1953411208) describes the escape characters in the URI. For example, 100GE1/0/1 is displayed as 100GE1%2F0%2F1 in the URI.

**Table 2** Escape characters in the URI
| Character | Escape Code |
| --- | --- |
| ! | %21 |
| " | %22 |
| # | %23 |
| $ | %24 |
| % | %25 |
| & | %26 |
| ' | %27 |
| ( | %28 |
| ) | %29 |
| \* | %2A |
| + | %2B |
| , | %2C |
| / | %2F |
| : | %3A |
| ; | %3B |
| = | %3D |
| ? | %3F |
| @ | %40 |
| [ | %5B |
| ] | %5D |



#### Method of Constructing the Message Body of a RESTCONF Request Packet

The method of constructing the message body of a request packet varies depending on the RESTCONF operation method. For details, see [Table 3](#EN-US_CONCEPT_0000001667408405__table753910316818).

**Table 3** Message bodies of RESTCONF request packets
| RESTCONF Operation Method | Request Message Body |
| --- | --- |
| OPTIONS | None |
| GET | None |
| HEAD | None |
| POST (Create) | Data to be created. The outermost node of the message body must be the child node of the node corresponding to <path>. For example, if <path> is huawei-snmp:snmp/usm-users and the subnode of usm-users in the YANG file is usm-user, the outermost node of the request body is usm-user. |
| POST (RPC) | RPC request data to be invoked. The outermost node of the message body must be the child node of the node corresponding to the URI. For example, if <path> is huawei-snmp:snmp/usm-users and the subnode of usm-users in the YANG file is usm-user, the outermost node of the request body is usm-user. |
| PATCH | Data to be modified. The outermost node of the message body must be the node corresponding to <path>. For example, if <path> is huawei-snmp:snmp/usm-users, the outermost node of the message body is usm-users. |
| DELETE | None |

RESTCONF request packets can be in JSON or XML format. [Table 4](#EN-US_CONCEPT_0000001667408405__table5933131914812) describes the escape characters in JSON request packets, and [Table 5](#EN-US_CONCEPT_0000001667408405__table20589185184918) describes the escape characters in XML request packets.

**Table 4** Escape characters in JSON request packets
| Character | Escape Code |
| --- | --- |
| " | \" |
| \ | \\ |
| / | \/ |
| Newline | \n |
| Carriage return | \r |
| Horizontal tab | \t |


**Table 5** Escape characters in XML request packets
| Character | Escape Code |
| --- | --- |
| & | &amp; |
| < | &lt; |
| > | &gt; |
| " | &quot; |
| ' | &apos; |
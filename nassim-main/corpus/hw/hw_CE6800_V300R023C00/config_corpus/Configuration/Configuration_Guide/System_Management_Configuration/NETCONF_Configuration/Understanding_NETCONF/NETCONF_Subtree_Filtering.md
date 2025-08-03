NETCONF Subtree Filtering
=========================

NETCONF Subtree Filtering

#### Overview

Subtree filtering is a mechanism that allows an application to query particular data for a <get> or <get-config> operation.

Subtree filtering provides a small set of filters for inclusion, simple content exact-match, and selection. The NETCONF agent does not need to use any semantics specific to any particular data model during processing, allowing for simple and centralized implementation policies.


#### Subtree Filter Components

Each node specified in subtree filtering represents a filter. The filter only selects nodes associated with the basic data model of a specified database on the NETCONF server. A node matching any filtering rule and element hierarchy is selected. [Table 1](#EN-US_TOPIC_0000001563762333__tab_3) describes subtree filter components.

**Table 1** Subtree filter components
| Component | Description |
| --- | --- |
| Namespace selection | If namespaces are used, the filter output will include only elements from the specified namespace. |
| Containment node | A containment node is a node that contains child elements within a subtree filter.  For each containment node specified in a subtree filter, all data model instances that are exact matches for the specified namespaces and element hierarchy are included in the filter output. |
| Content match node | A content match node is a leaf node that contains simple content within a subtree filter.  This node is used to select some or all of its relevant nodes for filter output and represents an exact-match filter of the leaf node element content. |
| Selection node | A selection node is an empty leaf node within a subtree filter.  This node represents an explicit selection filter of the underlying data model. Presence of any selection nodes within a set of sibling nodes will cause the filter to select the specified subtrees and suppress automatic selection of the entire set of sibling nodes in the underlying data model. |

* Namespace selection
  
  If the XML namespace associated with a specific node in the <filter> element is the same as that in the underlying data model, the namespace is matched.
  
  ```
  <filter type="subtree">
   <nacm xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm"/>
  </filter>
  ```
  
  In this example, the <nacm> element is a selection node. If the node namespace complies with **urn:ietf:params:xml:ns:yang:ietf-netconf-acm**, the node and its child nodes will be included in the filter for output.
* Containment node
  
  The child element of a containment node can be a node of any type, including another containment node. For each containment node specified in the subtree filter, all data model instances that completely match the specified namespace and element hierarchy, and any attribute-matching expression are included in the output.
  
  ```
  <filter type="subtree">
   <nacm xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm">
    <rule-list/>
   </nacm>
  </filter>
  ```
  
  In this example, the <rule-list> element is a containment node.
* Content match node
  
  A leaf node that contains simple content is called a content match node. It is used to select some or all of its sibling nodes for filter output and represents exact match of the leaf node element content.
  
  ```
  <filter type="subtree">
   <nacm xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm">
    <rule-list>
     <name>fred</name>
    </rule-list>
   </nacm>
  </filter>
  ```
  
  In this example, the <rule-list> node is a containment node, and the <name> node is a content match node. Because the sibling nodes of the <name> node are not specified, only <rule-list> nodes that comply with namespace **urn:ietf:params:xml:ns:yang:ietf-netconf-acm**, with their element hierarchies matching the **name** element and their values being **fred**, can be included in the filter output. All sibling nodes of the <name> node are included in the filter output.
  
  ![](public_sys-resources/note_3.0-en-us.png) 
  
  The support-filter statement in the YANG model indicates whether filtering based on node content is supported when a node is being operated.
  
  + For key nodes, filtering based on node content is supported by default.
  + For non-key nodes, filtering based on node content is not supported by default. If the value of the support-filter statement is set to **true** for a non-key node, filtering based on node content is supported.
* Selection node
  
  Selection nodes represent a basic data model for an explicit selection of filters. If any selection node appears in a group of same-level sibling nodes, the filter selects a specified subtree and suppresses the automatic selection of the entire sibling node set in the basic data model. In a filtering expression, an empty tag (such as <rule-list/>) or an expression with explicit start and end tags (such as <rule-list> </rule-list>) can be used to specify an empty leaf node. In this case, all blank characters will be ignored.
  
  ```
  <filter type="subtree">
   <nacm xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm">
    <rule-list/>
   </nacm>
  </filter>
  ```
  
  In this example, the <nacm> node is a containment node, and the <rule-list> node is a selection node. The <rule-list> node can be included for filter output only when the <rule-list> node complies with namespace **urn:ietf:params:xml:ns:yang:ietf-netconf-acm** and is contained in the <nacm> element in the root directory of the configuration database.

#### Subtree Filter Processing

First, the subtree filter output is set as empty. Each subtree filter can contain one or more data model segments, each of which represents one of the selected output parts of the selected data model. Each subtree data segment is composed of data models supported by the NETCONF server. If the entire subtree data segment completely matches part of the data models supported by the NETCONF server, all nodes and child nodes of the subtree data segment are selected and output to the query result.

* If no filter is used, all data in the current data model is returned in the query result.
  
  RPC request
  
  ```
  <rpc message-id="101"
  xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
   <get/>
  </rpc>
  ```
  
  RPC reply
  
  ```
  <rpc-reply message-id="101"
  xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
   <data>
    <!-- ... entire set of data returned ... -->
   </data>
  </rpc-reply>
  ```
* If an empty filter is used, the query result contains no data output, in that no content match or selection node is specified.
  
  RPC request
  
  ```
  <rpc message-id="101"
  xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
   <get>
    <filter type="subtree">
    </filter>
   </get>
  </rpc>
  ```
  
  RPC reply
  
  ```
  <rpc-reply message-id="101"
  xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
   <data>
   </data>
  </rpc-reply>
  ```
* Multi-subtree filtering
  
  The following example uses the **root**, **fred**, and **barney** subtree filters.
  
  The **root** subtree filter contains one containment nodes (<rule-list>), one content match node (<name>), and one selection node (<rule>). As for subtrees that meet selection criteria, only <rule> is selected.
  
  The **fred** subtree filter contains two containment nodes (<rule-list> and <rule>), one content match node (<name>), and one selection node (<module-name>). As for subtrees that meet the selection criteria, only the <module-name> element in <rule> is selected.
  
  The **barney** subtree filter contains two containment nodes (<rule-list> and <rule>), two content match nodes (<name> and <group>), and one selection node (<action>). User **barney** does not belong to the **netconf** group and does not comply with the subtree filtering rule. Therefore, the entire subtree of **barney** (including its parent node <rule-list>) is not selected.
  
  RPC request
  
  ```
  <rpc message-id="101"
  xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <get-config>
      <source>
        <running />
      </source>
      <filter type="subtree">
        <nacm xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm">
          <rule-list>
            <name>root</name>
            <rule />
          </rule-list>
          <rule-list>
            <name>fred</name>
            <rule>
              <module-name />
            </rule>
          </rule-list>
          <rule-list>
            <name>barney</name>
            <group>netconf</group>
            <rule>
              <action />
            </rule>
          </rule-list>
        </nacm>
      </filter>
    </get-config>
  </rpc>
  ```
  
  RPC reply
  
  ```
  <rpc-reply message-id="101"
  xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <data>
      <nacm xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm">
        <rule-list>
          <name>root</name>
          <rule>
            <name>aaa</name>
            <module-name>huawei-aaa</module-name>
            <access-operations>*</access-operations>
            <action>permit</action>
          </rule>
        </rule-list>
        <rule-list>
          <name>fred</name>
          <rule>
            <name>ifm</name>
            <module-name>huawei-ifm</module-name>
          </rule>
        </rule-list>
      </nacm>
    </data>
  </rpc-reply>
  ```
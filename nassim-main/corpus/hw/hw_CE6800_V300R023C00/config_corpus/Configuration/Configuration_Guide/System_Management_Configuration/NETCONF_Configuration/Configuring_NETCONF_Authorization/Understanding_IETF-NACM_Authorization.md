Understanding IETF-NACM Authorization
=====================================

Understanding IETF-NACM Authorization

#### Overview

IETF-NACM provides simple and easy-to-configure database access control rules. It helps flexibly manage specific users' permissions to perform NETCONF operations and access NETCONF resources.

The YANG model defines the capability in the **ietf-netconf-acm.yang** file.

IETF-NACM supports the following functions:

* Protocol operation authorization: authorizes users to perform specific NETCONF operations.
  
  Such operations include <get>, <get-config>, <edit-config>, <copy-config>, <delete-config>, <lock>, and <action>.
* Module authorization: authorizes users to access specific feature modules.
* Data node authorization: authorizes users to query and modify specific data nodes.
* Notification authorization: authorizes a system to report specified alarms or events through the notification mechanism.
* Action authorization: authorizes users to define operations for data nodes through "action" statements.
* Emergency session recovery: authorizes users to directly initialize or repair the IETF-NACM authorization configuration without the restriction of access control rules.
  
  Emergency session recovery is a process in which a management-level user or a user in the **manage-ug** group bypasses the access control rule and initializes or repairs the IETF-NACM authorization configuration.
  
  Management-level users are level-3 users.

![](public_sys-resources/note_3.0-en-us.png) 

By default, IETF-NACM authorization is disabled and the Huawei-NACM authorization process is followed. If IETF-NACM authorization is enabled, the IETF-NACM authorization process is followed.

If IETF-NACM authorization is enabled, this process is followed, and the access permission on **get/ietf-yang-library** must be enabled during session establishment. Otherwise, session establishment fails due to a lack of permissions.



#### Data Node Access

The access control permissions of IETF-NACM apply only to NETCONF databases (<candidate/>, <running/>, and <startup/>). The local or remote file or database accessed using the <url> parameter is not controlled by IETF-NACM.

The access permissions on data nodes are as follows:

* Create: allows a client to add new data nodes to a database.
* Read: allows a client to read a data node from a database or receive notification events.
* Update: allows a client to update existing data nodes in a database.
* Delete: allows a client to delete a data node from a database.
* Exec: allows a client to perform protocol operations.

![](public_sys-resources/note_3.0-en-us.png) 

Authorization is performed only for the delivered operations (it is not performed for all the changed nodes in the model tree). For example, when a delete operation is performed for a parent node, this operation automatically applies to its child nodes without authorization. In this case, the data of both the parent node and its child nodes is deleted.




#### Components of IETF-NACM

[Table 1](#EN-US_TOPIC_0000001512842446__tab_dc_vrp_feature_netconf_0001) describes the components and functions of IETF-NACM.

**Table 1** Description of IETF-NACM components
| Name | Description |
| --- | --- |
| User | User defined in the NACM view. The user must be an SSH user.  IETF-NACM authorizes only users. User authentication is implemented in AAA. |
| Group | Group defined in the NACM view. This group instead of a user performs protocol operations in a NETCONF session.  The group identifier is a group name, which is unique on the NETCONF server.  A user can be a member of multiple groups. |
| Global execution control | Execution control can be:   * enable-nacm: enables or disables the IETF-NACM authorization function. After IETF-NACM authorization is enabled, all requests are checked. Only the requests allowed by the control rules can be executed. After IETF-NACM authorization is disabled, the HUAWEI-NACM authorization process is followed. * read-default: sets the permission to view configuration databases and notifications. If the value is set to **permit**, NETCONF databases and notification events can be viewed. If the value is set to **undo permit**, NETCONF databases or notification events cannot be viewed. * write-default: sets the permission to modify configuration databases. If the value is set to **permit**, NETCONF databases can be modified. If the value is set to **undo permit**, NETCONF databases cannot be modified. * exec-default: sets the default execution permission for RPC operations. If the value is set to **permit**, NETCONF operations can be performed. If the value is set to **undo permit**, NETCONF operations cannot be performed. |
| Access control rule | There are five access control rules:   * Module name: specifies the control rule of the YANG module, which is identified using a module name.  For example, **ietf-netconf**. * Protocol operation: specifies the control rule of a protocol operation, which is identified using an RPC operation name defined in the YANG file.  For example, <get> or <get-config>. * Data node: specifies the control rule of a data node and whether an "action" statement can be used to define operations for the data node. The data node is identified using the XPath defined in the YANG file.  For example, **/ietf-netconf-acm:nacm/ietf-netconf-acm:rule-list**. * Notification: specifies the control rule of a notification event, which is identified using an alarm or event name defined in the YANG file.  For example, **netconf-config-change** defined by **ietf-netconf-notifications**. * Access control operation permission: specifies the control rule of an operation type for objects of NACM authorization.  For example, create, delete, read, update, and exec. |



#### Implementation

After a NETCONF session is established and a user passes the authentication, the NETCONF server controls access permissions based on the username, group name, and NACM authorization rule list. Authorization rules are associated with users through the user group. The administrator of a user group can manage the permissions of users in the group.

* An IETF-NACM user is associated with an IETF-NACM user group. After users are added to a user group, they have the same permissions.
* An IETF-NACM user group is associated with an IETF-NACM authorization rule list.
* An IETF-NACM authorization rule list is associated with IETF-NACM authorization rules.
  
  Various authorization rules can be added to an IETF-NACM authorization rule list in the format of combinations. Users associated with the list can use the rules it contains.

#### IETF-NACM Authorization Process

[Figure 1](#EN-US_TOPIC_0000001512842446__fig_feature_image_notification) shows the IETF-NACM authorization process.

**Figure 1** Process of IETF-NACM authorization  
![](figure/en-us_image_0000001513042210.png)

When a user group and an authorization rule list are traversed, if the username that is the same as that carried in the request is not found or no rule that matches the requested operation is detected, the operation performed varies with the authorized content. For details, see [Table 2](#EN-US_TOPIC_0000001512842446__tab_dc_vrp_feature_netconf_0002).

**Table 2** Operations performed for different authorized contents
| Authorized Content | Operation |
| --- | --- |
| Protocol operation | * If the RPC operation defined in the YANG file contains the "nacm:default-deny-all" statement, the RPC request is rejected. * If the requested operation is <kill-session> or <delete-config>, the RPC request is rejected. * If the user has the default execution permission of the RPC operation, the RPC request can be executed. Otherwise, the RPC request is rejected. |
| Data node | * If the definition of the data node contains the "nacm:default-deny-all" statement, the data node does not support the read or write operation. * If the definition of the data node contains the "nacm:default-deny-write" statement, the data node does not support the write operation. * If the user has the query permission, the read operation is allowed. Otherwise, the read operation is rejected. * If the user has the configuration permission, the write operation is allowed. Otherwise, the write operation is rejected. |
| Notification | * If the notification statement contains the "nacm:default-deny-all" statement, the notification cannot be reported. * If the user has the query permission, the notification can be reported. Otherwise, the notification is discarded. |
| Action | * If the data node definition contains the **nacm:default-deny-all** statement, no **action** statement can be used to define operations for the data node. * If an **action** statement can be used to define operations for a data node, the data node and each of its parent nodes must have the read permission, and the data node must also have the execute permission. If either of the two permissions is absent, operations for the data node cannot be defined using the **action** statement. |
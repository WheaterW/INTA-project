(Optional) Configuring Access Control on a BAS Interface
========================================================

This section describes how to configure a BAS interface to filter access users so that only specified users are allowed to access the Router.

#### Context

To filter users based on source MAC addresses, configure an ACL rule. When a DHCP or PPP user requests to go online, match the user's source MAC address against the ACL rule. If matched, the user is allowed to go online.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**acl**](cmdqueryname=acl) { **name** *link-acl-name* { **link** | [ **link** ] **number** *link-acl-number* } | [ **number** ] *link-acl-number* } [ **match-order** { **config** | **auto** } ]
   
   
   
   The ACL view is displayed.
3. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] { **deny** | **permit** } **source-mac** *source-mac* *sourcemac-mask*
   
   
   
   An ACL rule is configured.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   BAS interfaces support only ACLs in the range of 4000 and 4999.
   
   BAS interfaces support only ACL rules based on users' source MAC addresses. The source MAC address for DHCP users is the hardware address carried in DHCP packets.
   
   
   When a BAS interface uses a filter-policy to filter users, note the following:
   * If the action specified in the ACL rule is **permit**, only users matching the rule are allowed to access the Router.
   * If the action specified in the ACL rule is **deny**, users matching the rule are not allowed to access the Router, and the other users are allowed to access the Router.
   * If an ACL has no rules configured, the BAS interface that references this ACL does not filter access users based on users' MAC addresses.
   * If the ACL referenced by a BAS interface does not exist, the BAS interface does not filter access users based on users' MAC addresses.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
5. (Optional) Run [**ppp keepalive slow**](cmdqueryname=ppp+keepalive+slow) **acl** *acl-num* **source-mac**
   
   
   
   PPP slow reply is configured for PPP echo packets with a specified MAC address.
6. Run [**interface**](cmdqueryname=interface) *interface-type interface-number* [*. subinterface-number* ]
   
   
   
   The interface view is displayed.
7. Run [**bas**](cmdqueryname=bas)
   
   
   
   A BAS interface is created and the BAS interface view is displayed.
8. Run [**filter-policy acl**](cmdqueryname=filter-policy+acl) *acl-number* **dhcp**
   
   
   
   The BAS interface is configured to filter users based on ACL rules.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * Before running the [**filter-policy acl**](cmdqueryname=filter-policy+acl) command, the BAS interface must already have the [**access-type**](cmdqueryname=access-type) command configured.
   * An access type can be bound to only one ACL on an interface.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
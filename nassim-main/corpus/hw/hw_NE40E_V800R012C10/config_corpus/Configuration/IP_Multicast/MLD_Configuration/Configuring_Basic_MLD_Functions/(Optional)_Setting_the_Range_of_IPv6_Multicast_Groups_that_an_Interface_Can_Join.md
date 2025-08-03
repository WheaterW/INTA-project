(Optional) Setting the Range of IPv6 Multicast Groups that an Interface Can Join
================================================================================

To limit the range of IPv6 multicast groups that an interface can join, configure a filtering policy on the multicast device's interface connected to the user network segment. Then, the interface can join only IPv6 multicast groups that are permitted in this policy.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Configure a basic or an advanced ACL6 as needed.
   
   
   * Configure a basic ACL6.
     
     1. Run the [**acl ipv6**](cmdqueryname=acl+ipv6) [ **number** ] *basic-acl6-number* [ **match-order** { **auto** | **config** } ] command to create a basic ACL6 and enter the ACL6 view.
     2. Run the [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment** | **source** { *source-ipv6-address* *prefix-length* | *source-ipv6-address*/*prefix-length* | **any** } ] \* command to configure a rule for the basic ACL6.
   * Configure an advanced ACL6.
     1. Run the [**acl ipv6**](cmdqueryname=acl+ipv6) { **name** *advance-acl6-name* [ **advance** | [ **advance** ] **number** *advance-acl6-number* ] | [ **number** ] *advance-acl6-number* } [ **match-order** { **config** | **auto** } ] command to create an advanced ACL6 and enter the corresponding ACL6 view.
     2. Run the [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } **ipv6** [ **destination** { *destination-ipv6-address* *prefix-length* | *destination-ipv6-address*/*prefix-length* | **any** } | **source** { *source-ipv6-address* *prefix-length* | *source-ipv6-address*/*prefix-length* | **any** } ] \* command to configure a rule for the advanced ACL6.
   
   If a basic ACL6 is used, run the [**rule**](cmdqueryname=rule) command and set the **source** parameter to set the range of multicast groups that hosts can join on an interface
   
   If an advanced ACL6 is used, run the [**rule**](cmdqueryname=rule) command, set the **source** parameter to sources address that is allowed to send multicast data to multicast groups, and set the **destination** parameter to a multicast group address.
3. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The view of the interface connected to the user network segment is displayed.
4. Run [**mld group-policy**](cmdqueryname=mld+group-policy) { *acl6-number* | **acl6-name** *acl6-name* } [ **1** | **2** ]
   
   
   
   The range of IPv6 multicast groups that hosts can join on the interface is configured.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * If a multicast group matches an ACL rule and the action is **permit**, the interface allows hosts to join this group.
   * If a multicast group matches an ACL rule and the action is **deny**, the interface does not allow hosts to join this group.
   * If a multicast group does not match any ACL rule, the interface does not allow hosts to join this group.
   * If a specified ACL does not exist or contain rules, the interface does not allow hosts to join any multicast group.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
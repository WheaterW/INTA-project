Setting the Range of Multicast Groups that an Interface Can Join
================================================================

To limit the range of multicast groups that an interface can join, configure an IGMP group policy. Then, the interface can join only IGMP groups that are permitted in this policy.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Configure a basic or an advanced ACL as needed.
   
   
   * Configure a basic ACL.
     
     1. Run [**acl**](cmdqueryname=acl) [ **number** ] *basic-acl-number* [ **match-order** { **auto** | **config** } ]
        
        A basic ACL is created, and the basic ACL view is displayed.
     2. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } **source** { *source-ip-address* { *source-wildcard* | **0** } | **any** }
        
        Rules are configured for the basic ACL.
   * Configure an advanced ACL.
     
     1. Run [**acl**](cmdqueryname=acl) { **name** *advance-acl-name* [ **advance** | [ **advance** ] **number** *advance-acl-number* ] | [ **number** ] *advance-acl-number* } [ **match-order** { **config** | **auto** } ]
        
        An advanced ACL is created, and the advanced ACL view is displayed.
     2. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } **ip** [ **destination** { *destination-ip-address* { *destination-wildcard* | **0** } | **any** } | **source** { *source-ip-address* { *source-wildcard* | **0** } | **any** } ] \*
        
        Rules are configured for the advanced ACL.
   
   If a basic ACL is used, run the [**rule**](cmdqueryname=rule) command and set the **source** parameter to a multicast group address.
   
   If an advanced ACL is used, run the [**rule**](cmdqueryname=rule) command, set the **source** parameter to the address of the source that sends multicast data to multicast groups, and set the **destination** parameter to a multicast group address.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
5. Run [**igmp group-policy**](cmdqueryname=igmp+group-policy) { *acl-number* | **acl-name** *acl-name* } [ **1** | **2** | **3** ]
   
   
   
   The range of multicast groups that hosts can join on the interface is configured.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * If a multicast group matches an ACL rule and the action is **permit**, the interface allows hosts to join this group.
   * If a multicast group matches an ACL rule and the action is **deny**, the interface does not allow hosts to join this group.
   * If a multicast group does not match any ACL rule, the interface does not allow hosts to join this group.
   * If a specified ACL does not exist or contain rules, the interface does not allow hosts to join any multicast group.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
Configuring the maximum number of IGMP entries on an interface
==============================================================

IGMP-limit is configured on Router interfaces connected to users to limit the maximum number of multicast groups, including source-specific multicast groups. This mechanism enables users who have successfully joined multicast groups to enjoy smoother multicast services.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Configure a basic or an advanced ACL as needed.
   
   
   
   If a basic ACL is used, run the [**rule**](cmdqueryname=rule) command and set the **source** parameter to a multicast group address.
   
   If an advanced ACL is used, run the [**rule**](cmdqueryname=rule) command, set the **source** parameter to the source address of multicast packets, and set the **destination** parameter to a multicast group address.
   
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
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
5. Run [**igmp access-limit**](cmdqueryname=igmp+access-limit) *number* [ **except** { *acl-number* | **acl-name** *acl-name* } ]
   
   
   
   The maximum number of IGMP group memberships that can be created on an interface is specified.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
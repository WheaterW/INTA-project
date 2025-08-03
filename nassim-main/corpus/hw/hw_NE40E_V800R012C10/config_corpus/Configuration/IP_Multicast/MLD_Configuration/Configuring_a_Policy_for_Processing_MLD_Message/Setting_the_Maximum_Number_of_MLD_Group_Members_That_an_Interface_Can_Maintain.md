Setting the Maximum Number of MLD Group Members That an Interface Can Maintain
==============================================================================

This section describes how to configure an MLD entry limit on an interface to allow users who have joined multicast groups to enjoy smoother multicast services.

#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Configure a basic or an advanced ACL as needed.
   
   
   
   If a basic ACL is used, set **source** in the [**rule**](cmdqueryname=rule) command to a multicast group address.
   
   If an advanced ACL is used, set **source** in the [**rule**](cmdqueryname=rule) command to the address of the source that sends multicast data to multicast groups, and set **destination** to a multicast group address.
   
   * Configure a basic ACL.
     
     1. Run the [**acl ipv6**](cmdqueryname=acl+ipv6) [ **number** ] *basic-acl6-number* [ **match-order** { **auto** | **config** } ] command to create a basic ACL and enter the ACL view.
     2. Run the [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment** | **source** { *source-ipv6-address* *prefix-length* | *source-ipv6-address*/*prefix-length* | **any** } ] \* command to configure a rule for the basic ACL.
   * Configure an advanced ACL.
     
     1. Run the [**acl ipv6**](cmdqueryname=acl+ipv6) { **name** *advance-acl6-name* [ **advance** | [ **advance** ] **number** *advance-acl6-number* ] | [ **number** ] *advance-acl6-number* } [ **match-order** { **config** | **auto** } ] command to create an advanced ACL and enter the corresponding ACL view.
     2. Run the [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } **ipv6** [ **destination** { *destination-ipv6-address* *prefix-length* | *destination-ipv6-address*/*prefix-length* | **any** } | **source** { *source-ipv6-address* *prefix-length* | *source-ipv6-address*/*prefix-length* | **any** } ] \* command to configure a rule for the advanced ACL.
3. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
4. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the view of the interface connected to the user network segment.
5. Run the [**mld access-limit**](cmdqueryname=mld+access-limit) *number* [ **except** { *ExceptAclNumValue* | **acl6-name** *ExceptAclNameValue* } ] command to set the maximum number of MLD entries on the interface.
6. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
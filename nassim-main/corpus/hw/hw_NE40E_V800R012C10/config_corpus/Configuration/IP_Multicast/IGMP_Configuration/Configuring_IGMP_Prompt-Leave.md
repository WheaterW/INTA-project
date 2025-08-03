Configuring IGMP Prompt-Leave
=============================

Configuring IGMP Prompt-Leave

#### Usage Scenario

By default, IGMP-enabled interfaces send last-member query messages after receiving Leave messages for a specific multicast group from hosts. If the IGMP prompt leave function is enabled, the interfaces directly delete the records of the multicast group without sending last-member query messages. This feature shortens the delay in responding to Leave requests and reduces network bandwidth consumption. Currently, prompt-leave is available only in IGMPv2.


#### Pre-configuration Tasks

Before configuring prompt-leave, complete the following tasks:

* Configure a unicast routing protocol to ensure that unicast routes are reachable.
* [Configure basic IGMP functions](dc_vrp_multicast_cfg_2044.html).

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Configure a basic or an advanced ACL as needed.
   
   
   
   If a basic ACL is used, run the [**rule**](cmdqueryname=rule) command and set the **source** parameter to a multicast group address.
   
   If an advanced ACL is used, run the [**rule**](cmdqueryname=rule) command and set the **destination** parameter to a multicast group address.
   
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
5. Run [**igmp prompt-leave**](cmdqueryname=igmp+prompt-leave) [ **group-policy** { *acl-number* | **acl-name** *acl-name* } ]
   
   
   
   The IGMP prompt leave function is configured on the interface.
   
   
   
   In an ADSL dial-up access, the IGMP querier corresponds to only one host because one host corresponds to one port. When a receiver frequently joins or leaves multiple multicast groups, enable the prompt leave function on the querier.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * If **group-policy** is not specified, the interface implements prompt-leave for all Leave requests.
   * If **group-policy** is specified and a multicast group matches the **permit** action, the interface implements prompt-leave for Leave requests of this group.
   * If **group-policy** is specified and a multicast group matches the **deny** action, the interface does not implement prompt-leave for Leave requests of this group.
   * If **group-policy** is specified and a multicast group does not match any ACL rule, the interface does not implement prompt-leave for Leave requests of this group.
   * If the ACL specified in **group-policy** does not exist or no rules are configured in the ACL, the interface does not implement prompt-leave for any Leave requests.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Checking the Configurations

Run the [**display igmp**](cmdqueryname=display+igmp) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **interface** [ *interface-type* *interface-number* | **up** | **down** ] [ **verbose** ] command to check the configurations and operating status of IGMP on an interface.

Run the [**display igmp interface verbose**](cmdqueryname=display+igmp+interface+verbose) command to view detailed IGMP configurations of interfaces.
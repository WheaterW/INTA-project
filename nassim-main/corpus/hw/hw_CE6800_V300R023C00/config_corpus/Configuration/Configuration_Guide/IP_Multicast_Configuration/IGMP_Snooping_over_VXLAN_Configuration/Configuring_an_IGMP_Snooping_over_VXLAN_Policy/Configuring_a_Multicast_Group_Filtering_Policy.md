Configuring a Multicast Group Filtering Policy
==============================================

Configuring a Multicast Group Filtering Policy

#### Prerequisites

Before configuring a multicast group filtering policy, create an ACL and define rules for the policy. For details about ACL configuration, see [ACL Configuration](vrp_acl_cfg_0001.html). By default, the **permit** action in an ACL rule configured for a multicast group filtering policy in a BD applies to all multicast groups. To configure the device to accept multicast data of a specified multicast group only, you need to run the **[**rule**](cmdqueryname=rule) **deny** **source** **any**** command.


#### Context

A multicast group filtering policy determines which multicast groups the hosts in a BD can join. This function takes effect for dynamic multicast groups but not for static multicast groups.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Use either of the following methods to configure a multicast group filtering policy:
   
   
   * Configure a multicast group filtering policy in a BD.
     ```
     [bridge-domain](cmdqueryname=bridge-domain) bd-id
     [igmp snooping group-policy](cmdqueryname=igmp+snooping+group-policy) { acl-number | acl-name acl-name }[ version number ]
     ```
     
     If no IGMP version is specified for a multicast group filtering policy, the device applies the policy to all received IGMP messages.
   * Configure a multicast group filtering policy on a Layer 2 sub-interface.
     ```
     
     [interface](cmdqueryname=interface) interface-type interface-number.subnum mode l2
     [igmp snooping group-policy](cmdqueryname=igmp+snooping+group-policy) { acl-number | acl-name acl-name }[ version number ]
     ```
     
     If multicast group filtering policies are configured for the same BD in both the Layer 2 sub-interface view and BD view, the policy configured in the Layer 2 sub-interface view is implemented first, followed by the policy configured in the BD view.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
Configuring a Multicast Group Filtering Policy
==============================================

Configuring a Multicast Group Filtering Policy

#### Context

A multicast group filtering policy determines which multicast groups the hosts in a VLAN can join. This function takes effect for dynamic multicast groups but not for static multicast groups. It must be used together with an ACL6. Before deploying a multicast group filtering policy, you must create an ACL6 and define rules for the ACL6.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Use either of the following methods to configure a multicast group filtering policy:
   
   
   * Configure a multicast group filtering policy in a VLAN.
     ```
     [vlan](cmdqueryname=vlan) vlan-id
     [mld snooping group-policy](cmdqueryname=mld+snooping+group-policy) { acl6-number | acl6-name acl6-name } [ version number ] vlan { vlan-id1 [ to vlan-id2 ] }&<1-10>
     [quit](cmdqueryname=quit)
     ```
     
     By default, hosts in a VLAN can join any multicast group. If no MLD version is specified for a multicast group filtering policy, the device applies the policy to all received MLD messages.
     
     ![](../public_sys-resources/note_3.0-en-us.png) 
     
     By default, the **permit** action in an ACL6 rule configured for a multicast group filtering policy in a VLAN applies to all multicast groups. If you want the device to receive data from a specified multicast group only, you also need to run the **rule deny source any** command.
   * Configure a multicast group filtering policy on an interface.
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     [mld snooping group-policy](cmdqueryname=mld+snooping+group-policy) { acl6-number | acl6-name acl6-name } [ version version-number ] vlan { vlan-id1 [ to vlan-id2 ] }&<1-10>
     [quit](cmdqueryname=quit)
     ```
   
   
   
   If multicast group filtering policies are configured for the same VLAN in both the interface view and VLAN view, the policy configured in the interface view is implemented first, followed by the policy configured in the VLAN view.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
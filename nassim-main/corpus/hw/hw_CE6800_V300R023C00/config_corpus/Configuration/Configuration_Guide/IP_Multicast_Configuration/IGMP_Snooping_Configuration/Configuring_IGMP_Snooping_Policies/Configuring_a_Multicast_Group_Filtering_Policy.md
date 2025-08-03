Configuring a Multicast Group Filtering Policy
==============================================

Configuring a Multicast Group Filtering Policy

#### Context

A multicast group filtering policy determines which multicast groups the hosts in a VLAN can join. This function takes effect for dynamic multicast groups but not for static multicast groups. It must be used together with an ACL. Before deploying a multicast group filtering policy, you must create an ACL and define rules for the ACL.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Use either of the following methods to configure a multicast group filtering policy:
   
   
   * Configure a multicast group filtering policy in a VLAN.
     ```
     [vlan](cmdqueryname=vlan) vlan-id
     [igmp snooping group-policy](cmdqueryname=igmp+snooping+group-policy) { acl-number | acl-name acl-name } [ version version-number ]
     [quit](cmdqueryname=quit)
     ```
   * Configure a multicast group filtering policy on an interface.
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     [igmp snooping group-policy](cmdqueryname=igmp+snooping+group-policy) { acl-number | acl-name acl-name } [ version version-number ] vlan { vlan-id1 [ to vlan-id2 ] }&<1-10>
     [quit](cmdqueryname=quit)
     ```
   
   
   
   By default, hosts in a VLAN can join any multicast group. If no IGMP version is specified for a multicast group filtering policy, the device applies the policy to all received IGMP messages.
   
   If multicast group filtering policies are configured for the same VLAN in both the interface view and VLAN view, the policy configured in the interface view is implemented first, followed by the policy configured in the VLAN view.
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   By default, the **permit** action in an ACL rule configured for a multicast group filtering policy in a VLAN applies to all multicast groups. If you want the device to receive data from a specified multicast group only, you also need to run the **rule deny source any** command.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
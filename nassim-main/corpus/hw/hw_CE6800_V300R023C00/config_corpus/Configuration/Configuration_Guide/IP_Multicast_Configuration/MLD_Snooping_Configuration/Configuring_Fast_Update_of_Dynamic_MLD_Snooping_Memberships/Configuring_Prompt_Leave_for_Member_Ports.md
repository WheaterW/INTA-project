Configuring Prompt Leave for Member Ports
=========================================

Configuring Prompt Leave for Member Ports

#### Context

Upon receiving an MLD Done message from a member port, a device immediately deletes this port from the corresponding forwarding entry without resetting the aging timer and waiting for the forwarding entry to age out. This process is called prompt leave.

![](../public_sys-resources/note_3.0-en-us.png) 

You can enable prompt leave for member ports in a VLAN only when each interface in the VLAN is connected to only one receiver host.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the VLAN view.
   
   
   ```
   [vlan](cmdqueryname=vlan) vlan-id
   ```
3. Configure prompt leave for member ports.
   
   
   ```
   [mld snooping prompt-leave](cmdqueryname=mld+snooping+prompt-leave) [ group-policy { acl6-number  | acl6-name acl6-name } ]
   ```
   
   By default, the prompt leave function is disabled. You can specify the **group-policy** *acl6-number* parameter to limit the multicast groups for which prompt leave takes effect. In this case, you need to configure an ACL6 and define rules. By default, the **permit** action in an ACL6 rule applies to all multicast groups. To configure prompt leave for a specific multicast group, you also need to run the [**rule**](cmdqueryname=rule) **deny source any** command.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
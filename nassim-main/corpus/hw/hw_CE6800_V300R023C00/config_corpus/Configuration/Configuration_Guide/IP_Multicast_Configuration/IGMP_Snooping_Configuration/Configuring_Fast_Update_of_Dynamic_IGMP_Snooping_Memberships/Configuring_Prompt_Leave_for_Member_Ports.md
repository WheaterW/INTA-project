Configuring Prompt Leave for Member Ports
=========================================

Configuring Prompt Leave for Member Ports

#### Context

When a device receives an IGMP Leave message from a member port, the device immediately deletes this port from the forwarding table without resetting the aging timer or waiting for the forwarding entry to age out. This process is called prompt leave.

![](../public_sys-resources/note_3.0-en-us.png) 

You can enable prompt leave for member ports in a VLAN only when each interface in the VLAN is connected to only one receiver host.

Prompt leave takes effect for member ports in a VLAN only when the device is capable of processing IGMPv2 or IGMPv3 messages in the VLAN.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the VLAN view.
   
   
   ```
   [vlan](cmdqueryname=vlan) vlan-id
   ```
3. Configure the prompt leave function.
   
   
   ```
   [igmp snooping prompt-leave](cmdqueryname=igmp+snooping+prompt-leave) [ group-policy { acl-number  | acl-name acl-name } ]
   ```
   
   By default, the prompt leave function is disabled. You can specify the **group-policy** parameter to limit the multicast groups for which prompt leave takes effect. In this case, you need to configure an ACL and define rules. By default, the **permit** action in an ACL rule applies to all multicast groups. To configure prompt leave for a specific multicast group, you also need to run the [**rule**](cmdqueryname=rule) **deny source any** command.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
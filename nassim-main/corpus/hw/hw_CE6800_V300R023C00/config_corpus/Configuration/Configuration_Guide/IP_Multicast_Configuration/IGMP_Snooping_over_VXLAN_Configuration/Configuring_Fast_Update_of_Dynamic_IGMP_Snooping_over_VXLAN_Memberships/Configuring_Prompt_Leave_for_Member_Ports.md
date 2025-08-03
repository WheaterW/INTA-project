Configuring Prompt Leave for Member Ports
=========================================

Configuring Prompt Leave for Member Ports

#### Prerequisites

Before configuring prompt leave for member ports, you need to create an ACL and configure prompt leave rules for member ports. For details about ACL configuration, see [ACL Configuration](vrp_acl_cfg_0001.html).


#### Context

Upon receiving an IGMP Leave message from a member port, a device immediately deletes this port from the corresponding forwarding entry without resetting the aging timer or waiting for the forwarding entry to age out. This process is called prompt leave. Prompt leave takes effect for member ports only when the device can process IGMPv2 messages in a BD and each interface in the BD is connected to only one receiver host.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BD view.
   
   
   ```
   [bridge-domain](cmdqueryname=bridge-domain) bd-id
   ```
3. Configure prompt leave for member ports.
   
   
   ```
   [igmp snooping prompt-leave](cmdqueryname=igmp+snooping+prompt-leave) [ group-policy { acl-number | acl-name acl-name } ]
   ```
   
   You can specify the **group-policy** parameter to limit the multicast groups for which prompt leave takes effect. By default, the **permit** action in an ACL rule applies to all multicast groups. To configure prompt leave for a specific multicast group, you need to run the [**rule**](cmdqueryname=rule) **deny** **source** **any** command.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
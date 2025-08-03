Configuring a Report/Leave Message Filtering Policy
===================================================

Configuring a Report/Leave Message Filtering Policy

#### Prerequisites

Before configuring a policy for filtering Report/Leave messages, configure a basic or advanced ACL. A basic ACL can be used to filter IGMP Report/Leave messages based on a specified source address, whereas an advanced ACL can be used to filter IGMP Report/Leave messages based on both source and destination IP addresses. For details about ACL configuration, see [ACL Configuration](vrp_acl_cfg_0001.html).


#### Context

If no filtering policy is configured for Report/Leave messages in a BD, all user hosts can receive multicast services. To configure a device to process only the IGMP Report/Leave messages received from specified hosts and thereby improve multicast service security, configure a Report/Leave message filtering policy.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BD view.
   
   
   ```
   [bridge-domain](cmdqueryname=bridge-domain) bd-id
   ```
3. Configure the device to filter IGMP Report messages based on a source IP address.
   
   
   ```
   [igmp snooping ip-source-policy](cmdqueryname=igmp+snooping+ip-source-policy) { acl-number | acl-name acl-name }
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
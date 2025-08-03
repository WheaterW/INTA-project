(Optional) Configuring Report/Leave Message Suppression
=======================================================

(Optional) Configuring Report/Leave Message Suppression

#### Context

IGMP periodically sends query and response messages to maintain multicast group memberships. If multiple members have joined the same multicast group, they continuously send the same Report message to the corresponding IGMP router. In addition, when an IGMPv2 or IGMPv3 host leaves a multicast group, the host sends a Leave message repeatedly. To conserve bandwidth resources, you can enable a Layer 2 device to suppress Report/Leave messages.

After Report/Leave message suppression is configured, the device sends a Report message to its upstream device only when the first member joins a multicast group or when it receives an IGMP Query message. The device sends a Leave message to its upstream device only when the last member leaves the multicast group.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BD view.
   
   
   ```
   [bridge-domain](cmdqueryname=bridge-domain) bd-id
   ```
3. Configure Report/Leave message suppression.
   
   
   ```
   [igmp snooping report-suppress](cmdqueryname=igmp+snooping+report-suppress)
   ```
   
   
   
   Report/Leave message suppression and IGMP snooping proxy cannot be both configured in the same BD.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
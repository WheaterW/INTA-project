Configuring the Host Tracking Function
======================================

Configuring the Host Tracking Function

#### Context

If a host leaves a multicast group, the IGMP querier sends a Group-Specific Query message. If it does not receive any response within the specified time, the IGMP querier determines that the host has left and deletes the corresponding forwarding entry. While the IGMP querier waits for a response from the host, the multicast device continues to forward multicast traffic to the host. This delays the switching of multicast programs and wastes bandwidth.

To address this issue, you can configure the host tracking function. After this function is enabled, the IGMP querier will create an entry when a host joins a group. Upon receipt of a Leave message sent by a host, the IGMP querier determines that the host has left the multicast group without sending a Group-Specific Query message.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the VLAN view.
   
   
   ```
   [vlan](cmdqueryname=vlan) vlan-id
   ```
3. Configure host tracking in the VLAN.
   
   
   ```
   [igmp snooping explicit-tracking](cmdqueryname=igmp+snooping+explicit-tracking) [ all-version ]
   ```
   
   By default, host tracking is disabled in a VLAN.
   
   If **all-version** is specified, the host tracking function takes effect in all versions. Otherwise, the function takes effect only in IGMPv3 scenarios.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
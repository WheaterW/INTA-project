(Optional) Configuring Report and Leave Message Suppression
===========================================================

(Optional) Configuring Report and Leave Message Suppression

#### Context

IGMP periodically sends query and response messages to maintain group memberships. If multiple members have joined the same multicast group, they continuously send the same Report message to the IGMP device. In addition, IGMPv2 or IGMPv3 hosts send repetitive Leave messages when they leave a multicast group. These messages consume bandwidth resources. To address this issue, you can enable a Layer 2 device to suppress Report and Leave messages.

After Report and Leave message suppression is configured, the device sends a Report message to its upstream device only when the first member joins a group or when it receives an IGMP Query message. The device sends a Leave message to its upstream device only when the last member leaves a group.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the VLAN view.
   
   
   ```
   [vlan](cmdqueryname=vlan) vlan-id
   ```
3. Configure Report and Leave message suppression.
   
   
   ```
   [igmp snooping report-suppress](cmdqueryname=igmp+snooping+report-suppress)
   ```
   
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   When configuring the function, note the following:
   
   * After message suppression is configured in a VLAN, Layer 3 multicast functions, such as IGMP and PIM, cannot be enabled on the corresponding Layer 3 VLANIF interface.
   * Report and Leave message suppression and IGMP snooping proxy cannot be configured in the same VLAN.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
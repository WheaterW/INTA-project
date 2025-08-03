(Optional) Configuring Report and Done Message Suppression
==========================================================

(Optional) Configuring Report and Done Message Suppression

#### Context

MLD periodically sends Query and Report messages to maintain group memberships. During this process, if multiple members join the same multicast group, they continuously send the same Report message to the MLD device. In addition, when MLDv1 or MLDv2 hosts leave a multicast group, they send Done messages repeatedly. These messages consume bandwidth resources. To address this issue, you can enable a Layer 2 device to suppress Report and Done messages.

After Report and Done message suppression is configured, the device sends a Report message to its upstream device only when the first member joins a group or when it receives an MLD Query message. The device sends a Done message to its upstream device only when the last member leaves a group.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the VLAN view.
   
   
   ```
   [vlan](cmdqueryname=vlan) vlan-id
   ```
3. Configure Report and Done message suppression.
   
   
   ```
   [mld snooping report-suppress](cmdqueryname=mld+snooping+report-suppress)
   ```
   ![](../public_sys-resources/note_3.0-en-us.png) 
   * After message suppression is configured in a VLAN, Layer 3 multicast functions, such as MLD and PIM (IPv6), cannot be enabled on the corresponding Layer 3 VLANIF interface.
   * Report and Done message suppression and MLD snooping proxy cannot be configured in the same VLAN.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
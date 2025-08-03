Enabling Immediate Deletion of ARP Entries
==========================================

Enabling Immediate Deletion of ARP Entries

#### Context

By default, when a VLANIF member interface goes down, the device deletes the ARP entries learned by the member interface only after detecting that they are aged in an ARP probe. The device then updates routing entries. This processing mechanism may delay a link switchover in an ECMP scenario. To speed up a link switchover in an ECMP scenario, enable the device to delete ARP entries learned by the member interface immediately after the interface goes down without waiting for the ARP aging probe result.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the VLANIF interface view.
   
   
   ```
   [interface](cmdqueryname=interface) vlanif vlan-id
   ```
3. Enable immediate deletion of ARP entries.
   
   
   ```
   [arp delete trigger link-down enable](cmdqueryname=arp+delete+trigger+link-down+enable)
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display arp interface**](cmdqueryname=display+arp+interface) { *interface-name* | *interface-type interface-number* } command to check ARP entries on an interface.
Disabling ARP Learning on an Interface
======================================

Disabling ARP Learning on an Interface

#### Context

If a user host connected to a device's interface initiates an ARP attack, the device's ARP resources may be exhausted. To resolve this issue, you can disable the interface from learning dynamic ARP entries, ensuring device security.

![](public_sys-resources/notice_3.0-en-us.png) 

Disabling ARP learning on an interface may cause a traffic forwarding failure. Exercise caution when performing this operation.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) { interface-name | interface-type interface-number } 
   ```
3. Switch the interface working mode to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Disable ARP learning on the interface.
   
   
   ```
   [arp learning disable](cmdqueryname=arp+learning+disable)
   ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display arp packet statistics**](cmdqueryname=display+arp+packet+statistics) [ **interface** [ *interface-name* | *interface-type interface-number* ] ] command to check statistics about ARP messages sent and received by the device.
Configuring Intra-VLAN Proxy ARP
================================

Configuring Intra-VLAN Proxy ARP

#### Context

Hosts that belong to the same VLAN are unable to communicate with each other if Layer 2 interface isolation is configured in the VLAN. In this case, you can enable intra-VLAN proxy ARP on a device's interface associated with the VLAN to enable the hosts to communicate.


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
4. Enable intra-VLAN proxy ARP.
   
   
   ```
   [arp proxy intra-vlan enable](cmdqueryname=arp+proxy+intra-vlan+enable)
   ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display arp interface**](cmdqueryname=display+arp+interface) { *interface-name* | *interface-type* *interface-number* } command to check ARP entries on an interface.
Configuring Inter-VLAN Proxy ARP
================================

Configuring Inter-VLAN Proxy ARP

#### Context

Inter-VLAN proxy ARP enables devices in different VLANs to communicate with each other.

If two hosts belong to different VLANs and need to communicate with each other, you can enable inter-VLAN proxy ARP on the interfaces associated with the VLANs.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the VLAN view.
   
   
   ```
   [vlan](cmdqueryname=vlan) vlan-id
   ```
3. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
4. Enter the view of the VLANIF interface where inter-VLAN proxy ARP needs to be enabled.
   
   
   ```
   [interface vlanif](cmdqueryname=interface+vlanif) interface-number
   ```
5. Enable inter-VLAN proxy ARP.
   
   
   ```
   [arp proxy inter-vlan enable](cmdqueryname=arp+proxy+inter-vlan+enable)
   ```
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
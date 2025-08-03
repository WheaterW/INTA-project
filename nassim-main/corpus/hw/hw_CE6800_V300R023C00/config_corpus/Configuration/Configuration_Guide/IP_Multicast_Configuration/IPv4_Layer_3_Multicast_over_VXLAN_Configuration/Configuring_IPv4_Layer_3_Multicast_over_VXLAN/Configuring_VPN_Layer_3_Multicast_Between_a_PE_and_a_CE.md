Configuring VPN Layer 3 Multicast Between a PE and a CE
=======================================================

Configuring VPN Layer 3 Multicast Between a PE and a CE

#### Context

When a multicast receiver connected to a CE needs to access a receiver PE through a VPN Layer 3 multicast network, VPN Layer 3 multicast functions must be configured on the receiver PE and CE.


#### Procedure

* Configure the PE.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the view of the Layer 3 interface that is directly connected to the CE.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  3. Switch the interface working mode from Layer 2 to Layer 3.
     
     
     ```
     [undo portswitch](cmdqueryname=undo+portswitch)
     ```
  4. Bind the interface to an L3VPN instance.
     
     
     ```
     [ip binding vpn-instance](cmdqueryname=ip+binding+vpn-instance) vpn-instance-name
     ```
  5. Configure an IP address for the interface.
     
     
     ```
     [ip address](cmdqueryname=ip+address) ip-address { mask | mask-length }
     ```
     
     
     
     After the interface is bound to an L3VPN instance, the existing IP address of the interface is automatically deleted. For this reason, the IP address needs to be reconfigured.
  6. Enable PIM-SM.
     
     
     ```
     [pim sm](cmdqueryname=pim+sm)
     ```
  7. Enable IGMP.
     
     
     ```
     [igmp enable](cmdqueryname=igmp+enable)
     ```
  8. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure the CE.
  1. Enter the system view. 
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enable multicast routing.
     
     
     ```
     [multicast routing-enable](cmdqueryname=multicast+routing-enable)
     ```
  3. Enter the view of a Layer 3 interface.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  4. Switch the interface working mode from Layer 2 to Layer 3.
     
     
     ```
     [undo portswitch](cmdqueryname=undo+portswitch)
     ```
  5. Enable PIM-SM.
     
     
     ```
     [pim sm](cmdqueryname=pim+sm)
     ```
     
     
     
     This step must be performed on both the Layer 3 interface directly connected to the PE and the Layer 3 interface connected to the user network segment.
  6. Enable IGMP.
     
     
     ```
     [igmp enable](cmdqueryname=igmp+enable)
     ```
     
     
     
     Perform this step on the Layer 3 interface that is connected to the user network segment.
  7. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```

#### Follow-up Procedure

To enable communication between the CE and PE and allow the CE to obtain the route to the multicast source, configure a routing protocol on the PE and CE. For details, see [Configuring the MCE Function](vrp_L3VPNv4_cfg_0016.html) in *VPN Configuration*.
(Optional) Configuring BFD-based BDR Fast Switching
===================================================

BFD-based BDR fast switching reduces the convergence time and traffic loss during DR re-election triggered by a DR failure.

#### Context

If a DR on a network fails, a new DR is elected only after other devices detect the neighbor timeout or BFD detects the neighbor failure. The new DR then generates routing entries and outbound interface information through protocol calculation. Multicast routing entries are then delivered from the control plane to the forwarding plane to guide traffic forwarding. The whole process takes a long time and may cause traffic loss.

To solve this problem, configure the BFD-based BDR fast switching function on all devices on the same network segment. With this function, both a DR and a backup DR (BDR) are elected on the network. The BDR also delivers multicast entries and outbound interface information to the forwarding plane and associates the DR status with the BFD status on the forwarding plane. The BDR blocks traffic in normal cases. If the BDR detects a neighbor fault through BFD on the forwarding plane, it can quickly restore traffic, reducing the convergence time.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number.subinterface-number*
   
   
   
   The sub-interface view is displayed.
3. Run [**igmp enable**](cmdqueryname=igmp+enable)
   
   
   
   IGMP is enabled on the sub-interface.
4. Run [**pim bfd**](cmdqueryname=pim+bfd) **enable**
   
   
   
   BFD for IPv4 PIM is enabled on the sub-interface.
5. Run [**pim sticky-dr**](cmdqueryname=pim+sticky-dr)
   
   
   
   The sticky DR function is enabled, ensuring device stability after a BDR becomes the new DR.
6. Run [**pim bfd bdr fast-switch**](cmdqueryname=pim+bfd+bdr+fast-switch)
   
   
   
   BFD-based BDR fast switching is enabled.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
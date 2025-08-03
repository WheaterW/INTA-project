(Optional) Disabling ARP-MAC Association
========================================

By default, the device supports ARP-MAC association, which implements fast ARP entry updating and ensures real-time and stable user traffic. However, after learning ARP entries, a VLANIF interface synchronizes them on the device. As a result, a large number of ARP entries exist on all interface boards. To resolve this issue, disable ARP-MAC association in scenarios where ARP entry synchronization is not required on the device.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface vlanif**](cmdqueryname=interface+vlanif) *vlan-id*
   
   
   
   The VLANIF interface view is displayed.
3. Run [**mac-change notify-arp disable**](cmdqueryname=mac-change+notify-arp+disable)
   
   
   
   ARP-MAC association is disabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
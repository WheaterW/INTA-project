(Optional) Disabling ND-MAC Association
=======================================

By default, the device supports ND-MAC association, which implements fast ND entry updating and ensures real-time and stable user traffic. However, after learning ND entries, a VLANIF interface synchronizes them on the device. As a result, a large number of ND entries exist on all interface boards. To resolve this issue, disable ND-MAC association in scenarios where ND entry synchronization is not required on the device.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface vlanif**](cmdqueryname=interface+vlanif) *vlan-id*
   
   
   
   The VLANIF interface view is displayed.
3. Run [**mac-change notify-nd disable**](cmdqueryname=mac-change+notify-nd+disable)
   
   
   
   ND-MAC association is disabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
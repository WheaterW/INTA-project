(Optional) Setting a Delay After Which a VLANIF Interface Goes Down
===================================================================

Setting a delay after which a VLANIF interface goes down prevents network flapping caused by changes of VLANIF interface status. This function is also called VLAN damping.

#### Context

If a VLAN goes down because all ports in the VLAN go down, the system immediately reports the VLAN down event to the corresponding VLANIF interface, instructing the VLANIF interface to go down.

To prevent network flapping caused by changes of VLANIF interface status, enable VLAN damping on the VLANIF interface. After the last up port in a VLAN goes down, the system starts a VLAN damping delay timer and informs the corresponding VLANIF interface of the VLAN down event after the timer expires. If a port in the VLAN goes up during the delay period, the VLANIF interface remains up.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) **vlanif** *vlan-id*
   
   
   
   The VLANIF interface view is displayed.
   
   
   
   The VLAN ID specified in this command must be the ID of an existing VLAN.
3. Run [**damping time**](cmdqueryname=damping+time) *delay-time*
   
   
   
   The delay for VLAN damping is set.
   
   
   
   *delay-time* ranges from 0 to 20, in seconds.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
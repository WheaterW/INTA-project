(Optional) Disabling OSPF IP FRR on an Interface
================================================

If an interface runs key services, ensure that the backup path does not pass through this interface so that services will not be affected after FRR calculation.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The view of an OSPF interface on which FRR is enabled is displayed.
3. Run [**ospf frr block**](cmdqueryname=ospf+frr+block)
   
   
   
   FRR is blocked on the OSPF interface.
4. (Optional) To prevent the interface from participating in Remote LFA backup next hop calculation, run the [**ospf remote-lfa disable**](cmdqueryname=ospf+remote-lfa+disable) command.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
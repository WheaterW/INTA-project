(Optional) Blocking FRR on an OSPFv3 Interface
==============================================

If FRR is not required on certain OSPFv3 interfaces, FRR needs to be blocked on these interfaces.

#### Context

If an interface runs key services, ensure that the backup path does not pass through this interface so that services will not be affected after FRR calculation.

Perform the following steps on the interfaces of the device where OSPFv3 IP FRR has been configured:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The view of the OSPFv3 interface running FRR is displayed.
3. Run [**ospfv3 frr block**](cmdqueryname=ospfv3+frr+block)
   
   
   
   FRR is blocked on the OSPFv3 interface.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
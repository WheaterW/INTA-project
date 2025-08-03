(Optional) Configuring CBTS
===========================

Service class can be set for packets that MPLS TE tunnels allow to pass through.

#### Context

When services recurse to multiple TE tunnels, the **mpls te service-class** command is run on the TE tunnel interface to set a service class so that a TE tunnel transmits services of a specified service class.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *tunnel-number*
   
   
   
   The MPLS TE tunnel interface view is displayed.
3. Run [**mpls te service-class**](cmdqueryname=mpls+te+service-class) { *service-class* & <1-8> | **default** }
   
   
   
   A service class is set for packets that an MPLS TE tunnel allows to pass through.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * This command is used only on the ingress of an MPLS TE tunnel.
   * If the [**mpls te service-class**](cmdqueryname=mpls+te+service-class) command is run repeatedly on a tunnel interface, the latest configuration overrides the previous one.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
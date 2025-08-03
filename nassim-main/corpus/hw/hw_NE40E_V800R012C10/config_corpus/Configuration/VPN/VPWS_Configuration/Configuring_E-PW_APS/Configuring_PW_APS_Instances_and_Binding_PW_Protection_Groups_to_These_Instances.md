Configuring PW APS Instances and Binding PW Protection Groups to These Instances
================================================================================

This section describes how to configure PW and E-PW APS instances and bind PW protection groups to the APS instances.

#### Context

In an E-PW APS scenario, PW APS instances are further divided into master PW APS instances and slave PW APS instances. Only a master PW APS instance will establish the APS state machine, exchange APS signaling with the peer PW end, and notify the slave PW APS instance of the negotiated status through the bypass PW. APS protocol packets generally travel along the backup channel. The transmit and receive ends both know that they receive APS protocol packets through each other's backup channel. This implementation helps determine whether the primary and backup channel configurations on the two ends are consistent. In this example, the PW between PE1 and PE2 serves as the primary PW and that between PE1 and PE3 serves as the secondary PW. You need to configure the PW APS instance on PE3 as the master one and the PW APS instance on PE2 as the slave one.

In an E-PW APS scenario, perform the following configurations on PE1, PE2, and PE3.


#### Procedure

* Configure a PW APS instance and bind a PW protection group to the instance.
  
  
  
  To configure a PW APS instance on PE1 and bind a PW protection group to the instance, see [Configuring a PW APS Instance and Bind a PW Protection Group to the PW APS Instance](dc_vrp_vpws_cfg_6030.html).
* Configure E-PW APS instances and bind a PW protection group to each instance.
  
  
  
  Perform the following steps on PE2 and PE3.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**pw-aps**](cmdqueryname=pw-aps) *apsId*
     
     
     
     A PW APS instance is created, and its view is displayed.
  3. (Optional) Run [**description**](cmdqueryname=description) *text*
     
     
     
     A description is configured for the PW APS instance.
  4. Run [**role**](cmdqueryname=role) { **master** | **slave** }
     
     
     
     A master or slave role is configured for the E-PW APS instance.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Specify the role as **slave** for the E-PW APS instance on PE2 and as **master** for that on PE3.
  5. Run [**remote-aps**](cmdqueryname=remote-aps) *remoteApsId*
     
     
     
     A remote ID is configured for the PW APS instance.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     On PE2 and PE3, the remote ID of the master PW APS instance must be the ID of the slave PW APS instance, and the remote ID of the slave PW APS instance must be the ID of the master PW APS instance.
  6. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  7. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
     
     
     
     The view of the AC interface configured with the PW protection group is displayed.
  8. Run [**mpls l2vpn pw-aps**](cmdqueryname=mpls+l2vpn+pw-aps) *apsId* { **admin** | **reference** }
     
     
     
     The PW protection group is bound to the PW APS instance.
  9. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  10. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
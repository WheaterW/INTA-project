Configuring an EVPL Instance
============================

Before binding an AC interface on the user side to an MPLS tunnel interface on the network side, you must create an EVPL instance.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**evpl instance**](cmdqueryname=evpl+instance) *evpl-id*
   
   
   
   An EVPL instance is created, and its view is displayed.
3. Run [**evpn binding vpn-instance**](cmdqueryname=evpn+binding+vpn-instance) *vpn-instance-name*
   
   
   
   The EVPL instance is bound to an EVPN instance for a specified VPWS.
4. Run [**local-service-id**](cmdqueryname=local-service-id) *service-id* [**remote-service-id**](cmdqueryname=remote-service-id) *service-id*
   
   
   
   The device is configured to add the local and remote service IDs to the packets of the current EVPL instance.
5. (Optional) Run [**load-balancing ignore-esi**](cmdqueryname=load-balancing+ignore-esi)
   
   
   
   Checking ESI validity when an EVPL instance load balancing is performed is disabled.
   
   When active-active protection is deployed in the EVPN VPWS scenario, if an access device is single-homed to an aggregation device, no ESI is configured on the access interface. To form active-active load balancing, you can run the **load-balancing ignore-esi** command to enable the aggregation device to ignore ESI validity check during EVPL instance load balancing.
6. (Optional) Run [**control-word enable**](cmdqueryname=control-word+enable)
   
   
   
   The control word function is enabled for the EVPL instance.
   
   Out-of-order packets may be generated when the device performs in-depth parsing on MPLS packets. In this case, you can enable the control word function in the EVPL instances on both ends to reassemble MPLS packets.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
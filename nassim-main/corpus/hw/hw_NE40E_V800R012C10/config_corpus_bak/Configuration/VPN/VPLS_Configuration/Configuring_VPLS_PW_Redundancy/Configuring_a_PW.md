Configuring a PW
================

The following describes how to configure a PW in two networking modes: HVPLS and VPLS accessing VPWS. Currently, only LDP PWs can be configured.

#### Context

The service type determines which networking mode to use:

* HVPLS is best suited for multicast services.
* VPLS accessing VPWS is best suited for unicast services.

#### Procedure

* Configure a PW in an HVPLS networking scenario.
  
  
  
  For details, see [Configuring LDP HVPLS](dc_vrp_vpls_cfg_5009.html).
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**vsi**](cmdqueryname=vsi) *vsi-name* **static**
     
     
     
     A VSI is created, and the static member discovery mode is specified.
  3. Run [**pwsignal**](cmdqueryname=pwsignal) **ldp**
     
     
     
     LDP is configured as the PW signaling protocol, and the VSI-LDP view is displayed.
  4. Run [**vsi-id**](cmdqueryname=vsi-id) *vsi-id*
     
     
     
     An ID is configured for the VSI.
  5. Run the following commands to configure VSI peers so that PWs can be established:
     
     
     + To create a hub PW, run the [**peer**](cmdqueryname=peer) *peer-address* [ **negotiation-vc-id** *vc-id* ] [ **tnl-policy** *policy-name* ] [ [ **endpoint** *endpoint4-address* ] **color** *color-value* ] command to specify an SPE as a VSI peer on a UPE or specify an NPE as a VSI peer on an SPE.
     + To create a spoke PW, run the [**peer**](cmdqueryname=peer) *peer-address* [ **negotiation-vc-id** *vc-id* ] [ **tnl-policy** *policy-name* ] [ [ **endpoint** *endpoint4-address* ] **color** *color-value* ] **upe** [ **ignore-standby-state** ] command to specify a UPE as a VSI peer on an SPE.
  6. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the VSI view.
  7. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  8. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The AC interface view is displayed.
     
     
     
     This command must be run on UPEs and NPEs, but is not required on SPEs. In this scenario, a UPE's AC interfaces are Ethernet interfaces, and an NPE's AC interfaces are Eth-Trunk sub-interfaces.
  9. Run [**vlan-type dot1q**](cmdqueryname=vlan-type+dot1q) *vlan-id*
     
     
     
     The VLAN encapsulation type is configured for the AC interface.
  10. Run [**l2 binding**](cmdqueryname=l2+binding) **vsi** *vsi-name*
      
      
      
      The AC interface is bound to the VSI.
  11. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
* Configure a PW in a VPLS accessing VPWS networking scenario.
  + Configure the UPE. The configuration procedure is similar to that in the HVPLS scenario. For details, see [Configuring HVPLS](#EN-US_TASK_0172370177__step_dc_vrp_vpls_cfg_505001).
  + Configure the NPE:
    1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
    2. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the AC interface view.
    3. Run the [**mpls l2vc**](cmdqueryname=mpls+l2vc)  [ **instance-name** *instance-name* ] { *ip-address* | **pw-template** *template-name* } \* *vc-id* [ **tunnel-policy** *policy-name* [ { **endpoint** *endpoint-address* | [ **endpoint** *endpoint4-address* ] } **color** *color-value* ] | [ **control-word** | **no-control-word** ] | [ **raw** | **tagged** | **ip-layer2** | **ip-interworking**] | **access-port** | **ignore-standby-state** ] \* command to create a dynamic PW (VPLS connection) from the NPE to the peer UPE.
    4. (Optional) Run the [**mpls l2vc**](cmdqueryname=mpls+l2vc) { *ip-address* | **pw-template** *template-name* } \* *vc-id* [ **tunnel-policy** *policy-name* | [ { **endpoint** *endpoint-address* | [ **endpoint** *endpoint4-address* ] } **color** *color-value* ] [ **control-word** | **no-control-word** ] | [ **raw** | **tagged** ] | **access-port** | **ignore-standby-state** | **bypass** ] \* command to create a bypass PW between NPEs. To implement VPLS PW redundancy in master/slave mode, you must configure a bypass PW.
    5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
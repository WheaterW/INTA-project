(Optional) Configuring the Global Redundancy Mode
=================================================

A PE's global redundancy mode determines whether the PE can work with other PEs in load-balancing mode.

#### Context

By default, EVPN PEs work in all-active mode. If a CE is multi-homed to several EVPN PEs, these PEs will load-balance traffic. If you do not want to transmit traffic in load balancing mode, you can change the global redundancy mode of PEs to the single-active mode. When PEs work in all-active mode, each PE is in the active state. When PEs work in single-active mode, one PE is in the active state, and the other PEs are in the standby state.

Currently, either of the following methods can be used to determine the active/standby status of PEs:

* The active/standby status is determined by an E-Trunk. In this case, the CE needs to be configured with an Eth-Trunk interface to connect to the PE, and the PE also needs to be configured with an Eth-Trunk interface to connect to the CE.
* The active/standby status is determined based on the DF election result. In this case, a CE can be connected to a PE through an Eth-Trunk or a common physical interface, and no additional E-Trunk needs to be configured.

Perform the following steps on all-active PEs as required.


#### Procedure

* The E-Trunk is used to determine the active/standby status.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**e-trunk**](cmdqueryname=e-trunk) *e-trunk-id*
     
     
     
     An E-Trunk is configured, and its view is displayed.
  3. Run [**priority**](cmdqueryname=priority) *priority*
     
     
     
     An E-Trunk priority value is set.
  4. Run [**peer-address**](cmdqueryname=peer-address) *peer-ip-address* **source-address** *source-ip-address*
     
     
     
     IP addresses are configured for the local and peer ends of the E-Trunk.
  5. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  6. Run [**interface eth-trunk**](cmdqueryname=interface+eth-trunk) *trunk-id*
     
     
     
     The Eth-Trunk interface view is displayed.
  7. Run [**e-trunk**](cmdqueryname=e-trunk) *e-trunk-id*
     
     
     
     The Eth-Trunk interface is added to the E-Trunk.
     
     An Eth-Trunk interface can be added to only one E-Trunk.
  8. (Optional) Run [**e-trunk mode**](cmdqueryname=e-trunk+mode) **force-master**
     
     
     
     The E-Trunk member interface is forced to work in master mode.
     
     In an all-active scenario, you need to run this command to set the status of multiple PEs to master to implement load balancing. In single-active scenarios, this command cannot be run on PEs.
  9. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  10. Run [**lacp e-trunk system-id**](cmdqueryname=lacp+e-trunk+system-id) *mac-address*
      
      
      
      The LACP system ID is configured.
  11. (Optional) Run [**lacp e-trunk priority**](cmdqueryname=lacp+e-trunk+priority) *priority*
      
      
      
      The E-Trunk LACP system priority is configured.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      For devices in the same E-Trunk, their LACP system IDs must be the same, and their LACP system priorities must also be the same.
  12. (Optional) Run [**evpn redundancy-mode single-active**](cmdqueryname=evpn+redundancy-mode+single-active)
      
      
      
      The global redundancy mode is set to single-active.
      
      In single-active scenarios, this command must be configured on PEs. In all-active scenarios, this command cannot be configured on PEs.
  13. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
* The active/standby status is determined based on the DF election result (which applies to the single-active scenario).
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**evpn**](cmdqueryname=evpn+%28system+view%29)
     
     
     
     The EVPN global configuration view is displayed.
  3. Run [**esi**](cmdqueryname=esi) *esi*
     
     
     
     A static ESI instance name is configured. The *esi* value must be the same as the name of the statically configured ESI.
  4. Run [**evpn redundancy-mode single-active df-election**](cmdqueryname=evpn+redundancy-mode+single-active+df-election)
     
     
     
     The device is enabled to determine the active/standby status based on the DF election result when static ESI instances work in single-active mode.
     
     
     
     After the configurations are complete, the PE that is elected as the DF is in the active state, and the PEs that are not elected as DFs are in the standby state.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Currently, the active/standby status can be determined based on the DF election result only in the static ESI view. Therefore, you need to configure a static ESI when configuring an ESI on an interface.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
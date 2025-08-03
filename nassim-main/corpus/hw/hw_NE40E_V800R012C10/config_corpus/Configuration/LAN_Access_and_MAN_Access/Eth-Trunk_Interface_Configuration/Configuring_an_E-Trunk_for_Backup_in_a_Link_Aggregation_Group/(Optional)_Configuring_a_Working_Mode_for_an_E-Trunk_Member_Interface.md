(Optional) Configuring a Working Mode for an E-Trunk Member Interface
=====================================================================

To enable proper traffic transmission, configure a working mode for an E-Trunk member interface. An E-Trunk member interface can work in automatic, forcible master, or forcible backup mode.

#### Context

If a member interface in an E-Trunk works in automatic mode or is switched to the automatic mode from the forcible master or backup mode, the master/backup status of the member interface is determined by the master/backup status of the local E-Trunk and the peer member interface status.

* If the local E-Trunk works in master mode, the local member interface also works in master mode.
* If the local E-Trunk works in backup mode and the peer member interface fails, the local member interface works in master mode. If the local member interface receives a recovery message from the peer member interface, the local member interface enters the backup mode.

When E-Trunk member interfaces work in automatic mode, a change in the interval at which Hello packets are exchanged or the timeout period will result in master/backup status flapping. Therefore, configure the member interfaces to work in forcible master/backup mode before changing the interval at which Hello packets are exchanged. After master/backup status negotiation is complete, restore the member interfaces to the automatic mode.


#### Procedure

* Configure a working mode for a member Eth-Trunk interface of an E-Trunk.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**interface eth-trunk**](cmdqueryname=interface+eth-trunk) *trunk-id*
     
     The Eth-Trunk interface view is displayed.
     
     Only Eth-Trunk interfaces in manual load balancing, manual 1:1 master/backup,  or static LACP mode can be added to an E-Trunk.
     
     ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
     
     If an Eth-Trunk interface in static LACP mode is added to an E-Trunk, do not configure the maximum number of active links for the Eth-Trunk interface on each of the dual-homing E-Trunk-enabled devices for user access. Otherwise, LACP cannot select correct interfaces as active interfaces for service forwarding.
  3. Run [**e-trunk mode**](cmdqueryname=e-trunk+mode) *mode-type*
     
     A working mode is configured for the member Eth-Trunk interface of an E-Trunk. In a dual-homing active-active scenario, you need to configure *force-master* on the Eth-Trunk interfaces used for dual-homing access, so that both interfaces work in the master state.
* Configure a working mode for a member global VE interface of an E-Trunk.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**interface global-ve**](cmdqueryname=interface+global-ve) *ve-number*
     
     A global VE interface is created, and its view is displayed.
  3. Run [**e-trunk mode**](cmdqueryname=e-trunk+mode) *mode-type*
     
     A working mode is configured for the member global VE interface of an E-Trunk.
     
     In a dual-homing active-active scenario, you need to configure ***force-master*** on the global VE interfaces used for dual-homing access, so that both interfaces work in the master state.
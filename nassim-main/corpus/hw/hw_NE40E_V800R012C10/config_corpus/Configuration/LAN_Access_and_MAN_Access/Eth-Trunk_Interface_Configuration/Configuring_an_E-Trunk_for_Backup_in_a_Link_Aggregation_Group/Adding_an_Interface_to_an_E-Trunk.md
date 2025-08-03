Adding an Interface to an E-Trunk
=================================

An E-Trunk forwards packets through its member interfaces, which can be Eth-Trunk interfaces or global VE interfaces.

#### Context

Two E-Trunk-enabled devices must have the same E-Trunk ID, whereas the E-Trunk member interfaces can have different IDs. If two interfaces to be added to an E-Trunk have different IDs, the ID of the remote E-Trunk member interface must be specified when the local interface is added to an E-Trunk as a member interface.


#### Procedure

* Add an Eth-Trunk interface to an E-Trunk.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**interface eth-trunk**](cmdqueryname=interface+eth-trunk) *trunk-id*
     
     The Eth-Trunk interface view is displayed.
     
     Only Eth-Trunk interfaces in manual load balancing, manual 1:1 master/backup,  or static LACP mode can be added to an E-Trunk.
     
     ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
     
     If an Eth-Trunk interface in static LACP mode is added to an E-Trunk, do not configure the maximum number of active links for the Eth-Trunk interface on each of the dual-homing E-Trunk-enabled devices for user access. Otherwise, LACP cannot select correct interfaces as active interfaces for service forwarding.
  3. Run [**e-trunk**](cmdqueryname=e-trunk) *e-trunk-id* [ **remote-eth-trunk** *eth-trunk-id* ]The Eth-Trunk interface is added to an E-Trunk.
     
     An Eth-Trunk interface can be added to only one E-Trunk.
     
     If you want to add the Eth-Trunk interfaces with different IDs on two PEs to the same E-Trunk, specify **remote-eth-trunk** in the command to ensure that the E-Trunk works properly.
* Add a global VE interface to an E-Trunk.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**interface global-ve**](cmdqueryname=interface+global-ve) *ve-number*
     
     A global VE interface is created, and its view is displayed.
  3. Run [**ve-group**](cmdqueryname=ve-group) *ve-group-id* **l2-terminate**
     
     The global VE interface is configured as an L2VE interface.
  4. Run [**e-trunk**](cmdqueryname=e-trunk) *e-trunk-id* [ **remote-global-ve** *global-ve-id* ]
     
     A global VE interface is added to a specified E-Trunk.
     
     A global VE interface can be added to only one E-Trunk. A global VE interface must be removed from an E-Trunk before it is added to another one, and an E-Trunk can have only one member global VE interface.
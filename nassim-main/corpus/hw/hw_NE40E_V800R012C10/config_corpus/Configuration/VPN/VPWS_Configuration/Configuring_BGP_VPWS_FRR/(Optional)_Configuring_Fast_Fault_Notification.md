(Optional) Configuring Fast Fault Notification
==============================================

OAM mapping and physical-layer fault notification can accelerate AC fault detection and notification.

#### Context

Fast fault notification is classified into the following types:

* [OAM mapping](#EN-US_TASK_0172369854__step_dc_vrp_vpws_cfg_606801): supports a wide range of links, but requires PEs and CEs to support Ethernet OAM.
* [Physical layer fault notification](#EN-US_TASK_0172369854__step_dc_vrp_vpws_cfg_606802): can be configured only on Ethernet main interfaces.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

When a PW encounters a fault, OAM mapping does not trigger AC interfaces to go Down. If PEs and CEs support Ethernet OAM, using OAM mapping is recommended.



#### Procedure

* Configure OAM mapping.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The AC interface view is displayed.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The AC interface must be an Ethernet sub-interface.
  3. Run [**mpls l2vpn oam-mapping**](cmdqueryname=mpls+l2vpn+oam-mapping) **1ag** **md** *md-name* **ma** *ma-name*
     
     
     
     OAM mapping is enabled to associate PW OAM with AC OAM.
     
     
     
     + Ethernet OAM for ACs must be configured before the [**mpls l2vpn oam-mapping**](cmdqueryname=mpls+l2vpn+oam-mapping) **1ag** **md** *md-name* **ma** *ma-name* command is run.
     + After running the [**mpls l2vpn oam-mapping**](cmdqueryname=mpls+l2vpn+oam-mapping) command, run the [**display mpls l2vpn oam-mapping**](cmdqueryname=display+mpls+l2vpn+oam-mapping) [ **interface** *interface-type* *interface-number* ] command to check VC status. In the command output, **Local AC OAM State** indicates the AC link status.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure physical layer fault notification.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
     
     
     
     The AC interface view is displayed.
     
     
     
     + The AC interface must be an Ethernet main interface.
     + This interface must have a VC configured.
  3. Run [**mpls l2vpn trigger if-down**](cmdqueryname=mpls+l2vpn+trigger+if-down)
     
     
     
     Physical layer fault notification is enabled.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
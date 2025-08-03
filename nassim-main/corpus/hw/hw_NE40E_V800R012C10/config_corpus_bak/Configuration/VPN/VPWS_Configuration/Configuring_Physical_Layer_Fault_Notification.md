Configuring Physical Layer Fault Notification
=============================================

Physical layer fault notification expedites fault detection and notification.

#### Usage Scenario

In a scenario in which an Ethernet or GE main interface is configured with a remote LDP VPWS connection or local CCC connection, you can configure physical layer fault notification to expedite fault detection, so that upper-layer applications can quickly recover when a physical layer fault occurs.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In NE40E, physical layer fault notification can be configured on only Ethernet and GE main interfaces.

#### Pre-configuration Tasks

Before configuring physical layer fault detection, complete the following tasks:

* Configure network layer parameters for devices on the MPLS L2VPN to communicate.
* Configure a PW.![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  The PW must be established between the AC interfaces of PEs.

Configure physical layer fault notification on the PE.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The AC interface view is displayed.
   
   
   
   * The AC interface must be a primary Ethernet interface.
   * The AC interface is configured with a VC.
3. Run [**mpls l2vpn trigger if-down**](cmdqueryname=mpls+l2vpn+trigger+if-down)
   
   
   
   Physical layer fault notification is enabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Checking the Configurations

After configuring physical layer fault detection, check the configuration. Run the [**display mpls l2vc**](cmdqueryname=display+mpls+l2vc) command to check whether physical layer fault notification has been configured.
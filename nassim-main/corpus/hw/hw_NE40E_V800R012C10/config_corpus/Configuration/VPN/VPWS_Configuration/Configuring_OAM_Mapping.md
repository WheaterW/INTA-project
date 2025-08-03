Configuring OAM Mapping
=======================

OAM mapping accelerates AC fault detection and notification.

#### Usage Scenario

On an MPLS L2VPN, PEs and CEs do not notify the others of their master/backup status and link status. To detect the PW and AC status, deploy OAM separately for PWs and ACs. Then enable OAM mapping on PEs to associate PW OAM with AC OAM. This configuration accelerates AC fault detection and notification.


#### Pre-configuration Tasks

Before configuring OAM mapping, complete the following tasks:

* Configure network layer parameters for devices to communicate.
* Configure PWs.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The AC interface view is displayed.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The AC interface must be an Ethernet sub-interface.
3. Run [**mpls l2vpn oam-mapping**](cmdqueryname=mpls+l2vpn+oam-mapping) **1ag** **md** *md-name* **ma** *ma-name*
   
   
   
   OAM mapping between ACs and PWs is configured.
   
   
   
   * Before running this command, configure Ethernet OAM for ACs.
   * After running the preceding command, run the [**display mpls l2vc oam-mapping**](cmdqueryname=display+mpls+l2vc+oam-mapping) [ **interface** *interface-type* *interface-number* ] command to check the VC status. In this case, **Local AC OAM State** indicates the link status of the AC. If you run the [**display mpls l2vc oam-mapping**](cmdqueryname=display+mpls+l2vc+oam-mapping) [ **interface** *interface-type* *interface-number* ] command to check the VC status before the preceding command is run, **Local AC OAM State** remains **Up** and is not associated with the link status.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After configuring OAM mapping, verify the configuration as follows.

* Run the [**display mpls l2vc oam-mapping**](cmdqueryname=display+mpls+l2vc+oam-mapping) [ **interface** *interface-type* *interface-number* ] command to check OAM mapping information.
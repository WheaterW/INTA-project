(Optional) Configuring an AC Interface to Transparently Transmit TDM Frames/ATM Cells
=====================================================================================

A PW can be configured on an AC interface only after the AC interface has been configured to transparently transmit TDM frames/ATM cells.

#### Context

**Figure 1** Networking for multiple TDM/ATM base stations connected to a base station controller over an IP RAN  
![](images/fig_dc_vrp_vpws_cfg_600601.png)  

Wireless communication services are developing and 2G, 3G, and LTE services will be all transmitted on a bearer network. In addition to wireless services, an IP RAN utilizes PWE3 technology to transparently transmit TDM/ATM services, enabling carriers to maximize return on investment in existing networks.

On the network shown in [Figure 1](#EN-US_TASK_0172369797__fig_dc_vrp_vpws_cfg_600601), TDM/ATM services are sent to a CSG along E1, CE1, or CPOS links. The CSG sends the TDM/ATM services transparently to an RSG through a PWE3 connection. The RSG forwards these services to a base station controller over an E1, CE1, or CPOS link. E1, CE1, or CPOS interfaces are usually channelized into synchronous serial interfaces before transmitting upper-layer services. Synchronous serial interfaces are slow and cannot provide the 8 to 16 Mbit/s bandwidth needed for 3G RAN services. IMA group interfaces and ATM bundle interfaces are used to provide the required bandwidth and improve transmission resource utilization. In addition, ATM cell relay at different levels is provided to meet the connection requirements of various scenarios.

When an IP RAN carries TDM services, channelized serial interfaces can be used to transparently transmit TDM frames. In addition to serial interfaces that are seldom used due to insufficient bandwidth, IMA group interfaces and ATM bundle interfaces are generally used to transmit ATM services from base stations to CSGs.

* IMA group interfaces
  
  An IMA group is a logical link and consists of one or more links. An IMA group provides more bandwidth (approximately equal to the total bandwidth of all member links) than any single member link. IMA groups enable more flexible and efficient use of interfaces, conserving bandwidth resources.
* ATM bundle interfaces
  
  ATM bundle interfaces forward the same type of service from base stations along the same PW to a base station controller, reducing the load on the CSG and improving service scalability.
  
  On the network shown in [Figure 1](#EN-US_TASK_0172369797__fig_dc_vrp_vpws_cfg_600601), assume that multiple base stations connect to a CSG over E1 or CPOS links. Every base station may transmit voice, video, and data services. This requires the CSG to create three PVCs for each base station before transmitting voice, video, and data services.
  
  If a separate PW is used to transmit each type of service on each base station, a large number of PWs need to be configured on the CSG. The growing number of NodeBs and service types creates an increasing burden on the CSG.
  
  To address this issue, bind sub-interfaces transmitting the same type of service from different base stations to an ATM bundle interface on the CSG. Then, configure a PW on the ATM bundle interface to transmit service traffic from the CSG to the RNC. This means that each type of service requires only one ATM bundle interface and one PW on a CSG, reducing the number of PWs, alleviating the pressure on the CSG, and improving service scalability.
* ATM interface:
  
  When using a PW set up between the ATM interfaces on two CEs to emulate a private line connecting two remote ATM interfaces, you can configure ATM cell relay in port-based mode. Then, all ATM cells from an interface can be transparently transmitted to the peer interface without being processed or exchanged at the VPC/VCC layer.
* AAL5 SDU:
  
  When a large number of AAL5 service frames are transmitted on an ATM network, you can implement ATM cell relay in AAL5 SDU mode.


#### Procedure

* Configure a serial interface to transparently transmit TDM frames.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run either of the following commands:
     
     + To enter the view of a serial interface channelized from an E1/CE1 interface, run the [**interface**](cmdqueryname=interface) **serial** *controller-number* **:** *set-number* command.
     + To enter the view of a serial interface channelized from a CPOS interface, run the [**interface**](cmdqueryname=interface) **serial** *controller-number/e1-number* **:** *set-number* command.
  3. Run [**link-protocol tdm**](cmdqueryname=link-protocol+tdm)TDM is configured as the encapsulation protocol for serial interfaces.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     A serial interface running the TDM protocol does not recognize the valid bytes of received TDM frames. It is futile to view the rate and bandwidth of this serial interface.
  4. Run [**quit**](cmdqueryname=quit)
     
     Exit the serial interface view.
  5. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configure a serial interface or an IMA group interface to transparently transmit ATM cells.
  
  
  
  The L2VPN technology provides four levels of simulation services for transparently transmitting ATM cells on serial or IMA group interfaces.
  
  | Transparent Cell Transport Mode | AC Interface | Usage Scenario |
  | --- | --- | --- |
  | N-to-1 VCC | Serial and IMA group sub-interfaces | VCC: virtual circuit connection. A VCC is the basic unit on an ATM network and transmits various ATM services.  VPC: virtual path connection. A VPC is a group of VCCs destined for the same destination. It can be used to transmit various ATM services. If multiple VCCs destined for the same destination are needed, a VPC is more advantageous than VCCs, as it transmits cells more quickly than VCCs and is easier to manage and configure.  In N-to-1 mode, a physical link is divided into multiple PVCs, each of which transmits one type of service.  If a PSN transmitting ATM services requires high transmission speed and the service traffic is light, you can configure 1-to-1 ATM cell relay. |
  | 1-to-1 VCC | Serial and IMA group sub-interfaces |
  | N-to-1 VPC | Serial and IMA group sub-interfaces |
  | 1-to-1 VPC | Serial and IMA group sub-interfaces |
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Configure ATM cell relay based on the modes and AC interface types listed in the following table.
     
     | Transparent Cell Transport Mode | Serial Interface Channelized from an E1/CE1 Interface | Serial Interface Channelized from a CPOS Interface | IMA Group Interface |
     | --- | --- | --- | --- |
     | N-to-1 VCC | 1. Run the [**interface**](cmdqueryname=interface) **serial** *controller-number*:*set-number.subnumber* **p2mp** command to create a serial sub-interface and enter its view. | 1. Run the [**interface**](cmdqueryname=interface) **serial** *controller-number*/*e1-number*:*set-number*.*subnumber* **p2mp** command to create a serial sub-interface and enter its view. | 1. Create an IMA group interface and add the serial interface into the IMA group interface. For information about IMA group interface configuration, see [Configure an IMA group interface](#EN-US_TASK_0172369797__dc_vrp_vpws_cfg_6006_step_01). |
     | 2. Run the [**interface ima-group**](cmdqueryname=interface+ima-group) *interface-number.subnumber* **p2mp** command to create an IMA group sub-interface and enter its view. |
     | 2. Run the [**pvc**](cmdqueryname=pvc) *vpi/vci* command to create a PVC and enter its view. | | |
     | 1-to-1 VCC | 1. Run the [**interface**](cmdqueryname=interface) **serial** *controller-number*:*set-number.subnumber* **p2p** command to create a serial sub-interface and enter its view. | 1. Run the [**interface**](cmdqueryname=interface) **serial** *controller-number*/*e1-number*:*set-number*.*subnumber* **p2p** command to create a serial sub-interface and enter its view. | 1. Create an IMA group interface and add the serial interface into the IMA group interface. For information about IMA group interface configuration, see [Configure an IMA group interface](#EN-US_TASK_0172369797__dc_vrp_vpws_cfg_6006_step_01). |
     | 2. Run the [**interface ima-group**](cmdqueryname=interface+ima-group) *interface-number.subnumber* **p2p** command to create an IMA group sub-interface and enter its view. |
     | 2. Run the [**pvc**](cmdqueryname=pvc) *vpi/vci* command to create a PVC and enter its view. | | |
     | N-to-1 VPC | 1. Run the interface **serial** *controller-number*:*set-number.subnumber* **p2mp** command to create a serial sub-interface and enter its view. | 1. Run the [**interface**](cmdqueryname=interface) **serial** *controller-number*/*e1-number*:*set-number*.*subnumber* **p2mp** command to create a serial sub-interface and enter its view. | 1. Create an IMA group interface and add the serial interface into the IMA group interface. For information about IMA group interface configuration, see [Configure an IMA group interface](#EN-US_TASK_0172369797__dc_vrp_vpws_cfg_6006_step_01). |
     | 2. Run the [**interface ima-group**](cmdqueryname=interface+ima-group) *interface-number.subnumber* **p2mp** command to create an IMA group sub-interface and enter its view. |
     | 2. Run the [**pvp**](cmdqueryname=pvp) *vpi* command to create a PVP and enter its view. | | |
     | 1-to-1 VPC | 1. Run the [**interface**](cmdqueryname=interface) **serial** *controller-number*:*set-number.subnumber* **p2p** command to create a serial sub-interface and enter its view. | 1. Run the [**interface**](cmdqueryname=interface) **serial** *controller-number*/*e1-number*:*set-number*.*subnumber* **p2p** command to create a serial sub-interface and enter its view. | 1. Create an IMA group interface and add the serial interface into the IMA group interface. For information about IMA group interface configuration, see [Configure an IMA group interface](#EN-US_TASK_0172369797__dc_vrp_vpws_cfg_6006_step_01). |
     | 2. Run the [**interface ima-group**](cmdqueryname=interface+ima-group) *interface-number.subnumber* **p2p** command to create an IMA group sub-interface and enter its view. |
     | 2. Run the [**pvp**](cmdqueryname=pvp) *vpi* command to create a PVP and enter its view. | | |
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + N-to-1 ATM cell relay is only supported by P2MP ATM sub-interfaces. 1-to-1 ATM cell relay is only supported by P2P ATM sub-interfaces. ATM interface supports neither N-to-1 nor 1-to-1 ATM cell relay.
     + 1-to-1 ATM cell relay also supports VPI/VCI mapping. PEs on both ends of an ATM link create a PVC or a PVP by using VPI and VCI values equal to those set on the connected CE. The system automatically identifies L2VC connections as the same VC or VP based on VPI and VCI mapping.
  3. Run [**quit**](cmdqueryname=quit)
     
     Exit the serial or IMA group interface view.
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configure an ATM bundle interface to transparently transmit ATM cells.
  
  
  1. Configure an ATM bundle interface.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Create multiple ATM bundle interfaces and corresponding PWs to transmit various types of services.
     
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**interface atm-bundle**](cmdqueryname=interface+atm-bundle) *bundle-id*
        
        An ATM bundle interface is created.
     3. Run [**quit**](cmdqueryname=quit)
        
        Exit from the ATM bundle interface view.
  2. Add a serial or IMA group sub-interface to the ATM bundle interface.
     
     1. Run one of the following commands based on the sub-interface type:
     + To enter the view of a sub-interface of a serial interface channelized from E1/CE1 interfaces, run:
       ```
       [interface](cmdqueryname=interface) serial controller-number : set-number.subinterface-number
       ```
     + To enter the view of a sub-interface of a serial interface channelized from CPOS interfaces, run:
       ```
       [interface](cmdqueryname=interface) serial controller-number/e1-number : set-number.subinterface-number
       ```
     + To enter the IMA group sub-interface view, run:
       ```
       [interface ima-group](cmdqueryname=interface+ima-group) interface-number.subinterface-number
       ```![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + A serial sub-interface must be configured with a PVC or PVP before joining an ATM bundle interface; otherwise, the serial sub-interface will fail to join an ATM bundle interface.
     + Multiple serial sub-interfaces can join one ATM bundle interface, allowing the same type of services from multiple sources to travel through one PW.
  3. Run [**atm-bundle**](cmdqueryname=atm-bundle) *bundle-id*
     
     A serial or IMA group sub-interface is added to the ATM bundle interface.
  4. Run [**quit**](cmdqueryname=quit)
     
     Exit from the serial or IMA group sub-interface view.
  5. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configuring an IMA group interface to transparently transmit ATM cells.
  
  
  1. Create an IMA group interface.
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**interface ima-group**](cmdqueryname=interface+ima-group) *interface-number*
        
        An IMA group interface is created.
     3. Run [**quit**](cmdqueryname=quit)
        
        Exit from the IMA group interface view.
  2. Add a serial interface to an IMA group interface.
     1. Run either of the following commands:
        + To enter the view of a sub-interface of a serial interface channelized from E1/CE1 interfaces, run:
          ```
          [interface](cmdqueryname=interface) serial controller-number : set-number
          ```
        + To enter the view of a sub-interface of a serial interface channelized from CPOS interfaces, run:
          ```
          [interface](cmdqueryname=interface) serial controller-number/e1-number : set-number
          ```
        + To enter the view of a sub-interface of a serial interface channelized from CPOS interfaces, run:
          ```
          [interface](cmdqueryname=interface) serial controller-number/e1-number : set-number
          ```
     2. Run [**link-protocol atm**](cmdqueryname=link-protocol+atm)
        
        ATM is configured as a data-link-layer protocol for the serial interface.
     3. Run [**ima**](cmdqueryname=ima) { *iftype* *ifnumber* | *ifname* }
        
        The serial interface is added to the IMA group interface.
     4. Run [**quit**](cmdqueryname=quit)
        
        Exit the serial interface view.
     5. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
* Configure an ATM interface to work in ATM cell relay mode.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface atm**](cmdqueryname=interface+atm) *interface-number*
     
     
     
     The ATM interface view is displayed.
  3. Run [**atm cell transfer**](cmdqueryname=atm+cell+transfer)
     
     
     
     The ATM interface is configured to work in ATM cell relay mode.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     On a VRP-based device, run the [**atm cell transfer**](cmdqueryname=atm+cell+transfer) command to configure ATM cell relay on an ATM interface before configuring VPWS on the interface. If you configure VPWS first, the ATM interface will work in frame relay mode by default. After configuring the [**atm cell transfer**](cmdqueryname=atm+cell+transfer) command, you must run the [**shutdown**](cmdqueryname=shutdown) and [**shutdown**](cmdqueryname=shutdown) undo commands in succession for the configuration to take effect.
* Configure AAL5 SDU frame relay on an ATM interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface atm**](cmdqueryname=interface+atm) *interface-number*.*sub-interface-number* **p2p**
     
     
     
     A P2P ATM sub-interface is created, and the sub-interface view is displayed.
  3. Run [**pvc**](cmdqueryname=pvc) { *pvc-name* [ *vpi* / *vci* ] | *vpi* / *vci* }
     
     
     
     A PVC is created, and the PVC view is displayed.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + When configuring AAL5 SDU frame relay, you must create a PVC before creating a VPWS connection. After the VPWS connection is established, the PVC cannot be deleted. To delete the PVC, you must delete the established VPWS connection first.
     + An ATM sub-interface can work in any of the following modes: cell relay, frame relay, and IPoA (IP over AAL5).
       - In cell relay mode, the [**atm cell transfer**](cmdqueryname=atm+cell+transfer) command must be configured on the ATM interface.
       - In frame relay mode, the [**atm cell transfer**](cmdqueryname=atm+cell+transfer) command does not need to be configured on the ATM interface.
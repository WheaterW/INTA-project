Configuring Basic PVC Functions
===============================

After a mapping between a Permanent Virtual Circuit (PVC) and a remote protocol address is configured, upper-layer protocol packets can be encapsulated in ATM cells and transmitted on ATM networks.

#### Context

[Table 1](#EN-US_TASK_0172364316__tab_dc_vrp_cfg_01405701) lists the relationships between PVC encapsulation types and upper-layer protocols.

**Table 1** Relationships between PVC encapsulation types and upper-layer protocols
| Upper-Layer Protocol/Encapsulation Type | aal5snap | aal5mux | aal5nlpid | aal5nlpidietf |
| --- | --- | --- | --- | --- |
| IPoA | Supported | Supported (not supported if Inverse Address Resolution Protocol [InARP] is used) | Supported (not supported if InARP is used) | Supported (not supported if InARP is used) |




#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface atm**](cmdqueryname=interface+atm) *interface-number*[.*subinterface* ] [ **p2mp** | **p2p** ]
   
   
   
   The view of an ATM interface or sub-interface is displayed.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After you enter the view of an ATM interface or sub-interface, you can configure the following parameters:
   
   * To enable OAM on an ATM sub-interface, run the [**atm-link check**](cmdqueryname=atm-link+check) command. If the PVC and PVP status of the ATM sub-interface goes Down, the protocol status on the sub-interface also goes Down.
   * To configure the maximum number of VCs on an ATM interface, run the [**pvc max-number**](cmdqueryname=pvc+max-number) command. If the number of PVCs configured on the ATM interface reach the maximum limit, no new PVC can be configured on the interface.
3. Run [**pvc**](cmdqueryname=pvc) { *pvc-name* [ *vpi*/*vci* ] | *vpi*/*vci* }
   
   
   
   A PVC is created and the PVC view is displayed.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * The VCI values 3, 4 are reserved.
   * The VPI and VCI values cannot be both 0s.
   * The value of *vpi*/*vci* cannot be 255/65535.
4. (Optional) Run [**description**](cmdqueryname=description) *text*
   
   
   
   The description is configured for the PVC.
5. Run [**encapsulation**](cmdqueryname=encapsulation) { **aal5snap** | **aal5mux** | **aal5nlpid** | **aal5nlpidietf** }
   
   
   
   An AAL5 encapsulation type is configured for the PVC.
   
   [Table 1](#EN-US_TASK_0172364316__tab_dc_vrp_cfg_01405701) lists the relationships between PVC encapsulation types and upper-layer protocols.
6. Run [**map ip**](cmdqueryname=map+ip) { *ip-address* | **inarp** [ *minutes* ] } [ **broadcast** ]
   
   
   
   The IPoA mapping is configured on the PVC so that AAL5 carries IP packets.
   
   Running the [**map ip**](cmdqueryname=map+ip) *ip-address* command configures a mapping between a PVC and a destination IP address. Every IP packet to be transmitted on an IPoA network must be mapped to a PVC, and therefore multiple mappings are required. To configure mappings in batches, perform the following operations as required:
   * To map all the IP packets destined for the same network segment to one PVC, run the [**map ip**](cmdqueryname=map+ip) *ip-address* *mask* command.
   * If the local device is the DTE, run the [**map ip**](cmdqueryname=map+ip) **inarp** [ *minutes* ] command to use InARP for automatic mapping. In this case, you do not need to configure mappings between IP addresses and PVCs.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     *minutes* must be set to a proper value based on the network topology stability. If the network topology changes frequently, set a small *minutes* value. If the network topology is stable, set a large *minutes* value.
   
   If the upper-layer protocol, for example, OSPF, transmits packets in broadcast mode, configure **broadcast** for the PVC. If a PVC is configured with **broadcast**, all broadcast packets transmitted through the interface where the PVC resides will be copied to the PVC.
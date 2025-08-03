Configuring a VXLAN Service Access Point
========================================

Layer 2 sub-interfaces are used for service access on VXLANs. These Layer 2 sub-interfaces can have different encapsulation types configured to transmit various types of data packets. A Layer 2 sub-interface can transmit data packets through a BD after being associated with it.

#### Context

As described in [Table 1](#EN-US_TASK_0000001480051193__en-us_task_0274174837_tab_1), Layer 2 sub-interfaces can have different encapsulation types configured to transmit various types of data packets.

**Table 1** Traffic encapsulation types
| Traffic Encapsulation Type | Description |
| --- | --- |
| **dot1q** | This type of sub-interface accepts only packets with a specified VLAN tag. The **dot1q** traffic encapsulation type has the following restrictions:  * The VLAN ID encapsulated by a Layer 2 sub-interface cannot be the same as that permitted by the Layer 2 main interface of the sub-interface. * The VLAN IDs encapsulated by a Layer 2 sub-interface and a Layer 3 sub-interface cannot be the same. |
| **untag** | This type of sub-interface accepts only packets that do not carry VLAN tags. The **untag** traffic encapsulation type has the following restrictions:  * The physical interface where the involved sub-interface resides must have only default configurations. * Only Layer 2 physical interfaces and Eth-Trunk interfaces can have **untag** Layer 2 sub-interfaces created. * Only one **untag** Layer 2 sub-interface can be created on a main interface. |
| **default** | This type of sub-interface accepts all packets, regardless of whether they carry VLAN tags. The **default** traffic encapsulation type has the following restrictions:  * The main interface where the involved sub-interface resides cannot be added to any VLAN. * Only Layer 2 physical interfaces and Eth-Trunk interfaces can have **default** Layer 2 sub-interfaces created. * If a **default** Layer 2 sub-interface is created on a main interface, the main interface cannot have other types of Layer 2 sub-interfaces configured. |
| **qinq** | This type of sub-interface receives packets that carry two or more VLAN tags and determines whether to accept the packets based on the innermost two VLAN tags. |


A service access point needs to be configured on a Layer 2 gateway.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id*
   
   
   
   A BD is created, and the BD view is displayed.
3. (Optional) Run [**description**](cmdqueryname=description) *description*
   
   
   
   A BD description is configured.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view from the BD view.
5. Run [**interface**](cmdqueryname=interface) *interface-type interface-number.subnum* **mode l2**
   
   
   
   A Layer 2 sub-interface is created, and the sub-interface view is displayed.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Before running this command, ensure that the involved Layer 2 main interface does not have the [**port link-type**](cmdqueryname=port+link-type) **dot1q-tunnel** command configuration. If the configuration exists, run the [**undo port link-type**](cmdqueryname=undo+port+link-type) command to delete it.
6. Run [**encapsulation**](cmdqueryname=encapsulation) { **dot1q** [ **vid** *vid* ] | **default** | **untag** | **qinq** [ **vid** *pe-vid* **ce-vid** { *low-ce-vid* [ **to** *high-ce-vid* ] } ] }
   
   
   
   A traffic encapsulation type is configured for the Layer 2 sub-interface.
7. Run [**rewrite pop**](cmdqueryname=rewrite+pop) { **single** | **double** }
   
   
   
   The Layer 2 sub-interface is enabled to remove single or double VLAN tags from received packets.
   
   
   
   If the received packets each carry a single VLAN tag, specify **single**.
   
   If the traffic encapsulation type has been specified as **qinq** using the [**encapsulation**](cmdqueryname=encapsulation) **qinq** **vid** *pe-vid* **ce-vid** { *low-ce-vid* [ **to** *high-ce-vid* ] | **default** } command in the preceding step, specify **double**.
8. Run [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id*
   
   
   
   The Layer 2 sub-interface is added to the BD so that it can transmit data packets through this BD.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If a [**default**](cmdqueryname=default) Layer 2 sub-interface is added to a BD, no VBDIF interface can be created for the BD.
9. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view from the Layer 2 sub-interface view.
10. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.
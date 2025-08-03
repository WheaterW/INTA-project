Configuring the MSTP Protocol Packet Format on an Interface
===========================================================

MSTP protocol packets can be transmitted in auto, dot1s, or legacy mode.

#### Context

MSTP protocol packets have two formats: dot1s (IEEE 802.1s standard packets) and legacy (proprietary protocol packets). The auto mode is introduced to allow an interface to automatically use the format of MSTP protocol packets sent from the remote interface. In this manner, the two interfaces use the same MSTP protocol packet format.

Do as follows on a device in a Multiple Spanning Tree (MST) region:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The view of the Ethernet interface participating in spanning tree protocol calculation is displayed.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The following configuration can be configured both on a Layer 2 interface and a Layer 3 interface.
3. (Optional) Run [**stp binding process**](cmdqueryname=stp+binding+process) *process-id*
   
   
   
   The interface is bound to an MSTP process.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   This step is performed only when the interface needs to be bound to an MSTP process with a non-zero ID. If the interface belongs to process 0, skip this step.
4. Run [**stp compliance**](cmdqueryname=stp+compliance) { **auto** | **dot1s** | **legacy** }
   
   
   
   The MSTP protocol packet format is configured on the interface.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
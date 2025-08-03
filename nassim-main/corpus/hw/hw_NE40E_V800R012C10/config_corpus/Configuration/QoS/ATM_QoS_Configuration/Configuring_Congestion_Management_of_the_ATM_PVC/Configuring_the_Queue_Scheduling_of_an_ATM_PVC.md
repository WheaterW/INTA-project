Configuring the Queue Scheduling of an ATM PVC
==============================================

When the network is congested, you can buffer the packets that exceed the PVC bandwidth and then send the packets out when the network becomes idle.

#### Context

Perform the following steps on the Router:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) **atm** *interface-number* [.*sub-interface* ]
   
   
   
   The ATM interface view or sub-interface view is displayed.
3. Run [**pvc**](cmdqueryname=pvc) { *pvc-name* [ *vpi*/*vci* ] | *vpi*/*vci* }
   
   
   
   The PVC view is displayed.
4. Run [**shutdown**](cmdqueryname=shutdown)
   
   
   
   The PVC is shut down.
5. Run [**pvc-queue**](cmdqueryname=pvc-queue) { **ef** | **af1** | **af2** | **af3** | **af4** | **be** | **cs6** | **cs7** } { **pq** | **wfq** **weight** *weight* } [ **shaping** **pir** { *pir-value* | **percentage** *pir-percent* } ] **outbound**
   
   
   
   The queue scheduling parameter of the ATM PVC is configured.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * Of the eight queues for a PVC, only one queue can be configured with the PQ scheduling.
   * If one PVC queue is configured with the PQ or WFQ scheduling, the rest queues are configured with the WFQ scheduling by default. The default scheduling parameter is 20.
   * Queue scheduling of ATM PVCs can be configured only for downstream packets.
6. Run [**undo shutdown**](cmdqueryname=undo+shutdown)
   
   
   
   The queue scheduling parameter for the PVC is enabled.
   
   Before configuring the queue scheduling parameter of an ATM PVC, you must run the [**shutdown**](cmdqueryname=shutdown) command to shut down the PVC.
Failed to Find Routes of a Non-Local Area
=========================================

Failed to Find Routes of a Non-Local Area

#### Fault Symptom

When links are normal, OSPF cannot find routes of a non-local area.


#### Procedure

1. Check whether the local area is connected to the backbone area.
   
   
   
   Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **brief** command on the ABR in the local area to check the area configuration.
   
   OSPF requires that all non-backbone areas be connected to the backbone area.
   
   If the backbone area configuration does not exist on the ABR, run the [**area**](cmdqueryname=area) *area-id* command in the OSPF view to modify the OSPF area configuration. Ensure that at least one interface on the ABR runs in the backbone area.
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   If not all non-backbone areas can be connected to the backbone area due to networking restrictions, configure OSPF virtual links to resolve this problem.
2. Check whether the local area is a totally stubby area.
   
   
   
   Run the [**display current-configuration**](cmdqueryname=display+current-configuration) **configuration** **ospf** [ *process-id* ] command on the device to check the OSPF process configuration.
   
   If you specify the **no-summary** parameter on the ABR when configuring a non-backbone area as a stub area (running the [**stub**](cmdqueryname=stub) **no-summary** command in the OSPF area view), the area will become a totally stubby area.
   
   A totally stubby area allows only intra-area routes to be advertised. Specifically, AS external routes or inter-area routes cannot be advertised in a totally stubby area.
   
   If the area where the device resides is configured as a totally stubby area, perform either of the following operations as needed:
   * To restore the totally stubby area to a common area, run the [**undo stub**](cmdqueryname=undo+stub) command in the OSPF area view on each device in this area.
   * To change the totally stubby area to a stub area, run the [**undo stub**](cmdqueryname=undo+stub) command in the OSPF area view on the ABR in this area and then run the [**stub**](cmdqueryname=stub) command.
3. Check whether the area where the device resides is a totally NSSA.
   
   
   
   Run the [**display current-configuration**](cmdqueryname=display+current-configuration) **configuration** **ospf** [ *process-id* ] command on the device to check the OSPF process configuration.
   
   If you specify the **no-summary** parameter on the ABR when configuring a non-backbone area as an NSSA (running the [**nssa**](cmdqueryname=nssa) **no-summary** command in the OSPF area view), the area will become a totally NSSA.
   
   A totally NSSA allows only intra-area routes to be advertised. Specifically, AS external routes or inter-area routes cannot be advertised in a totally NSSA.
   
   If the area where the device resides is configured as a totally NSSA, perform either of the following operations as needed:
   * To restore the totally NSSA to a common area, run the [**undo nssa**](cmdqueryname=undo+nssa) command in the OSPF area view on each device in this area.
   * To change the totally NSSA to an NSSA, run the [**undo nssa**](cmdqueryname=undo+nssa) command in the OSPF area view on the ABR in this area and then run the [**nssa**](cmdqueryname=nssa) command.
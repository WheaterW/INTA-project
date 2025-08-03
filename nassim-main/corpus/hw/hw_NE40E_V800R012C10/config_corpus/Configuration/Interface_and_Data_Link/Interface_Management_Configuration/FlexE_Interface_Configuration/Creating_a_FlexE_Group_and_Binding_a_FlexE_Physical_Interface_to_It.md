Creating a FlexE Group and Binding a FlexE Physical Interface to It
===================================================================

After a FlexE group is created, you can bind a group of FlexE physical interfaces to it, flexibly allocating bandwidth to FlexE clients based on the sub-timeslot granularity.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**flexe group**](cmdqueryname=flexe+group) *group-index*
   
   
   
   A FlexE group is created, or the view of a specified FlexE group is displayed.
3. (Optional) Run [**description**](cmdqueryname=description) *text*
   
   
   
   A description is configured for the FlexE group.
   
   
   
   To facilitate memorization and management, you can perform this step to describe a specific FlexE group.
4. Run [**binding interface**](cmdqueryname=binding+interface) *interface-type* *interface-number*
   
   
   
   A specified FlexE physical interface is bound to the FlexE group.
5. (Optional) Run [**padding enable**](cmdqueryname=padding+enable)
   
   
   
   Padding is enabled. The
6. (Optional) Run [**timeslot-negotiation mode disable**](cmdqueryname=timeslot-negotiation+mode+disable)
   
   
   
   Timeslot negotiation is disabled.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the timeslot mode has been configured on the FlexE card where the PHYs bound to a FlexE group reside, ensure that the FlexE clients in the group are not bound to any sub-timeslots before disabling timeslot negotiation.
   
   * If the peer device does not support timeslot negotiation, you need to disable it in the FlexE group view of the local device.
   * The same timeslot negotiation mode must be configured for the FlexE groups on both ends. Otherwise, the FlexE interfaces may fail to go up or fail to forward traffic after a reliability operation (such as an active/standby switchover, subcard reset, or interface shutdown/startup) is performed.
   * After timeslot negotiation is disabled for the FlexE groups on both ends, the same timeslot number must be configured for the corresponding FlexE clients. Otherwise, the FlexE interfaces may fail to go up or fail to forward traffic.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
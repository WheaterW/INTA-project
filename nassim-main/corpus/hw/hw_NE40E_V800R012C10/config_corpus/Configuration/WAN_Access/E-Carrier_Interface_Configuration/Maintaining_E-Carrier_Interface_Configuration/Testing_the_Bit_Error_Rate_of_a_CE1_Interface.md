Testing the Bit Error Rate of a CE1 Interface
=============================================

The testing results can be used to locate link faults.

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In VS mode, this configuration
process is supported only by the admin VS.

When faults
occur on a CE1 interface, you can run the **test connectivity controller
e1** command for fault locating.


#### Prerequisites

The serial interface service
has been configured.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**test connectivity controller e1**](cmdqueryname=test+connectivity+controller+e1) *controller-number* { **unframed** | **channelized timeslot-list** *slot-list* } **duration** *time*
   
   
   
   The bit error rate is tested on a specified CE1 interface.
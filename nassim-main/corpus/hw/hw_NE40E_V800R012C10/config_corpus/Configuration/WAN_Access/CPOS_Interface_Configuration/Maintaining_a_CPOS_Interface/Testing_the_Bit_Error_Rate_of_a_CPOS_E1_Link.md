Testing the Bit Error Rate of a CPOS E1 Link
============================================

The testing results can be used to locate link faults.

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In VS mode, this configuration process is supported only by the admin VS.

When faults occur on a CPOS E1 link, you can run the **test connectivity controller cpos e1** command for fault locating.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**test connectivity controller cpos**](cmdqueryname=test+connectivity+controller+cpos)  *controller-number* **e1** *e1-number* { **unframed** | **channelized timeslot-list** *slot-list* } **duration** *time*
   
   
   
   The bit error rate is tested on a specified CPOS E1 link.
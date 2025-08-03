Configuring OTN Delay Measurement
=================================

Configuring OTN delay measurement allows you to obtain the two-way delay on an OTN.

#### Context

As shown in [Figure 1](#EN-US_TASK_0172364272__fig_dc_ne_wdm_cfg_001), OTN delay measurement can be configured to measure the OTN delay.

**Figure 1** Networking for OTN delay measurement  
![](images/fig_dc_ne_wdm_cfg_200801.png)  

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This configuration is mainly performed on Device A and Device B, which function as the source and sink devices, respectively.



#### Procedure

1. Enable delay measurement at the sink end.
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**controller wdm**](cmdqueryname=controller+wdm) *interface-number* command to enter the WDM interface view.
   3. Run the [**delay-measurement sink pm enable**](cmdqueryname=delay-measurement+sink+pm+enable) command to enable delay measurement on Device B.
2. Start delay measurement at the source end.
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**controller wdm**](cmdqueryname=controller+wdm) *interface-number* command to enter the WDM interface view.
   3. Run the [**delay-measurement source start pm**](cmdqueryname=delay-measurement+source+start+pm) [ **duration** *value* ] command to start delay measurement at the source end.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      Before starting delay measurement at the source end, you need to enable delay measurement at the sink end. This command is valid only in the specified delay measurement duration.

#### Verifying the Configuration

After the configuration is complete, run the [**display delay-measurement pm controller**](cmdqueryname=display+delay-measurement+pm+controller) *controller-type* *controller-number* command on Device A to check statistics about two-way delay measurement.
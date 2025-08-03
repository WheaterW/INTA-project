(Optional) Configuring Network-Side PRBS Testing
================================================

After PRBS testing is enabled, you can perform a one-click test to check the service connectivity on the NNI side, that is, whether the PW between PEs is functioning properly.

#### Context

As shown in [Figure 1](#EN-US_TASK_0172364445__fig_dc_ne_cfg_prbs_000102), PW connectivity between PE1 and PE2 can be tested by enabling PE1 to send a PRBS bit stream to PE2, which has local loopback enabled.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Before performing a NNI-side PRBS test on a local device, you must configure local loopback on the remote interface connecting to the local device. Services on the remote interface are then interrupted. After the test is completed, manually restore services on the remote interface.


**Figure 1** Network-side PRBS testing  
![](images/fig_dc_ne_cfg_prbs_000102.png)  
![](../../../../public_sys-resources/note_3.0-en-us.png) 

Both the PE1 and PE2 are NE40Es in this example.




#### Procedure

1. Configure local loopback on the E1 interface of the PE2 connecting to PE1.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**controller cpos**](cmdqueryname=controller+cpos) *cpos-number*
      
      
      
      The CPOS interface view is displayed.
   3. Run [**e1**](cmdqueryname=e1) *e1-number* **set** **loopback** **local**
      
      
      
      Local loopback is enabled for the E1 interface.
2. Perform a PRBS test on PE1.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**test connectivity**](cmdqueryname=test+connectivity) **interface** { *interface-name* | *interface-type* *interface-number* } **nni-direction** **pattern** *pattern-list* **interval** { **hour** *hour-value* | **minute** *minute-value* | **second** *second-value* } **interval-repeat** *repeat-count*
      
      
      
      An enhanced PRBS connectivity test is performed on a network-side low-speed interface.
   3. (Optional) Run [**test connectivity**](cmdqueryname=test+connectivity) **error-insert** **interface** { *interface-name* | *interface-type* *interface-number* } { **single-bit** | **insert-ratio** *ratio-list* }
      
      
      
      Bit errors are injected into a PRBS bit stream while the enhanced PRBS connectivity test is going on.
   4. (Optional) Run [**test connectivity**](cmdqueryname=test+connectivity) **abort** **interface** { *interface-name* | *interface-type* *interface-number* }
      
      
      
      The enhanced PRBS connectivity test is ended.
3. After the PRBS test is completed, cancel the local loopback configuration on the E1 interface of the PE2.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**controller cpos**](cmdqueryname=controller+cpos) *cpos-number*
      
      
      
      The CPOS interface view is displayed.
   3. Run [**undo e1**](cmdqueryname=undo+e1) *e1-number* **set** **loopback**
      
      
      
      Local loopback of the E1 interface is canceled.
Configuring Dynamic Load Balancing
==================================

If existing load balancing configurations do not meet actual needs, configure dynamic load balancing.

#### Context

The Router supports multiple load balancing configurations, including IP packet, VPLS, VLL, and trunk member interface-based load balancing configurations. If these configurations do not meet actual needs, configure dynamic load balancing to enable the Router to dynamically adjust load balancing.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In VS mode, this configuration process is supported only by the admin VS.



#### Procedure

* Configure dynamic adjustment of trunk load balancing.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**load-balance dynamic-adjust trunk enable**](cmdqueryname=load-balance+dynamic-adjust+trunk+enable)
     
     
     
     Dynamic adjustment of trunk load balancing is enabled.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     To modify parameters for dynamic adjustment of trunk load balancing, perform the following optional steps.
  4. (Optional) Run [**slot**](cmdqueryname=slot) *slot-id*
     
     
     
     The slot view is displayed.
  5. (Optional) Run [**load-balance dynamic-adjust trunk**](cmdqueryname=load-balance+dynamic-adjust+trunk) { **scan** *scan-period* | **cpu** *cpu-threshold* | **cpu-detect** *cpu-detect-period* | **cpu-restore** *cpu-restore-threshold* | **statistics** *statistics-period* | **precision** *precision-threshold* }
     
     
     
     Parameters for dynamic adjustment of trunk load balancing are configured.
  6. (Optional) Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure dynamic load balancing.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**slot**](cmdqueryname=slot) *slot-id*
     
     
     
     The slot view is displayed.
  3. Run [**load-balance dynamic-adjust enable**](cmdqueryname=load-balance+dynamic-adjust+enable)
     
     
     
     Dynamic load balancing is enabled.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
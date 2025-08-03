(Optional) Configuring the CAR Function for Mirrored Traffic
============================================================

This section describes how to configure the committed access rate (CAR) function for mirrored traffic. This function helps prevent a large volume of mirrored traffic from affecting packet processing.

#### Context

The mirrored port and observing port required for mirroring must be configured before you configure the CAR function for mirrored traffic.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number* if the mirrored port is not an EVC Layer 2 sub-interface
   
   
   
   The interface view is displayed.
   
   
   
   To limit the rate of mirrored traffic in a scenario where the mirrored port is an EVC Layer 2 sub-interface or a BD, enter the corresponding view to configure the CAR function. The view varies according to the scenario.
   * If the mirrored port is configured in common mode, run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number**.subnum* **mode** **l2** command to enter the EVC Layer 2 sub-interface view.
   * If the mirrored port is configured in mirroring instance mode, run the [**mirror instance**](cmdqueryname=mirror+instance) *instance-name* **location** command to enter the mirroring instance view.
3. Run [**port-mirroring car cir**](cmdqueryname=port-mirroring+car+cir) *cir-value* [ **pir** *pir-value* ] [ **cbs** *cbs-value* [ **pbs** *pbs-value* ] ]
   
   
   
   The CAR function is configured to limit the rate of mirrored traffic.
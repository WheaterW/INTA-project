Configuring a Clock Recovery Domain
===================================

Configuring a Clock Recovery Domain

#### Context

This section describes how to configure a clock recovery domain for clock recovery.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Configure a clock recovery domain on the slave device that needs clock recovery.
   
   
   * # If the device is installed with an E1 subcard, perform the following operations:
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     This step is supported only on the NE40E-M2E, NE40E-M2F, NE40E-M2H, NE40E-M2K.
     
     1. Run the [**controller e1**](cmdqueryname=controller+e1) *controller-number* command to enter the corresponding E1 interface view.
     2. Run the [**clock**](cmdqueryname=clock) **recovery-domain** *domain-value* command to configure a clock recovery domain for the E1 interface.
     3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
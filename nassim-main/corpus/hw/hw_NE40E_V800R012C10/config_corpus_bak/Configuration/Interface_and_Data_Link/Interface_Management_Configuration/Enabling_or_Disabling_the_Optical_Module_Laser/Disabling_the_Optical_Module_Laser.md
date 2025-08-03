Disabling the Optical Module Laser
==================================

Disabling the optical module laser before troubleshooting a link failure protects maintenance engineers from the laser.

#### Context

Before locating or troubleshooting a link failure, maintenance engineers should ensure that the optical module laser is disabled so that it cannot cause injury. The optical module can be configured to disable the laser automatically if it detects a link failure. The laser can also be disabled manually.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number* or [**controller**](cmdqueryname=controller) *interface-type* *interface-number*
   
   
   
   The corresponding interface view is displayed.
3. Perform either of the following operations:
   
   
   * Configure the optical module to disable the laser automatically.
     
     1. To configure the optical module to disable the laser automatically, run the [**laser autoshutdown enable**](cmdqueryname=laser+autoshutdown+enable) command.
     2. (Optional) To configure intervals at which the optical module laser is disabled or enabled and the system checks for link failures, run the [**laser auto-shutdown-interval**](cmdqueryname=laser+auto-shutdown-interval) { **open** *open-value* | **close** *close-value* } command.
   * Disable the optical module laser manually.
     
     To disable the optical module laser manually, run the [**laser turn-off**](cmdqueryname=laser+turn-off) command.
     
     ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
     
     Running the [**laser turn-off**](cmdqueryname=laser+turn-off) command interrupts services on the interface. Therefore, do not run the command when the interface is working properly.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
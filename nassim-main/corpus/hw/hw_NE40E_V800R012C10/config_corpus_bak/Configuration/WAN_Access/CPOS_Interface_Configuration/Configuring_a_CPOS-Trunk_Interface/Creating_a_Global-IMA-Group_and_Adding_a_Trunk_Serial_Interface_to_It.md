Creating a Global-IMA-Group and Adding a Trunk Serial Interface to It
=====================================================================

To increase transmission bandwidth and improve network reliability, add trunk serial interfaces to a global IMA-group interface.

#### Context

To improve network reliability, a protection channel can be configured to take over traffic from one or more working channels if the working channels fail.

Before deploying and protecting ATM services on CPOS interfaces, add two CPOS interfaces to a CPOS-Trunk interface and channelize the CPOS-Trunk interface into trunk serial interfaces. Then, add the trunk serial interfaces to a global IMA-group interface to carry the ATM services. If one CPOS link fails, the other CPOS link takes over traffic.


#### Procedure

1. Create a global-ima-group interface.
   
   
   1. Run [**system-view**](cmdqueryname=system-view)
      
      The system view is displayed.
   2. Run [**interface global-ima-group**](cmdqueryname=interface+global-ima-group) *global-ima-group-number*
      
      A global-ima-group interface is created.
   3. Run [**commit**](cmdqueryname=commit)
      
      The configuration is committed.
2. Add a trunk serial interface to the global-ima-group interface.
   
   
   1. Run [**system-view**](cmdqueryname=system-view)
      
      The system view is displayed.
   2. Run [**interface trunk-serial**](cmdqueryname=interface+trunk-serial) *trunk-serial-id*
      
      The trunk serial interface view is displayed.
   3. Run [**link-protocol atm**](cmdqueryname=link-protocol+atm)
      
      The link layer protocol is configured as ATM for the trunk serial interface.
   4. Run [**ima global-ima-group**](cmdqueryname=ima+global-ima-group) *global-ima-group-number*
      
      The trunk serial interface is added to the global-ima-group interface.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) After a trunk serial interface is added to a global-ima-group interface, the interface type previously configured for the global-ima-group interface becomes invalid. To reconfigure an interface type for the global-ima-group interface, run the [**atm interface-type**](cmdqueryname=atm+interface-type) { **uni** | **nni** } command in the global-ima-group interface view.
      * If a device connects to a user-side device, configure the global-ima-group interface as a UNI.
      * If a device connects to another network-side device, configure the global-ima-group interface as an NNI.
   5. Run [**commit**](cmdqueryname=commit)
      
      The configuration is committed.
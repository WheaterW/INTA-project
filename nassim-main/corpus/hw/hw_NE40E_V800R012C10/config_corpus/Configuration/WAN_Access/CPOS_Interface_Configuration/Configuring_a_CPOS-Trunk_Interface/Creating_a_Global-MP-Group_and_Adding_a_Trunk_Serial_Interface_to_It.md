Creating a Global-MP-Group and Adding a Trunk Serial Interface to It
====================================================================

To increase transmission bandwidth and improve network reliability, add trunk serial interfaces to a global MP-group interface.

#### Context

To improve network reliability, a protection channel can be configured to take over traffic from one or more working channels if the working channels fail.

Before deploying and protecting PPP services on CPOS interfaces, add two CPOS interfaces to a CPOS-Trunk interface and channelize the CPOS-Trunk interface into trunk serial interfaces. Then, add the trunk serial interfaces to a global MP-group interface to carry the PPP services. If one CPOS link fails, the other CPOS link takes over traffic.


#### Procedure

1. Create a global-mp-group interface.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**interface global-mp-group**](cmdqueryname=interface+global-mp-group) *global-mp-group-number*
      
      
      
      A global MP-group interface is created.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
2. Add a trunk serial interface to the global-mp-group interface.
   
   
   1. Run [**system-view**](cmdqueryname=system-view)
      
      The system view is displayed.
   2. Run [**interface trunk-serial**](cmdqueryname=interface+trunk-serial) *trunk-serial-id*
      
      The trunk serial interface view is displayed.
   3. Run [**link-protocol ppp**](cmdqueryname=link-protocol+ppp)
      
      The link layer protocol is configured as PPP for the trunk serial interface.
   4. Run [**ppp mp-global global-mp-group**](cmdqueryname=ppp+mp-global+global-mp-group) *global-mp-group-number*
      
      The trunk serial interface is added to the global-mp-group interface.
   5. Run [**commit**](cmdqueryname=commit)
      
      The configuration is committed.
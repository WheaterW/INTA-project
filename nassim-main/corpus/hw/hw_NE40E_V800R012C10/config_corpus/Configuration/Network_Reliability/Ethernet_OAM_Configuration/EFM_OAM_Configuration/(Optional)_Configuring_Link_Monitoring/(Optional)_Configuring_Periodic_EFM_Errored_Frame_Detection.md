(Optional) Configuring Periodic EFM Errored Frame Detection
===========================================================

If the number of errored frames that an EFM-enabled interface detects within a configured detection period reaches or exceeds a configured threshold, the interface notifies its peer interface of the errored frame fault.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The view of the interface at one end of a link is displayed.
3. Run [**efm error-frame-period notification enable**](cmdqueryname=efm+error-frame-period+notification+enable)
   
   
   
   The interface is enabled to detect and notify its peer device of errored frames that EFM periodically detects.
4. Run [**efm error-frame-period period**](cmdqueryname=efm+error-frame-period+period) *period*
   
   
   
   The interval at which EFM detects errored frames on the interface is set.
5. Run [**efm error-frame-period threshold**](cmdqueryname=efm+error-frame-period+threshold) *threshold*
   
   
   
   The alarm threshold for errored frames that EFM periodically detects on the interface is set.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
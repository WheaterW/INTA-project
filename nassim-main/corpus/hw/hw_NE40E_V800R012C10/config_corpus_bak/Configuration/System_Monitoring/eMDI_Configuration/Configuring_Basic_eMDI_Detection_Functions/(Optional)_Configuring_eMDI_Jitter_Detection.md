(Optional) Configuring eMDI Jitter Detection
============================================

This section describes how to configure eMDI jitter detection.

#### Context

By default, the eMDI detection solution detects only the packet loss rate and packet out-of-order rate. If the jitter indicator also needs to be detected, eMDI jitter detection needs to be configured.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**emdi**](cmdqueryname=emdi)
   
   
   
   The eMDI view is displayed.
3. Run [**emdi rtp-jitter enable**](cmdqueryname=emdi+rtp-jitter+enable)
   
   
   
   Jitter detection is enabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
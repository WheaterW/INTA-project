(Optional) Changing the BFD Detection Time
==========================================

This section describes how to change the BFD detection time to more efficiently use a BFD session to monitor links on a network.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bfd**](cmdqueryname=bfd) *session-name*
   
   
   
   The BFD session view is displayed.
3. Run [**min-echo-rx-interval**](cmdqueryname=min-echo-rx-interval) *interval*
   
   
   
   A minimum interval at which unaffiliated BFD echo session packets are received is configured.
4. Run [**detect-multiplier**](cmdqueryname=detect-multiplier) *multiplier*
   
   
   
   A local detection multiplier is configured.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
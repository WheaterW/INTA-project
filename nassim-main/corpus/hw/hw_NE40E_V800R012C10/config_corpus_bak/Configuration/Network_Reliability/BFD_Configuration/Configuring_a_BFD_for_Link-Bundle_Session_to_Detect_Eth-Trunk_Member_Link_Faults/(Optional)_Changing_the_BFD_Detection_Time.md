(Optional) Changing the BFD Detection Time
==========================================

This section describes how to change the BFD detection time so that the BFD session monitors links on a network more efficiently.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bfd**](cmdqueryname=bfd) *session-name*
   
   
   
   The BFD session view is displayed.
3. Run [**min-tx-interval**](cmdqueryname=min-tx-interval) *tx-interval*
   
   
   
   The minimum interval at which BFD control packets are sent is set.
4. Run [**min-rx-interval**](cmdqueryname=min-rx-interval) *rx-interval*
   
   
   
   The minimum interval at which BFD control packets are received is set.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If a BFD session goes down, a device automatically changes the intervals at which BFD control packets are sent and received to random values greater than 1000 milliseconds. After the BFD session goes up, the device restores the configured interval.
5. Run [**detect-multiplier**](cmdqueryname=detect-multiplier) *multiplier*
   
   
   
   The local detection multiplier that takes effect after the BFD session goes up is configured.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In a BFD for route scenario, if a route's outbound interface is an inter-board trunk interface, the board on which the trunk interface's any member interface resides fails, and the BFD detection time is less than 200 ms, the BFD session goes down because the inter-board trunk switching time is 200 ms. Therefore, you are advised to set the BFD detection time to a value greater than 3 x 100 ms.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
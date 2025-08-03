Disabling BFD Session Status Persistence
========================================

Disabling BFD Session Status Persistence

#### Context

If the peer BFD session is in the AdminDown or deleted state and the local BFD session is down before the device restarts, no service switching is triggered. After the local device restarts, the previous local BFD session status information is lost. Therefore, the local BFD session cannot go up through negotiation. After the negotiation times out, service switching is triggered. As a result, the service association behavior is inconsistent before and after the device restarts.

If the peer BFD session is in admindown status or deleted before the device restarts, the local device saves the session status before the restart. After the device is restarted, the BFD session status remains unchanged and no service switchover is triggered. This ensures that the associated services behave the same before and after the device is restarted. If the BFD session status before and after the restart does not need to be the same, disable the BFD session status persistence function.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bfd**](cmdqueryname=bfd)
   
   
   
   BFD is enabled globally and the BFD view is displayed.
3. Run [**bfd-state-record disable**](cmdqueryname=bfd-state-record+disable)
   
   
   
   The BFD session status persistence function is disabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
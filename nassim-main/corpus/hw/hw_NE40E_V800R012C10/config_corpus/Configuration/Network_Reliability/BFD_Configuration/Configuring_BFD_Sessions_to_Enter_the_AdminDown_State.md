Configuring BFD Sessions to Enter the AdminDown State
=====================================================

This section describes how to configure BFD sessions to enter the AdminDown state. After entering the AdminDown state, BFD sessions are not deleted but they do not monitor links.

#### Usage Scenario

To modify BFD session configurations or stop BFD sessions from monitoring links without affecting upper-layer applications, configure BFD sessions to enter the AdminDown state to suspend the BFD sessions. After the modification is complete or if BFD needs to be restarted, you can restart the BFD sessions.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bfd**](cmdqueryname=bfd) *session-name*
   
   
   
   The BFD session view is displayed.
3. Run [**shutdown**](cmdqueryname=shutdown)
   
   
   
   The BFD session is shut down and enters the AdminDown state.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
5. (Optional) Run [**bfd**](cmdqueryname=bfd)
   
   
   
   The BFD view is displayed.
6. (Optional) Run [**batch-shutdown**](cmdqueryname=batch-shutdown) { **all** | **lsp** | **pw** | **tunnel** | **ip** }
   
   
   
   BFD sessions are shut down in batches and enter the AdminDown state.
   
   When a large number of BFD sessions flap, frequent link switchovers are performed. As a result, service forwarding is affected. If the [**undo bfd**](cmdqueryname=undo+bfd) command is run to disable BFD for service restoration, a large number of BFD configurations are lost, making subsequent fault locating difficult. To resolve this issue, shut down BFD sessions in batches.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
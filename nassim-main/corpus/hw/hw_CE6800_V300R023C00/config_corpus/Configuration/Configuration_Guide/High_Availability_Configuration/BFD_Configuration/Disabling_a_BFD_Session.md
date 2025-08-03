Disabling a BFD Session
=======================

Disabling a BFD Session

#### Context

A BFD session has four states: Down, Init, Up, and AdminDown. For details, see [BFD Session Management](vrp_bfd_cfg_0003.html#EN-US_CONCEPT_0000001130622344__section_dc_vrp_bfd_feature_000604). To modify BFD session configurations or stop BFD sessions from monitoring links without affecting upper-layer applications, configure BFD sessions to enter the AdminDown state to suspend the BFD sessions. After the modification is complete or if BFD needs to be restarted, you can restart the BFD sessions.


#### Procedure

* Disable a BFD session.
  1. Enter the system view.
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the BFD session view.
     ```
     [bfd](cmdqueryname=bfd) session-name
     ```
  3. Shut down the BFD session so that it enters the AdminDown state.
     ```
     [shutdown](cmdqueryname=shutdown)
     ```
     
     By default, a BFD session is enabled.
  4. Commit the configuration.
     ```
     [commit](cmdqueryname=commit)
     ```
* Disable BFD sessions in batches.
  1. Enter the system view.
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the BFD view.
     ```
     [bfd](cmdqueryname=bfd)
     ```
  3. Shut down BFD sessions in batches so that they enter the AdminDown state.
     ```
     [batch-shutdown](cmdqueryname=batch-shutdown) { all | ip }
     ```
     
     If a large number of BFD sessions flap, frequent link switchovers are triggered. As a result, service forwarding is affected. If you run the [**undo bfd**](cmdqueryname=undo+bfd) command to disable BFD for service restoration, a large number of BFD configurations are lost, making subsequent fault locating difficult. To resolve this problem, shut down BFD sessions in batches.
  4. Commit the configuration.
     ```
     [commit](cmdqueryname=commit)
     ```
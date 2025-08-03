(Optional) Enabling the Function to Trigger Trap Messages Only for Public Network LDP Sessions
==============================================================================================

In an LDP multi-instance scenario, a device can be enabled to trigger trap messages only for public network LDP sessions, which prevents a failure to distinguish trap messages for both the private and public network sessions with the same ID.

#### Context

In an LDP multi-instance scenario, multiple LDP instances may contain sessions of the same ID. Since trap messages do not contain VPN instance information, these trap messages carrying the same session ID cannot be differentiated based on VPN instances. To distinguish trap messages for public and private network sessions with the same ID, run the [**session-state-trap public-only**](cmdqueryname=session-state-trap+public-only) command to enable a device to generate trap messages only for public network LDP sessions.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
   
   
   
   The MPLS-LDP view is displayed.
3. Run [**session-state-trap public-only**](cmdqueryname=session-state-trap+public-only)
   
   
   
   The device is enabled to generate trap messages only for public network LDP sessions.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
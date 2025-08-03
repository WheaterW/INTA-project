Configuring LDP Session Protection
==================================

LDP session protection enables a device to start the extended LDP discovery mechanism to continue to maintain an LDP session established with an LDP peer if the basic LDP discovery mechanism fails. After the basic LDP discovery mechanism recovers, the LDP protocol can rapidly converge.

#### Usage Scenario

If the direct link of a local LDP session between two devices fails, an LDP adjacency for the LDP session is torn down. The LDP session and related labels are also deleted. After the direct link recovers, the LDP session can be reestablished and distribute labels so that an LDP LSP over the session can converge. During this process, LDP LSP traffic is dropped.

With LDP session protection configured, LDP establishes a remote adjacency when establishing local adjacencies and uses both adjacencies to maintain LDP sessions. If the direct link of an LDP session is faulty and other paths and routes are available, the remote adjacency can be used to maintain the LDP session without interruption. After the direct link recovers, the local outgoing label can still be used, without being distributed by the downstream node again. The LDP session does not need to be reestablished. This speeds up LDP LSP convergence and reduces traffic loss.


#### Pre-configuration Tasks

Before configuring LDP session protection, complete the following task:

* [Configure a local LDP session](dc_vrp_ldp-p2p_cfg_0003.html).

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
   
   
   
   The MPLS-LDP view is displayed.
3. Run [**session protection**](cmdqueryname=session+protection+peer-group+duration+infinite) [ **peer-group** *peer-group-name* ] [ **duration** { **infinite** | *time-value* } ]
   
   
   
   LDP session protection is enabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After completing the configurations, run the [**display mpls ldp remote-peer**](cmdqueryname=display+mpls+ldp+remote-peer) command in any view to view the LDP session protection configuration and the function status. The command output shows that this function takes effect.
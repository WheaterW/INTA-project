Disabling LDP Session Flapping Suppression
==========================================

Disabling_LDP_Session_Flapping_Suppression

#### Context

If an LDP session goes down due to a protocol or interface fault, LDP immediately attempts to reestablish the LDP session to ensure the fastest LDP hard convergence. For an LDP session that alternates between up and down multiple times within a period of time, the involved upstream and downstream LSPs are frequently created and deleted, wasting resources. To prevent this problem, LDP session flapping suppression is enabled by default. For a stable LDP network, you can disable LDP session flapping suppression.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**mpls**](cmdqueryname=mpls) command to enable MPLS globally and enter the MPLS view.
3. Run the [**mpls ldp**](cmdqueryname=mpls+ldp) command to enable LDP globally and enter the MPLS-LDP view.
4. Run the [**session suppress disable**](cmdqueryname=session+suppress+disable) command to disable LDP session flapping suppression.
5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
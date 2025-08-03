(Optional) Configuring Timers for a Local LDP Session
=====================================================

Timers of a local LDP session include the link Hello hold timer, link Hello send timer, Keepalive hold timer, Keepalive send timer, and Exponential backoff timer.

#### Context

The following timers are used in a local LDP session:

**Table 1** Timers for a local LDP session
| LDP Timers | Description | Suggestion |
| --- | --- | --- |
| Link Hello send timer | Used to send Hello messages periodically to notify a peer LSR of the local LSR's presence and establish a Hello adjacency. Similar to a remote LDP session, a local LDP session uses a link Hello send timer. | On an unstable network, decrease the value of a link Hello send timer, speeding up network fault detection. |
| Link Hello hold timer | Used to exchange Hello messages periodically between two LDP peers to maintain the Hello adjacency. If no Hello message is received after the link Hello hold timer expires, the Hello adjacency is torn down. Similar to a remote LDP session, a local LDP session uses a link Hello hold timer. | On a network with unstable links or a large number of packets, increase the value of the link Hello hold timer, preventing a local LDP session from being torn down and set up frequently. |
| KeepAlive send timer | Used to send KeepAlive messages periodically, maintaining the local LDP session. | On an unstable network, set a smaller value for a KeepAlive send timer, speeding up network fault detection. |
| KeepAlive hold timer | Used to send LDP PDUs over an LDP session, maintaining the local LDP session. If no LDP PDU is received after the KeepAlive hold timer expires, the TCP connection is closed and the local LDP session is terminated. | On a network with unstable links, increase the value of the KeepAlive hold timer, preventing the local LDP session from flapping. |
| Exponential backoff timer | Started by an LSR that plays an active role after an LDP Initialization message sent by the LSR to another LSR that plays a passive role fails to be processed or parameters carried in the message are rejected. The LSP that plays the active role periodically resends an LDP Initialization message to initiate an LDP session before the Exponential backoff timer expires. | * When a device is upgraded, prolong the period for the active role to retry setting up a session. In this case, you can set larger initial and maximum values for the Exponential backoff timer. * When a device that bears services tends to alternate between Up and Down, shorten the period for the active role to retry setting up a session. In this case, you can set smaller initial and maximum values for the Exponential backoff timer. |


The default timer values are recommended.


#### Procedure

* Configure a link Hello send timer.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the interface on which an LDP session is to be established is displayed.
  3. Run [**mpls ldp timer hello-send**](cmdqueryname=mpls+ldp+timer+hello-send) *interval*
     
     
     
     A link Hello send timer is configured.
     
     Effective link Hello send timer value = Min{Configured link Hello send timer value, 1/3 of the link Hello hold timer value}
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a link Hello hold timer.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the interface on which an LDP session is to be established is displayed.
  3. Run [**mpls ldp timer hello-hold**](cmdqueryname=mpls+ldp+timer+hello-hold) *interval*
     
     
     
     A link Hello hold timer is configured.
     
     If a link Hello hold timer is configured on each end of a local LDP session, the smaller value takes effect.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a Keepalive send timer for a local LDP session.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the interface on which an LDP session is to be established is displayed.
  3. Run [**mpls ldp timer keepalive-send**](cmdqueryname=mpls+ldp+timer+keepalive-send) *interval*
     
     
     
     A Keepalive send timer is configured for the local LDP session.
     
     Effective Keepalive send timer value = Min{Configured Keepalive send timer value, 1/3 of the Keepalive hold timer value}
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a Keepalive hold timer for a local LDP session.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the interface on which an LDP session is to be established is displayed.
  3. Run [**mpls ldp timer keepalive-hold**](cmdqueryname=mpls+ldp+timer+keepalive-hold) *interval*
     
     
     
     A Keepalive hold timer is configured for the local LDP session.
     
     If a Keepalive hold timer is configured on each end of a local LDP session, the smaller value takes effect.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure an Exponential backoff timer.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     The MPLS view is displayed.
  3. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
     
     
     
     The MPLS-LDP view is displayed.
  4. Run [**backoff timer**](cmdqueryname=backoff+timer) *init* *max*
     
     
     
     The Exponential backoff timer is configured.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
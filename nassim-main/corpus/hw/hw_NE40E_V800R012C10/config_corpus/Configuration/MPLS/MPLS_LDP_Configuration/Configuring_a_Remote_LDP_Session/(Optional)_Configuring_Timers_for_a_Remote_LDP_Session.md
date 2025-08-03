(Optional) Configuring Timers for a Remote LDP Session
======================================================

LDP timers include the target Hello hold timer, target Hello send timer, Keepalive hold timer, Keepalive send timer, and Exponential backoff timer.

#### Context

The following timers are used in a remote LDP session:

* Target Hello send timer: An LSR sends Hello messages to a peer LSR at an interval specified by the Hello send timer. The LSR can advertise its existence and establish a Hello adjacency with the peer LSR.
* Target Hello hold timer: LDP peers that establish a Hello adjacency periodically exchange Hello messages indicating that they expect to maintain the adjacency. If the Hello hold timer expires and no Hello messages are received, the Hello adjacency is torn down.
* Keepalive send timer: LSRs on both ends of an established LDP session start Keepalive send timers and periodically exchange Keepalive messages to maintain the LDP session.
* Keepalive hold timer: LDP peers start Keepalive hold timers and periodically send LDP PDUs over an LDP session connection to maintain the LDP session. If the Keepalive hold timers expire and no LDP PDUs are received, the connection is closed, and the LDP session is torn down.
* Exponential backoff timer: An active LSR starts this timer after it fails to process an LDP Initialization message or after it receives the notification that the passive LSR to which the active LSR sends the LDP Initialization message has rejected the parameters carried in the message. The active LSP periodically resends an LDP Initialization message to initiate an LDP session before the Exponential backoff timer expires.

The default timer values are recommended.


#### Procedure

* Configure a target Hello send timer.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls ldp remote-peer**](cmdqueryname=mpls+ldp+remote-peer) *remote-peer-name*
     
     
     
     The remote MPLS LDP peer view is displayed.
  3. Run [**mpls ldp timer hello-send**](cmdqueryname=mpls+ldp+timer+hello-send) *interval*
     
     
     
     The target Hello send timer value is set.
     
     
     
     Effective target Hello send timer value = Min {Configured target Hello send timer value, 1/3 of the target Hello hold timer value}
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a target Hello hold timer.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls ldp remote-peer**](cmdqueryname=mpls+ldp+remote-peer) *remote-peer-name*
     
     
     
     The remote MPLS LDP peer view is displayed.
  3. Run [**mpls ldp timer hello-hold**](cmdqueryname=mpls+ldp+timer+hello-hold) *interval*
     
     
     
     The target Hello hold timer value is set.
     
     
     
     The value of the Hello hold timer configured on the local LSR may not be the actual effective value. The actual effective value is the smaller of the two values configured on the two ends of a remote LDP session.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a Keepalive send timer for a remote LDP session.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls ldp remote-peer**](cmdqueryname=mpls+ldp+remote-peer) *remote-peer-name*
     
     
     
     The remote MPLS LDP peer view is displayed.
  3. Run [**mpls ldp timer keepalive-send**](cmdqueryname=mpls+ldp+timer+keepalive-send) *interval*
     
     
     
     The Keepalive send timer value is set for a remote LDP session.
     
     
     
     Effective Keepalive send timer value = Min {Configured Keepalive send timer value, 1/3 of the Keepalive hold timer value}
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a Keepalive hold timer for a remote LDP session.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls ldp remote-peer**](cmdqueryname=mpls+ldp+remote-peer) *remote-peer-name*
     
     
     
     The remote MPLS LDP peer view is displayed.
  3. Run [**mpls ldp timer keepalive-hold**](cmdqueryname=mpls+ldp+timer+keepalive-hold) *interval*
     
     
     
     The Keepalive hold timer value is set for the remote LDP session.
     
     
     
     The value of the Keepalive hold timer configured on the local LSR may not be the actual effective value. The actual effective value is the smaller of the two values configured on the two ends of a remote LDP session.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the global Keepalive hold timer of the remote LDP session.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
     
     
     
     The MPLS-LDP view is displayed.
  3. Run [**timer auto-remote keepalive-hold**](cmdqueryname=timer+auto-remote+keepalive-hold) *interval*
     
     
     
     The global Keepalive hold timer value is set for the remote LDP session.
     
     
     
     The value of the Keepalive hold timer configured on the local LSR may not be the actual effective value. The actual effective value is the smaller of the two values configured on the two ends of a remote LDP session.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The value of the timer that takes effect is the smaller of the values of the two Keepalive hold timers configured on both ends of a remote LDP session. The Keepalive hold timer configured in the remote MPLS-LDP peer view takes precedence over the global Keepalive hold timer. If the Keepalive hold timer is configured both globally and in the remote MPLS-LDP peer view, the Keepalive hold timer configured in the remote MPLS-LDP peer view takes effect.
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
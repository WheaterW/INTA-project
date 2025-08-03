(Optional) Configuring Timers for an ERPS Ring
==============================================

To prevent the blocked port from alternating between Up and Down in case a faulty device or link on an ERPS ring recovers, enable timers for the ERPS ring to reduce the traffic interruption time.

#### Context

ERPS defines the following timers:

* Guard timer
  
  After a faulty link or node recovers or a clear operation is executed, the nodes on the two ends of the link or the recovered node sends R-APS No Request (NR) messages to inform the other nodes of the link or node recovery and starts a guard timer. Before the timer expires, each involved node does not process any R-APS PDUs to avoid receiving out-of-date R-APS (SF) messages. After the timer expires, if the involved node still receives an R-APS (SF) message, the local port enters the Forwarding state.
* WTR Timer
  
  If the RPL owner port is unblocked due to a link or node failure, the involved port may not go Up immediately after the link or node recovers. To prevent the RPL owner port from alternating between Up and Down, the node where the RPL owner port resides starts a WTR timer after receiving an R-APS (NR) message. If the node receives an R-APS Signal Fail (SF) message before the timer expires, it terminates the WTR timer (R-APS SF message: a message sent by a node to other nodes after the node in an ERPS ring detects that one of its ring ports becomes Down). If the node does not receive any R-APS (SF) message before the timer expires, it blocks the RPL owner port when the timer expires and sends an R-APS (NR, RB) message. After receiving this R-APS (NR, RB) message, the nodes set their recovered ports on the ring to the Forwarding state.
* Hold-off timer
  
  Protection switching sequence requirements vary for Layer 2 networks running ERPS. For example, in a multi-layer service application, a certain period of time is required for a server to recover should it fail. (During this period, no protection switching is performed, and the client does not detect the failure.) A hold-off timer can be set to ensure that the server is given adequate time to recover. If a fault occurs, the fault is not immediately reported to ERPS. Instead, the hold-off timer starts. If the fault persists after the timer expires, the fault will be reported to ERPS.
* WTB timer
  
  The WTB timer starts after an FS or MS operation is performed. When multiple nodes on an ERPS ring are in the FS or MS state, the clear operation takes effect only after the WTB timer expires. This ensures that the RPL owner port will not be blocked immediately.
  
  The WTB timer value cannot be configured. Its value is the guard timer value plus 5.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**erps ring**](cmdqueryname=erps+ring) *ring-id*
   
   
   
   The ERPS ring view is displayed.
3. Run the following commands to configure one or more timers for the ERPS ring:
   
   
   * To configure the WTR timer for an ERPS ring, run the [**wtr-timer**](cmdqueryname=wtr-timer) *time-value* command.
   * To configure the guard timer for an ERPS ring, run the [**guard-timer**](cmdqueryname=guard-timer) *time-value* command.
   * To configure the hold-off timer for an ERPS ring, run the [**holdoff-timer**](cmdqueryname=holdoff-timer) *time-value* command.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
(Optional) Setting Timers for mLDP P2MP FRR Link Protection
===========================================================

Timers can be set for mLDP P2MP FRR link protection, which helps properly perform a traffic switchover.

#### Context

The following timers can be set for mLDP P2MP FRR link protection:

* Delay timer for deleting mLDP P2MP LSP labels: This timer delays in deleting labels for a faulty mLDP P2MP LSP, preventing local link flapping from spreading globally.
* Timer for a downstream node to wait for an MBB Notification message sent by an upstream node: Within this timer period, a downstream node confirms that a branch LSP is successfully established only after receiving an MBB Notification message replied by an upstream node during MBB LSP establishment. This timer sets the period of time for the downstream node to wait for an MBB Notification message.
* Timer for delaying an MBB LSP switchover: After an MBB LSP is established, LSP switching is delayed to ensure the proper traffic switching on the forwarding and control planes.

Default timer values are recommended.


#### Procedure

* Configure a delay timer for deleting mLDP P2MP LSP labels.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
     
     
     
     The MPLS-LDP view is displayed.
  3. Run [**mldp p2mp**](cmdqueryname=mldp+p2mp)
     
     
     
     mLDP P2MP is enabled globally.
  4. Run [**mldp label-withdraw-delay**](cmdqueryname=mldp+label-withdraw-delay) *delay-time-value*
     
     
     
     A delay timer is set for deleting mLDP P2MP LSP labels.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a timer for a downstream node to wait for an MBB Notification message sent by an upstream node.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
     
     
     
     The MPLS-LDP view is displayed.
  3. Run [**mldp p2mp**](cmdqueryname=mldp+p2mp)
     
     
     
     mLDP P2MP is enabled globally.
  4. Run [**mldp make-before-break**](cmdqueryname=mldp+make-before-break)
     
     
     
     The MBB capability is configured.
  5. Run [**mldp make-before-break timer wait-ack**](cmdqueryname=mldp+make-before-break+timer+wait-ack) *wait-ack-time-value*
     
     
     
     A timer is set for a downstream node to wait for an MBB Notification message sent by an upstream node.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a timer for delaying an MBB LSP switchover.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
     
     
     
     The MPLS-LDP view is displayed.
  3. Run [**mldp p2mp**](cmdqueryname=mldp+p2mp)
     
     
     
     mLDP P2MP is enabled globally.
  4. Run [**mldp make-before-break**](cmdqueryname=mldp+make-before-break)
     
     
     
     The MBB capability is configured.
  5. Run [**mldp make-before-break timer switch-delay**](cmdqueryname=mldp+make-before-break+timer+switch-delay) *switch-delay-time-value*
     
     
     
     A timer for delaying an MBB LSP switchover is configured.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
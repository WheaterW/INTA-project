Setting BFD Parameters on the Ingress
=====================================

This section describes how to set BFD parameters on the ingress to monitor CR-LSPs using BFD sessions.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bfd**](cmdqueryname=bfd) *sessname-value* **bind** **mpls-te** **interface** *tunnel-type* *tunnel-num* **te-lsp** [ **backup** ] [ **one-arm-echo** ]
   
   
   
   BFD is configured to monitor the primary or backup LSP that is bound to a TE tunnel.
   
   
   
   If the **backup** parameter is specified, the BFD session is bound to the backup CR-LSP.
3. Run [**discriminator**](cmdqueryname=discriminator) **local** *discr-value*
   
   
   
   The local discriminator of the BFD session is set.
4. Run [**discriminator**](cmdqueryname=discriminator) **remote** *discr-value*
   
   
   
   A remote discriminator is configured for the BFD session.
   
   
   
   A remote discriminator does not need to be configured for an unaffiliated session.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The local discriminator of the local device and the remote discriminator of the remote device are the same. The remote discriminator of the local device and the local discriminator of the remote device are the same. A discriminator inconsistency causes the BFD session to fail to be established.
5. (Optional) Run [**min-tx-interval**](cmdqueryname=min-tx-interval) *tx-interval*
   
   
   
   The minimum interval at which the local device sends BFD packets is changed.
   
   
   
   This command cannot be run for an unaffiliated session.
   
   Effective local interval at which BFD packets are sent = max{Configured local interval at which BFD packets are sent, Configured local interval at which BFD packets are received}
   
   Effective local interval at which BFD packets are received = max{Configured remote interval at which BFD packets are sent, Configured local interval at which BFD packets are received}
   
   Effective local detection period = Effective local interval at which BFD packets are received x Configured remote BFD detection multiplier
   
   For example, if:
   
   * The local interval at which BFD packets are sent is set to 200 ms, the local interval at which BFD packets are received is set to 300 ms, and the local detection multiplier is set to 4.
   * The remote interval at which BFD packets are sent is set to 100 ms, the remote interval at which BFD packets are received is set to 600 ms, and the remote detection multiplier is set to 5.
   
   Then:
   
   * On the local device, the actual interval for sending BFD packets is 600 ms, which is calculated using the formula max{200 ms, 600 ms}; the interval for receiving BFD packets is 300 ms, which is calculated using the formula max {100 ms, 300 ms}; the detection period is 1500 ms (300 ms Ã 5).
   * On the remote device, the actual interval for sending BFD packets is 300 ms, which calculated using the formula max{100 ms, 300 ms}; the interval for receiving BFD packets is 600 ms, which is calculated using the formula max{200 ms, 600 ms}; the detection period is 2400 ms (600 ms Ã 4).
6. (Optional) Run [**min-rx-interval**](cmdqueryname=min-rx-interval) *rx-interval*
   
   
   
   The minimum interval at which the local device receives BFD packets is changed.
   
   
   
   For an unaffiliated session, run the [**min-echo-rx-interval**](cmdqueryname=min-echo-rx-interval) *interval* command to configure the minimum interval at which the local device receives BFD packets.
7. (Optional) Run [**detect-multiplier**](cmdqueryname=detect-multiplier) *multiplier*
   
   
   
   The local BFD detection multiplier is set.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
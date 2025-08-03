Setting BFD Parameters on the Egress
====================================

This section describes how to set BFD parameters on the egress to monitor CR-LSPs using BFD sessions.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. The IP link, LSP, or TE tunnel can be used as the reverse tunnel to inform the ingress of a fault. If there is a reverse LSP or a TE tunnel, use the reverse LSP or the TE tunnel. If no LSP or TE tunnel is established, use an IP link as a reverse tunnel. If the configured reverse tunnel requires BFD detection, you can configure a pair of BFD sessions for it. Run the following commands as required:
   
   
   * Configure a BFD session to monitor reverse channels.
     
     + For an IP link, run [**bfd**](cmdqueryname=bfd) *session-name* **bind** **peer-ip** *ip-address* [ **vpn-instance** *vpn-name* ] [ **source-ip** *ip-address* ]
     + For an LDP LSP, run [**bfd**](cmdqueryname=bfd) *session-name* **bind** **ldp-lsp** **peer-ip** *ip-address* **nexthop** *ip-address* [ **interface** *interface-type* *interface-number* ]
     + For a CR-LSP, run [**bfd**](cmdqueryname=bfd) *session-name* **bind** **mpls-te** **interface** **tunnel** *interface-number* **te-lsp** [ **backup** ]
     + For a TE tunnel, run [**bfd**](cmdqueryname=bfd) *session-name* **bind** **mpls-te** **interface** **tunnel** *interface-number*
3. Run [**discriminator**](cmdqueryname=discriminator) **local** *discr-value*
   
   
   
   The local discriminator of the BFD session is set.
4. Run [**discriminator**](cmdqueryname=discriminator) **remote** *discr-value*
   
   
   
   The remote discriminator of the BFD session is set.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The local discriminator of the local device and the remote discriminator of the remote device are the same. The remote discriminator of the local device and the local discriminator of the remote device are the same. A discriminator inconsistency causes the BFD session to fail to be established.
5. (Optional) Run [**min-tx-interval**](cmdqueryname=min-tx-interval) *tx-interval*
   
   
   
   The local minimum interval at which BFD packets are sent is configured.
   
   
   
   If an IP link is used as a reverse tunnel, this parameter is inapplicable.
   
   * Effective local interval at which BFD packets are sent = MAX { Configured local interval at which BFD packets are sent, Configured remote interval at which BFD packets are received }
   * Effective local interval at which BFD packets are received = MAX { Configured remote interval at which BFD packets are sent, Configured local interval at which BFD packets are received }
   * Effective local detection interval = Effective local interval at which BFD packets are received x Configured remote detection multiplier
   
   For example:
   
   * The local interval at which BFD packets are sent is set to 200 ms, the local interval at which BFD packets are received is set to 300 ms, and the local detection multiplier is set to 4.
   * The remote interval at which BFD packets are sent is set to 100 ms, the remote interval at which BFD packets are received is set to 600 ms, and the remote detection multiplier is set to 5.
   
   Then,
   
   * Effective local interval at which BFD packets are sent = MAX { 200 ms, 600 ms } = 600 ms; effective local interval at which BFD packets are received = MAX { 100 ms, 300 ms } = 300 ms; effective local detection period = 300 ms x 5 = 1500 ms
   * Effective remote interval at which BFD packets are sent = MAX { 100 ms, 300 ms } = 300 ms; effective remote receiving interval = MAX { 200 ms, 600 ms } = 600 ms; effective remote detection period = 600 ms x 4 = 2400 ms
6. (Optional) Run [**min-rx-interval**](cmdqueryname=min-rx-interval) *rx-interval*
   
   
   
   The local minimum interval at which BFD packets are received is set.
7. (Optional) Run [**detect-multiplier**](cmdqueryname=detect-multiplier) *multiplier*
   
   
   
   The BFD detection multiplier is set.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
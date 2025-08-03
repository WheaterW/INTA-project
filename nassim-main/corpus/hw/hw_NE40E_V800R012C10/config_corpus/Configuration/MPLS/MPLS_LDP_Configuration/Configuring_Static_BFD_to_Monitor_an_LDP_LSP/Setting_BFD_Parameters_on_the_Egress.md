Setting BFD Parameters on the Egress
====================================

BFD parameters must be configured on the egress before a BFD session is established to monitor an LDP LSP.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. The IP link, LSP, or TE tunnel can be used as the reverse tunnel to inform the ingress of a fault. If there is an LSP or a TE tunnel, use an LSP or the TE tunnel. If no LSP or TE tunnel is available, use an IP link. If the configured reverse tunnel requires BFD, configure a pair of BFD sessions for it. Perform one of the following configurations as required:
   
   
   * For an IP link, run the [**bfd**](cmdqueryname=bfd) *session-name* [**bind**](cmdqueryname=bind+peer-ip+vpn-instance+source-ip) **peer-ip** *ip-address* [ **vpn-instance** *vpn-name* ] [ **source-ip** *ip-address* ] command.
   * For an LDP LSP, run the [**bfd**](cmdqueryname=bfd+bind+ldp-lsp+peer-ip+nexthop+interface) *session-name* **bind** **ldp-lsp** **peer-ip** *ip-address* **nexthop** *ip-address* [ **interface** *interface-type* *interface-number* ] command.
   * For an MPLS TE tunnel, run the [**bfd**](cmdqueryname=bfd+bind+mpls-te+interface+tunnel+te-lsp) *session-name* **bind** **mpls-te** **interface** **tunnel** *interface-number* [ **te-lsp** ] command.
   
   The **peer-ip** *ip-address* value is the LSR ID of the remote device.
3. Run [**discriminator**](cmdqueryname=discriminator+local) **local** *discr-value*
   
   
   
   A local discriminator is configured for the BFD session.
4. Run [**discriminator**](cmdqueryname=discriminator+remote) **remote** *discr-value*
   
   
   
   A remote discriminator is configured for the BFD session.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The local discriminator of the local device and the remote discriminator of the remote device are the same. The remote discriminator of the local device and the local discriminator of the remote device are the same. A discriminator inconsistency causes the BFD session to fail to be established.
5. (Optional) Run [**min-tx-interval**](cmdqueryname=min-tx-interval) *tx-interval*
   
   
   
   The minimum interval at which the local device sends BFD packets is changed.
   
   
   
   If the reverse link is an IP link, this command cannot be run.
   
   Effective local interval at which BFD packets are sent = MAX { Locally configured interval at which BFD packets are sent, Remotely configured interval at which BFD packets are received}
   
   Effective local interval at which BFD packets are received = MAX { Remotely configured interval at which BFD packets are sent, Locally configured interval at which BFD packets are received }
   
   Local BFD detection period = Actual local interval at which BFD packets are received x Remotely configured BFD detection multiplier
   
   For example, if: On the local device, the intervals at which BFD packets are sent and received are 200 ms and 300 ms, respectively, and the detection multiplier is 4; on the remote device, the intervals at which BFD packets are sent and received are 100 ms and 600 ms, respectively, and the detection multiplier is 5. Then:
   
   * On the local device, the actual interval for sending BFD packets is 600 ms calculated using the formula MAX { 200 ms, 600 ms }, the interval for receiving BFD packets is 300 ms calculated using the formula MAX { 100 ms, 300 ms }, and the detection period is 1500 ms (300 ms Ã 5).
   * On the remote device, the actual interval for sending BFD packets is 300 ms calculated using the formula MAX { 100 ms, 300 ms }, the interval for receiving BFD packets is 600 ms calculated using the formula MAX { 200 ms, 600 ms }, and the detection period is 2400 ms (600 ms Ã 4).![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   When POS-Trunk interfaces work in 1:1 mode, the local actual receiving interval must be greater than or equal to three times of the POS-Trunk interface switching time. Otherwise, the BFD session may go Down during the POS-Trunk interface switching.
6. (Optional) Run [**min-rx-interval**](cmdqueryname=min-rx-interval) *rx-interval*
   
   
   
   The minimum interval at which the local device receives BFD packets is changed.
   
   
   
   If the reverse link is an IP link, this command cannot be run.
7. (Optional) Run [**detect-multiplier**](cmdqueryname=detect-multiplier) *multiplier*
   
   
   
   A local BFD detection multiplier is set.
8. (Optional) Run [**process-pst**](cmdqueryname=process-pst)
   
   
   
   The BFD session is allowed to modify the port or link state table upon detection of a fault.
   
   
   
   If an LSP is used as a reverse tunnel to notify the ingress of a fault, you can run this command to allow the reverse tunnel to switch traffic if the BFD session goes Down. If a single-hop IP link is used as a reverse tunnel, this command can be configured because the [**process-pst**](cmdqueryname=process-pst) command can only be configured for BFD single-link detection.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
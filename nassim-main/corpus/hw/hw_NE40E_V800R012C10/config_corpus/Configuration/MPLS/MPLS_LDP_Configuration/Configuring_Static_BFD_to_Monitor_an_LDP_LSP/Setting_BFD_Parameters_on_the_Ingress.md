Setting BFD Parameters on the Ingress
=====================================

BFD parameters must be configured on the ingress before a BFD session is established to monitor an LDP LSP.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bfd**](cmdqueryname=bfd+bind+ldp-lsp+peer-ip+nexthop+interface) *session-name* **bind** **ldp-lsp** **peer-ip** *ip-address* **nexthop** *ip-address* [ **interface** *interface-type* *interface-number* ]
   
   
   
   A BFD session is bound to a dynamic LSP.
3. Run [**discriminator**](cmdqueryname=discriminator+local) **local** *discr-value*
   
   
   
   A local discriminator is configured for the BFD session.
4. Run [**discriminator**](cmdqueryname=discriminator+remote) **remote** *discr-value*
   
   
   
   A remote discriminator is configured for the BFD session.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The local discriminator of the local device and the remote discriminator of the remote device are the same. The remote discriminator of the local device and the local discriminator of the remote device are the same. A discriminator inconsistency causes the BFD session to fail to be established.
5. Run [**process-pst**](cmdqueryname=process-pst)
   
   
   
   The BFD session is allowed to modify the port or link state table upon detection of a fault.
   
   
   
   If the BFD session bound to a trunk or VLANIF member interface is enabled to modify the port state table and the corresponding main interface is configured with a BFD session, you must configure a wait to restore (WTR) time for the BFD session bound to the main interface. This prevents the BFD session bound to the main interface from flapping when its member interface joins or leaves the interface.
6. (Optional) Run [**min-tx-interval**](cmdqueryname=min-tx-interval) *tx-interval*
   
   
   
   The minimum interval at which the local device sends BFD packets is changed.
   
   
   
   If the reverse link is an IP link, this command cannot be run.
   
   Effective local interval at which BFD packets are sent = MAX { Locally configured interval at which BFD packets are sent, Remotely configured interval at which BFD packets are received }
   
   Effective local interval at which BFD packets are received = MAX { Remotely configured interval at which BFD packets are sent, Locally configured interval at which BFD packets are received }
   
   Local BFD detection period = Actual local interval at which BFD packets are received x Remotely configured BFD detection multiplier
   
   For example, if: On the local device, the intervals at which BFD packets are sent and received are 200 ms and 300 ms, respectively, and the detection multiplier is 4; on the remote device, the intervals at which BFD packets are sent and received are 100 ms and 600 ms, respectively, and the detection multiplier is 5. Then:
   
   * On the local device, the actual interval for sending BFD packets is 600 ms calculated using the formula MAX { 200 ms, 600 ms }, the interval for receiving BFD packets is 300 ms calculated using the formula MAX { 100 ms, 300 ms }, and the detection period is 1500 ms (300 ms Ã 5).
   * On the remote device, the actual interval for sending BFD packets is 300 ms calculated using the formula MAX { 100 ms, 300 ms }, the interval for receiving BFD packets is 600 ms calculated using the formula MAX { 200 ms, 600 ms }, and the detection period is 2400 ms (600 ms Ã 4).![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   When POS-Trunk interfaces work in 1:1 mode, the local actual receiving interval must be greater than or equal to three times of the POS-Trunk interface switching time. Otherwise, the BFD session may go Down during the POS-Trunk interface switching.
7. (Optional) Run [**min-rx-interval**](cmdqueryname=min-rx-interval) *rx-interval*
   
   
   
   The minimum interval at which the local device receives BFD packets is changed.
   
   
   
   If the reverse link is an IP link, this command cannot be run.
8. (Optional) Run [**detect-multiplier**](cmdqueryname=detect-multiplier) *multiplier*
   
   
   
   A local BFD detection multiplier is set.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
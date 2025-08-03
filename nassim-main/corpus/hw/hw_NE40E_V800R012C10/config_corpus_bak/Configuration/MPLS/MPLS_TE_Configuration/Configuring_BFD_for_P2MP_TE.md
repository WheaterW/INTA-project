Configuring BFD for P2MP TE
===========================

BFD for P2MP TE rapidly monitors P2MP TE tunnels, which helps speed up responses to faults and improve network reliability.

#### Usage Scenario

If P2MP TE tunnels are established to transmit NG MVPN and multicast VPLS services, BFD for P2MP TE can be configured to rapidly detect faults in P2MP TE tunnels, which improves network reliability. To configure BFD for P2MP TE, run the [**bfd enable**](cmdqueryname=bfd+enable) command in the P2MP tunnel template view so that BFD sessions for P2MP TE can be automatically established while P2MP TE tunnels are being established.


#### Context

Before configuring BFD for P2MP TE, [configure an automatic P2MP TE tunnel.](dc_vrp_te-p2p_cfg_0133.html)


#### Procedure

1. Configure the ingress.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bfd**](cmdqueryname=bfd)
      
      
      
      BFD is enabled.
   3. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   4. Run [**mpls te p2mp-template**](cmdqueryname=mpls+te+p2mp-template) *template-name*
      
      
      
      A P2MP tunnel template is created, and the MPLS TE P2MP template view is displayed.
   5. Run [**bfd enable**](cmdqueryname=bfd+enable)
      
      
      
      BFD for P2MP TE is enabled.
   6. (Optional) Run [**bfd**](cmdqueryname=bfd) { **min-tx-interval** *tx-interval* | **min-rx-interval** *rx-interval* | **detect-multiplier** *multiplier* } \*
      
      
      
      BFD for P2MP TE parameters are set.
   7. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
2. Configure each leaf node.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bfd**](cmdqueryname=bfd)
      
      
      
      BFD is enabled, and the BFD view is displayed.
   3. Run [**mpls-passive**](cmdqueryname=mpls-passive)
      
      
      
      The egress is enabled to create a BFD session passively.
      
      
      
      The egress has to receive an LSP ping request carrying a BFD TLV before creating a BFD session.
   4. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.

#### Verifying the Configuration

* Run the [**display bfd multicast session**](cmdqueryname=display+bfd+multicast+session) { [**all**](cmdqueryname=all) | **p2mp-te** [ **p2mp-id** *p2mp-id-value* **ingress-lsr-id** *ingress-lsr-id* **tunnel-id** *tunnel-id* ] } command to check BFD for P2MP TE session information.
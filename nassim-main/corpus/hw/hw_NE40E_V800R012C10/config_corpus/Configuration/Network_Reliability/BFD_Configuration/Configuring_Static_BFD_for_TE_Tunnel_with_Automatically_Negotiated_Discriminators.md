Configuring Static BFD for TE Tunnel with Automatically Negotiated Discriminators
=================================================================================

This section describes how to configure a static BFD session with automatically negotiated discriminators to detect TE tunnel faults.

#### Usage Scenario

As shown in the [Figure 1](#EN-US_TASK_0172361671__fig_dc_vrp_te-p2p_cfg_012601), when configuring a BFD session with automatically negotiated discriminators to detect TE tunnels, you can specify a reverse tunnel. In this way, you do not need to manually plan or configure BFD session discriminators, simplifying the configuration.

**Figure 1** Static BFD for TE Tunnel with automatically negotiated discriminators  
![](figure/en-us_image_0000001993245758.png)  


#### Pre-configuration Tasks

Before configuring static BFD for TE Tunnel with automatically negotiated discriminators, configure MPLS TE tunnels.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bfd**](cmdqueryname=bfd)
   
   
   
   BFD is enabled globally on the local node, and the BFD view is displayed.
   
   BFD can be configured only after the [**bfd**](cmdqueryname=bfd) command is run globally.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. Run [**bfd**](cmdqueryname=bfd) *sessname-value* **bind** **mpls-te** **interface** { *tunnel-type* *tunnel-num* } [ **te-lsp** [ **backup** ] ] [ **reverse-te** **lsr-id** *lsr-id* **tunnel-id** *tunnel-id* **auto** ]
   
   
   
   BFD with automatically negotiated discriminators is configured to detect TE tunnel faults.
   
   In the command, the **reverse-te** **lsr-id** *lsr-id* **tunnel-id** *tunnel-id* parameter specifies reverse TE tunnel information.
5. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

Run the [**display bfd session**](cmdqueryname=display+bfd+session) command to check BFD session information on the ingress of a tunnel.
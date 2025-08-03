Loopback Detection for a Specified Static Bidirectional Co-Routed CR-LSP
========================================================================

Loopback detection for a specified static bidirectional co-routed CR-LSP locates faults if a few packets are dropped or bit errors occur on links along the CR-LSP.

#### Context

On a network with a static bidirectional co-routed CR-LSP used to transmit services, if a few packets are dropped or bit errors occur on links, no alarms indicating link or LSP failures are generated, which poses difficulties in locating the faults. To locate the faults, loopback detection can be enabled for the static bidirectional co-routed CR-LSP.


#### Procedure

1. (Optional) In the MPLS view, run [**lsp-loopback autoclear**](cmdqueryname=lsp-loopback+autoclear) **period** *period-value*
   
   
   
   The timeout period is set, after which loopback detection for a static bidirectional co-routed LSP is automatically disabled.
2. In the specified static bidirectional LSP transit view, run [**lsp-loopback start**](cmdqueryname=lsp-loopback+start).
   
   
   
   Loopback detection is enabled for the specified static bidirectional co-routed CR-LSP.
   
   Loopback detection enables a transit node on the CR-LSP to loop traffic back to the ingress. A professional monitoring device connected to the ingress monitors data packets that the ingress sends and receives and checks whether a fault occurs on the link between the ingress and transit node. [Figure 1](#EN-US_TASK_0172368296__fig_dc_vrp_te-p2p_cfg_020502) illustrates the network on which loopback is enabled to monitor a static bidirectional co-routed CR-LSP.**Figure 1** Loopback detection for a static bidirectional co-routed CR-LSP  
   ![](images/fig_dc_vrp_te-p2p_cfg_020502.png)
   
   ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
   
   During loopback detection, a loop occurs, which adversely affects service transmission. After loopback detection is complete, immediately run the [**lsp-loopback stop**](cmdqueryname=lsp-loopback+stop) command to disable loopback detection. If you do not manually disable loopback detection, loopback detection will be automatically disabled after the specified timeout period elapses.
3. Perform one of the following operations to check the loopback status on a transit node:
   
   
   * Run the [**display mpls te bidirectional**](cmdqueryname=display+mpls+te+bidirectional) command.
   * View the MPLS\_LSPM\_1.3.6.1.4.1.2011.5.25.121.2.1.75 hwMplsLspLoopBack alarm that is generated after loopback detection is started.
   * View the MPLS\_LSPM\_1.3.6.1.4.1.2011.5.25.121.2.1.76 hwMplsLspLoopBackClear alarm that is generated after loopback detection is stopped.
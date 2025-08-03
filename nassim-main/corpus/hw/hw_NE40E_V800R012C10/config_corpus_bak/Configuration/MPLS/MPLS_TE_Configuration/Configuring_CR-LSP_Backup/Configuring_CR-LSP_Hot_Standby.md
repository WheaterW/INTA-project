Configuring CR-LSP Hot Standby
==============================

A hot-standby CR-LSP is established immediately after a primary CR-LSP is set up. If the primary CR-LSP fails, traffic is switched to the hot-standby CR-LSP.

#### Context

CR-LSP hot-standby is disabled by default. After CR-LSP hot-standby is configured on the ingress of a primary CR-LSP, the system automatically selects a path for a hot-standby CR-LSP.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *tunnel-number*
   
   
   
   The view of the MPLS TE tunnel interface is displayed.
3. [Establish a primary RSVP-TE tunnel.](dc_vrp_te-p2p_cfg_0003.html)
4. Run [**mpls te backup**](cmdqueryname=mpls+te+backup) **hot-standby** { **mode** { **revertive** [ **wtr** *interval* ] | **non-revertive** } | **wtr** *interval* }
   
   
   
   The mode of establishing a hot-standby CR-LSP is configured.
   
   
   
   Select the following parameters as needed to enable sub-functions:
   * **mode** **revertive** [ **wtr** *interval* ]: enables a device to switch traffic back to the primary CR-LSP.
   * **mode** **non-revertive**: disables a device from switching traffic back to the primary CR-LSP.
   * **wtr** *interval*: sets the time before a traffic switchback is performed.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The bypass and backup tunnels cannot be configured on the same tunnel interface. The [**mpls te bypass-tunnel**](cmdqueryname=mpls+te+bypass-tunnel) and [**mpls te backup**](cmdqueryname=mpls+te+backup) commands cannot be configured on the same tunnel interface. Also, the [**mpls te protected-interface**](cmdqueryname=mpls+te+protected-interface) and [**mpls te backup**](cmdqueryname=mpls+te+backup) commands cannot be configured on the same tunnel interface.
5. (Optional) Run [**mpls te backup**](cmdqueryname=mpls+te+backup) **hot-standby** **overlap-path**
   
   
   
   The device is configured to allow the path of a primary CR-LSP and the path of a hot-standby CR-LSP to overlap.
6. (Optional) Run [**mpls te backup**](cmdqueryname=mpls+te+backup) **hot-standby** **dynamic-bandwidth**
   
   
   
   The dynamic bandwidth adjustment function is enabled for the hot-standby CR-LSP.
   
   This function enables a hot-standby CR-LSP to obtain bandwidth resources only after the hot-standby CR-LSP takes over traffic from a faulty primary CR-LSP. This function helps efficiently use network resources and reduce network costs.
7. (Optional) Configure CR-LSP backup parameters.
   * Run the [**mpls te path explicit-path**](cmdqueryname=mpls+te+path+explicit-path) *path-name* **secondary** command to specify an explicit path for the backup CR-LSP.
     
     This parameter can be used to control the path of the backup CR-LSP.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The [**mpls te path explicit-path**](cmdqueryname=mpls+te+path+explicit-path) *path-name* **secondary** and [**mpls te backup**](cmdqueryname=mpls+te+backup) commands must be configured at the same time for the configuration to take effect.
   * Run the [**mpls te affinity property**](cmdqueryname=mpls+te+affinity+property) *properties* [ **mask** *mask-value* ] **secondary** command to configure an affinity property for the backup CR-LSP.
     
     This parameter can be used to control the path of the backup CR-LSP.
   * Run the [**mpls te hop-limit**](cmdqueryname=mpls+te+hop-limit) *hop-limit-value* **secondary** command to configure a hop limit for the backup CR-LSP.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The [**mpls te hop-limit**](cmdqueryname=mpls+te+hop-limit) *hop-limit-value* **secondary** and [**mpls te backup**](cmdqueryname=mpls+te+backup) commands must be configured at the same time for the configuration to take effect.
8. (Optional) Run [**hotstandby-switch**](cmdqueryname=hotstandby-switch) { **force** | **clear** }
   
   
   
   Forcible traffic switching is configured.
   
   
   
   If the primary CR-LSP goes down, traffic is switched to the hot-standby CR-LSP. If the primary LSP goes up, traffic is switched back to the primary LSP by default. This configuration provides the flexibility to control the traffic switchover behavior.
   
   If **force** is specified, traffic is temporarily switched to the hot-standby CR-LSP. If **clear** is specified, traffic is switched back to the primary CR-LSP.
9. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
10. (Optional) Run [**mpls te multi-protect fast-switch enable**](cmdqueryname=mpls+te+multi-protect+fast-switch+enable)
    
    
    
    Coexistence of FRR switching and MPLS TE HSB is enabled.
    
    
    
    To enable the coexistence of FRR switching and MPLS TE HSB, TE FRR must be deployed on the entire network. HSB must be deployed on the ingress, BFD for TE LSP must be enabled, and the delayed down function must be enabled on the outbound interface of the P. Otherwise, rapid switching cannot be performed in case of the dual points of failure.
11. (Optional) Configure CSPF fast switching.
    
    
    
    In a scenario where BFD is not configured, only protocol convergence can trigger TE hot-standby switching if the primary LSP fails. To improve the switching speed, you can configure CSPF-based fast switching so that hot-standby switching can be performed quickly.
    
    
    
    1. Run the [**mpls**](cmdqueryname=mpls) command to enter the MPLS view.
    2. Run the [**mpls te tedb fast-notice**](cmdqueryname=mpls+te+tedb+fast-notice) command to configure CSPF fast switching.
12. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.
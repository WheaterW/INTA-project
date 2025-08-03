Configuring Ordinary Backup for CR-LSPs
=======================================

An ordinary backup CR-LSP is set up after the primary CR-LSP fails. If the primary CR-LSP fails, traffic is switched to the ordinary backup CR-LSP.

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Ordinary CR-LSP backup cannot be configured together with the best-effort path or hot standby.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *tunnel-number*
   
   
   
   The tunnel interface view of the MPLS TE tunnel is displayed.
3. Run [**mpls te backup**](cmdqueryname=mpls+te+backup) **ordinary**
   
   
   
   An ordinary backup path is configured for the CR-LSP.
4. (Optional) Configure CR-LSP backup parameters.
   * Run the [**mpls te path explicit-path**](cmdqueryname=mpls+te+path+explicit-path) *path-name* **secondary** command to specify an explicit path for the backup CR-LSP.
     
     This parameter can be used to control the path of the backup CR-LSP.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The [**mpls te path explicit-path**](cmdqueryname=mpls+te+path+explicit-path) *path-name* **secondary** and [**mpls te backup**](cmdqueryname=mpls+te+backup) commands must be configured at the same time for the configuration to take effect.
   * Run the [**mpls te affinity property**](cmdqueryname=mpls+te+affinity+property) *properties* [ **mask** *mask-value* ] **secondary** command to configure an affinity property for the backup CR-LSP.
     
     This parameter can be used to control the path of the backup CR-LSP.
   * Run the [**mpls te hop-limit**](cmdqueryname=mpls+te+hop-limit) *hop-limit-value* **secondary** command to configure a hop limit for the backup CR-LSP.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The [**mpls te hop-limit**](cmdqueryname=mpls+te+hop-limit) *hop-limit-value* **secondary** and [**mpls te backup**](cmdqueryname=mpls+te+backup) commands must be configured at the same time for the configuration to take effect.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
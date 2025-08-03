(Optional) Configuring an LDP Split Horizon Policy
==================================================

An LDP split horizon policy can be configured to prevent an LSR from distributing labels to a specified downstream LDP peer.

#### Context

By default, an LSR distributes labels to both upstream and downstream LDP peers, speeding up LDP LSP convergence. If low-performance digital subscriber line access multiplexers (DSLAMs) are deployed as access devices on an MPLS network, you are advised to configure an LDP split horizon policy on an LSR to allow the LSR to distribute labels only to its upstream LDP peers.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
   
   
   
   The MPLS-LDP view is displayed.
3. Run [**outbound peer**](cmdqueryname=outbound+peer+all+split-horizon) { *peer-id* | **all** } **split-horizon**
   
   
   
   An LDP split horizon policy is configured on the LSR, disabling the LSR from distributing labels to a specified or all downstream LDP peers.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
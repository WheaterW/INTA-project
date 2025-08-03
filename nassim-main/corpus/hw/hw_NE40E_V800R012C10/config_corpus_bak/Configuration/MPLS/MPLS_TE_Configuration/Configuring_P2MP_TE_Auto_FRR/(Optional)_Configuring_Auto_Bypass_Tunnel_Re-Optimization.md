(Optional) Configuring Auto Bypass Tunnel Re-Optimization
=========================================================

Auto bypass tunnel re-optimization allows paths to be recalculated at certain intervals for an auto bypass tunnel. If an optimal path is recalculated, a new auto bypass tunnel will be set up over this optimal path. In this manner, network resources are optimized.

#### Context

Network changes often cause the changes in optimal paths. Auto bypass tunnel re-optimization allows the system to re-optimize an auto bypass tunnel if an optimal path to the same destination is found due to some reasons, such as the changes in the cost. In this manner, network resources are optimized.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This configuration task is invalid for LSPs in the FRR-in-use state.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS view is displayed.
3. Run [**mpls te auto-frr reoptimization**](cmdqueryname=mpls+te+auto-frr+reoptimization) [ **frequency** *interval* ]
   
   
   
   Auto bypass tunnel re-optimization is enabled.
4. (Optional) Run [**return**](cmdqueryname=return)
   
   
   
   Return to the user view.
5. (Optional) Run [**mpls te reoptimization**](cmdqueryname=mpls+te+reoptimization) [ **auto-tunnel name** *tunnel-interface* | **tunnel** *tunnel-number* ]
   
   
   
   Manual re-optimization is performed for all tunnels marked with the re-optimization attribute.
   
   
   
   After you configure automatic re-optimization in the MPLS view, you can return to the user view and run the [**mpls te reoptimization**](cmdqueryname=mpls+te+reoptimization) command to immediately re-optimize the tunnels on which automatic re-optimization is enabled. After you perform manual re-optimization, the timer of automatic re-optimization is reset and counts again.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
Configuring Leaf Lists
======================

Configuring a leaf list on an ingress specifies all leaf nodes on a P2MP TE tunnel. A leaf list helps you configure and manage these leaf nodes uniformly. The steps in this section must be performed if P2MP TE tunnels are manually established. The steps in this section are optional if the establishment of P2MP TE tunnels is automatically triggered by a service.

#### Context

For a P2MP TE tunnel, the path that originates from the ingress and is destined for each leaf node can be calculated either by constraint shortest path first (CSPF) or by planning an explicit path for a specific leaf node or each leaf node. After each leaf node is configured on an ingress, the ingress sends signaling packets to each leaf node and then establishes a P2MP TE tunnel. The NE40E uses leaf lists to configure and manage leaf nodes. All leaf nodes and their explicit paths are integrated into a table, which helps you configure and manage the leaf nodes uniformly.

An MPLS network that transmits multicast services selects dynamically leaf nodes on an automatic P2MP TE tunnel and uses constrained shortest path first (CSPF) to calculate a path destined for each leaf node. To control the leaf nodes of an automatic P2MP TE tunnel, configure a leaf list.

Explicit path planning requires you to configure an explicit path for a specific leaf node or each leaf node, and use the explicit path in the leaf list view.

![](../../../../public_sys-resources/note_3.0-en-us.png) The configuration must prevent a remerge or crossover problem:

* Remerge event: occurs when two sub-LSPs have different inbound interfaces but the same outbound interface on a transit node. [Figure 1](#EN-US_TASK_0172368141__fig_dc_vrp_te-p2p_cfg_013501) shows that a remerge event occurs on the outbound interface shared by two sub-LSPs.
* Crossover event: occurs when two sub-LSPs have different inbound and outbound interfaces on a transit node. [Figure 1](#EN-US_TASK_0172368141__fig_dc_vrp_te-p2p_cfg_013501) shows that a crossover event occurs on the transit node shared by the two sub-LSPs.


**Figure 1** Remerge and crossover events  
![](images/fig_dc_vrp_te-p2p_cfg_013501.png)


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. (Optional) Configure an explicit path to each leaf node.
   1. Run [**explicit-path**](cmdqueryname=explicit-path) *path-name*
      
      
      
      An explicit path is created and the explicit path view is displayed.
   2. Run [**next hop**](cmdqueryname=next+hop) *ip-address* [ **include** [ [ **strict** | **loose** ] | [ **incoming** | **outgoing** ] ] \* | **exclude** ]
      
      
      
      A next-hop address is specified for the explicit path.
      
      
      
      You can configure either the include or include parameter:
   3. (Optional) Run [**add hop**](cmdqueryname=add+hop) *ip-address1* [ **include** [ [ **strict** | **loose** ] | [ **incoming** | **outgoing** ] ] \* | **exclude** ] { **after** | **before** } *ip-address2*
      
      
      
      A node is added to the explicit path.
   4. (Optional) Run [**modify hop**](cmdqueryname=modify+hop) *ip-address1* *ip-address2* [ **include** [ [ **strict** | **loose** ] | [ **incoming** | **outgoing** ] ] \* | **exclude** ]
      
      
      
      The address of a node on the explicit path is changed.
   5. (Optional) Run [**delete hop**](cmdqueryname=delete+hop) *ip-address*
      
      
      
      A node is excluded from the explicit path.
   6. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   7. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   
   
   
   For a P2MP TE tunnel, an explicit tunnel can be configured for a specific leaf node or each leaf node.
3. Run [**mpls te leaf-list**](cmdqueryname=mpls+te+leaf-list) *leaf-list-name*
   
   
   
   A leaf list is specified for the P2MP TE tunnel, and the leaf list view is displayed.
4. Run [**destination**](cmdqueryname=destination) *leaf-address*
   
   
   
   A leaf node is created in the leaf list, and the leaf node view is displayed.
   
   
   
   Generally, the *leaf-address* value is the MPLS LSR ID of a leaf node.
5. (Optional) Run [**path**](cmdqueryname=path) **explicit-path** *path-name*
   
   
   
   An explicit path is specified for the leaf node.
   
   
   
   The **explicit-path** *path-name* parameter specifies the name of the explicit path established in Step 2.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Repeat Step 3 and Step 4 on a P2MP TE tunnel to configure all leaf nodes.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
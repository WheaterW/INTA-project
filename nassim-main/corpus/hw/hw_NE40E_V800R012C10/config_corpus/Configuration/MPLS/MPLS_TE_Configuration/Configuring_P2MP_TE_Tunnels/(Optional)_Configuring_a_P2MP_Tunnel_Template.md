(Optional) Configuring a P2MP Tunnel Template
=============================================

Attributes can be set in a P2MP tunnel template that is used to automatically establish P2MP TE tunnels.

#### Context

Attributes of an automatic P2MP TE tunnel can only be defined in a P2MP tunnel template, but cannot be configured on a tunnel interface because the automatic P2MP TE tunnel has no tunnel interface. When NG MVPN or multicast VPLS is deployed on a network, nodes that transmit multicast traffic can reference the template and use attributes defined in the template to automatically establish P2MP TE tunnels.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls te p2mp-template**](cmdqueryname=mpls+te+p2mp-template) *template-name*
   
   
   
   A P2MP tunnel template is created, and the P2MP tunnel template view is displayed.
3. Select one or multiple operations.
   
   
   
   **Table 1** Operations
   | Operation | Description |
   | --- | --- |
   | Run [**leaf-list**](cmdqueryname=leaf-list) *leaf-list-name*  A leaf list is configured. | When multicast services arrive at a node, the node automatically selects leaf nodes and establishes a sub-LSP destined for each leaf node.  This step enables a node that multicast services access to select leaf nodes in a specified leaf list.  NOTE:  Before running the [**leaf-list**](cmdqueryname=leaf-list) command, the task described in [configuring a leaf list](dc_vrp_te-p2p_cfg_0135.html) must be complete. The *leaf-list-name* value in this step must specify an existing leaf list. |
   | Run [**bandwidth**](cmdqueryname=bandwidth) **ct0** *bw-value*  The CT0 bandwidth is set for the automatic P2MP TE tunnel. | Before bandwidth protection is provided for traffic transmitted along an automatic P2MP TE tunnel, run the [**bandwidth**](cmdqueryname=bandwidth) command to set the required bandwidth value for the tunnel. Nodes on the P2MP TE tunnel can then reserve bandwidth for services, which implements bandwidth protection. |
   | Run [**record-route**](cmdqueryname=record-route) [ **label** ]  The route and label record function for an automatic P2MP TE tunnel is enabled. | This step enables nodes along an automatic P2MP TE tunnel to use RSVP messages to record detailed P2MP TE tunnel information, including the IP address of each hop. The **label** parameter in the [**record-route**](cmdqueryname=record-route) command enables RSVP messages to record label values. |
   | Run [**resv-style**](cmdqueryname=resv-style) { **se** | **ff** }  A resource reservation style is specified. | - |
   | Run [**path metric-type**](cmdqueryname=path+metric-type) { **igp** | **te** }  A link metric type used to select links is specified. | - |
   | Run [**affinity property**](cmdqueryname=affinity+property) *properties* [ **mask** *mask-value* ] or [**affinity**](cmdqueryname=affinity) **primary** { **include-all** | **include-any** | **exclude** } *bit-name* &<1-32>  An affinity and its mask are specified. | An affinity is a 32-bit vector value used to describe an MPLS link. An affinity and an administrative group attribute define the nodes through which an MPLS TE tunnel passes. Affinity masks determine the link properties that a device must check. If some bits in the mask are 1, at least one bit in an administrative group is 1, and the corresponding bit in the affinity must be 1. If the bits in the affinity are 0s, the corresponding bits in the administrative group cannot be 1.  You can use an affinity to control the nodes through which an automatic P2MP TE tunnel passes. |
   | Run [**hop-limit**](cmdqueryname=hop-limit) *hop-limit-value*  A hop limit is set for an automatic P2MP TE tunnel. | To set the maximum number of hops for a P2MP LSP on a P2MP TE tunnel, run this command. |
   | Run [**tie-breaking**](cmdqueryname=tie-breaking) { **least-fill** | **most-fill** | **random** }  A rule for selecting a route among multiple routes to the same destination is specified. | - |
   | Run [**priority**](cmdqueryname=priority) *setup-priority* [ *hold-priority* ]  The setup and holding priorities are set. | The setup priority of a tunnel must be no higher than its holding priority. A setup priority value must be greater than or equal to a holding priority value.  If resources are insufficient, setting the setup and holding priority values allows LSPs with lower priorities to release resources for establishing LSPs with higher priorities. |
   | Run [**reoptimization**](cmdqueryname=reoptimization) [ **frequency** *interval* ]  Periodic re-optimization is enabled for an automatic P2MP TE tunnel. | Periodic re-optimization allows a P2MP TE tunnel to be automatically reestablished over a better path. After a better path to the same destination has been calculated for a certain reason, such as a cost change, a TE tunnel will be automatically reestablished, optimizing resources on a network. |
   | Run [**lsp-tp outbound**](cmdqueryname=lsp-tp+outbound)  Traffic policing is enabled for an automatic P2MP TE tunnel. | Physical links over which a P2MP TE tunnel is established transmit traffic of other TE tunnels, traffic of non-CR LSP traffic, or even IP traffic, in addition to TE tunnel traffic. To limit TE traffic within a configured bandwidth range, run the [**lsp-tp outbound**](cmdqueryname=lsp-tp+outbound) command. |
4. (Optional) Run [**cspf disable**](cmdqueryname=cspf+disable)
   
   
   
   CSPF is disabled in the P2MP template.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In an inter-AS scenario, if a loose explicit path is configured in a P2MP template, you need to run this command only when NG MVPN triggers the establishment of a dynamic P2MP tunnel. You are advised not to run this command in other scenarios.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
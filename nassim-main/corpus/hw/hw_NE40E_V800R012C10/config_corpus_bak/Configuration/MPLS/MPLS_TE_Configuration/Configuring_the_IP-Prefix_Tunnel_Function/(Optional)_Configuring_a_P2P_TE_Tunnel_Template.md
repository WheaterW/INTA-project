(Optional) Configuring a P2P TE Tunnel Template
===============================================

A P2P TE tunnel template can be configured, and MPLS TE tunnel attributes can be set in the template.

#### Usage Scenario

Before you create P2P TE tunnels in a batch, create a P2P TE tunnel template and configure parameters, such as bandwidth and a path limit, in the template. The [**mpls te auto-primary-tunnel**](cmdqueryname=mpls+te+auto-primary-tunnel) command can then be run to reference this template. The device automatically uses the parameters configured in the P2P TE tunnel template to create P2P TE tunnels in a batch.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls te p2p-template**](cmdqueryname=mpls+te+p2p-template) *template-name*
   
   
   
   A P2P TE tunnel template is created, and the P2P TE tunnel template view is displayed.
3. Select one or more operations.
   
   
   
   **Table 1** Operations
   | Operation | Description |
   | --- | --- |
   | Run the [**bandwidth**](cmdqueryname=bandwidth) **ct0** *bw-value* command to configure the CT0 bandwidth for MPLS TE tunnels. | Before bandwidth protection is provided for traffic transmitted along a P2P TE tunnel, run the [**bandwidth**](cmdqueryname=bandwidth) command to set the required bandwidth value for the tunnel. Nodes on the P2P TE tunnel can then reserve bandwidth for services, which implements bandwidth protection. |
   | Run the [**record-route**](cmdqueryname=record-route) [ **label** ] command to enable the route and label record for MPLS TE tunnels. | This step enables nodes along a P2P TE tunnel to use RSVP messages to record detailed P2P TE tunnel information, including the IP address of each hop. The **label** parameter in the [**record-route**](cmdqueryname=record-route) command enables RSVP messages to record label values. |
   | Run the [**resv-style**](cmdqueryname=resv-style) { **se** | **ff** } command to specify the resource reservation style for MPLS TE tunnels. | - |
   | Run the [**path metric-type**](cmdqueryname=path+metric-type) { **igp** | **te** } command to specify the link metric type for MPLS TE tunnels. | - |
   | Run the [**affinity property**](cmdqueryname=affinity+property) *properties* [ **mask** *mask-value* ] command to configure an affinity constraint for MPLS TE tunnels. | An affinity is a 32-bit vector value used to describe an MPLS link. An affinity and an administrative group attribute define the nodes through which an MPLS TE tunnel passes. Affinity masks determine the link properties that should be checked by a device. If some bits in the mask are 1, at least one bit in an administrative group is 1, and the corresponding bit in the affinity must be 1. If the bits in the affinity are 0s, the corresponding bits in the administrative group cannot be 1.  You can use an affinity to control the nodes through which a P2P TE tunnel passes. |
   | Run the [**affinity**](cmdqueryname=affinity) **primary** { **include-all** | **include-any** | **exclude** } *bit-name* &<1-32> command to configure an affinity for an MPLS TE tunnel. | Before running this command, run the [**path-constraint affinity-mapping**](cmdqueryname=path-constraint+affinity-mapping) command in the system view to create an affinity name template. In addition, run the [**attribute**](cmdqueryname=attribute) *affinity-name* **bit-sequence** *bit-number* command to configure the mappings between affinity bit values and names in the template view. |
   | Run the [**hop-limit**](cmdqueryname=hop-limit) *hop-limit-value* command to set the maximum number of hops on an MPLS TE tunnel. | Run this command to set the maximum number of hops that each CR-LSP in an MPLS TE tunnel supports. |
   | Run the [**tie-breaking**](cmdqueryname=tie-breaking) { **least-fill** | **most-fill** | **random** } command to configure a rule for selecting a route among multiple routes to the same destination. | - |
   | Run the [**priority**](cmdqueryname=priority) *setup-priority* [ *hold-priority* ] command to set the setup and holding priority values for MPLS TE tunnels. | The setup priority of a tunnel must be no higher than its holding priority. To be specific, a setup priority value must be greater than or equal to a holding priority value.  If resources are insufficient, setting the setup and holding priority values helps a device release LSPs with lower priorities and use the released resources to establish LSPs with higher priorities. |
   | Run the [**reoptimization**](cmdqueryname=reoptimization) [ **frequency** *interval* ] command to enable the periodic re-optimization for MPLS TE tunnels. | Periodic re-optimization allows an MPLS TE tunnel to be automatically reestablished over a path with a lower cost. After a path with a lower cost to the same destination has been calculated for a specific reason, such as a cost change, a TE tunnel will be automatically reestablished, optimizing resources on a network. |
   | Run the [**bfd enable**](cmdqueryname=bfd+enable) command to enable BFD for TE CR-LSP. | To rapidly detect LSP faults and improve network reliability, configuring BFD for TE CR-LSP is recommended. |
   | Run the [**bfd**](cmdqueryname=bfd) { **min-tx-interval** *tx-interval* | **min-rx-interval** *rx-interval* | **detect-multiplier** *multiplier* } \* command to configure BFD for TE CR-LSP parameters. | BFD parameters can be set to control BFD detection sensitivity. |
   | Run the [**fast-reroute**](cmdqueryname=fast-reroute) [ **bandwidth** ] command to enable TE FRR. | TE FRR is recommended for primary MPLS TE tunnels, which improves network reliability. |
   | Run the [**bypass-attributes**](cmdqueryname=bypass-attributes) { **bandwidth** *bandwidth* | **priority** *setup-priority* [ *hold-priority* ] } \* command to configure bypass tunnel attributes. | A bypass tunnel is established using the configured bypass tunnel attributes. The bypass tunnel bandwidth cannot exceed the primary tunnel bandwidth. The setup priority of a bypass tunnel must be lower than or equal to the holding priority. Both of them must be lower than or equal to those of the primary tunnel. |
   | Run the [**lsp-tp outbound**](cmdqueryname=lsp-tp+outbound) command to enable traffic policing for MPLS TE tunnels. | Physical links over which a TE tunnel is established may also transmit traffic of other TE tunnels, non-CR-LSP traffic, or even IP traffic, in addition to the TE tunnel traffic. To limit TE traffic within a configured bandwidth range, enable traffic policing for a specific MPLS TE tunnel. |
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
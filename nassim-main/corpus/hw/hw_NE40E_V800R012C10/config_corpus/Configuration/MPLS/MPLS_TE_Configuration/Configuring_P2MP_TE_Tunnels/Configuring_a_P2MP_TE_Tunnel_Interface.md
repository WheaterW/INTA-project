Configuring a P2MP TE Tunnel Interface
======================================

Configuring a tunnel interface on an ingress helps you to manage and maintain the P2MP TE tunnel.

#### Context

A P2MP TE tunnel is established by binding multiple sub-LSPs to a P2MP TE tunnel interface. A network administrator configures a tunnel interface to manage and maintain the tunnel. After a tunnel interface is configured on an ingress, the ingress sends signaling packets to all leaf nodes to establish a tunnel.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *tunnel-number*
   
   
   
   A tunnel interface is created, and the tunnel interface view is displayed.
3. Run either of the following commands to assign an IP address to the tunnel interface:
   
   
   * Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* } [ **sub** ]
     
     An IP address is assigned to the tunnel interface.
   * Run [**ip address unnumbered**](cmdqueryname=ip+address+unnumbered) **interface** *interface-type* *interface-number*
     
     The tunnel interface is allowed to borrow the IP address of a specified interface.
   
   A tunnel interface must obtain an IP address before it can forward traffic. An MPLS TE tunnel is unidirectional and does not need a peer address. Therefore, there is no need to specifically configure an IP address for the tunnel interface. A TE tunnel interface usually uses the ingress LSR ID as its IP address.
4. Run [**tunnel-protocol**](cmdqueryname=tunnel-protocol) **mpls** **te**
   
   
   
   MPLS TE is configured as the tunneling protocol.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Changing, deleting, or initially configuring the tunnel mode of a tunnel interface will delete all tunnel-related configurations on the interface, such as the MTU. Exercise caution when performing this operation.
5. Run [**mpls te p2mp-mode**](cmdqueryname=mpls+te+p2mp-mode)
   
   
   
   A P2MP TE tunnel is established.
6. Run [**mpls te tunnel-id**](cmdqueryname=mpls+te+tunnel-id) *tunnel-id*
   
   
   
   A tunnel ID is set.
7. Run [**mpls te leaf-list**](cmdqueryname=mpls+te+leaf-list) *leaf-list-name*
   
   
   
   A leaf list is specified for the P2MP TE tunnel.
8. (Optional) Perform the following operations to set other tunnel attributes as needed:
   
   
   
   **Table 1** Operations
   | Operation | Description |
   | --- | --- |
   | Run [**mpls te bandwidth**](cmdqueryname=mpls+te+bandwidth) **ct0** *ct0-bw-value*  The bandwidth is configured for the tunnel. | * A P2MP TE tunnel is established to provide sufficient network bandwidth for multicast services. Therefore, set the bandwidth value. * The bandwidth used by the tunnel cannot be higher than the maximum reservable link bandwidth. * Ignore this step if the TE tunnel is used only for changing the data transmission path. |
   | Run [**mpls te record-route**](cmdqueryname=mpls+te+record-route) [ **label** ]  The route and label recording function for a manual P2MP TE tunnel is enabled. | This step enables nodes along a P2MP TE tunnel to use RSVP messages to record detailed P2MP TE tunnel information, including the IP address of each hop. The **label** parameter in the command enables RSVP messages to record label values. |
   | Run [**mpls te resv-style**](cmdqueryname=mpls+te+resv-style) { **se** | **ff** }  A resource reservation style is specified. | - |
   | Run [**mpls te path metric-type**](cmdqueryname=mpls+te+path+metric-type) { **igp** | **te** }  A link metric type used to select links is specified. | - |
   | Run [**mpls te affinity property**](cmdqueryname=mpls+te+affinity+property) *properties* [ **mask** *mask-value* ]  An affinity and its mask are specified. | An affinity is a 32-bit vector value used to describe an MPLS link. An affinity and an administrative group attribute define the nodes through which an MPLS TE tunnel passes. Affinity masks determine the link properties that a device must check. If some bits in the mask are 1, at least one bit in an administrative group is 1, and the corresponding bit in the affinity must be 1. If the bits in the affinity are 0s, the corresponding bits in the administrative group cannot be 1.  You can use an affinity to control the nodes through which a manual P2MP TE tunnel passes. |
   | Run [**mpls te hop-limit**](cmdqueryname=mpls+te+hop-limit) *hop-limit-value*  A hop limit is set for a manual P2MP TE tunnel. | The [**mpls te hop-limit**](cmdqueryname=mpls+te+hop-limit) command sets the maximum number of hops that each sub-LSP in a P2MP TE tunnel supports. |
   | Run [**mpls te tie-breaking**](cmdqueryname=mpls+te+tie-breaking) { **least-fill** | **most-fill** | **random** }  A rule for selecting a route among multiple routes to the same destination is specified. | - |
   | Run [**mpls te priority**](cmdqueryname=mpls+te+priority) *setup-priority* [ *hold-priority* ]  The priorities of the tunnel are set. | The setup priority of a tunnel must be no higher than its holding priority. A setup priority value must be greater than or equal to a holding priority value.  If resources are insufficient, setting the setup and holding priority values allows LSPs with lower priorities to release resources for establishing LSPs with higher priorities. |
   | Run [**mpls te reoptimization**](cmdqueryname=mpls+te+reoptimization) [ **frequency** *interval* ]  Periodic re-optimization is enabled for a manual P2MP TE Tunnel. | Periodic re-optimization allows a P2MP TE tunnel to be automatically reestablished over a better path. After a better path to the same destination has been calculated for a certain reason, such as a cost change, a TE tunnel will be automatically reestablished, optimizing resources on a network. |
   | Run [**mpls te lsp-tp outbound**](cmdqueryname=mpls+te+lsp-tp+outbound)  Traffic policing is enabled for a manual P2MP TE tunnel. | Physical links over which a P2MP TE tunnel is established transmit traffic of other TE tunnels, traffic of non-CR LSP traffic, or even IP traffic, in addition to TE tunnel traffic. To limit TE traffic within a configured bandwidth range, run the [**mpls te lsp-tp outbound**](cmdqueryname=mpls+te+lsp-tp+outbound) command. |
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
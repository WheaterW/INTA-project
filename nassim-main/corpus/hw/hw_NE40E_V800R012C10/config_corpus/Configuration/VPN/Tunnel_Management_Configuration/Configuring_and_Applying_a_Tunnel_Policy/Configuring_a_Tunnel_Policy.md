Configuring a Tunnel Policy
===========================

Tunnel policies are divided into tunnel type prioritizing policies and tunnel binding policies.

#### Context

VPN data needs to be carried over tunnels. By default, the system selects LSPs for VPN service transmission and does not perform load balancing on an IPv4 network. If the default tunnel configuration cannot meet VPN service requirements, a tunnel policy needs to be used.

The tunnel policy may be a tunnel type prioritizing policy or a tunnel binding policy. Select either of the following policies as needed:

* A tunnel type prioritizing policy can be used to switch a tunnel type to another one for VPN service transmission and implement load balancing among tunnels.
* A tunnel binding policy can bind multiple TE tunnels to provide QoS guarantee for a VPN.

On an IPv6 network, SRv6 TE Policies and SRv6 TE flow groups can participate in tunnel selection. In this case, only tunnel type prioritizing policies can be configured.

Perform the following steps on the PE that requires a tunnel policy.


#### Procedure

* Configure a tunnel type prioritizing policy.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**tunnel-policy**](cmdqueryname=tunnel-policy) *policy-name*
     
     
     
     A tunnel policy is created, and its view is displayed.
  3. (Optional) Run [**description**](cmdqueryname=description) *description-information*
     
     
     
     A description is configured for the tunnel policy.
     
     The tunnel policy description reminds users of the purpose of the tunnel policy.
  4. Configure the sequence of priority in which types of tunnels are selected and the maximum number of tunnels that can participate in load balancing.
     
     
     + Run one of the following commands for an IPv4 network:
       - [**tunnel select-seq**](cmdqueryname=tunnel+select-seq) { **gre** | **lsp** | **cr-lsp** | **sr-te-policy** **| flex-algo-lsp** } \* **load-balance-number** *load-balance-number* [ **unmix** ]
       - [**tunnel select-seq**](cmdqueryname=tunnel+select-seq) { **gre** | **ldp** | **bgp** | **cr-lsp** | **sr-lsp** | **sr-te-policy** **| flex-algo-lsp** } \* **load-balance-number** *load-balance-number* [ **unmix** ]
       - [**tunnel select-seq**](cmdqueryname=tunnel+select-seq) { **gre** | **lsp** | **te** | **sr-te** | **sr-te-policy** **| flex-algo-lsp** | **colored-sr-te**} \* **load-balance-number** *load-balance-number* [ **unmix** ]
       - [**tunnel select-seq**](cmdqueryname=tunnel+select-seq) { **gre** | **ldp** | **bgp** | **te** | **sr-te** | **sr-lsp** | **sr-te-policy** **| flex-algo-lsp** | **colored-sr-te** } \* **load-balance-number** *load-balance-number* [ **unmix** ]
       
       After this command is run, the system selects the tunnel type in the specified sequence of priority. If tunnels with higher priorities are unreachable, the system will continue to select tunnels with lower priorities in the specified sequence of priority. For example, if the **tunnel select-seq cr-lsp lsp load-balance-number 3** command is run, the system preferentially selects CR-LSPs followed by LSPs for VPN service transmission and uses a maximum of three tunnels for load balancing. If the number of available CR-LSP tunnels is less than three, LSPs can be used together with CR-LSPs in load balancing.
       
       LSPs include LDP LSPs, SR-LSPs, and BGP LSPs. If **lsp** is specified, the default sequence of priority, in descending order, is LDP LSP > BGP LSP > SR-LSP. If **sr-lsp**, **ldp** or **bgp** is specified, you can specify the sequence of priority in which LSPs are selected.
       
       CR-LSPs include RSVP-TE and SR-MPLS TE tunnels. If **cr-lsp** is specified in the command, a tunnel that goes up earlier has a higher priority.
       
       To enable the system to preferentially select RSVP-TE or SR-MPLS TE tunnels for VPN service transmission, specify the sequence of the **te** or **sr-te** parameter in the [**tunnel select-seq**](cmdqueryname=tunnel+select-seq) command.
       
       If **unmix** is configured, only one type of tunnel can be selected. For example, the **tunnel select-seq cr-lsp lsp load-balance-number 3 unmix** command is run for the tunnel policy:
       - If three or more CR-LSPs are available, the system randomly selects three of them for service transmission.
       - If less than three CR-LSPs are available, the system selects only these available CR-LSPs, but does not select other types of tunnels.
     + Run one of the following commands for an IPv6 network:
       - [**tunnel select-seq ipv6**](cmdqueryname=tunnel+select-seq+ipv6) { **srv6-te-policy** | **srv6-te-flow-group** | **gre6** } **load-balance-number** *loadBalanceNumber*
       - [**tunnel select-seq ipv6**](cmdqueryname=tunnel+select-seq+ipv6) **srv6-te-policy** **srv6-te-flow-group** **load-balance-number** *loadBalanceNumber* **unmix**
       - [**tunnel select-seq ipv6**](cmdqueryname=tunnel+select-seq+ipv6) **srv6-te-flow-group srv6-te-policy** **load-balance-number** *loadBalanceNumber* **unmix**
       
       After the command is run, the system selects tunnels of different types in the specified sequence. If tunnels that have higher priorities are unreachable, the system will continue to select tunnels that have lower priorities in the specified sequence.
       
       SRv6 TE Policies and SRv6 TE flow groups cannot both be selected.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a common tunnel binding policy.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *interface-number*
     
     
     
     The tunnel interface view is displayed.
  3. Run [**mpls te reserved-for-binding**](cmdqueryname=mpls+te+reserved-for-binding)
     
     
     
     Tunnel binding is enabled for the TE tunnel.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  5. Run [**tunnel-policy**](cmdqueryname=tunnel-policy) *policy-name*
     
     
     
     A tunnel policy is created.
  6. (Optional) Run [**description**](cmdqueryname=description) *description-information*
     
     
     
     A description is configured for the tunnel policy.
     
     
     
     The tunnel policy description helps users memorize the tunnel policy.
  7. Run [**tunnel binding**](cmdqueryname=tunnel+binding) **destination** *dest-ip-address* **te** { **tunnel-type** | *tunnel-type interface-number* } &<1-32> [ **ignore-destination-check** ] [ **down-switch** | **include-ldp** ]
     
     
     
     A specified TE tunnel is bound to a specified destination IP address in the tunnel policy view.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + If the **down-switch** parameter is specified in the command, the system selects an LSP or CR-LSP in descending order of priority for VPN data transmission when the bound TE tunnel is unavailable.
     + If a PE has multiple peers, you can run the [**tunnel binding**](cmdqueryname=tunnel+binding) command several times with different destination addresses specified.
       
       If a destination IP address is not bound to a tunnel using the [**tunnel binding**](cmdqueryname=tunnel+binding) command, the tunnel management module searches for a tunnel based on the default tunnel policy. By default, routes can recurse only to an LSP. To change the default type of tunnel to which routes recurse, run the [**tunnel policy binding-default down-switch enable**](cmdqueryname=tunnel+policy+binding-default+down-switch+enable) command to configure a tunnel policy to select a tunnel from available ones in descending order of priority: LSP > TE tunnel > GRE tunnel. LSP tunnels include LDP LSPs, BGP LSPs, and SR-MPLS BE tunnels. Their priorities are as follows: LDP LSP > BGP LSP > SR-MPLS BE tunnel.
  8. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
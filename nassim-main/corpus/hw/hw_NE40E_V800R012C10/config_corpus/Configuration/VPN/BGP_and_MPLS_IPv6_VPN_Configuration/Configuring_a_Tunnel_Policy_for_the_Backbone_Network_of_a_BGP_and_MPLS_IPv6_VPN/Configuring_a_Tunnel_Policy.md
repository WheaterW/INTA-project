Configuring a Tunnel Policy
===========================

A tunnel policy can determine the sequence in which tunnels are selected or bind a TE tunnel to a specified destination IP address.

#### Context

In the tunnel policy view, the tunnel type prioritizing policy and tunnel binding policy are mutually exclusive. Choose either of the following configurations as needed.


#### Procedure

* Configure a tunnel type prioritizing policy.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**tunnel-policy**](cmdqueryname=tunnel-policy) *policy-name*
     
     
     
     A tunnel policy is created, and the tunnel policy view is displayed.
  3. Run [**tunnel select-seq**](cmdqueryname=tunnel+select-seq) { { **cr-lsp** | { **te** | **sr-te** } } | **gre** | { **lsp** | { **ldp** | **bgp** | **sr-lsp** } } } \* **load-balance-number** *load-balance-number* [ **unmix** ]
     
     
     
     The sequence in which each type of tunnel is selected and the number of tunnels participating in load balancing are configured.
     
     
     
     After this command is run, the system selects tunnels based on the specified sequence. If tunnels that have higher priorities are unreachable, the system will continue to select tunnels that have lower priorities based on the sequence. For example, if the **tunnel select-seq cr-lsp lsp load-balance-number 3** command is run, the system can select CR-LSPs (as preferred ones) or LSPs for VPN service transmission and use a maximum of three tunnels for load balancing. If the number of available CR-LSPs is smaller than 3, LSPs will be qualified to join CR-LSPs in load balancing.
     
     LSPs include LDP LSPs, SR-LSPs, and BGP LSPs. If **lsp** is specified, the default priority sequence in descending order is LDP LSP > BGP LSP > SR-LSP. If **sr-lsp**, **ldp** or **bgp** is used, the priority sequence for LSPs can be specified.
     
     CR-LSPs include RSVP-TE tunnels and SR-MPLS TE tunnels. If **cr-lsp** is specified in the command, the tunnel that goes up earlier has a higher priority.
     
     To enable a VPN to preferentially select an RSVP-TE or SR-MPLS TE tunnel, specify the sequence of the **te** or **sr-te** parameter in the [**tunnel select-seq**](cmdqueryname=tunnel+select-seq) command.
     
     If **unmix** is configured, only one type of tunnel can be selected. For example, in a scenario where the **tunnel select-seq cr-lsp lsp load-balance-number 3 unmix** command is configured for the tunnel policy:
     + If three or more CR-LSPs are available on the network, the system randomly selects three of them for service transmission.
     + If less than three CR-LSPs are available on the network, the system selects only the available CR-LSPs for service transmission.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a tunnel binding policy.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**tunnel-policy**](cmdqueryname=tunnel-policy) *policy-name*
     
     
     
     A tunnel policy is created, and the tunnel policy view is displayed.
  3. Run [**tunnel binding**](cmdqueryname=tunnel+binding) **destination** *dest-ip-address* **te** { **tunnel-type** | *tunnel-type interface-number* } &<1-32> [ **ignore-destination-check** ] [ **down-switch** | **include-ldp** ]
     
     
     
     A tunnel binding policy is configured to bind a TE tunnel to the specified destination address.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
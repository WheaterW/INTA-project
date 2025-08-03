Configuring SBFD for SR-MPLS BE Tunnel
======================================

This section describes how to configure SBFD for SR-MPLS BE to detect SR-MPLS BE tunnel faults.

#### Usage Scenario

With SBFD for SR-MPLS BE, applications such as VPN FRR can be triggered to perform a fast traffic switching when the primary tunnel fails, minimizing the impact on services.

This configuration task applies to both common SR-MPLS BE tunnels and Flex-Algo-based SR-MPLS BE tunnels.


#### Pre-configuration Tasks

Before configuring SBFD for SR-MPLS BE tunnel, complete the following tasks:

* Configure an SR-MPLS BE tunnel.
* Run the [**mpls lsr-id**](cmdqueryname=mpls+lsr-id) *lsr-id* command to configure an LSR ID and ensure that the route from the peer to the local address specified using *lsr-id* is reachable.

#### Procedure

* Configuring an SBFD Initiator
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bfd**](cmdqueryname=bfd)
     
     
     
     BFD is globally enabled.
     
     
     
     You can set BFD parameters only after running the [**bfd**](cmdqueryname=bfd) command to enable global BFD.
  3. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  4. Run [**sbfd**](cmdqueryname=sbfd)
     
     
     
     SBFD is enabled globally, and the SBFD view is displayed.
  5. (Optional) Run [**destination ipv4**](cmdqueryname=destination+ipv4) *ip-address* [**remote-discriminator**](cmdqueryname=remote-discriminator) *discriminator-value*
     
     
     
     The mapping between the SBFD reflector IP address and discriminator is configured.
     
     
     
     On the device functioning as an SBFD initiator, if the mapping between the SBFD reflector IP address and discriminator is configured using the [**destination ipv4 remote-discriminator**](cmdqueryname=destination+ipv4+remote-discriminator) command, the initiator uses the configured discriminator to negotiate with the reflector in order to establish an SBFD session. If such a mapping is not configured, the SBFD initiator uses the reflector IP address as a discriminator by default to complete the negotiation.
     
     This step is optional. If it is performed, the value of *discriminator-value* must be the same as that of *unsigned-integer-value* in the [**reflector discriminator**](cmdqueryname=reflector+discriminator) command configured on the reflector.
  6. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  7. Run [**segment-routing**](cmdqueryname=segment-routing)
     
     
     
     The Segment Routing view is displayed.
  8. Run [**seamless-bfd enable**](cmdqueryname=seamless-bfd+enable) **mode** **tunnel** [ **filter-policy** **ip-prefix** *ip-prefix-name* | **effect-sr-lsp** ] \*
     
     
     
     SBFD is enabled for the SR-MPLS tunnel.
  9. (Optional) Run [**seamless-bfd**](cmdqueryname=seamless-bfd) **tunnel** { **min-rx-interval** *receive-interval* | **min-tx-interval** *transmit-interval* | **detect-multiplier** *multiplier-value* } \*
     
     
     
     SBFD parameters are set for the SR-MPLS tunnel.
  10. (Optional) Run [**seamless-bfd flex-algo**](cmdqueryname=seamless-bfd+flex-algo) **exclude** { *flex-algo-begin* [ **to** *flex-algo-end* ] } &<1-10>
      
      
      
      Flex-Algos that do not require SBFD session establishment are excluded.
      
      
      
      After the [**seamless-bfd enable**](cmdqueryname=seamless-bfd+enable) command is run, SBFD sessions are established for all common SR-MPLS BE tunnels and Flex-Algo-based SR-MPLS BE tunnels. If some Flex-Algo-based SR-MPLS BE tunnels do not require SBFD session establishment, run the preceding command to exclude the corresponding Flex-Algos.
  11. (Optional) Configure an IS-IS SBFD source address.
      
      
      
      In IS-IS multi-process scenarios, you can configure source addresses for SBFD sessions in different IS-IS processes.
      
      By default, MPLS LSR IDs are used to create SBFD sessions. During SBFD deployment, only an LSR ID can be used as the source of an SBFD session, but the source belongs to only one IS-IS process. As a result, in the multi-process scenarios, LSR ID-based host routes must be imported in route import mode. Otherwise, SBFD cannot take effect. If IS-IS process isolation prevents route import, the device must support SBFD session establishment using different sources in different IS-IS processes.
      
      1. Run [**quit**](cmdqueryname=quit)
         
         Return to the system view.
      2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
         
         The IS-IS view is displayed.
      3. Run [**cost-style**](cmdqueryname=cost-style) { **wide** | **compatible** | **wide-compatible** }
         
         The IS-IS wide metric is configured.
      4. Run [**segment-routing mpls**](cmdqueryname=segment-routing+mpls)
         
         IS-IS SR-MPLS is enabled.
      5. Run [**segment-routing sbfd source-address**](cmdqueryname=segment-routing+sbfd+source-address) *ip-address*
         
         An SBFD source address is configured.
  12. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
* Configuring an SBFD Reflector
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bfd**](cmdqueryname=bfd)
     
     
     
     BFD is globally enabled.
     
     
     
     You can set BFD parameters only after running the [**bfd**](cmdqueryname=bfd) command to enable global BFD.
  3. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  4. Run [**sbfd**](cmdqueryname=sbfd)
     
     
     
     SBFD is enabled globally, and the SBFD view is displayed.
  5. Run [**reflector discriminator**](cmdqueryname=reflector+discriminator) { *unsigned-integer-value* | *ip-address-value* }
     
     
     
     A discriminator is configured for the SBFD reflector.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.

#### Verifying the Configuration

After successfully configuring SBFD for SR-MPLS BE tunnel, run the [**display segment-routing seamless-bfd tunnel session**](cmdqueryname=display+segment-routing+seamless-bfd+tunnel+session) [ **prefix** *ip-address* { *mask* | *mask-length* } ] [ **flex-algo** [ *flexAlgoId* ] ] command to check information about the SBFD session that monitors the SR tunnel.
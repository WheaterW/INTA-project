Configuring SRv6 Microloop Avoidance (OSPFv3)
=============================================

A network topology change may cause a loop. To effectively avoid loops on the network, a network node can create a loop-free SRv6 segment list to steer traffic to the destination address. Then normal traffic forwarding is restored after all the involved network nodes converge.

#### Usage Scenario

If a network failure occurs or is rectified, an IGP performs route convergence. A transient forwarding status inconsistency between nodes results in different convergence rates on devices, presenting the risk of microloops. To address this issue, configure the microloop avoidance function.


#### Pre-configuration Tasks

Before configuring OSPFv3 SRv6 microloop avoidance, enable OSPFv3 SRv6.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospfv3**](cmdqueryname=ospfv3) [ *process-id* ]
   
   
   
   An OSPFv3 process is enabled, and its view is displayed.
3. Run [**avoid-microloop frr-protected**](cmdqueryname=avoid-microloop+frr-protected)
   
   
   
   OSPFv3 local microloop avoidance is enabled.
4. (Optional) Run [**avoid-microloop frr-protected rib-update-delay**](cmdqueryname=avoid-microloop+frr-protected+rib-update-delay) *interval*
   
   
   
   A delay in OSPFv3 route delivery is configured.
5. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6) **locator** *locator-name*
   
   
   
   OSPFv3 SRv6 is enabled.
6. Run [**avoid-microloop segment-routing**](cmdqueryname=avoid-microloop+segment-routing)
   
   
   
   OSPFv3 remote microloop avoidance is enabled.
7. (Optional) Run [**avoid-microloop segment-routing rib-update-delay**](cmdqueryname=avoid-microloop+segment-routing+rib-update-delay) *rib-update-delay*
   
   
   
   A delay in SRv6 OSPFv3 route delivery is configured.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After completing OSPFv3 SRv6 microloop avoidance, verify the configuration.

* Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **routing** [ [ *ipv6-address* *prefix-length* ] | **ase-routes** | **inter-routes** | **intra-routes** | **nssa-routes** ] **verbose** command to check OSPFv3 SRv6 route information.
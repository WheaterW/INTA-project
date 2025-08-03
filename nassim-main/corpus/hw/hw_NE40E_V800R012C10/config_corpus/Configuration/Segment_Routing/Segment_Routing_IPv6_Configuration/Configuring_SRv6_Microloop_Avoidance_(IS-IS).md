Configuring SRv6 Microloop Avoidance (IS-IS)
============================================

A network topology change may cause a loop. To effectively avoid loops on the network, a network node can create a loop-free SRv6 segment list to steer traffic to the destination address. Then normal traffic forwarding is restored after all the involved network nodes converge.

#### Usage Scenario

If a network failure occurs or is rectified, an IGP performs route convergence. A transient forwarding status inconsistency between nodes results in different convergence rates on devices, presenting the risk of microloops. To address this issue, configure the microloop avoidance function.


#### Pre-configuration Tasks

Before configuring IS-IS SRv6 microloop avoidance, enable IS-IS SRv6.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
   
   
   
   An IS-IS process is enabled, and its view is displayed.
3. (Optional) Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6+compress+enable) **compress** **enable**
   
   
   
   An IS-IS SRv6 compression mode is enabled so that a compressed SID stack is preferentially formed during label stack computation in IS-IS SRv6 TI-LFA and microloop avoidance scenarios.
4. (Optional) Run [**encapsulation-mode**](cmdqueryname=encapsulation-mode) { **insert** | **encaps** }
   
   
   
   An encapsulation mode is configured for the IS-IS SRv6 SID stack.
5. Run [**avoid-microloop frr-protected**](cmdqueryname=avoid-microloop+frr-protected)
   
   
   
   IS-IS local microloop avoidance is enabled.
6. (Optional) Run [**avoid-microloop frr-protected rib-update-delay**](cmdqueryname=avoid-microloop+frr-protected+rib-update-delay) *rib-update-delay*
   
   
   
   A delay in IS-IS route delivery is configured.
7. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6) **locator** *locator-name*
   
   
   
   IS-IS SRv6 is enabled.
8. Run [**ipv6 avoid-microloop segment-routing**](cmdqueryname=ipv6+avoid-microloop+segment-routing)
   
   
   
   IS-IS remote microloop avoidance is enabled.
9. (Optional) Run [**ipv6 avoid-microloop segment-routing rib-update-delay**](cmdqueryname=ipv6+avoid-microloop+segment-routing+rib-update-delay) *rib-update-delay*
   
   
   
   A delay in SRv6 IS-IS route delivery is configured.
10. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.

#### Verifying the Configuration

After completing IS-IS SRv6 microloop avoidance, verify the configuration.

* Run the [**display isis**](cmdqueryname=display+isis) [ *process-id* ] **route** **ipv6** [ **level-1** | **level-2** ] [ **verbose** ] command to check IS-IS route information.
* Run the [**display isis**](cmdqueryname=display+isis+avoid-microloop+information) [ *process-id* ] **avoid-microloop information** **ipv6** [ **level-1** | **level-2** ] [ **systemid** *systemid* ] command to check microloop avoidance information about a node.
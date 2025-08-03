Configuring IS-IS TI-LFA FRR
============================

This section describes how to configure IS-IS TI-LFA FRR.

#### Usage Scenario

With the development of networks, VoIP and on-line video services require high-quality real-time transmission. Nevertheless, if an IS-IS fault occurs, multiple processes, including fault detection, LSP update, LSP flooding, route calculation, and FIB entry delivery, must be performed to switch traffic to a new link. As a result, the traffic interruption time is longer than 50 ms, leading to a failure to satisfy real-time requirements.

TI-LFA FRR provides link and node protection for Segment Routing (SR) tunnels. If a link or node fails, traffic is rapidly switched to a backup path, which minimizes traffic loss.

In some LFA or RLFA scenarios, the P space and Q space do not share nodes or have direct neighbors. If a link or node fails, no backup path can be calculated, causing traffic loss and resulting in a failure to meet reliability requirements. In this situation, TI-LFA can be used.


#### Pre-configuration Tasks

Before configuring IS-IS TI-LFA FRR, complete the following tasks:

* Configure addresses for interfaces to ensure that neighboring devices are reachable at the network layer.
* [Configure basic IPv4 IS-IS functions](dc_vrp_isis_cfg_1000.html).
* Globally enable the Segment Routing capability.
* Enable the Segment Routing capability in an IS-IS process.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
   
   
   
   An IS-IS process is created, and the IS-IS view is displayed.
3. Run [**frr**](cmdqueryname=frr)
   
   
   
   The IS-IS FRR view is displayed.
4. Run [**loop-free-alternate**](cmdqueryname=loop-free-alternate) [ **level-1** | **level-2** | **level-1-2** ]
   
   
   
   IS-IS LFA is enabled, and LFA links can be generated.
5. Run [**ti-lfa**](cmdqueryname=ti-lfa) [ **remote-srlg** ] [ **level-1** | **level-2** | **level-1-2** ]
   
   
   
   IS-IS TI-LFA is enabled.
6. (Optional) Run [**inter-level-protect level-1**](cmdqueryname=inter-level-protect+level-1) [ **prefer** ]
   
   
   
   Inter-level protection is enabled in IS-IS Level-1.
   
   
   
   By default, IS-IS TI-LFA computes backup paths only in the same IS-IS level. After the [**inter-level-protect level-1**](cmdqueryname=inter-level-protect+level-1) command is run, if no TI-LFA backup path exists in IS-IS Level-1, inter-level TI-LFA backup path computation is performed.
   
   If the **prefer** parameter is specified, an inter-level TI-LFA backup path is preferentially selected even if there is a TI-LFA backup path in IS-IS Level-1.
7. (Optional) Run [**tiebreaker**](cmdqueryname=tiebreaker) { **node-protecting** | **lowest-cost** | **srlg-disjoint** | **hold-max-cost** } **preference** *preference* [ **level-1** | **level-2** | **level-1-2** ]
   
   
   
   An IS-IS TI-LFA FRR tiebreaker is configured for backup path computation.
   
   
   
   A larger value indicates a higher preference.
   
   Before configuring the **srlg-disjoint** parameter, you need to run the [**isis srlg**](cmdqueryname=isis+srlg) *srlg-value* command in the IS-IS interface view to configure the IS-IS SRLG function.
8. (Optional) After completing the preceding configuration, IS-IS TI-LFA is enabled on all IS-IS interfaces. If you do not want to enable IS-IS TI-LFA on some interfaces, perform the following operations:
   1. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the IS-IS FRR view.
   2. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the IS-IS view.
   3. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
      
      
      
      The interface view is displayed.
   4. Run [**isis**](cmdqueryname=isis) [ **process-id** *process-id* ] **ti-lfa disable** [ **level-1** | **level-2** | **level-1-2** ]
      
      
      
      TI-LFA is disabled on the interface.
9. If a network fault occurs or is rectified, an IGP performs route convergence. A transient forwarding status inconsistency between nodes results in different convergence rates on devices, posing the risk of microloops. To prevent microloops, perform the following steps:
   
   
   1. Run [**quit**](cmdqueryname=quit)
      
      Exit the interface view.
   2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
      
      The IS-IS process is created, and the IS-IS view is displayed.
   3. Run [**avoid-microloop frr-protected**](cmdqueryname=avoid-microloop+frr-protected)
      
      IS-IS local microloop avoidance is enabled.
   4. (Optional) Run [**avoid-microloop frr-protected rib-update-delay**](cmdqueryname=avoid-microloop+frr-protected+rib-update-delay) *rib-update-delay*
      
      The delay after which IS-IS delivers routes is configured.
   5. Run [**avoid-microloop segment-routing**](cmdqueryname=avoid-microloop+segment-routing)
      
      IS-IS remote microloop avoidance is enabled.
   6. (Optional) Run [**avoid-microloop segment-routing rib-update-delay**](cmdqueryname=avoid-microloop+segment-routing+rib-update-delay) *rib-update-delay*
      
      The delay in delivering IS-IS route in an SR scenario is set.
10. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.

#### Verifying the Configuration

After configuring IS-IS TI-LFA FRR, run the [**display isis route**](cmdqueryname=display+isis+route) [ *process-id* ] [ **level-1** | **level-2** ] [ **verbose** ] command to check information about the primary and backup links.
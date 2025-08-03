Configuring OSPF TI-LFA FRR
===========================

This section describes how to configure OSPF TI-LFA FRR.

#### Usage Scenario

For some large networks, especially for the networks where the P space and Q space neither intersect nor have directly connected neighbors, if a link or node fails, LFA and RLFA cannot compute a backup path, causing traffic loss and failing to meet reliability requirements. To resolve this issue, TI-LFA is introduced.

TI-LFA FRR provides link and node protection for SR tunnels. If a link or node fails, it enables traffic to be rapidly switched to a backup path, minimizing traffic loss.


#### Pre-configuration Tasks

Before configuring OSPF TI-LFA FRR, complete the following tasks:

* Configure addresses for interfaces to ensure that neighboring devices are reachable at the network layer.
* Configure basic OSPF functions
* Enable SR globally.
* Enable SR for the corresponding OSPF process.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospf**](cmdqueryname=ospf) [ *process-id* ]
   
   
   
   An OSPF process is created, and the OSPF view is displayed.
3. Run [**frr**](cmdqueryname=frr)
   
   
   
   The OSPF FRR view is displayed.
4. Run [**loop-free-alternate**](cmdqueryname=loop-free-alternate)
   
   
   
   OSPF LFA is enabled, and LFA links can be generated.
5. Run [**ti-lfa enable**](cmdqueryname=ti-lfa+enable)
   
   
   
   OSPF TI-LFA is enabled.
6. (Optional) Run [**tiebreaker**](cmdqueryname=tiebreaker) { **node-protecting** | **lowest-cost** | **ldp-sync hold-max-cost** | **srlg-disjoint** } **preference** *preference*
   
   
   
   An OSPF TI-LFA FRR tiebreaker for backup path computation is configured.
   
   
   
   A larger value indicates a higher preference.
   
   Before configuring the **srlg-disjoint** parameter, you need to run the [**ospf srlg**](cmdqueryname=ospf+srlg) *srlg-value* command in the OSPF interface view to configure the OSPF SRLG function.
7. (Optional) After completing the preceding configuration, OSPF TI-LFA is enabled on all OSPF interfaces. If you do not want to enable OSPF TI-LFA on some interfaces, perform the following operations:
   1. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the OSPF FRR view.
   2. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the OSPF view.
   3. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
      
      
      
      The interface view is displayed.
   4. To disable the OSPF TI-LFA on a specified interface, run either of the following commands:
      
      
      * For a common interface, run the [**ospf ti-lfa disable**](cmdqueryname=ospf+ti-lfa+disable) command.
      * For a multi-area interface, run the [**ospf ti-lfa disable multi-area**](cmdqueryname=ospf+ti-lfa+disable+multi-area) *area-id* command.
8. If a network fault occurs or is rectified, an IGP performs route convergence. A transient forwarding status inconsistency between nodes results in different convergence rates on devices, posing the risk of microloops. To prevent microloops, perform the following steps:
   
   
   1. Run [**quit**](cmdqueryname=quit)
      
      Exit the interface view.
   2. Run [**ospf**](cmdqueryname=ospf) [ *process-id* ]
      
      An OSPF process is created, and the OSPF view is displayed.
   3. Run [**avoid-microloop frr-protected**](cmdqueryname=avoid-microloop+frr-protected)
      
      OSPF local microloop avoidance is enabled.
   4. Run [**avoid-microloop frr-protected rib-update-delay**](cmdqueryname=avoid-microloop+frr-protected+rib-update-delay) *rib-update-delay*
      
      The delay after which OSPF delivers routes is configured.
   5. Run [**avoid-microloop segment-routing**](cmdqueryname=avoid-microloop+segment-routing)
      
      OSPF remote microloop avoidance is enabled.
   6. (Optional) Run [**avoid-microloop segment-routing rib-update-delay**](cmdqueryname=avoid-microloop+segment-routing+rib-update-delay) *rib-update-delay*
      
      A delay in delivering OSPF routes in an SR scenario is set.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After completing all OSPF TI-LFA FRR configurations, run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **segment-routing** **routing** [ *ip-address* [ *mask* | *mask-length* ] ] command to check OSPF SR routing table information.
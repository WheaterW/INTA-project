Configuring SRv6 TI-LFA FRR (IS-IS)
===================================

SRv6 topology-independent loop-free alternate (TI-LFA) fast reroute (FRR) uses an explicit path to represent a backup path, which poses no topology constraints and provides more reliable FRR.

#### Usage Scenario

For some large networks, especially for the networks where the P space and Q space neither intersect nor have directly connected neighbors, if a link or node fails, LFA and RLFA cannot compute a backup path, causing traffic loss and failing to meet reliability requirements. To resolve this issue, TI-LFA FRR is introduced.

SRv6 TI-LFA FRR provides link and node protection for SRv6 services. If a link or node fails, it enables traffic to be rapidly switched to a backup path, minimizing traffic loss.

SRv6 TI-LFA FRR applies to both SRv6 BE and SRv6 TE Policy scenarios. Although SRv6 BE packets typically do not carry SRH information, they do in TI-LFA FRR scenarios to encapsulate repair list information.


#### Pre-configuration Tasks

Before configuring IS-IS SRv6 TI-LFA FRR, enable IS-IS SRv6.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
   
   
   
   An IS-IS process is created, and the IS-IS view is displayed.
3. Run [**ipv6 enable**](cmdqueryname=ipv6+enable) **topology ipv6**
   
   
   
   IPv6 is enabled for the IS-IS process.
4. (Optional) Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6+compress+enable) **compress** **enable**
   
   
   
   An IS-IS SRv6 compression mode is enabled so that a compressed SID stack is preferentially formed during label stack computation in IS-IS SRv6 TI-LFA and microloop avoidance scenarios.
5. (Optional) Run [**encapsulation-mode**](cmdqueryname=encapsulation-mode) { **insert** | **encaps** }
   
   
   
   An encapsulation mode is configured for the IS-IS SRv6 SID stack.
6. Run [**ipv6 frr**](cmdqueryname=ipv6+frr)
   
   
   
   The IPv6 IS-IS FRR view is displayed.
7. Run [**loop-free-alternate**](cmdqueryname=loop-free-alternate) [ **level-1** | **level-2** | **level-1-2** ]
   
   
   
   IPv6 IS-IS FRR is enabled, so that a loop-free backup link is generated using the LFA algorithm.
8. Run [**ti-lfa**](cmdqueryname=ti-lfa) [ **level-1** | **level-2** | **level-1-2** ]
   
   
   
   IS-IS SRv6 TI-LFA is enabled.
9. (Optional) Run [**inter-level-protect level-1**](cmdqueryname=inter-level-protect+level-1) [ **prefer** ]
   
   
   
   Inter-level protection is enabled in IS-IS Level-1.
   
   
   
   By default, SRv6 TI-LFA computes backup paths only in the same IS-IS level. After the [**inter-level-protect level-1**](cmdqueryname=inter-level-protect+level-1) command is run, if no SRv6 TI-LFA backup path exists in IS-IS Level-1, inter-level SRv6 TI-LFA backup path computation is performed.
   
   If the **prefer** parameter is specified, an inter-level SRv6 TI-LFA backup path is preferentially selected even if there is an SRv6 TI-LFA backup path in IS-IS Level-1.
10. (Optional) Run [**tiebreaker**](cmdqueryname=tiebreaker) { **node-protecting** | **lowest-cost** | **srlg-disjoint** | **hold-max-cost** } **preference** *preference* [ **level-1** | **level-2** | **level-1-2** ]
    
    
    
    An IS-IS SRv6 TI-LFA FRR tiebreaker is configured for backup path computation.
    
    
    
    A larger value indicates a higher preference.
    
    Before configuring the **srlg-disjoint** parameter, you need to run the [**isis srlg**](cmdqueryname=isis+srlg) *srlg-value* command in the IS-IS interface view to configure the IS-IS SRLG function.
11. (Optional) Disable IS-IS SRv6 TI-LFA on some interfaces. The preceding configurations enable IS-IS SRv6 TI-LFA on all IPv6 IS-IS interfaces. Perform the following steps to disable it on required interfaces:
    1. Run [**quit**](cmdqueryname=quit)
       
       
       
       Exit the IS-IS FRR view.
    2. Run [**quit**](cmdqueryname=quit)
       
       
       
       Exit the IS-IS view.
    3. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
       
       
       
       The interface view is displayed.
    4. Run [**isis ipv6 ti-lfa disable**](cmdqueryname=isis+ipv6+ti-lfa+disable) [ **level-1** | **level-2** | **level-1-2** ]
       
       
       
       IPv6 IS-IS TI-LFA is disabled on the interface.
12. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.

#### Verifying the Configuration

After configuring IS-IS SRv6 TI-LFA FRR, verify the configuration.

* Run the [**display isis**](cmdqueryname=display+isis) [ *process-id* ] **route** **ipv6** [ **level-1** | **level-2** ] [ **verbose** ] command to check information about the primary and backup links after IS-IS SRv6 TI-LFA FRR is enabled.
* Run the [**display isis**](cmdqueryname=display+isis+srv6+ti-lfa-node) [ *process-id* ] **srv6** **ti-lfa-node** [ **ipv6** ] [ **level-1** | **level-2** ] [ **systemid** *systemid* ] command to check TI-LFA information about a specified node.
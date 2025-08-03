Configuring SRv6 TI-LFA FRR (OSPFv3)
====================================

SRv6 topology-independent loop-free alternate (TI-LFA) fast reroute (FRR) uses an explicit path to represent a backup path, which poses no topology constraints and provides more reliable FRR.

#### Usage Scenario

For some large networks, especially for the networks where the P space and Q space neither intersect nor have directly connected neighbors, if a link or node fails, SRv6 TI-LFA FRR provides link and node protection for SRv6 services, minimizing traffic loss.

SRv6 TI-LFA FRR applies to both SRv6 BE and SRv6 TE Policy scenarios. Although SRv6 BE packets typically do not carry SRH information, they do in TI-LFA FRR scenarios to encapsulate repair list information.


#### Pre-configuration Tasks

Before configuring OSPFv3 SRv6 TI-LFA FRR, enable OSPFv3 SRv6.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospfv3**](cmdqueryname=ospfv3) [ *process-id* ]
   
   
   
   An OSPFv3 process is enabled, and its view is displayed.
3. Run [**frr**](cmdqueryname=frr)
   
   
   
   The OSPFv3 FRR view is displayed.
4. Run [**loop-free-alternate**](cmdqueryname=loop-free-alternate)
   
   
   
   OSPFv3 FRR is enabled, so that a loop-free backup link can be generated using the LFA algorithm.
5. Run [**ti-lfa enable**](cmdqueryname=ti-lfa+enable)
   
   
   
   OSPFv3 SRv6 TI-LFA is enabled.
6. (Optional) Run [**tiebreaker**](cmdqueryname=tiebreaker) { **node-protecting** | **lowest-cost** | **srlg-disjoint** } **preference** *value*
   
   
   
   An OSPFv3 SRv6 TI-LFA FRR tiebreaker is configured for backup path computation.
   
   
   
   A larger value indicates a higher preference.
   
   Before configuring the **srlg-disjoint** parameter, you need to run the [**ospfv3 srlg**](cmdqueryname=ospfv3+srlg) *srlg-value* [ **instance** *instanceId* ] command in the OSPFv3 interface view to configure the OSPFv3 SRLG function.
7. (Optional) After you complete the preceding configuration, SRv6 TI-LFA is enabled on all OSPFv3 interfaces. If you do not want to enable SRv6 TI-LFA on some interfaces, perform the following steps in sequence:
   1. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the OSPFv3 FRR view.
   2. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the OSPFv3 process view.
   3. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
      
      
      
      The interface view is displayed.
   4. Run [**ipv6 enable**](cmdqueryname=ipv6+enable)
      
      
      
      IPv6 is enabled on the interface.
   5. Run [**ospfv3**](cmdqueryname=ospfv3) *process-id* **area** *area-id* [ **instance** *instance-id* ]
      
      
      
      OSPFv3 is enabled on the interface. The specified area ID can be a decimal integer or in the IPv4 address format. It is displayed as an IPv4 address regardless of its format adopted.
   6. To prevent TI-LFA backup next hop computation on the interface, run [**ospfv3 ti-lfa disable**](cmdqueryname=ospfv3+ti-lfa+disable) [ **instance** *instance-id* ]
      
      
      
      TI-LFA backup next hop computation is prevented on the interface.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After configuring OSPFv3 SRv6 TI-LFA FRR, verify the configuration.

* Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **routing** [ [ *ipv6-address* *prefix-length* ] | **ase-routes** | **inter-routes** | **intra-routes** | **nssa-routes** ] **verbose** command to check information about the primary and backup links after OSPFv3 SRv6 TI-LFA FRR is enabled.
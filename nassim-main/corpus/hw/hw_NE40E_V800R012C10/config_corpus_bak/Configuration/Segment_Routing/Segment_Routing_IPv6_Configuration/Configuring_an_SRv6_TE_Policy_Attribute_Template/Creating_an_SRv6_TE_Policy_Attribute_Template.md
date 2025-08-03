Creating an SRv6 TE Policy Attribute Template
=============================================

An SRv6 TE Policy attribute template can be used to implement batch configuration, minimizing the configuration workload and improving configuration efficiency.

#### Context

Currently, you can use the SRv6 TE Policy attribute template to configure multiple functions, including SBFD, BFD bypass/no-bypass, hot standby, fault detection, and traffic statistics collection. These functions can also be configured globally in the Segment Routing IPv6 view or individually in the SRv6 TE Policy view.

If a function is configured using all three of the preceding methods, the individual configuration in the SRv6 TE Policy view has the highest priority, followed by the configuration in the SRv6 TE Policy attribute template. The global configuration in the Segment Routing IPv6 view has the lowest priority.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**segment-routing policy-template**](cmdqueryname=segment-routing+policy-template) *template-value*
   
   
   
   An SR Policy attribute template is created, and the SR Policy template view is displayed.
3. Run [**description**](cmdqueryname=description)*description-value*
   
   
   
   A description is configured for the attribute template.
4. Run [**bfd**](cmdqueryname=bfd) **seamless** **enable** [ **reverse-path binding-sid** ]
   
   
   
   The SBFD function in the attribute template is enabled.
   
   
   
   In SBFD for SRv6 TE Policy scenarios, the **reverse-path binding-sid** parameter enables SBFD return packets to be forwarded over an SRv6 TE Policy.
5. Run [**bfd**](cmdqueryname=bfd) **unaffiliated** **enable** [ **reverse-path binding-sid** ]
   
   
   
   The U-BFD function in the attribute template is enabled.
   
   
   
   In U-BFD for SRv6 TE Policy scenarios, the **reverse-path binding-sid** parameter enables U-BFD return packets to be forwarded over an SRv6 TE Policy.
6. Run [**bfd**](cmdqueryname=bfd){ **no-bypass** [ **preferred** ] | **bypass** }
   
   
   
   The BFD bypass/no-bypass function in the attribute template is enabled.
   
   
   
   If you do not want the U-BFD packets of the SRv6 TE Policy to transit local protection paths such as TI-LFA and TE FRR paths, select the **no-bypass** parameter. Otherwise, select the **bypass** parameter.
   
   If you specify both the **no-bypass** and **preferred** parameters, the traffic forwarded over an SRv6 TE Policy is not preferentially transmitted over local protection paths. If an SRv6 TE Policy has a backup path, BFD packets on the primary path are not transmitted over local protection paths such as TI-LFA and TE FRR paths. If the primary path fails, BFD goes down, and traffic is then switched to the backup path. BFD packets on the backup path can be transmitted over local protection paths to ensure service continuity.
7. Run [**backup hot-standby**](cmdqueryname=backup+hot-standby){ **enable** | **disable** }
   
   
   
   The hot standby function in the attribute template is enabled or disabled.
8. Run [**path verification**](cmdqueryname=path+verification){ [ ****specified-sid**** ]**enable** | **disable** }
   
   
   
   The fault detection function in the attribute template is enabled or disabled.
9. Run [**traffic-statistics**](cmdqueryname=traffic-statistics){ **enable** | **disable** }
   
   
   
   The traffic statistics collection function in the attribute template is enabled or disabled.
10. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.
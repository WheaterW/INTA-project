Configuring the Function to Collect VPWS PW Traffic Statistics
==============================================================

The function to collect VPWS PW traffic statistics helps network administrators monitor network operating status and locate problems in an easier way.

#### Usage Scenario

To monitor network operating status and locate problems in an easier way on a VPWS network, configure the function to collect VPWS PW traffic statistics.


#### Pre-configuration Tasks

Before configuring the function to collect VPWS PW traffic statistics, complete the following tasks:

* Configure network-layer parameters for devices to communicate.
* Configure VPWS PWs.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The AC interface view is displayed.
3. Run [**mpls l2vpn pw traffic-statistics enable**](cmdqueryname=mpls+l2vpn+pw+traffic-statistics+enable) [ **secondary** | **bypass** ]
   
   
   
   The function to collect VPWS PW traffic statistics is enabled. Note that:
   
   
   
   * If you do not specify **secondary** or **bypass**, the traffic statistics collection function applies to the primary VPWS PW.
   * If you specify **secondary**, the traffic statistics collection function applies to the secondary VPWS PW.
   * If you specify **bypass**, the traffic statistics collection function applies to the bypass VPWS PW.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
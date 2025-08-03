Configuring Traffic Statistics Collection for VPWS QoS
======================================================

You can collect VPWS QoS traffic statistics in real time to check whether the QoS requirements are met.

#### Usage Scenario

To monitor network operating status and locate problems in an easier way on a VPWS network, you can configure traffic statistics collection for VPWS QoS.

If VPWS QoS and VPWS traffic statistics collection are both configured, you can determine whether the QoS requirements of VPWS services are met based on VPWS QoS traffic statistics collected in real time.


#### Pre-configuration Tasks

Before configuring VPWS QoS traffic statistics collection, complete the following tasks:

* Configure VPWS PWs.
* Configure VPWS QoS.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The view of an AC interface is displayed.
3. Run [**mpls l2vpn pw traffic-statistics enable**](cmdqueryname=mpls+l2vpn+pw+traffic-statistics+enable) [ **secondary** | **bypass** ]
   
   
   
   VPWS QoS traffic statistics collection is configured.
   
   
   
   Note that:
   
   * If you do not specify **secondary** or **bypass**, the statistics collection function applies to the primary VPWS PW.
   * If you specify **secondary**, the statistics collection function applies to the secondary VPWS PW.
   * If you specify **bypass**, the statistics collection function applies to the bypass VPWS PW.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After configuring VPWS QoS traffic statistics collection, verify the configuration.

* Run the [**display traffic-statistics l2vpn qos pw**](cmdqueryname=display+traffic-statistics+l2vpn+qos+pw) **interface** *interface-type* *interface-number* [ **secondary** | **bypass** ] command to check collected VPWS QoS traffic statistics.
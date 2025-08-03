Configuring IFIT Tunnel-Level Quality Measurement
=================================================

Configuring IFIT tunnel-level quality measurement is a prerequisite for implementing intelligent traffic steering.

#### Prerequisites

Before configuring IFIT tunnel-level quality measurement in an SRv6 scenario, complete the following tasks:

* [Configure an SRv6 TE Policy (manual configuration + IS-IS as IGP)](dc_vrp_srv6_cfg_all_0110.html)/[Configure an SRv6 TE Policy (controller-based dynamic delivery + IS-IS as IGP)](dc_vrp_srv6_cfg_all_0116.html).
  
  Bidirectional binding SIDs must be configured to ensure normal MCP calculation.
* Configure a clock synchronization protocol to implement clock synchronization between devices. In this scenario, NTP is generally used because interworking with other types of devices may be required. For details, see *NTP Configuration*.


#### Context

Users want to use the NMS to monitor tunnel quality on the network in real time so that tunnel exceptions can be quickly detected and paths promptly switched. You can configure IFIT measurement on devices so that the devices can periodically collect statistics about packet loss and delay and perform intelligent traffic steering through tunnel quality analysis, simplifying the O&M process and improving O&M experience.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The following steps need to be performed only on the ingress and egress.



#### Procedure

1. Configure IFIT measurement for an SRv6 TE Policy.
   
   
   1. Run [**system-view**](cmdqueryname=system-view)
      
      The system view is displayed.
   2. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6)
      
      The SRv6 view is displayed.
   3. Run [**srv6-te policy**](cmdqueryname=srv6-te+policy) *name-value* **endpoint** *endpoint-ip* **color** *color-value*
      
      The SRv6 TE Policy view is displayed.
   4. Run [**ifit loss-measure enable**](cmdqueryname=ifit+loss-measure+enable)
      
      IFIT packet loss measurement is enabled for the SRv6 TE Policy.
   5. Run [**ifit delay-measure enable**](cmdqueryname=ifit+delay-measure+enable)
      
      IFIT delay measurement is enabled for the SRv6 TE Policy.
   6. Run [**ifit measure-mode**](cmdqueryname=ifit+measure-mode) { **e2e** | **trace** }
      
      An IFIT measurement mode is set for the SRv6 TE Policy.
      
      By default, end-to-end measurement is used.
   7. (Optional) Run [**ifit interval**](cmdqueryname=ifit+interval) *interval-value*
      
      An IFIT measurement interval is configured for the SRv6 TE Policy.
   8. Run [**commit**](cmdqueryname=commit)
      
      The configuration is committed.
   9. Run [**quit**](cmdqueryname=quit)
      
      Exit the SRv6 TE Policy view.
   10. Run [**quit**](cmdqueryname=quit)
       
       Return to the system view.
2. Run [**ifit**](cmdqueryname=ifit)
   
   
   
   IFIT is enabled globally, and its view is displayed.
3. Run [**node-id**](cmdqueryname=node-id) *node-id*
   
   
   
   A node ID is configured.
4. Run [**work-mode**](cmdqueryname=work-mode) [ **mcp** | **dcp** | **auto** ]
   
   
   
   An IFIT working mode is configured, and its view is displayed.
5. Run [**service-type**](cmdqueryname=service-type) **srv6-segment-list**
   
   
   
   The service type for IFIT measurement is set to SRv6 TE Policy.
6. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the IFIT view.
7. (Optional) Run [**dynamic-flow age interval-multiplier**](cmdqueryname=dynamic-flow+age+interval-multiplier) *multi-value*
   
   
   
   The aging time of dynamic IFIT flows is set.
8. (Optional) Run [**reset dynamic**](cmdqueryname=reset+dynamic) **flow** { *flowId* | **all** }
   
   
   
   All dynamic IFIT flows or a specific one is cleared.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

* Run the [**display ifit**](cmdqueryname=display+ifit) command to check information about IFIT flows.
* Run the [**display ifit dynamic-hop**](cmdqueryname=display+ifit+dynamic-hop) [ **flow-id** *flow-id* ] command to check information about dynamic IFIT flows on transit and egress nodes.
* Run the [**display ifit srv6-segment-list**](cmdqueryname=display+ifit+srv6-segment-list) [ *segment-list-id* ] command to check SRv6 TE Policy instance information.
* Run the [**display ifit statistic-type**](cmdqueryname=display+ifit+statistic-type) { **one-way-delay** | **two-way-delay** | **one-way-loss** } { **srv6-segment-list** *segment-list-id* | **flow-id** *flowId* } command to check original performance statistics on the MCP.
* Run the [**display license resource usage ifit all**](cmdqueryname=display+license+resource+usage+ifit+all) command to check the usage of IFIT license resources.
* Run the [**display ifit resource**](cmdqueryname=display+ifit+resource) [ **per-packet-delay** ] command to check the resource usage of IFIT flows.

#### Follow-up Procedure

After the preceding configuration is complete, the IFIT measurement result is reported to the SPR module to facilitate intelligent traffic steering. For details, see [Configuring TE-Class-based Traffic Steering into an SRv6 TE Policy](dc_vrp_srv6_cfg_all_0294.html).
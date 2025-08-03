(Optional) Configuring Association Between ERPS and Ethernet CFM
================================================================

Association between Ethernet CFM and ERPS on an ERPS ring port helps promptly detect failures, converge topologies, and shorten the traffic interruption time. Currently, ERPS can be associated only with outward-facing MEPs.

#### Prerequisites

Ethernet CFM has been configured on an ERPS ring port. For details, see [CFM Configuration](dc_vrp_cfm_cfg_000001.html).


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The interface view is displayed.
3. Run [**erps ring**](cmdqueryname=erps+ring) *ring-id* [**track cfm**](cmdqueryname=track+cfm) **md** *md-name* **ma** *ma-name* **mep** *mep-id* **remote-mep** *rmep-id*
   
   
   
   ERPS is associated with Ethernet CFM to promptly detect link failures.
   
   The association between ERPS and CFM takes effect only when the interface has ERPS associated with CFM and has an interface-based MEP created using the [**mep mep-id**](cmdqueryname=mep+mep-id) command.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Follow-up Procedure

After ERPS is associated with Ethernet CFM, ensure that the maintenance entity group level (MEL) in R-APS PDUs on ERPS rings is higher than that in CFM protocol packets. Otherwise, Ethernet CFM cannot allow R-APS PDUs to pass through. When ERPS is used for communication between Huawei and non-Huawei devices, the same MEL also allows them to communicate smoothly.

You can run the [**raps-mel**](cmdqueryname=raps-mel) *level-id* command in the ERPS ring view to set the MEL in R-APS PDUs.
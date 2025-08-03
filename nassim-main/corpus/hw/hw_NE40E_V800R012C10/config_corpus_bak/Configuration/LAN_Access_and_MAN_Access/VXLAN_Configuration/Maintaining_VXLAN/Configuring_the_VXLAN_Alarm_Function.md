Configuring the VXLAN Alarm Function
====================================

To learn the VXLAN operating status in time, configure the VXLAN alarm function so that the NMS will be notified of the VXLAN status changes. This facilitates O&M.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**snmp-agent trap enable feature-name**](cmdqueryname=snmp-agent+trap+enable+feature-name) **nvo3** [ **trap-name** { **hwnvo3vxlantnldown** | **hwnvo3vxlantnlup** } ]
   
   
   
   The VXLAN alarm function is enabled.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After the VXLAN alarm function is enabled, check the VXLAN alarm status.

Run the [**display snmp-agent trap feature-name**](cmdqueryname=display+snmp-agent+trap+feature-name) **nvo3 all** command to check configurations of all alarm functions of the VXLAN module.
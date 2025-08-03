Configuring the Alarm Function for the Sharp Decrease in the Number of Multicast (S, G) Entries
===============================================================================================

Configuring the Alarm Function for the Sharp Decrease in the Number of Multicast (S, G) Entries

#### Context

To enable the device to generate an alarm for the sharp decrease in the number of multicast entries when traffic is interrupted, you can configure the alarm function. If the number of (S, G) entries decreased sharply within a specified period reaches the configured threshold, an hwPimSGInactiveThreshold alarm is generated.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**pim-ipv6**](cmdqueryname=pim-ipv6) [ **vpn-instance** *vpn-instance-name* ]
   
   
   
   The IPv6 PIM view or VPN instance IPv6 PIM view is displayed.
3. Run [**source-inactive alarm-threshold**](cmdqueryname=source-inactive+alarm-threshold) **time** *alarm-interval* **number** *inactive-threshold*
   
   
   
   The alarm function is configured for the sharp decrease in the number of multicast (S, G) entries. An alarm is generated when the number of entries decreased within a specified period reaches a specified threshold.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
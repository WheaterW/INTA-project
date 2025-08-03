Enabling IP Traffic Monitoring
==============================

Enabling IP Traffic Monitoring

#### Context

On an IP RAN, if a fault occurs (for example, a base station is disconnected or IP service traffic is interrupted), the fault has to be diagnosed based on collaborative information between routers and wireless controllers or base stations. IP traffic monitoring helps quickly diagnose faults, improving O&M efficiency.

IP traffic monitoring implements automatic traffic statistics based on IP addresses. After this function is enabled, you can create an IP service flow table, collect statistics on the number of IP packets, and store the statistics to a CF card periodically. You can use a tool to parse a stored file and display its content in graphics, quickly locating faulty nodes.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run **[**service-stream table**](cmdqueryname=service-stream+table) **sip**** **source-ip** ****dip**** **destination-ip** [ ****vpn-instance**** **vpn-name** ]
   
   
   
   IP traffic monitoring is enabled.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
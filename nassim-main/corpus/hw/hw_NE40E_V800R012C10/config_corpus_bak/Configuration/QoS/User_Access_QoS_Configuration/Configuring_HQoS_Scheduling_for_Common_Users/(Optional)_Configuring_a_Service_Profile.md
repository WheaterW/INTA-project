(Optional) Configuring a Service Profile
========================================

You can configure a network header length in a service profile to compensate a processed packet with the length, precisely controlling traffic.

#### Context

The length of user packets varies according to the processing mode of the scheduling module, which affects the accuracy of traffic shaping. In this case, you can configure a network header length in a service profile to compensate a processed packet with the length, improving the accuracy of traffic shaping.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**service-template**](cmdqueryname=service-template) *service-template-name*
   
   
   
   The service profile view is displayed.
3. Run [**network-header-length**](cmdqueryname=network-header-length) *network-header-length* { **inbound** | **outbound** }
   
   
   
   A network header length is configured for the service profile.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   To specify network header lengths for both non-eTM and eTM subcards, you must configure them separately in the global service profile. The detailed operations are as follows:
   
   * Run the **[**network-header-length**](cmdqueryname=network-header-length)** *network-header-length* **outbound** command in the service profile view to configure a network header length for the service profile. After the service profile is applied to a QoS profile, the network header length takes effect on a non-eTM subcard in the outbound direction.
   * Run the **[**network-header-length**](cmdqueryname=network-header-length)** *network-header-length* **outbound** command in the service profile view to configure a network header length for the service profile. After the service profile is applied to a QoS profile and the **adjust-on-card** parameter is specified to make the service profile take effect on an eTM subcard, the network header length takes effect on an eTM subcard in the outbound direction.
   * Run the [**network-header-length**](cmdqueryname=network-header-length) *network-header-length* **outbound** **adjust-on-etm** command in the service profile view to configure a network header length in the service profile and make it take effect on an eTM subcard. After the service profile is applied to a QoS profile, the network header length takes effect on an eTM subcard in the outbound direction.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
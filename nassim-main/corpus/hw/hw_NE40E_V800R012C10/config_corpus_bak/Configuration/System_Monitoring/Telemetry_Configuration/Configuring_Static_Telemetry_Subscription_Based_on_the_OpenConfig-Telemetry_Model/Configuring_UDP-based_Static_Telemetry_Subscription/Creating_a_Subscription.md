Creating a Subscription
=======================

When configuring static telemetry subscription to the sampled data, you need to create a subscription to associate the configured destination group with the configured sampling sensor group so that data can be sent to the collector.

#### Context

A device functions as a client, and a collector functions as a server. To statically subscribe to the sampled data, you need to create a subscription to set up a data sending channel. The protocol used to send data can be gRPC or UDP. The following uses UDP as an example.

Before configuring an SSL policy on the client to establish a secure SSL connection between the client and server, ensure that the SSL policy has been created. For details about how to create an SSL policy, see "Configuring and Binding an SSL Policy" in *HUAWEI NE40E-M2 series Product Documentation* > Configuration > Basic Configuration > Accessing Other Devices Configuration.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**telemetry**](cmdqueryname=telemetry) [ **openconfig** ]
   
   
   
   The telemetry view is displayed.
3. (Optional) Run [**protocol udp message-header ietf-netconf-udp-notif**](cmdqueryname=protocol+udp+message-header+ietf-netconf-udp-notif)
   
   
   
   The UDP header in the draft-ietf-netconf-udp-notif-08 format is used.
4. Run [**subscription**](cmdqueryname=subscription) *subscription-name*
   
   
   
   A subscription is created to associate a destination group with a sampling sensor group, and the subscription view is displayed.
5. Run [**sensor-group**](cmdqueryname=sensor-group) *sensor-name* [ **sample-interval** *sample-interval* { [ **suppress-redundant** ] | [ **heartbeat-interval** *heartbeat-interval* ] } \* ]
   
   
   
   A sampling sensor group is associated with the subscription, and a sampling interval, a heartbeat interval, and redundancy suppression are configured for the sampling sensor group.
6. Run [**destination-group**](cmdqueryname=destination-group) *destination-name*
   
   
   
   A destination group is associated with the subscription.
7. (Optional) Run the following commands to configure telemetry adaptive sampling:
   1. Run the [**sensor-group**](cmdqueryname=sensor-group) *sensor-group-name* [**sample-adaptive**](cmdqueryname=sample-adaptive) command to configure a sampling sensor group that requires adaptive sampling, and enter the sample-adaptive view.
   2. Run the [**sample-interval**](cmdqueryname=sample-interval) *interval* **op-field** *field* **op-type** { **eq** | **gt** | **ge** | **lt** | **le** } **op-value** *value* command to configure an interval and conditions for adaptive sampling
   3. Run the [**quit**](cmdqueryname=quit) command to return to the subscription view.
   
   
   
   Generally, a small sampling interval is set for an analyzer to obtain more accurate data for analysis. However, a large amount of redundant data is generated when a small sampling interval is used. The data requires a large amount of storage space and is inconvenient for data management. If adaptive sampling is configured, telemetry dynamically adjusts the sampling interval based on preset conditions. When the monitoring indicators are normal, telemetry reduces the sampling interval. When the monitoring indicators reach the threshold, telemetry automatically adjusts the sampling interval based on the configuration to report collected data at a higher frequency, reducing the amount of data on the analyzer.
8. Run [**protocol**](cmdqueryname=protocol) **udp**
   
   
   
   A protocol and encryption mode are configured for sending data to the destination collector that is associated with this subscription.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) Both this command and the [**ipv4-address port**](cmdqueryname=ipv4-address+port)/[**ipv6-address port**](cmdqueryname=ipv6-address+port) command in the destination group view can configure a protocol and encryption mode for sending data to the destination collector. If the destination collector is associated with the subscription, command configurations take effect based on the following rules:
   * If this command has been run, the protocol and encryption mode configured using this command in the subscription view take effect.
   * If this command is not run, the protocol and encryption mode configured using the [**ipv4-address port**](cmdqueryname=ipv4-address+port)/[**ipv6-address port**](cmdqueryname=ipv6-address+port) command in the destination group view take effect.
9. (Optional) Run [**dampening-interval**](cmdqueryname=dampening-interval) *interval*
   
   
   
   A dampening interval is configured for the subscription.
10. (Optional) Run [**resync-interval**](cmdqueryname=resync-interval) *interval*
    
    
    
    A full data reporting interval is configured.
    
    
    
    By default, no full data reporting interval is configured.
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    The dampening interval and full data reporting interval apply only to sampling of the OnChange+ type. If a non-zero sampling interval is configured using the [**sample-interval**](cmdqueryname=sample-interval) command, the dampening interval and full data reporting interval cannot be configured.
11. (Optional) Based on the collector type, run either of the following commands to configure a source IP address for UDP-based data sending:
    
    
    * For an IPv4 collector, run the [**local-source-address ipv4**](cmdqueryname=local-source-address+ipv4) *ipv4-address* [ [**port**](cmdqueryname=port) *port-value* ] command.
    * For an IPv6 collector, run the [**local-source-address ipv6**](cmdqueryname=local-source-address+ipv6) *ipv6-address* [ [**port**](cmdqueryname=port) *port-value6* ] command.
12. (Optional) Run [**local-source-interface**](cmdqueryname=local-source-interface) { *if-name* | *if-type* *if-number* } [ [**port**](cmdqueryname=port) *port-value*
    
    
    
    A source interface and source port are configured for UDP-based data sending.
    
    
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    In the same subscription view, either the source interface or the source IP address can be configured for the packets to be sent.
13. (Optional) Run [**dscp**](cmdqueryname=dscp) *value*
    
    
    
    A DSCP value is set for data packets to be sent.
14. (Optional) Run [**encoding**](cmdqueryname=encoding) { **json** | **gpb** }
    
    
    
    An encoding format is configured for data packets to be sent.
15. (Optional) Run [**anchor-time**](cmdqueryname=anchor-time) *anchortime-value*
    
    
    
    The anchor time for periodically sampling data packets to be sent is configured.
16. Run [**quit**](cmdqueryname=quit)
    
    
    
    Return to the telemetry view.
17. (Optional) Run [**cpu-usage max-percent**](cmdqueryname=cpu-usage+max-percent) *usage*
    
    
    
    A maximum usage is configured for the amount of CPU resources the main control board occupies when telemetry collects data.
    
    
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    This command is supported only by the admin VS.
18. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.
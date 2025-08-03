Creating a Static Subscription
==============================

Creating a Static Subscription

#### Prerequisites

Before configuring gRPC in dial-out mode, you have completed the following tasks:

Create an SSL policy if you need to create an SSL connection between the server and client. For details about how to create an SSL policy, see "SSL Configuration" in Configuration Guide > Security Configuration.


#### Context

When configuring static subscription to collect sampled data, you need to create a sampling sensor group and specify a sampling path and filter criteria. When the sampling path meets the filter criteria, the device reports sampled data to the collector for service policy determination.


#### Procedure

1. Create a subscription.
   1. Enter the system view.
      
      
      ```
      [system-view](cmdqueryname=system-view)
      ```
   2. Enter the telemetry view.
      
      
      ```
      [telemetry](cmdqueryname=telemetry) [ openconfig ]
      ```
   3. (Optional) Configure the format of the UDP header.
      
      
      ```
      protocol udp message-header ietf-netconf-udp-notif
      ```
      
      By default, telemetry uses the UDP header in draft-ietf-netconf-udp-pub-channel format. You can run this command to switch the format to draft-ietf-netconf-udp-notif-08 as required.
   4. Create a subscription for associating a destination group and a sampling sensor group, and enter the subscription view.
      
      
      ```
      [subscription](cmdqueryname=subscription) subscription-name
      ```
   5. Associate the subscription with a destination group.
      
      
      ```
      [destination-group](cmdqueryname=destination-group) destination-name
      ```
   6. Associate the subscription with a sampling sensor group, and configure a sampling interval, redundancy suppression, and a heartbeat interval for the sampling sensor group.
      
      
      ```
      [sensor-group](cmdqueryname=sensor-group) sensor-name [ sample-interval sample-interval { [ suppress-redundant ] | [ heartbeat-interval heartbeat-interval ] } * ]
      ```
      ![](public_sys-resources/note_3.0-en-us.png) 
      * When the sampling path type is alarm, the sampling interval, redundancy suppression, and heartbeat interval configurations do not take effect.
      * When the sampling type is OnChange or OnChange+, the sampling interval takes effect only when it is set to 0 ms. The redundancy suppression and heartbeat interval configurations are mutually exclusive with the OnChange or OnChange+ sampling.
      * When the sampling type is OnChange or OnChange+:
        + If the configured sampling interval is 0, sampling is performed immediately in OnChange sampling, and incremental sampling is performed in OnChange+ sampling.
        + If the configured sampling interval is not 0 and the service supports periodic sampling, the larger value between the configured sampling interval and the minimum sampling interval takes effect.
      * When the sampling interval is set to 0 ms, periodic sampling and user-defined sampling do not take effect.
      * You can run the [**display telemetry sensor-path**](cmdqueryname=display+telemetry+sensor-path) command to check the sampling paths and types supported by the device.
2. (Optional) Configure telemetry adaptive sampling.
   
   
   
   Generally, a small sampling interval is set for an analyzer to obtain more accurate data for analysis. However, a large amount of redundant data is generated when a small sampling interval is used. The data requires a large amount of storage space and is inconvenient for data management. If adaptive sampling is configured, telemetry dynamically adjusts the sampling interval based on preset conditions. When the monitoring indicators are normal, telemetry reduces the sampling interval. When the monitoring indicators reach the threshold, telemetry automatically adjusts the sampling interval based on the configuration to report collected data at a higher frequency, reducing the amount of data on the analyzer.
   
   
   
   1. Configure a sampling sensor group that requires adaptive sampling, and enter the sample-adaptive view.
      
      
      ```
      [sensor-group](cmdqueryname=sensor-group) sensor-group-name sample-adaptive
      ```
      ![](public_sys-resources/note_3.0-en-us.png) 
      
      Adaptive sampling can be configured only when the sampling sensor group meets the following conditions:
      
      1. The group has only one sampling path, and the path is a container or list that contains leaf nodes and cannot be a pure container node.
      2. The type of the sampling path in the group is not OnChange, Alarm, or Event.
      3. The minimum sampling interval of the sampling path in the group is greater than or equal to 1000 ms.
   2. Configure the sampling interval and conditions for adaptive sampling.
      
      
      ```
      [sample-interval](cmdqueryname=sample-interval) interval op-field field op-type { eq | gt | ge | lt | le } op-value value
      ```
      
      By default, adaptive sampling is not configured.
      
      When adaptive sampling conditions are met, the device samples data based on the specified sampling interval. If the command is run multiple times, only the latest configuration takes effect.
3. (Optional) Configure information about the protocol for the destination collector associated with this subscription.
   1. Configure the protocol and encryption mode for the destination collector.
      
      
      ```
      [protocol](cmdqueryname=protocol) { grpc [ no-tls ] [ compression gzip ] | udp }
      ```
      
      By default, no protocol and encryption mode are configured for the destination collector that is associated with this subscription.
      
      ![](public_sys-resources/note_3.0-en-us.png) Both this command and the [**ipv4-address port**](cmdqueryname=ipv4-address+port) command in the destination group view can configure a protocol and encryption mode for the destination collector. If the destination collector is associated with a subscription, command configurations take effect based on the following rules:
      * If this command has been run, the encryption mode configured using this command in the subscription view takes effect.
      * If this command has not been run, the encryption mode configured using the [**ipv4-address port**](cmdqueryname=ipv4-address+port) command in the destination group view takes effect.
   2. Configure the source IP address for the packets to be reported.
      
      
      * Run the following command if the source IP address is an IPv4 address:
        ```
        [local-source-address ipv4](cmdqueryname=local-source-address+ipv4) ipv4-address [ [port](cmdqueryname=port) port-value ]
        ```
      * Run the following command if the source IP address is an IPv6 address:
        ```
        [local-source-address ipv6](cmdqueryname=local-source-address+ipv6) ipv6-address [ [port](cmdqueryname=port) port-value6 ]
        ```
      
      
      
      By default, the source IP address is the IP address of the route's outbound interface, and the port number is randomly allocated.
   3. Configure the source interface for the packets to be reported.
      
      
      ```
      [local-source-interface](cmdqueryname=local-source-interface) { if-name | if-type if-number } [ [port](cmdqueryname=port) port-value ]
      ```
      
      By default, no source interface is configured for the packets to be reported.
      
      ![](public_sys-resources/note_3.0-en-us.png) 
      
      In the same subscription view, only the source interface or source IP address can be configured for the packets to be reported.
      
      In different subscription views, only two types of source interfaces and source IP addresses can be configured for the packets to be reported. If the same source interface or source IP address is configured for the packets to be reported in different subscription views, the system considers that the configurations are of the same type.
   4. (Optional) Set the DSCP value in the packets to be reported.
      
      
      ```
      [dscp](cmdqueryname=dscp) value
      ```
      
      By default, the DSCP value in the packets to be reported is 0.
4. (Optional) Configure the encoding format for the packets to be reported.
   
   
   ```
   [encoding](cmdqueryname=encoding) { json | gpb }
   ```
   
   By default, the encoding format of the packets to be reported is GPB.
5. (Optional) Configure the telemetry layer and service data layer of the to-be-reported packets to use the GPB and JSON encoding formats respectively when a static subscription uses the JSON encoding format.
   
   
   1. Return to the telemetry view.
      ```
      [quit](cmdqueryname=quit)
      ```
   2. Configure the telemetry layer and service data layer of the to-be-reported packets to use the GPB and JSON encoding formats respectively when a static subscription uses the JSON encoding format.
      ```
      [json only-content](cmdqueryname=json+only-content)
      ```
      
      By default, when a static subscription uses the JSON encoding format, both the telemetry layer and service data layer of the to-be-reported packets use the JSON encoding format.
6. (Optional) Configure the maximum usage of CPU resources used for telemetry data sampling.
   
   
   ```
   [cpu-usage max-percent](cmdqueryname=cpu-usage+max-percent) usage
   ```
   
   By default, telemetry data sampling can occupy at most 5% of the CPU resources.
7. (Optional) Specify the maximum size of a packet sent by telemetry through UDP.
   
   
   ```
   [protocol udp packet-max-size](cmdqueryname=protocol+udp+packet-max-size) size
   ```
   
   By default, the value is 0, indicating that the maximum size of a UDP packet is not limited.
8. (Optional) Configure the client to combine multiple data packets into one data packet when sending packets.
   
   
   ```
   [pack enable](cmdqueryname=pack+enable)
   ```
   
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   When the transport protocol is UDP, the device does not support the [**pack enable**](cmdqueryname=pack+enable) command.
   
   After telemetry adaptive sampling is configured, the combined packet sending interval is still the same as the sampling interval specified before adaptive sampling is configured.
   
   If the same subscription has different sampling intervals, the longest one is used as the combined packet sending interval. If the sampling interval is 0, the combined packet sending interval is 1 second.
9. (Optional) Configure an SSL policy for the client or enable the client to perform SSL verification on the server.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The certificate to be loaded must be supported by both the client and server.
   
   
   
   1. Return to the system view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
   2. Enter the gRPC view.
      
      
      ```
      [grpc](cmdqueryname=grpc)
      ```
   3. Enter the gRPC client view.
      
      
      ```
      [grpc client](cmdqueryname=grpc+client)
      ```
   4. (Optional) Configure the gRPC client to perform SSL verification on the gRPC server.
      
      
      ```
      [ssl-verify peer](cmdqueryname=ssl-verify+peer)
      ```
      
      By default, a server does not perform SSL verification on a client.
      
      ![](public_sys-resources/note_3.0-en-us.png) 
      
      If the **no-tls** parameter has been configured in the [**ipv4-address port**](cmdqueryname=ipv4-address+port) or [**protocol**](cmdqueryname=protocol) command (subscription view) and taken effect, the TLS encryption mode is not used. In this case, the client-specific SSL policy configured using this command does not take effect.
   5. (Optional) Configure an SSL policy for the gRPC client.
      
      
      ```
      [ssl-policy](cmdqueryname=ssl-policy) ssl-policy-name [ [verify-san](cmdqueryname=verify-san) san ]
      ```
      
      By default, no SSL policy is configured for a client.
      
      
      
      ![](public_sys-resources/note_3.0-en-us.png) 
      
      If the **no-tls** parameter has been configured in the [**ipv4-address port**](cmdqueryname=ipv4-address+port) or [**protocol**](cmdqueryname=protocol) command (subscription view) and taken effect, the TLS encryption mode is not used. In this case, the configuration that enables the client to perform SSL verification on a server does not take effect.
10. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```

#### Verifying the Configuration

* Run the [**display telemetry subscription**](cmdqueryname=display+telemetry+subscription) [ *subscription-name* ]command to check subscription information.
* Run the [**display telemetry destination**](cmdqueryname=display+telemetry+destination) [ *dest-name* ] command to check information about the destination group.
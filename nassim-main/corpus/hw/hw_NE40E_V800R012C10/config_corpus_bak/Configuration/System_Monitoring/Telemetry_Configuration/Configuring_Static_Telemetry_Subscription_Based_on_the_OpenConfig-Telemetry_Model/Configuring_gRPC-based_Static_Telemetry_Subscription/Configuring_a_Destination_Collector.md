Configuring a Destination Collector
===================================

When configuring a static telemetry subscription to the sampled data or a customized event, you need to create a destination group and specify a destination collector to which the data is sent.

#### Context

A device functions as a client, and a collector functions as a server. To statically subscribe to the sampled data or a customized event, you need to configure an IP address and port number for a destination collector, and configure a protocol and encryption mode for sending data to the destination collector.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**telemetry**](cmdqueryname=telemetry) [ **openconfig** ]
   
   
   
   The telemetry view is displayed.
3. Run [**destination-group**](cmdqueryname=destination-group) *destination-group-name*
   
   
   
   A destination group to which the data sampled is sent is created, and the destination group view is displayed.
4. Based on the collector type, run either of the following commands to configure an IP address and port number for the destination collector, and configure a protocol and encryption mode for sending data to the destination collector:
   
   
   * For an IPv4 collector, run the [**ipv4-address**](cmdqueryname=ipv4-address) *ip-address-ipv4* **port** *port* [ **vpn-instance** *vpn-instance* ] [ **protocol** **grpc** [ **no-tls** ] [ **compression** **gzip** ]] command.
   * For an IPv6 collector, run the [**ipv6-address**](cmdqueryname=ipv6-address)**ip-address-ipv6** **port** *port* [ **vpn-instance** *vpn-instance* ] [ **protocol** **grpc** [ **no-tls** ] [ **compression** **gzip** ]] command.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * This command can be run for no more than five times for each destination group.
   * Both this command and the [**protocol**](cmdqueryname=protocol) command in the subscription view can configure a protocol and encryption mode for sending data to the destination collector. If the destination collector is associated with the subscription, command configurations take effect based on the following rules:
     + If the [**protocol**](cmdqueryname=protocol) command has been run in the subscription view, the protocol and encryption mode configured in the subscription view take effect.
     + If the [**protocol**](cmdqueryname=protocol) command is not run in the subscription view, the protocol and encryption mode configured in the destination group view take effect.
     + Configuring **no-tls** may pose security risks.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
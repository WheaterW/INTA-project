Configuring a Destination Collector
===================================

When configuring a static telemetry subscription to the sampled data based on the YANG-Push model, you need to create a receiver for the sampled data.

#### Context

A device functions as a client, and a collector functions as a server. To statically subscribe to the sampled data through the YANG-Push model, you need to configure the IP address and port number of the receiver for the sampled data and configure the fragmentation capability for the receiver.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**telemetry ietf**](cmdqueryname=telemetry+ietf)
   
   
   
   The telemetry IETF view is displayed.
3. Run [**receiver**](cmdqueryname=receiver) *receiver-name*
   
   
   
   A receiver for the sampled data is created, and the telemetry IETF receiver view is displayed.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   A maximum of five receivers can be associated with each VS using this command.
4. Based on the collector type, run either of the following commands to configure an IP address and a port number for sending data to the destination collector:
   
   
   * For an IPv4 collector, run the [**ipv4-address**](cmdqueryname=ipv4-address) *ipv4-addr* **port** *port-number* command.
   * For an IPv6 collector, run the [**ipv6-address**](cmdqueryname=ipv6-address)**ipv6-addr** **port** *port-number* command.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * Each receiver can be configured with only one IP address and one port number, and the latest configuration overrides the previous one.
   * For each two receivers, their IP addresses, port numbers, or both must be different.
5. (Optional) Run [**fragment enable**](cmdqueryname=fragment+enable)
   
   
   
   Fragmentation is enabled on the receiver.
6. (Optional) Run [**fragment max-size**](cmdqueryname=fragment+max-size)*size*
   
   
   
   The size of each fragment is set for the receiver.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
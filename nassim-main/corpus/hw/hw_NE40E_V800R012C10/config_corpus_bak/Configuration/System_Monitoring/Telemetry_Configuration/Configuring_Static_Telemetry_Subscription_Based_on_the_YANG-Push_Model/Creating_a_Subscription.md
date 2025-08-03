Creating a Subscription
=======================

When configuring a static telemetry subscription to the sampled data based on the YANG-Push model, you need to create a subscription to associate the configured receiver with the configured sampling filter so that data can be sent to the sampling filter.

#### Context

A device functions as a client, and a collector functions as a server. To statically subscribe to the sampled data through the YANG-Push model, you need to create a subscription to set up a data sending channel. Only UDP can be used as the protocol for data reporting.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**telemetry ietf**](cmdqueryname=telemetry+ietf)
   
   
   
   The telemetry IETF view is displayed.
3. Run [**subscription**](cmdqueryname=subscription) *subscription-id*
   
   
   
   A subscription is created to associate a receiver with a sampling filter, and the subscription view is displayed.
4. Run [**transport udp-notif**](cmdqueryname=transport+udp-notif)
   
   
   
   The transport protocol is set to UDP-NOTIF for the receiver associated with the subscription.
5. Run [**encoding json**](cmdqueryname=encoding+json)
   
   
   
   The encoding format is set to JSON\_IETF for the data packets to be sent.
6. (Optional) Run [**distribute enable**](cmdqueryname=distribute+enable)
   
   
   
   The data reporting mode is set to distributed for the telemetry IETF subscription.
7. (Optional) Run [**collect-depth**](cmdqueryname=collect-depth) *depth*
   
   
   
   A sampling depth is configured for the subscription.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * When the data reporting mode is set to distributed, the default sampling depth is 1. The sampling depth can be configured in the range from 1 to 3. If the configured sampling depth differs from the maximum value supported by services, the smaller of the two values takes effect.
   * If the data reporting mode is not set to distributed, data of all nodes along the specified path is collected by default. The sampling depth can be configured in the range from 1 to 3.
8. (Optional) Run [**purpose**](cmdqueryname=purpose) *purpose-string*
   
   
   
   A description is configured for the subscription.
9. (Optional) Configure a source address for the packets to be sent using either of the following methods:
   
   
   * Configure a source IP address and bound VPN instance for the packets to be sent.
     + If the source IP address of the packets to be sent is an IPv4 address, run the [**local-source-address**](cmdqueryname=local-source-address) { *ipv4-address* | [**vpn-instance**](cmdqueryname=vpn-instance) vpn-value} command.
     + If the source IP address of the packets to be sent is an IPv6 address, run the [**local-source-address**](cmdqueryname=local-source-address) { **ipv6** *ipv6-address* | [**vpn-instance**](cmdqueryname=vpn-instance) vpn-value} command.
   * Run the [**local-source-interface**](cmdqueryname=local-source-interface) { *if-name* | *if-type* *if-number* } command to configure a source interface for the packets to be sent.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The configured source interface must have an IPv4 address.
10. Run [**update-trigger**](cmdqueryname=update-trigger) { **period***period-value* | **on-change** [ **dampening-period***dampening-period-value* ]}
    
    
    
    A sampling interval for periodic sampling and a suppression period for OnChange sampling are configured.
11. Run [**filter**](cmdqueryname=filter) *name* [**type**](cmdqueryname=type) [**datastore**](cmdqueryname=datastore)
    
    
    
    The subscription is associated with a sampling filter of the dataset type.
12. (Optional) Run [**dscp**](cmdqueryname=dscp) *dscp-value*
    
    
    
    A DSCP value is set for the data packets to be sent.
13. Run [**receiver**](cmdqueryname=receiver) *name*
    
    
    
    A receiver is created in the subscription, and the telemetry IETF receiver view is displayed.
14. Run [**bind-receiver**](cmdqueryname=bind-receiver)*name*
    
    
    
    The subscription is associated with the receiver in the telemetry IETF view.
    
    
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    This command can be run to associate the subscription with only one receiver.
15. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.
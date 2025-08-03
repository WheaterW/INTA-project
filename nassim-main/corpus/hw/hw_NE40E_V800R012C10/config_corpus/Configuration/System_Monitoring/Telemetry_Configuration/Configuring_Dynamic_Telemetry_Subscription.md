Configuring Dynamic Telemetry Subscription
==========================================

In dynamic telemetry subscription, a collector functioning as a client initiates a connection to a device functioning as a server, and the device collects and reports data.

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The dynamic subscription capability based on the YANG-Push model is provided by NETCONF. For details, see "YANG Push" in *HUAWEI NE40E-M2 series Product Documentation*  > Feature Description > System Management > NETCONF Description. The following configuration process about dynamic telemetry subscription is based on the OpenConfig model.

A collector functioning as a client initiates a connection to a device functioning as a server. To dynamically subscribe to the sampled data, you need to configure the source IP address and number of the port to be listened for, and enable the gRPC service. gRPC can be used as the protocol to send data.

If the connection where dynamic telemetry subscription resides is interrupted, the device automatically cancels the subscription and stops data sampling and reporting. The configuration cannot be restored unless the collector sends a connection request again. For example, if a user wants to monitor an interface for a period of time, dynamic telemetry subscription can be configured. To stop monitoring, tear down the connection. The subscription is automatically canceled and cannot be restored. This avoids long-term loads on devices and simplifies the interaction between users and devices.


#### Pre-configuration Tasks

Before configuring dynamic telemetry subscription, complete the following tasks:

* Configure a dynamic routing protocol or static routes to ensure that devices can communicate at the network layer.
* Create a local user, add the user to the administrator group, and configure the service type of the user.
* Create an ACL if it is needed for the gRPC service to control which clients can connect to the server. For details about how to create an ACL, see "ACL Configuration" in Configuration Guide > IP Services.
* Create an SSL policy if it is needed for the gRPC service so that a secure SSL connection can be established between the server and client. For details about how to create an SSL policy, see "Configuring and Binding an SSL Policy" in *Configuration Guide > Basic Configuration > Accessing Other Devices Configuration*.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**grpc**](cmdqueryname=grpc)
   
   
   
   The gRPC view is displayed.
3. (Optional) Based on the collector type, run either of the following commands to enter the corresponding server view:
   
   
   * For an IPv4 collector, run the [**grpc server**](cmdqueryname=grpc+server) command to enter the gRPC server view.
   * For an IPv6 collector, run the [**grpc server ipv6**](cmdqueryname=grpc+server+ipv6) command to enter the gRPC IPv6 server view.
4. Run [**source-ip**](cmdqueryname=source-ip) *ip-address* [ **vpn-instance** *vpn-instance-name* ]
   
   
   
   The source IP address to be listened for during dynamic telemetry subscription is configured.
5. (Optional) Run [**compression gzip**](cmdqueryname=compression+gzip)
   
   
   
   The gRPC server is configured to transmit data in gzip compression mode.
6. (Optional) Run [**server-port**](cmdqueryname=server-port) *port-number*
   
   
   
   The number of the port to be listened for during dynamic telemetry subscription is set.
7. (Optional) Run [**acl**](cmdqueryname=acl) { *acl-name* | *acl-number* }
   
   
   
   An ACL is configured for the gRPC service during dynamic telemetry subscription.
8. (Optional) Run [**idle-timeout**](cmdqueryname=idle-timeout) *time*
   
   
   
   An idle timeout period is configured for the gRPC service during dynamic telemetry subscription.
9. (Optional) Run [**ssl-policy**](cmdqueryname=ssl-policy) *ssl-policy-name*
   
   
   
   An SSL policy is configured for the gRPC service during dynamic telemetry subscription.
10. (Optional) Run [**ssl-verify peer**](cmdqueryname=ssl-verify+peer)
    
    
    
    The server is configured to perform SSL verification on a client during dynamic telemetry subscription.
11. (Optional) Run [**dscp**](cmdqueryname=dscp) *value*
    
    
    
    A DSCP value is set for data packets to be sent.
12. Run [**server enable**](cmdqueryname=server+enable)
    
    
    
    The gRPC service is enabled.
13. (Optional) Configure a maximum usage for the main control board's CPU used when telemetry collects data.
    
    
    1. Run [**quit**](cmdqueryname=quit)
       
       Return to the gRPC view.
    2. Run [**quit**](cmdqueryname=quit)
       
       Return to the system view.
    3. Run [**telemetry**](cmdqueryname=telemetry) [ **openconfig** ]
       
       The telemetry view is displayed.
    4. Run [**cpu-usage max-percent**](cmdqueryname=cpu-usage+max-percent) *usage*
       
       A maximum usage is configured for the amount of CPU resources the main control board occupies when telemetry collects data.![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    This command is supported only by the admin VS.
14. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.

#### Verifying the Configuration

After the preceding configurations are performed and the collector delivers the sampled data, verify the configuration.

Run the [**display telemetry dynamic-subscription**](cmdqueryname=display+telemetry+dynamic-subscription) [ *subName* ] command to check the dynamic subscription information.
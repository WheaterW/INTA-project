Configuring and Querying Data Using gRPC
========================================

You can configure and query data using gRPC.

#### Prerequisites

* The route between the device and NMS is reachable.
* The user configuration is correct, the user has been added to the administrator group, and the service type is HTTP.
* An ACL has been created if it is needed for the gRPC service to control which clients can connect to the server. For details about how to create an ACL, see "ACL Configuration" in Configuration > IP Services.
* An SSL policy has been created and bound to the gRPC service so that a secure SSL connection can be established between the server and client. For details about how to create an SSL policy, see "Configuring and Binding an SSL Policy" in Configuration > Basic Configuration.

#### Context

In dial-in mode where the device functions as the gRPC server and the collector functions as the gRPC client, you can configure and query data through gRPC.

For details about how to subscribe to data using gRPC, see telemetry subscription sections.


#### Procedure

1. Run **[**system-view**](cmdqueryname=system-view)**
   
   
   
   The system view is displayed.
2. Run **[**grpc**](cmdqueryname=grpc)**
   
   
   
   The gRPC view is displayed.
3. Run either of the following commands as required to enter the server view:
   
   
   * On an IPv4 network, run the [**grpc server**](cmdqueryname=grpc+server) command to enter the gRPC server view.
   * On an IPv6 network, run the [**grpc server ipv6**](cmdqueryname=grpc+server+ipv6) command to enter the gRPC IPv6 server view.
4. Run [**source-ip**](cmdqueryname=source-ip) *ip-address* [ **vpn-instance** *vpn-instance-name* ]
   
   
   
   The source IP address to be listened for is configured.
5. (Optional) Run [**server-port**](cmdqueryname=server-port) *port-number*
   
   
   
   The number of the port to be listened for is configured.
6. (Optional) Run [**acl**](cmdqueryname=acl) { *acl-name* | *acl-number* }
   
   
   
   An ACL is configured for the gRPC service.
7. (Optional) Run [**idle-timeout**](cmdqueryname=idle-timeout) *time*
   
   
   
   An idle timeout period is configured for the gRPC service.
8. Run [**ssl-policy**](cmdqueryname=ssl-policy) *ssl-policy-name*
   
   
   
   An SSL policy is configured for the gRPC service.
9. (Optional) Run [**ssl-verify peer**](cmdqueryname=ssl-verify+peer)
   
   
   
   The server is configured to perform SSL verification on the client.
10. (Optional) Run [**permit no-tls**](cmdqueryname=permit+no-tls) { **gnmi** }
    
    
    
    Selected services are allowed to run over an unencrypted gRPC channel.
    
    
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    * If an SSL policy has been configured on the gRPC server, services can run only on an encrypted gRPC channel.
    * If no SSL policy is configured on the gRPC server, the connections that are established for services after the [**permit no-tls**](cmdqueryname=permit+no-tls) command is run will be disconnected after the [**undo permit no-tls**](cmdqueryname=undo+permit+no-tls) command is run.
11. Run [**server enable**](cmdqueryname=server+enable)
    
    
    
    The gRPC service is enabled.
12. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.
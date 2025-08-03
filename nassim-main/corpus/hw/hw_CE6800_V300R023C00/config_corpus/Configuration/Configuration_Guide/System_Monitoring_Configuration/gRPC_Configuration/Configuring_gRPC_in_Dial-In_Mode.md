Configuring gRPC in Dial-In Mode
================================

Configuring gRPC in Dial-In Mode

#### Prerequisites

Before configuring gRPC in dial-in mode, you have completed the following tasks:

* Create an ACL if you need to control which clients can connect to the server. For details about how to create an ACL, see "ACL Configuration" in Configuration Guide > IP Addresses and Services Configuration.
* Create an SSL policy if you need to create an SSL connection between the server and client. For details about how to create an SSL policy, see "SSL Configuration" in Configuration Guide > Security Configuration.
* Configure the gRPC server to perform AAA authentication, so that only authenticated users can log in to the device and perform related operations. For details about how to configure AAA authentication, see "AAA Configuration" in Configuration Guide > User Access and Authentication Configuration.


#### Context

In dial-in mode, a collector functioning as a client initiates a gRPC connection to a device functioning as a server, and the device collects specified data and reports the data to the collector.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the gRPC view.
   
   
   ```
   [grpc](cmdqueryname=grpc)
   ```
3. Enter the server view.
   
   
   * If an IPv4 network is used, enter the gRPC server view.
     ```
     [grpc server](cmdqueryname=grpc+server)
     ```
   * If an IPv6 network is used, enter the gRPC IPv6 server view.
     ```
     [grpc server ipv6](cmdqueryname=grpc+server+ipv6)
     ```
4. Configure the source IPv4 or IPv6 address to be listened on in dial-in mode.
   
   
   ```
   [source-ip](cmdqueryname=source-ip) ip-address [ vpn-instance vpn-instance-name ]
   ```
   
   By default, no source IPv4 or IPv6 address is configured to be listened on in dial-in mode.
5. Configure the number of the port to be listened on in dial-in mode.
   
   
   ```
   [server-port](cmdqueryname=server-port) port-number
   ```
   
   By default, port 57400 is listened on in dial-in mode.
6. (Optional) Configure an ACL for the gRPC service.
   
   
   ```
   [acl](cmdqueryname=acl) { acl-name | acl-number }
   ```
   
   By default, no ACL is configured for the gRPC service.
7. (Optional) Configure the idle timeout interval for the gRPC service.
   
   
   ```
   [idle-timeout](cmdqueryname=idle-timeout) time
   ```
   
   By default, the idle timeout interval of the gRPC service is 10s.
8. (Optional) Configure an SSL policy for the gRPC server.
   
   
   ```
   [ssl-policy](cmdqueryname=ssl-policy) ssl-policy-name
   ```
   
   By default, no SSL policy is configured for a gRPC server.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   After the device is switched to the FIPS mode, the gRPC function can be used only after an SSL policy is configured.
9. (Optional) Configure the gRPC server to perform SSL verification on the gRPC client.
   
   
   ```
   [ssl-verify peer](cmdqueryname=ssl-verify+peer)
   ```
   
   By default, a gRPC server does not perform SSL verification on a gRPC client.
10. (Optional) Configure the device to allow the selected service to run on an unencrypted gRPC channel.
    
    
    ```
    [permit no-tls](cmdqueryname=permit+no-tls) { gnmi }
    ```
    
    By default, services are not allowed to run on an unencrypted gRPC channel.
    
    ![](public_sys-resources/note_3.0-en-us.png) 
    
    If an SSL policy has been configured on the gRPC server, services can run only on an encrypted gRPC channel.
    
    If no SSL policy is configured on the gRPC server, the connections that are established for services after the [**permit no-tls**](cmdqueryname=permit+no-tls) command is run will be disconnected after the [**undo permit no-tls**](cmdqueryname=undo+permit+no-tls) command is run.
11. Enable the gRPC service.
    
    
    ```
    [server enable](cmdqueryname=server+enable)
    ```
    
    By default, the gRPC service is disabled.
12. Return to the gRPC view.
    
    
    ```
    [quit](cmdqueryname=quit)
    ```
13. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```
Creating a Dynamic Subscription
===============================

Creating a Dynamic Subscription

#### Prerequisites

Before configuring gRPC in dial-in mode, you have completed the following tasks:

* Create an ACL if you need to control which clients can connect to the server. For details about how to create an ACL, see "ACL Configuration" in Configuration Guide > IP Addresses and Services Configuration.
* Create an SSL policy if you need to create an SSL connection between the server and client. For details about how to create an SSL policy, see "SSL Configuration" in Configuration Guide > Security Configuration.
* Configure the gRPC server to perform AAA authentication, so that only authenticated users can log in to the device and perform related operations. For details about how to configure AAA authentication, see "AAA Configuration" in Configuration Guide > User Access and Authentication Configuration.


#### Context

When configuring a dynamic subscription on a device, you need to configure information about a gRPC server and enable the gRPC service. The collector will deliver the dynamic subscription configuration to the device, according to which the device reports data to the collector for service policy determination.


#### Procedure

1. Configure gRPC server information and enable the gRPC service.
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
   4. (Optional) Configure the gRPC server to transmit data in gzip compression mode.
      
      
      ```
      [compression gzip](cmdqueryname=compression+gzip)
      ```
   5. Configure the source IPv4 or IPv6 address to be listened on in dial-in mode.
      
      
      ```
      [source-ip](cmdqueryname=source-ip) ip-address [ vpn-instance vpn-instance-name ]
      ```
      
      By default, no source IPv4 or IPv6 address is configured to be listened on in dial-in mode.
   6. Configure the number of the port to be listened on in dial-in mode.
      
      
      ```
      [server-port](cmdqueryname=server-port) port-number
      ```
      
      By default, port 57400 is listened on in dial-in mode.
   7. (Optional) Configure an ACL for the gRPC service.
      
      
      ```
      [acl](cmdqueryname=acl) { acl-name | acl-number }
      ```
      
      By default, no ACL is configured for the gRPC service.
   8. (Optional) Configure the idle timeout interval for the gRPC service.
      
      
      ```
      [idle-timeout](cmdqueryname=idle-timeout) time
      ```
      
      By default, the idle timeout interval of the gRPC service is 10s.
   9. (Optional) Configure an SSL policy for the gRPC server.
      
      
      ```
      [ssl-policy](cmdqueryname=ssl-policy) ssl-policy-name
      ```
      
      By default, no SSL policy is configured for a gRPC server.
      
      ![](public_sys-resources/note_3.0-en-us.png) 
      
      After the device is switched to the FIPS mode, the gRPC function can be used only after an SSL policy is configured.
   10. (Optional) Configure the gRPC server to perform SSL verification on the gRPC client.
       
       
       ```
       [ssl-verify peer](cmdqueryname=ssl-verify+peer)
       ```
       
       By default, a gRPC server does not perform SSL verification on a gRPC client.
   11. Enable the gRPC service.
       
       
       ```
       [server enable](cmdqueryname=server+enable)
       ```
       
       By default, the gRPC service is disabled.
2. (Optional) Configure the maximum usage of CPU resources used for telemetry data sampling.
   
   
   ```
   [cpu-usage max-percent](cmdqueryname=cpu-usage+max-percent) usage
   ```
   
   By default, telemetry data sampling can occupy at most 5% of the CPU resources.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the **display telemetry dynamic-subscription** [ *subName* ] command to check dynamic subscription information.
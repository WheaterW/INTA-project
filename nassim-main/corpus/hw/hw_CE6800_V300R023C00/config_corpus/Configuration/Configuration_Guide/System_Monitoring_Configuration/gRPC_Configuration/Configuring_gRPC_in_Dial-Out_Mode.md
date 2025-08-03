Configuring gRPC in Dial-Out Mode
=================================

Configuring gRPC in Dial-Out Mode

#### Prerequisites

Before configuring gRPC in dial-out mode, you have completed the following tasks:

Create an SSL policy if you need to create an SSL connection between the server and client. For details about how to create an SSL policy, see "SSL Configuration" in Configuration Guide > Security Configuration.


#### Context

In dial-out mode, a device functioning as a client initiates a connection to a collector functioning as a server to send device data.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
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
   
   By default, a gRPC client does not perform SSL verification on a gRPC server.
5. (Optional) Configure an SSL policy for the gRPC client.
   
   
   ```
   [ssl-policy](cmdqueryname=ssl-policy) ssl-policy-name [ [verify-san](cmdqueryname=verify-san) san ]
   ```
   
   By default, no SSL policy is configured for a gRPC client.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   After the device is switched to the FIPS mode, the gRPC function can be used only after an SSL policy is configured.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
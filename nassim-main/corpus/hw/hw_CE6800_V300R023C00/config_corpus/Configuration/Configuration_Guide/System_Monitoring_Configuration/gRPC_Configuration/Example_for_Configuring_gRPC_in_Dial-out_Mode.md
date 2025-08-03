Example for Configuring gRPC in Dial-out Mode
=============================================

Example for Configuring gRPC in Dial-out Mode

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001513165810__fig168713817385), DeviceA functioning as a gRPC client connects to the collector functioning as a gRPC server. You need to configure gRPC in dial-out mode on the device, enabling the device to push the device capability information of the interface module to the collector at an interval of 10 seconds.

**Figure 1** Network diagram of gRPC in dial-out mode![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 represents 100GE 1/0/1.


  
![](figure/en-us_image_0000001564006077.png)

#### Procedure

1. Configure an SSL policy.
   
   
   
   # Upload the obtained digital certificate to the **/pki/public** directory of the device through SFTP. For details about how to apply for a digital certificate in PKI mode, see Configuration Guide > PKI Configuration.
   
   # Configure a PKI realm and import the local certificate and private key file.
   
   ```
   
   [~DeviceA] pki realm domain1
   [*DeviceA-pki-realm-domain1] commit
   [~DeviceA-pki-realm-domain1] quit
   [~DeviceA] pki import-certificate local realm domain1 pem filename restconf_local.pem
   [~DeviceA] pki import rsa-key-pair restconf-key pem restconf.pem //Skip this step if the private key file is generated on the local device.
   ```
   
   # Import the CA certificate of the peer collector to verify the validity of the local certificate for the collector.
   
   ```
   [~DeviceA] pki import-certificate ca realm domain1 pem filename restconf_ca.pem
   ```
   
   # Configure an SSL policy and bind it to the PKI realm.
   
   
   
   ```
   [~DeviceA] ssl policy policy1
   [*DeviceA-ssl-policy-policy1] pki-domain domain1
   [*DeviceA-ssl-policy-policy1] commit
   [~DeviceA-ssl-policy-policy1] quit
   ```
2. Configure the gRPC client function.
   
   
   ```
   [~DeviceA] grpc
   [~DeviceA-grpc] grpc client
   [~DeviceA-grpc-client] ssl-verify peer
   [~DeviceA-grpc-client] ssl-policy policy1
   [~DeviceA-grpc-client] quit
   [~DeviceA-grpc] quit
   [~DeviceA] commit
   ```
3. Configure a destination collector for receiving sampled data. For details, see "Configuring a Destination Collector for Receiving Sampled Data" in Configuration Guide > Telemetry Configuration.
   
   
   
   # On DeviceA, create the destination group **destination1** to which a destination collector belongs, set the IP address and port number of the destination collector to 192.168.2.1 and 10001, respectively, and set the gRPC encryption mode to TLS.
   
   ```
   [~DeviceA] telemetry
   [~DeviceA-telemetry] destination-group destination1
   [*DeviceA-telemetry-destination-group-destination1] ipv4-address 192.168.2.1 port 10001 protocol grpc
   [*DeviceA-telemetry-destination-group-destination1] quit
   [*DeviceA-telemetry] commit
   ```
4. Configure the sampling path and filter criteria. For details, see "Configuring the Sampling Path and Filter Criteria" in Configuration Guide > Telemetry Configuration.
   
   
   
   # Configure the sampling sensor group **sensor1**.
   
   ```
   [~DeviceA-telemetry] sensor-group sensor1
   [*DeviceA-telemetry-sensor-group-sensor1] quit
   [*DeviceA-telemetry] commit
   ```
5. Create a subscription. For details, see "Creating a Static Subscription" in Configuration Guide > Telemetry Configuration.
   
   
   
   # Create the subscription **subscription1**, associate it to **sensor1** and **destination1**, and set the data sampling and push intervals to 10 seconds.
   
   ```
   [~DeviceA-telemetry] subscription subscription1
   [*DeviceA-telemetry-subscription-subscription1] sensor-group sensor1 sample-interval 10000
   [*DeviceA-telemetry-subscription-subscription1] destination-group destination1
   [*DeviceA-telemetry-subscription-subscription1] quit
   [*DeviceA-telemetry] commit
   ```

#### Verifying the Configuration

# Display detailed subscription information.

```
[~DeviceA] display telemetry subscription subscription1
---------------------------------------------------------------------------     
Sub-name           : subscription1                                              
Source Address     : -                                                          
Dscp               : 0                                                          
Protocol           : GRPC                                                       
Encoding           : GPB                                                        
Send bytes         : 0                                                          
Send packets       : 0                                                          
Total send delay   : 0                                                          
Total send error   : 0                                                          
Total send  drop   : 0                                                          
Total other error  : 0                                                          
Last send-time     : 0000-00-00 00:00:00                                        
Sensor group:                                                                   
---------------------------------------------------------------------------     
Sensor-name  Sample-interval(ms) Heartbeat-interval(s) Suppression State        
---------------------------------------------------------------------------     
sensor1      10000               -                     NO          RESOLVED     
---------------------------------------------------------------------------     
Destination group:                                                              
---------------------------------------------------------------------------     
Dest-name    Dest-IP          Dest-port  State        Vpn-name      Protocol   Compression
---------------------------------------------------------------------------     
destination1 192.168.2.1      10001      RESOLVED     -             GRPC       GZIP
---------------------------------------------------------------------------     
Sub-state          : PASSIVE                                                    
---------------------------------------------------------------------------     

Total subscription number is :  1  
```

#### Configuration Scripts

DeviceA

```
#
sysname DeviceA
#
pki realm domain1
#
ssl policy policy1
 pki-domain domain1
#
grpc
 #
 grpc client 
  ssl-policy policy1
  ssl-verify peer
#
telemetry
 #
 sensor-group sensor1 
 #
 destination-group destination1
  ipv4-address 192.168.2.1 port 10001 protocol grpc
 #
 subscription subscription1
  sensor-group sensor1 sample-interval 10000
  destination-group destination1
#
return
```
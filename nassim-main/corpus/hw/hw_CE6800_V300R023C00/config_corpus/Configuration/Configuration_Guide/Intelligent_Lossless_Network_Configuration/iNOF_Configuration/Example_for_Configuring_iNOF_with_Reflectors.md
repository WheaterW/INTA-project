Example for Configuring iNOF with Reflectors
============================================

Example for Configuring iNOF with Reflectors

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001564003597__fig19978171395514), Host1 and Host2 connect to the network through Client1 and Client2. To achieve effective host management, iNOF needs to be configured on Reflector1, Reflector2, Client1, and Client2; Reflector1 and Reflector2 need to be configured as iNOF reflectors and Client1 and Client2 as iNOF clients.

**Figure 1** Networking diagram of the iNOF function with two reflectors![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent 100GE1/0/1, 100GE1/0/2, and 100GE1/0/3, respectively.


  
![](figure/en-us_image_0000001513043394.png)

#### Precautions

The SNSD function must be enabled for the host and storage array (Host1 and Host2 in [Figure 1](#EN-US_TASK_0000001564003597__fig19978171395514), respectively).


#### Procedure

1. Assign IP addresses to interfaces and configure a routing protocol to ensure Layer 3 connectivity.
   
   
   
   # Assign an IP address to each interface and configure OSPF on Reflector1. The configurations on Reflector2, Client1, and Client2 are similar.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname Reflector1
   [*HUAWEI] commit
   [~Reflector1] interface 100ge 1/0/1
   [~Reflector1-100GE1/0/1] undo portswitch
   [*Reflector1-100GE1/0/1] ip address 10.1.3.1 24
   [*Reflector1-100GE1/0/1] quit
   [*Reflector1] interface 100ge 1/0/2
   [*Reflector1-100GE1/0/2] undo portswitch
   [*Reflector1-100GE1/0/2] ip address 10.1.4.1 24
   [*Reflector1-100GE1/0/2] quit
   [*Reflector1] interface loopback 0
   [*Reflector1-LoopBack0] ip address 192.168.1.1 32
   [*Reflector1-LoopBack0] quit
   [*Reflector1] ospf 1 
   [*Reflector1-ospf-1] area 0 
   [*Reflector1-ospf-1-area-0.0.0.0] network 10.1.3.0 0.0.0.255 
   [*Reflector1-ospf-1-area-0.0.0.0] network 10.1.4.0 0.0.0.255 
   [*Reflector1-ospf-1-area-0.0.0.0] network 192.168.1.1 0.0.0.0 
   [*Reflector1-ospf-1-area-0.0.0.0] quit 
   [*Reflector1-ospf-1] quit
   [*Reflector1] commit
   ```
2. Enable the LLDP function on devices.
   
   
   
   # Enable the LLDP function on Reflector1. The configurations on Reflector2, Client1, and Client2 are similar.
   
   ```
   [~Reflector1] lldp enable
   [*Reflector1] commit
   ```
3. Configure the authentication mode and password for transmitting iNOF packets.
   
   
   
   # On Reflector1, set the authentication mode for transmitting iNOF packets to HMAC-SHA256 and the authentication password to **YsHsjx\_202206**. The configurations on Reflector2, Client1, and Client2 are similar.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   iNOF packets can be transmitted only after they pass authentication. Therefore, after configuring the authentication mode and password for transmitting iNOF packets on a device, ensure that the same authentication mode and password are configured on the peer device; otherwise, the packets cannot pass authentication.
   
   ```
   [~Reflector1] ai-service
   [*Reflector1-ai-service] inof
   [*Reflector1-ai-service-inof] authentication-mode hmac-sha256 password YsHsjx_202206
   [*Reflector1-ai-service-inof] quit
   [*Reflector1-ai-service] quit
   [*Reflector1] commit
   ```
4. Configure iNOF reflectors and clients.
   
   
   
   # Configure Reflector1 as an iNOF reflector. On Reflector1, set the local IP address to 192.168.1.1 and the port number for transmitting iNOF packets to 10002.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   All devices in the iNOF system must be configured with the same port number for transmitting iNOF packets.
   
   ```
   [~Reflector1] ai-service
   [~Reflector1-ai-service] inof
   [~Reflector1-ai-service-inof] role reflector
   [*Reflector1-ai-service-inof] service-address 192.168.1.1 port-id 10002
   [*Reflector1-ai-service-inof] quit
   [*Reflector1-ai-service] quit
   [*Reflector1] commit
   ```
   
   
   
   # Configure Reflector2 as an iNOF reflector. On Reflector2, set the local IP address to 192.168.1.4 and the port number for transmitting iNOF packets to 10002.
   
   ```
   [~Reflector2] ai-service
   [~Reflector2-ai-service] inof
   [~Reflector2-ai-service-inof] role reflector
   [*Reflector2-ai-service-inof] service-address 192.168.1.4 port-id 10002
   [*Reflector2-ai-service-inof] quit
   [*Reflector2-ai-service] quit
   [*Reflector2] commit
   ```
   
   # Configure Client1 as an iNOF client. On Client1, set the local IP address to 192.168.1.2 and the port number for transmitting iNOF packets to 10002.
   
   ```
   [~Client1] ai-service
   [~Client1-ai-service] inof
   [~Client1-ai-service-inof] role reflect-client
   [*Client1-ai-service-inof] service-address 192.168.1.2 port-id 10002
   [*Client1-ai-service-inof] quit
   [*Client1-ai-service] quit
   [*Client1] commit
   ```
   
   
   
   # Configure Client2 as an iNOF client. On Client2, set the local IP address to 192.168.1.3 and the port number for transmitting iNOF packets to 10002.
   
   ```
   [~Client2] ai-service
   [~Client2-ai-service] inof
   [~Client2-ai-service-inof] role reflect-client
   [*Client2-ai-service-inof] service-address 192.168.1.3 port-id 10002
   [*Client2-ai-service-inof] quit
   [*Client2-ai-service] quit
   [*Client2] commit
   ```
5. Specify the client IP addresses on iNOF reflectors.
   
   
   
   # On Reflector1, specify 192.168.1.2 and 192.168.1.3 as the IP addresses of Client1 and Client2, respectively, and also specify Reflector2 as the client of Reflector1.
   
   ```
   [~Reflector1] ai-service
   [~Reflector1-ai-service] inof
   [~Reflector1-ai-service-inof] peer 192.168.1.2 reflect-client
   [*Reflector1-ai-service-inof] peer 192.168.1.3 reflect-client
   [*Reflector1-ai-service-inof] peer 192.168.1.4 reflect-client
   [*Reflector1-ai-service-inof] quit
   [*Reflector1-ai-service] quit
   [*Reflector1] commit
   ```
   
   # On Reflector2, specify 192.168.1.2 and 192.168.1.3 as the IP addresses of Client1 and Client2, respectively, and also specify Reflector1 as the client of Reflector2.
   
   ```
   [~Reflector2] ai-service
   [~Reflector2-ai-service] inof
   [~Reflector2-ai-service-inof] peer 192.168.1.2 reflect-client
   [*Reflector2-ai-service-inof] peer 192.168.1.3 reflect-client
   [*Reflector2-ai-service-inof] peer 192.168.1.1 reflect-client
   [*Reflector2-ai-service-inof] quit
   [*Reflector1-ai-service] quit
   [*Reflector2] commit
   ```
6. Create a customized zone on iNOF reflectors.
   
   
   
   # On Reflector1, disable the function for automatically adding hosts to the default zone to save network resources. The configurations on Reflector2 are similar.
   
   ```
   [~Reflector1] ai-service
   [~Reflector1-ai-service] inof
   [~Reflector1-ai-service-inof] undo default-zone enable
   [*Reflector1-ai-service-inof] quit
   [*Reflector1-ai-service] quit
   [*Reflector1] commit
   ```
   
   # On Reflector1, create a customized zone named **zone1** and add the IP addresses of Host1 and Host2 to the zone. The configurations on Reflector2 are similar.
   
   ```
   [~Reflector1] ai-service
   [~Reflector1-ai-service] inof
   [~Reflector1-ai-service-inof] zone zone1
   [*Reflector1-ai-service-inof-zone-zone1] host 10.1.1.1
   [*Reflector1-ai-service-inof-zone-zone1] host 10.1.2.1
   [*Reflector1-ai-service-inof] quit
   [*Reflector1-ai-service] quit
   [*Reflector1] commit
   ```
   
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   To ensure successful data backup between Reflector1 and Reflector2, they must have the same zone configurations.
7. Configure BFD for iNOF.
   
   
   
   # Configure BFD for iNOF on Reflector1. The configurations on Reflector2 are similar.
   
   ```
   [~Reflector1] bfd
   [*Reflector1-bfd] quit
   [*Reflector1] commit
   [~Reflector1] ai-service
   [~Reflector1-ai-service] inof
   [~Reflector1-ai-service-inof] inof bfd enable
   [*Reflector1-ai-service-inof] quit
   [*Reflector1-ai-service] quit
   [*Reflector1] commit
   ```
8. Enable iNOF zone isolation.
   
   
   
   # Configure iNOF zone isolation on Reflector1. The configurations on Reflector2 are similar.
   
   ```
   [~Reflector1] ai-service
   [~Reflector1-ai-service] inof
   [~Reflector1-ai-service-inof] hard-zoning enable
   [*Reflector1-ai-service-inof] quit
   [*Reflector1-ai-service] quit
   [*Reflector1] commit
   ```

#### Verifying the Configuration

# On Reflector1, after the iNOF reflector and clients are configured, check information about the iNOF connections established between the local and peer devices.

```
[~Reflector1] display inof peer connection  
Role: Reflector
IPv4 Info:
Port: 10002
ServiceAddress: 192.168.1.1
----------------------------------------------------------
Index  PeerIP           ConnectStatus  EstablishTime
----------------------------------------------------------
    1  192.168.1.2      Established    2020-09-03 23:31:12
    1  192.168.1.3      Established    2020-09-03 23:31:12
    2  192.168.1.4      Established    2020-09-03 23:32:12
----------------------------------------------------------
```

# Display the configuration of iNOF zone members on Reflector1.

```
[~Reflector1] display inof configuration host
IPv4 Info:

Host:10.1.1.1
----------------------------------------------------------------------------------
Learned-From                             ZoneName
----------------------------------------------------------------------------------
Local                                    zone1
192.168.1.4                              zone1
----------------------------------------------------------------------------------

Host:10.1.2.1
----------------------------------------------------------------------------------
Learned-From                             ZoneName
----------------------------------------------------------------------------------
Local                                    zone1
192.168.1.4                              zone1
----------------------------------------------------------------------------------
```

#### Configuration Scripts

Reflector1

```
#
sysname Reflector1
#
bfd
#
lldp enable
#
interface 100GE1/0/1
 undo portswitch
 ip address 10.1.3.1 255.255.255.0
#
interface 100GE1/0/2
 undo portswitch
 ip address 10.1.4.1 255.255.255.0
#
interface LoopBack0
  ip address 192.168.1.1 255.255.255.255 
#
ai-service
 #
 inof
  authentication-mode hmac-sha256 password %+%##!<x@k!01K6<Di#Xie66M:rx~U7=>Ws*I$1!!!!!!!!!!!!!!!;!!!!%7&7
  hard-zoning enable
  inof bfd enable
  peer 192.168.1.2 reflect-client
  peer 192.168.1.3 reflect-client
  peer 192.168.1.4 reflect-client
  role reflector
  service-address 192.168.1.1 port-id 10002
  undo default-zone enable
  #
  zone zone1
   host 10.1.1.1
   host 10.1.2.1
# 
ospf 1
 area 0.0.0.0 
  network 10.1.3.0 0.0.0.255
  network 10.1.4.0 0.0.0.255 
  network 192.168.1.1 0.0.0.0 
#
return

```

Reflector2

```
#
sysname Reflector2
#
bfd
#
lldp enable
#
interface 100GE1/0/1
 undo portswitch
 ip address 10.1.5.1 255.255.255.0
#
interface 100GE1/0/2
 undo portswitch
 ip address 10.1.6.1 255.255.255.0
#
interface LoopBack0
  ip address 192.168.1.4 255.255.255.255 
#
ai-service
 #
 inof
  authentication-mode hmac-sha256 password %+%##!<x@k!01Q_/8W\@B'Bq$FrD66M:rx~U7=>Ws*I$1!!!!!!!!!!!!;!!!!%7&7
  hard-zoning enable
  inof bfd enable
  peer 192.168.1.2 reflect-client
  peer 192.168.1.3 reflect-client
  peer 192.168.1.1 reflect-client
  role reflector
  service-address 192.168.1.4 port-id 10002
  undo default-zone enable
  #
  zone zone1
   host 10.1.1.1
   host 10.1.2.1
#
ospf 1
 area 0.0.0.0 
  network 10.1.5.0 0.0.0.255
  network 10.1.6.0 0.0.0.255 
  network 192.168.1.4 0.0.0.0 
#
return

```

Client1

```
#
sysname Client1
#
lldp enable
#
interface 100GE1/0/1
 undo portswitch
 ip address 10.1.3.2 255.255.255.0
#
interface 100GE1/0/2
 undo portswitch
 ip address 10.1.1.2 255.255.255.0
#
interface 100GE1/0/3
 undo portswitch
 ip address 10.1.5.2 255.255.255.0
#
interface LoopBack0
  ip address 192.168.1.2 255.255.255.255 
#
ai-service
 #
 inof
  authentication-mode hmac-sha256 password %+%##!!!<x@k!01Kv>7iLc"ypITVI3>d<2PQ\g)Y(!!!!!!!!!!!!!!!:!!!!'JVz
  role reflect-client
  service-address 192.168.1.2 port-id 10002
#
ospf 1
 area 0.0.0.0 
  network 10.1.1.0 0.0.0.255
  network 10.1.3.0 0.0.0.255 
  network 10.1.5.0 0.0.0.255 
  network 192.168.1.2 0.0.0.0 
#
return

```

Client2

```
#
sysname Client2
#
lldp enable
#
interface 100GE1/0/1
 undo portswitch
 ip address 10.1.4.2 255.255.255.0
#
interface 100GE1/0/2
 undo portswitch
 ip address 10.1.2.2 255.255.255.0
#
interface 100GE1/0/3
 undo portswitch
 ip address 10.1.6.2 255.255.255.0
#
interface LoopBack0
  ip address 192.168.1.3 255.255.255.255 
#
ai-service
 #
 inof
  authentication-mode hmac-sha256 password %+%#!!!!"!!x@k!01Km:Q_/8W\@B'Bq$FrD\i;tK-\(!!!!!!!!!!!!!!!;!!!!&.lER
  role reflect-client
  service-address 192.168.1.3 port-id 10002
#
ospf 1
 area 0.0.0.0 
  network 10.1.2.0 0.0.0.255
  network 10.1.4.0 0.0.0.255 
  network 10.1.6.0 0.0.0.255 
  network 192.168.1.3 0.0.0.0 
#
return

```
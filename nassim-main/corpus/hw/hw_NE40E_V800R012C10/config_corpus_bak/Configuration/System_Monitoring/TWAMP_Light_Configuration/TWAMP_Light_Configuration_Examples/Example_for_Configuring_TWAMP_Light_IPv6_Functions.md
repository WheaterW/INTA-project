Example for Configuring TWAMP Light IPv6 Functions
==================================================

This section provides an example for configuring TWAMP Light IPv6 functions.

#### Networking Requirements

On the IP network shown in [Figure 1](#EN-US_TASK_0172373305__fig_dc_vrp_cfg_twamp-light_011101), DeviceA functions as the Controller, and DeviceB functions as the Responder.

* DeviceA: sends and receives packets over a test session, collects and calculates performance statistics, and reports the statistics to the performance management system.
* DeviceB: responds to the packets received over a test session.

**Figure 1** TWAMP Light  
![](images/fig_dc_vrp_cfg_twamp-light_011103.png)
#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IP address and a routing protocol for each interface so that all the devices can communicate at the network layer.
2. Configure the TWAMP Light Responder on DeviceB.
3. Configure the TWAMP Light Controller on DeviceA.
4. Configure the Controller to send statistics to the performance management system through telemetry.
#### Data Preparation

To complete the configuration, you need the following data:

* Responder DeviceB
  + IP address: 2001:DB8:2::2
  + UDP port number 2010
* Controller DeviceA
  + IP address: 2001:DB8:1::1
  + UDP port number: 2001
* Performance management system
  + IP address: 2001:db8:100::100
  + gRPC port number: 10001


#### Procedure

1. Configure an IP address and a routing protocol for each involved interface so that all the devices can communicate at the network layer. The configuration procedure is not provided here.
2. Configure the TWAMP Light Responder.
   
   
   ```
   <DeviceB> system-view
   ```
   ```
   [~DeviceB] nqa twamp-light
   ```
   ```
   [*DeviceB-twamp-light] responder
   ```
   ```
   [*DeviceB-twamp-light-responder] test-session 1 local-ipv6 2001:DB8:2::2 remote-ipv6 2001:DB8:1::1 local-port 2010 remote-port 2001
   ```
   ```
   [*DeviceB-twamp-light-responder] commit
   ```
   ```
   [~DeviceB-twamp-light-responder] quit
   ```
   ```
   [~DeviceB-twamp-light] quit
   ```
3. Configure the TWAMP Light Controller.
   
   
   ```
   <DeviceA> system-view
   ```
   ```
   [~DeviceA] nqa twamp-light
   ```
   ```
   [*DeviceA-twamp-light] client
   ```
   ```
   [*DeviceA-twamp-light-client] test-session 1 sender-ipv6 2001:DB8:1::1 reflector-ipv6 2001:DB8:2::2 sender-port 2001 reflector-port 2010
   ```
   ```
   [*DeviceA-twamp-light-client] commit
   ```
   ```
   [~DeviceA-twamp-light-client] quit
   ```
   ```
   [~DeviceA-twamp-light] sender
   ```
   ```
   [*DeviceA-twamp-light-sender] commit
   ```
   ```
   [~DeviceA-twamp-light-sender] test start-continual test-session 1 period 10
   ```
   ```
   [*DeviceA-twamp-light-sender] commit
   ```
   ```
   [~DeviceA-twamp-light-sender] quit
   ```
   ```
   [~DeviceA-twamp-light] quit
   ```
4. Verify the configuration.
   
   
   
   # Check real-time TWAMP Light session statistics on DeviceA.
   
   ```
   [~DeviceA] display twamp-light test-session 1
   ```
   ```
   Session ID                       : 1
   State                            : active
   Type                             : continual
   Sender IP                        : 2001:DB8:1::1
   Sender Port                      : 2001
   Reflector IP                     : 2001:DB8:2::2
   Reflector Port                   : 2010
   Mode                             : unauthenticated
   DSCP                             : 0
   Padding Length                   : 128
   Padding Type                     : 00
   VPN Instance                     : -
   Link-Bundle Interface            : -
   Last Start Time                  : 2018-11-13 15:33:52
   Last Stop Time                   : never
   Regular Time(in minute)          : - 
   Period Time(in millisecond)      : 10
   Time Out(in second)              : 5
   Duration Time(in second)         : -
   Packet Count                     : - 
   ```
   
   # Check two-way delay statistics of a TWAMP Light session on DeviceA.
   
   ```
   [~DeviceA] display twamp-light statistic-type twoway-delay test-session 1
   ```
   ```
   Latest two-way delay statistics(usec): 
   -------------------------------------------------------------------------------- 
        Index      Delay(Avg)     Jitter(Avg)     Tx-Jitter(Avg)    Rx-Jitter(Avg) 
   -------------------------------------------------------------------------------- 
        11027             345               5                 3                 4 
        11028             345               5                 3                 4 
        11029             345               5                 4                 4 
        11030             347               5                 3                 4 
        11031             347               4                 3                 4 
        11032             347               4                 3                 4 
        11033             347               4                 3                 4 
        11034             346               4                 3                 4 
        11035             346               5                 3                 4 
        11036             346               5                 3                 4 
        11037             346               5                 3                 4 
        11038             346               4                 4                 3 
        11039             347               4                 4                 3 
        11040             347               4                 4                 3 
        11041             347               4                 4                 3 
        11042             347               4                 4                 3 
        11043             347               5                 3                 4 
        11044             346               5                 3                 4
        11045             346               5                 3                 4
        11046             346               5                 3                 4
        11047             346               5                 3                 4 
        11048             346               5                 3                 4 
        11049             346               4                 3                 4 
        11050             346               4                 3                 4 
        11051             345               4                 3                 3 
        11052             345               4                 3                 3 
        11053             345               5                 4                 3 
        11054             345               5                 4                 3 
        11055             345               4                 4                 3  
        11056             345               4                 3                 3  
   -------------------------------------------------------------------------------- 
   Average Delay    :          346    Average Jitter   :          5 
   Maximum Delay    :          370    Maximum Jitter   :          32 
   Minimum Delay    :          328    Minimum Jitter   :          0 
   Average TxJitter :            3    Average RxJitter :          4 
   Maximum TxJitter :           29    Maximum RxJitter :          23 
   Minimum TxJitter :            0    Minimum RxJitter :          0 
   ```
   
   # Check two-way packet loss statistics of a TWAMP Light session on DeviceA.
   
   ```
   [~DeviceA] display twamp-light statistic-type twoway-loss test-session 1
   ```
   ```
   Latest two-way loss statistics:
   --------------------------------------------------------------------------------
        Index      Loss count      Loss ratio      Error count      Error ratio
   --------------------------------------------------------------------------------
       108196               0         0.0000%                0          0.0000%
       108197               0         0.0000%                0          0.0000%
       108198               0         0.0000%                0          0.0000%
       108199               0         0.0000%                0          0.0000%
       108200               0         0.0000%                0          0.0000%
       108201               0         0.0000%                0          0.0000%
       108202               0         0.0000%                0          0.0000%
       108203               0         0.0000%                0          0.0000%
       108204               0         0.0000%                0          0.0000%
       108205               0         0.0000%                0          0.0000%
       108206               0         0.0000%                0          0.0000%
       108207               0         0.0000%                0          0.0000%
       108208               0         0.0000%                0          0.0000%
       108209               0         0.0000%                0          0.0000%
       108210               0         0.0000%                0          0.0000%
       108211               0         0.0000%                0          0.0000%
       108212               0         0.0000%                0          0.0000%
       108213               0         0.0000%                0          0.0000%
       108214               0         0.0000%                0          0.0000%
       108215               0         0.0000%                0          0.0000%
       108216               0         0.0000%                0          0.0000%
       108217               0         0.0000%                0          0.0000%
       108218               0         0.0000%                0          0.0000%
       108219               0         0.0000%                0          0.0000%
       108220               0         0.0000%                0          0.0000%
       108221               0         0.0000%                0          0.0000%
       108222               0         0.0000%                0          0.0000%
       108223               0         0.0000%                0          0.0000%
       108224               0         0.0000%                0          0.0000%
       108225               0         0.0000%                0          0.0000%
   --------------------------------------------------------------------------------
   Average Loss Count   :          0    Average Loss Ratio   :   0.0000%
   Maximum Loss Count   :          0    Maximum Loss Ratio   :   0.0000%
   Minimum Loss Count   :          0    Minimum Loss Ratio   :   0.0000%
   Average RxError Count:          0    Average RxError Ratio:   0.0000%
   Maximum RxError Count:          0    Maximum RxError Ratio:   0.0000%
   Minimum RxError Count:          0    Minimum RxError Ratio:   0.0000%
   ```
5. Configure DeviceA to send statistics to the performance management system through telemetry.
   
   
   ```
   [~DeviceA] telemetry
   ```
   ```
   [~DeviceA-telemetry] destination-group twamp
   ```
   ```
   [*DeviceA-telemetry-destination-group-twamp] ipv6-address 2001:DB8:100::100 port 10001 protocol grpc no-tls
   ```
   ```
   [*DeviceA-telemetry-destination-group-twamp] quit
   ```
   ```
   [*DeviceA-telemetry] sensor-group twamp
   ```
   ```
   [*DeviceA-telemetry-sensor-group-twamp] sensor-path huawei-twamp-controller:twamp-controller/client/sessions/session/huawei-twamp-statistics:statistics
   ```
   ```
   [*DeviceA-telemetry-sensor-group-twamp] quit
   ```
   ```
   [*DeviceA-telemetry] subscription twamp
   ```
   ```
   [*DeviceA-telemetry-subscription-twamp] sensor-group twamp sample-interval 5000
   ```
   ```
   [*DeviceA-telemetry-subscription-twamp] destination-group twamp
   ```
   ```
   [*DeviceA-telemetry-subscription-twamp] commit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   You are advised to configure devices to send data using a secure TLS encryption mode. For details, see *Telemetry Configuration*.

#### Configuration Files

DeviceA configuration file
```
#
sysname DeviceA
#
interface GigabitEthernet0/1/0
 undo shutdown
 ipv6 enable
 ipv6 address 2001:DB8:1::1/64
#
nqa twamp-light
 client
  test-session 1 sender-ipv6 2001:DB8:1::1 reflector-ipv6 2001:DB8:2::2 sender-port 2001 reflector-port 2010
 sender
  test start-continual test-session 1 period 10
#
telemetry
 #
 sensor-group twamp
  sensor-path huawei-twamp-controller:twamp-controller/client/sessions/session/huawei-twamp-statistics:statistics
 #
 destination-group twamp
  ipv6-address 2001:DB8:100::100 port 10001 protocol grpc no-tls
 #
 subscription twamp
  sensor-group twamp sample-interval 5000
  destination-group twamp
#
return
```

DeviceB configuration file

```
#
sysname DeviceB
#
interface GigabitEthernet0/1/0
 undo shutdown
 ipv6 enable
 ipv6 address 2001:DB8:2::2/64
#
nqa twamp-light
 responder
  test-session 1 local-ipv6 2001:DB8:2::2 remote-ipv6 2001:DB8:1::1 local-port 2010 remote-port 2001
#
return
```
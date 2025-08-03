Example for Configuring 1588 ACR Clock Synchronization in a Single-Server Scenario
==================================================================================

This section describes how to configure 1588 ACR on the Router functioning as a client and the Router functioning as a server to restore clock information in a single-server scenario by using an example.

#### Networking Requirements

On the IP RAN shown in [Figure 1](#EN-US_TASK_0000001779081038__fig_dc_ne_1588v2_cfg_503601), DeviceA functions as a clock server. DeviceC functions as a client, and sends a 1588 ACR Layer 3 unicast negotiation request to the server to achieve clock synchronization.

**Figure 1** Network diagram of configuring 1588 ACR clock synchronization in a single-server scenario  
![](figure/en-us_image_0000001778921490.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure DeviceA as a server.
2. Configure DeviceC as a client.
3. Configure unicast negotiation on the server and client.
4. On the client, configure a PTP clock reference source.

#### Data Preparation

To complete the configuration, you need the following data:

* IP address of the server and the IP address of the client

#### Procedure

1. Configure DeviceA as a server.
   
   
   ```
   <DeviceA> system-view
   ```
   ```
   [~DeviceA] interface loopback 0
   ```
   ```
   [*DeviceA-Loopback0] ip address 1.1.1.1 32
   ```
   ```
   [*DeviceC-Loopback0] commit
   ```
   ```
   [~DeviceA-Loopback0] quit
   ```
   ```
   [~DeviceA] ptp-adaptive enable
   ```
   ```
   [*DeviceA] ptp-adaptive device-type server
   ```
   ```
   [*DeviceA] ptp-adaptive local-ip 1.1.1.1
   ```
   ```
   [~DeviceA] commit
   ```
2. Configure DeviceC as a client.
   
   
   ```
   <DeviceC> system-view
   ```
   ```
   [~DeviceC] interface loopback 0
   ```
   ```
   [*DeviceC-Loopback0] ip address 2.2.2.2 32
   ```
   ```
   [*DeviceC-Loopback0] commit
   ```
   ```
   [~DeviceC-Loopback0] quit
   ```
   ```
   [~DeviceC] ptp-adaptive enable
   ```
   ```
   [*DeviceC] ptp-adaptive device-type client
   ```
   ```
   [*DeviceC] ptp-adaptive local-ip 2.2.2.2
   ```
   ```
   [*DeviceC] ptp-adaptive remote-server1-ip 1.1.1.1
   ```
   ```
   [~DeviceC] commit
   ```
3. Configure unicast negotiation on the server and client.
   
   
   
   # Configure the server.
   
   ```
   [~DeviceA] ptp-adaptive acr unicast-negotiate enable
   ```
   ```
   [*DeviceA] commit
   ```
   
   
   
   # Configure the client.
   
   ```
   [~DeviceC] ptp-adaptive acr unicast-negotiate enable
   ```
   ```
   [*DeviceC] commit
   ```
4. On the client, configure a PTP clock reference source.
   
   
   ```
   [~DeviceC] clock source ptp synchronization enable
   ```
   ```
   [*DeviceC] clock source ptp priority 10
   ```
   ```
   [*DeviceC] clock source ptp ssm prc
   ```
   ```
   [*DeviceC] commit
   ```
5. Verify the configuration.
   
   
   
   # Check the 1588 ACR configuration on DeviceC.
   
   ```
   <DeviceC> display ptp-adaptive all
   ```
   ```
    Device config info
    ---------------------------------------------------------------------------
    Ptp adaptive state      :enable         Device type        :client
    Sync mode               :frequency      Current state      :slave
    Packet dscp             :56             Domain value       :0
    Announce interval       :11             Announce duration  :300s
    Sync interval           :3              Sync duration      :300s
    Delay_resp interval     :3              Delay_resp duration:300s
    Announce receipt timeout:3              Acr mode           :one-way
    Local ip                :2.2.2.2        Client board       :3
    Frequency profile       :no
    VPN                     :none
   
    BMCA run info
    ---------------------------------------------------------------------------
    Current trace source    :server1
    Frequency lock success  :yes
   
    Time performance statistics(ns):
    ------------------------------------------------------------------------
    Realtime(T2-T1)         :987740873
    Max(T2-T1)              :987742555
    Min(T2-T1)              :987423502
   
    Remote server info
    ---------------------------------------------------------------------------
             Ip address        Negotiate state  Pri1 Class   Accuracy  Pri2
    Server1: 1.1.1.1           Nego success     128  6       0x34      128
    Server2:                                                               
   
   ```
   
   # Check the 1588 ACR configuration on DeviceA.
   
   ```
   <DeviceA> display ptp-adaptive all
   ```
   ```
    Device config info
    ---------------------------------------------------------------------------
    Ptp adaptive state      :enable         Device type        :server
    Sync mode               :frequency      Current state      :master
    Packet dscp             :56             Domain value       :0
    Local ip                :1.1.1.1        Server board       :3
    Frequency profile       :no
    VPN                     :none
   
    Client info
        ID  Ip Address        Clock ID          Mode    Announce  Sync  Delay_resp
    ---------------------------------------------------------------------------
    1   0   2.2.2.2           001882fffed48301  one-way 11         3     3
   
   ```

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  ```
  ```
  sysname DeviceA
  ```
  ```
  #
  ptp-adaptive enable
  ptp-adaptive device-type server
  ptp-adaptive local-ip 1.1.1.1
  ptp-adaptive acr unicast-negotiate enable
  #
  interface Loopback0
   ip address 1.1.1.1 255.255.255.255
  #
  return
  ```
* DeviceC configuration file
  
  ```
  #
  ```
  ```
  sysname DeviceC
  ```
  ```
  #
  ptp-adaptive enable
  ptp-adaptive device-type client
  ptp-adaptive local-ip 2.2.2.2
  ptp-adaptive remote-server1-ip 1.1.1.1
  ptp-adaptive acr unicast-negotiate enable
  clock source ptp synchronization enable
  clock source ptp priority 10
  clock source ptp ssm prc
  #
  interface GE0/1/0
   clock synchronization enable
  #
  interface Loopback0
   ip address 2.2.2.2 255.255.255.255
  #
  return
  ```
Example for Configuring 1588 ACR Clock Synchronization in a Dual-Server Scenario
================================================================================

In a 1588 ACR domain, a client sets up the client/server relationship with two remote clock servers that work in the master/slave mode, and sends a unicast negotiation request to the two clock servers to restore clock information. Once the master clock server becomes faulty, the client sends a request for establishing a connection to the slave clock server.

#### Networking Requirements

On the IP RAN shown in [Figure 1](#EN-US_TASK_0000001825720917__fig_dc_ne_1588v2_cfg_503701), DeviceA and DeviceB function as clock servers that work in the master/slave mode. DeviceC functions as a client and first sends a 1588 ACR Layer 3 unicast negotiation request to DeviceA that functions as the master clock server to achieve clock synchronization. If the link between DeviceC and DeviceA goes down, DeviceC sends a Layer 3 unicast negotiation request to DeviceB to ensure that its clock is synchronized with that of the clock server.

**Figure 1** Network diagram of configuring 1588 ACR clock synchronization in a dual-server scenario  
![](figure/en-us_image_0000001779081194.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure DeviceA as server 1.
2. Configure DeviceB as server 2.
3. Configure DeviceC as a client.
4. Configure unicast negotiation on servers and the client.
5. On the client, configure a PTP clock reference source.

#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of the servers and the IP address of the client

#### Procedure

1. Configure DeviceA as server 1.
   
   
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
   [*DeviceA-Loopback0] commit
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
   [*DeviceA] commit
   ```
2. Configure DeviceB as server 2.
   
   
   ```
   <DeviceB> system-view
   ```
   ```
   [~DeviceB] interface loopback 0
   ```
   ```
   [*DeviceB-Loopback0] ip address 2.2.2.2 32
   ```
   ```
   [*DeviceB-Loopback0] commit
   ```
   ```
   [~DeviceB-Loopback0] quit
   ```
   ```
   [~DeviceB] ptp-adaptive enable
   ```
   ```
   [*DeviceB] ptp-adaptive device-type server
   ```
   ```
   [*DeviceB] ptp-adaptive local-ip 2.2.2.2
   ```
   ```
   [*DeviceB] commit
   ```
3. Configure DeviceC as a client.
   
   
   ```
   <DeviceC> system-view
   ```
   ```
   [~DeviceC] interface loopback 0
   ```
   ```
   [*DeviceC-Loopback0] ip address 3.3.3.3 32
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
   [*DeviceC] ptp-adaptive local-ip 3.3.3.3
   ```
   ```
   [*DeviceC] ptp-adaptive remote-server1-ip 1.1.1.1
   ```
   ```
   [*DeviceC] ptp-adaptive remote-server2-ip 2.2.2.2
   ```
   ```
   [*DeviceC] commit
   ```
4. Configure unicast negotiation on servers and the client.
   
   
   
   # Configure server 1.
   
   ```
   [~DeviceA] ptp-adaptive acr unicast-negotiate enable
   ```
   ```
   [*DeviceA] commit
   ```
   
   
   
   # Configure server 2.
   
   ```
   [~DeviceB] ptp-adaptive acr unicast-negotiate enable
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
5. On the client, configure a PTP clock reference source.
   
   
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
6. Verify the configuration.
   
   
   
   # Check the 1588 ACR configuration on DeviceC.
   
   ```
   <DeviceC> display ptp-adaptive all
     Device config info
     ------------------------------------------------------------------------------
     Ptp adaptive state      :enable           Device type        :client
     Sync mode               :frequency        Current state      :slave
     Packet dscp             :56               Domain value       :4
     Announce interval       :11               Announce duration  :300s
     Sync interval           :3                Sync duration      :300s
     Delay_resp interval     :3                Delay_resp duration:400s
     Announce receipt timeout:3                One-way or two-way :one-way
     Local ip                :3.3.3.3          Profile            :frequency
     Client board            :3
     VPN                     :none
   
     BMCA run info
     ------------------------------------------------------------------------------
     Current trace source    :server1
   
     Time performance statistics
     ------------------------------------------------------------------------------
     Realtime(T2-T1)         :+0s, 23281ns
     Max(T2-T1)              :+0s, 26277ns
     Min(T2-T1)              :+0s, 21853ns
   
     Remote server info
     ------------------------------------------------------------------------------
     Ip address                Negotiate state    SSM    Priority    PTSF
     Server1: 1.1.1.1          Nego success       PRC    1           normal
     Server2: 2.2.2.2          Nego success       PRC    1           normal
   ```
   
   # Check the 1588 ACR configuration on the server. Take the display on DeviceA as an example.
   
   ```
   <DeviceA> display ptp-adaptive all
     Device config info
     ------------------------------------------------------------------------------
     Ptp adaptive state      :enable           Device type        :server
     Sync mode               :frequency        Current state      :master
     Packet dscp             :56               Domain value       :4
     Local ip                :1.1.1.1          Profile            :frequency
     Server board            :3
     VPN                     :none
   
     Client info
         ID  Ip Address       Clock ID          Mode     Announce  Sync  Delay_resp
     ------------------------------------------------------------------------------
     1   500 3.3.3.3          00259efffed1efcf  two-way  1         -3    -3
     2   489 4.4.4.4          286ed4fffebcdc76  one-way  1         -3    -3
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
  ```
  ```
  # 
  ```
  ```
  return
  ```
* DeviceB configuration file
  
  ```
  #
  ```
  ```
  sysname DeviceB
  ```
  ```
  #
  ptp-adaptive enable
  ptp-adaptive device-type server
  ptp-adaptive local-ip 2.2.2.2
  ptp-adaptive acr unicast-negotiate enable
  #
  interface Loopback0
   ip address 2.2.2.2 255.255.255.255
  ```
  ```
  # 
  ```
  ```
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
  ptp-adaptive local-ip 3.3.3.3
  ptp-adaptive remote-server1-ip 1.1.1.1
  ptp-adaptive remote-server2-ip 2.2.2.2
  ptp-adaptive acr unicast-negotiate enable
  clock source ptp synchronization enable
  clock source ptp priority 10
  clock source ptp ssm prc
  #
  interface Loopback0
   ip address 3.3.3.3 255.255.255.255
  ```
  ```
  # 
  ```
  ```
  return
  ```
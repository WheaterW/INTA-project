Example for Configuring Time Synchronization of 1588 ATR Transparent Transmission
=================================================================================

In a 1588 ATR domain, a client can establish a client/server relationship with two remote clock servers and send unicast negotiation requests to these clock servers to implement 1588 ATR time synchronization. Once the master clock server becomes faulty, the client automatically initiates a connection request to the slave clock server.

#### Networking Requirements

On the IP RAN shown in [Figure 1](#EN-US_TASK_0000001782038062__fig_dc_ne_atr_cfg_900301), time synchronization needs to be performed between gNodeBs, but the third-party network (such as a microwave or switch network) does not support 1588v2. In this case, 1588 ATR can be configured to allow time synchronization over the third-party network. NE40Es enabled with 1588 ATR can function as a BC to synchronize time information with upstream devices and as a 1588 ATR server to synchronize time information with gNodeBs.

Server1 and Server2 are the master and slave clock servers. A client initiates Layer 3 unicast negotiation requests to both Server1 and Server2 using 1588 ATR packets to obtain time synchronization information. If the client is disconnected from Server1, the client then initiates a Layer 3 unicast negotiation request to Server2 to ensure time synchronization with the clock server.

**Figure 1** 1588 ATR configuration in a dual-server scenario  
![](figure/en-us_image_0000001782197742.png "Click to enlarge")

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure unicast negotiation on a 1588 ATR client.
2. Configure unicast negotiation on Server1 and Server2.

#### Data Preparation

To complete the configuration, you need the following data:

* Local server's IP address
* 1588 ATR domain where the servers reside
* Outbound interface for transmitting 1588 ATR packets
* DSCP priority value of 1588 ATR packets

#### Procedure

1. Configure unicast negotiation on a 1588 ATR client.
   
   
   
   For details about how to configure unicast negotiation on a client, see the related configuration guide.
2. Configure unicast negotiation on Server1 and Server2.
   
   
   * Configure Server1 as the server.
     ```
     <Server1> system-view
     ```
     ```
     [~Server1] interface loopback 0
     ```
     ```
     [*Server1-Loopback0] ip address 1.1.1.1 32
     ```
     ```
     [*Server1-Loopback0] commit
     ```
     ```
     [~Server1-Loopback0] quit
     ```
     ```
     [~Server1] ptp-adaptive enable
     ```
     ```
     [*Server1] ptp-adaptive device-type server
     ```
     ```
     [*Server1] ptp-adaptive time profile
     ```
     ```
     [*Server1] ptp-adaptive domain 45
     ```
     ```
     [*Server1] ptp-adaptive dscp 60
     ```
     ```
     [*Server1] ptp-adaptive local-ip 1.1.1.1
     ```
     ```
     [*Server1] ptp-adaptive atr unicast-negotiate enable
     ```
     ```
     [*Server1] interface gigabitethernet 0/1/0
     ```
     ```
     [*Server1-GigabitEthernet0/1/0] ptp-adaptive atr enable
     ```
     ```
     [*Server1-GigabitEthernet0/1/0] commit
     ```
     ```
     [*Server1-GigabitEthernet0/1/0] quit
     ```
     ```
     [*Server1] commit
     ```
   * Configure unicast negotiation on Server2.
     ```
     <Server2> system-view
     ```
     ```
     [~Server2] interface loopback 0
     ```
     ```
     [*Server2-Loopback0] ip address 2.2.2.2 32
     ```
     ```
     [*Server2-Loopback0] commit
     ```
     ```
     [~Server2-Loopback0] quit
     ```
     ```
     [~Server2] ptp-adaptive enable
     ```
     ```
     [*Server2] ptp-adaptive device-type server
     ```
     ```
     [*Server2] ptp-adaptive time profile
     ```
     ```
     [*Server2] ptp-adaptive domain 45
     ```
     ```
     [*Server2] ptp-adaptive dscp 60
     ```
     ```
     [*Server2] ptp-adaptive local-ip 2.2.2.2
     ```
     ```
     [*Server2] ptp-adaptive atr unicast-negotiate enable
     ```
     ```
     [*Server2] interface gigabitethernet 0/1/0
     ```
     ```
     [*Server2-GigabitEthernet0/1/0] ptp-adaptive atr enable
     ```
     ```
     [*Server2-GigabitEthernet0/1/0] commit
     ```
     ```
     [*Server2-GigabitEthernet0/1/0] quit
     ```
     ```
     [*Server2] commit
     ```
3. Verify the configuration.
   
   
   
   # View all configurations of the 1588 ATR module on the servers. The following example uses the command output on Server1.
   
   ```
   <Server1> display ptp-adaptive all
   ```
   ```
   Device config info
   -------------------------------------------------------------------------------
   Ptp adaptive state      :enable           Device type        :server
   Sync mode               :time             Current state      :master
   Packet dscp             :60               Domain value       :45
   Local ip                :1.1.1.1          Server board       :3
   Profile                 :time
   VPN                     :none
   
   Client info
       ID  Ip Address       Clock ID          Mode     Announce  Sync  Delay_resp
   -------------------------------------------------------------------------------
   0   0   3.3.3.3          2cab00fffec65e58  two-way  1         -7    -7
   1   1   4.4.4.4          286ed4fffebcdc76  two-way  1         -7    -7
   
   ```
   
   # View 1588 ATR related configurations on the servers. The following example uses the command output on Server1.
   
   ```
   <Server1> display ptp-adaptive config
   ```
   ```
   Device config info
   -------------------------------------------------------------------------------
   Ptp adaptive state      :enable           Device type        :server
   Sync mode               :time             Current state      :master
   Packet dscp             :60               Domain value       :45
   Local ip                :1.1.1.1          Server board       :
   3
   Profile                 :time
   VPN                     :none
   
   Port config info
   Name                         ATR enable
   -----------------------------------
   GigabitEthernet0/1/0         true
   
   ```
   
   # View configurations of the 1588 ATR client.
   
   ```
   <Server1> display ptp-adaptive client 0
   ```
   ```
   Client id           :0                 IP address          :3.3.3.3
   Clock id            :2cab00fffec65e58  Mode                :two-way
   Announce interval   :1                 Announce duration   :300s
   Sync interval       :-7                Sync duration       :300s
   Delay_resp interval :-7                Delay_resp duration :300s
   
   Receive packet statistics
   ---------------------------------------------------------------------------
   Signalling          :60                Delay_req           :655778
   
   Send packet statistics
   ---------------------------------------------------------------------------
   Signalling          :60                Announce            :2547
   Sync                :655945            Delay_resp          :655778
   
   Discard packet statistics
   ---------------------------------------------------------------------------
   Signalling          :0
   Delay_req           :0
   
   ```

#### Configuration Files

* Server1 configuration file
  
  ```
  #
  ```
  ```
  sysname Server1
  ```
  ```
  #
  ptp-adaptive enable
  ptp-adaptive device-type server
  ptp-adaptive time profile
  ptp-adaptive domain 45
  ptp-adaptive dscp 60
  ptp-adaptive local-ip 1.1.1.1
  ptp-adaptive atr unicast-negotiate enable
  #
  interface gigabitethernet 0/1/0
   ptp-adaptive atr enable
  #
  interface LoopBack0                                                                                                                 
   ip address 1.1.1.1 255.255.255.255
  ```
  ```
  # 
  ```
  ```
  return
  ```
* Server2 configuration file
  
  ```
  #
  ```
  ```
  sysname Server2
  ```
  ```
  #
  ptp-adaptive enable
  ptp-adaptive device-type server
  ptp-adaptive time profile
  ptp-adaptive domain 45
  ptp-adaptive dscp 60
  ptp-adaptive local-ip 2.2.2.2
  ptp-adaptive atr unicast-negotiate enable
  #
  interface gigabitethernet 0/1/0
   ptp-adaptive atr enable
  #
  interface LoopBack0                                                                                                                 
   ip address 2.2.2.2 255.255.255.255
  ```
  ```
  # 
  ```
  ```
  return
  ```
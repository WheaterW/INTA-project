Example for Configuring a Delay for a BFD Session to Go Up
==========================================================

This section provides an example for configuring a delay for a BFD session to go up. This configuration prevents traffic loss because a routing protocol goes up later than an interface.

#### Networking Requirements

Some devices switch traffic according to whether a BFD session is up. When a routing protocol goes up later than an interface, no route can be found during traffic switchbacks. As a result, traffic is discarded. To resolve this issue, configure a delay to compensate for the time difference caused when the routing protocol goes up later than the interface.

As shown in [Figure 1](#EN-US_TASK_0172361715__fig_dc_vrp_bfd_cfg_006501), BFD in asynchronous mode is used to monitor the direct link between DeviceA and DeviceB.

**Figure 1** Configuring a delay for a BFD session to go up![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 represents GE 0/1/0.

  
![](figure/en-us_image_0000001508389141.png)  




#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a BFD session on DeviceA to monitor the direct link from DeviceA to DeviceB.
2. Configure a BFD session on DeviceB to monitor the direct link from DeviceB to DeviceA.

#### Precautions

None


#### Data Preparation

To complete the configuration, you need the following data:

* Peer IP address monitored by BFD
* IP address of a local interface that sends and receives BFD control packets
* Name of the BFD session
* Local and remote discriminators of BFD sessions
* Delay of the BFD session to go up

#### Procedure

1. Assign IP addresses to the interfaces connecting DeviceA and DeviceB.
   
   
   
   # Assign an IP address to the interface on DeviceA.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceA
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] ip address 10.1.1.1 24
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] quit
   ```
   
   # Assign an IP address to the interface on DeviceB.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceB
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceB] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] ip address 10.1.1.2 24
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] quit
   ```
2. Configure a delay for the BFD session to go up.
   
   
   
   # Enable BFD on DeviceA and set the delay of the BFD session to go up to 120s in the BFD view.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   To configure the delay of a BFD session to go up, run the **delay-up** command only in the BFD view. This command takes effect only for BFD sessions to be established.
   
   ```
   [~DeviceA] bfd
   ```
   ```
   [*DeviceA-bfd] delay-up 120
   ```
   ```
   [*DeviceA-bfd] commit
   ```
   ```
   [~DeviceA-bfd] quit
   ```
   
   # Configure BFD on DeviceA. The following example uses the configuration of single-hop BFD.
   
   ```
   [~DeviceA] bfd atob bind peer-ip 10.1.1.2 interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceA-bfd-session-atob] discriminator local 10
   ```
   ```
   [*DeviceA-bfd-session-atob] discriminator remote 20
   ```
   ```
   [*DeviceA-bfd-session-atob] commit
   ```
   ```
   [~DeviceA-bfd-session-atob] quit
   ```
   
   # Enable BFD on DeviceB and set the delay of the BFD session to go up to 120s in the BFD view.
   
   ```
   [~DeviceB]bfd
   ```
   ```
   [*DeviceB-bfd] delay-up 120
   ```
   ```
   [*DeviceB-bfd] commit
   ```
   ```
   [~DeviceB-bfd] quit
   ```
   
   # Configure BFD on DeviceB. The following example uses the configuration of single-hop BFD.
   
   ```
   [~DeviceB] bfd btoa bind peer-ip 10.1.1.1 interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceB-bfd-session-btoa] discriminator local 20
   ```
   ```
   [*DeviceB-bfd-session-btoa] discriminator remote 10
   ```
   ```
   [*DeviceB-bfd-session-btoa] commit
   ```
   ```
   [~DeviceB-bfd-session-btoa] quit
   ```
3. Verify the configuration.
   
   
   
   After completing the configurations, run the **display bfd statistics** command on DeviceA and DeviceB. The command output shows that **System Session Delay Up Timer** is **120**, indicating that the BFD session goes up after a delay of 120s.
   
   # The following example uses the command output on DeviceA.
   
   ```
   [~DeviceA] display bfd statistics
   ```
   ```
   Current Display Board Number : Main
   Total Up/Down Session Number : 1/0
   Total Up/Down Main Session Number : 0/0
   Total Up/Down Sub Session Number  : 0/0
   Total Used/Supported Resource Number  : 1/12288
   Total Used/Supported Crc Resource Number  : 0/1024
   Current Session Number :
         Static session           : 1                Dynamic session        : 0
         E_Dynamic session        : 0                STATIC_AUTO session    : 0
         LDP_LSP session          : 0                STATIC_LSP session     : 0
         TE_TUNNEL session        : 0                TE_LSP session         : 0
         PW session               : 0                IP session             : 1
         VSI PW session           : 0               
   --------------------------------------------------------------------------------
   PAF/LCS Name                       Maxnum         Minnum         Create
   --------------------------------------------------------------------------------
   BFD_SESSION_NUM                    12288          1              1
   BFD_IO_SESSION_NUM                 4096           1              -
   --------------------------------------------------------------------------------
   IO Board Current Create Session Statistics Information :(slot/number)
   --------------------------------------------------------------------------------
   0 /0     2/1        
   --------------------------------------------------------------------------------
   Current Total Used Discriminator Num               : 1
   --------------------------------------------------------------------------------
   BFD HA Information :
   --------------------------------------------------------------------------------
   Current HA Status                                  : Work
   --------------------------------------------------------------------------------
   BFD for LSP Information :
   --------------------------------------------------------------------------------
   Ability of auto creating BFD session on egress     : Disable 
   Period of LSP Ping                                 : 60
   --------------------------------------------------------------------------------
   BFD Global Information :
   --------------------------------------------------------------------------------
   System Session Delay Up Timer                      : 120 s  
   --------------------------------------------------------------------------------
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
  ```
  ```
  bfd
  ```
  ```
   delay-up 120
  ```
  ```
  #
  ```
  ```
  interface gigabitethernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.1.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  bfd atob bind peer-ip 10.1.1.2 interface gigabitethernet 0/1/0
  ```
  ```
   discriminator local 10
  ```
  ```
   discriminator remote 20
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
  ```
  ```
  bfd
  ```
  ```
   delay-up 120
  ```
  ```
  #
  ```
  ```
  interface gigabitethernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.1.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  bfd btoa bind peer-ip 10.1.1.1 interface gigabitethernet 0/1/0
  ```
  ```
   discriminator local 20
  ```
  ```
   discriminator remote 10
  ```
  ```
  #
  ```
  ```
  return
  ```
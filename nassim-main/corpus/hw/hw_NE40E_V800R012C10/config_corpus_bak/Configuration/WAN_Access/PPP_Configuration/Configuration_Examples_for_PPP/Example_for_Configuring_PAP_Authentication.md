Example for Configuring PAP Authentication
==========================================

This section provides an example for configuring PAP authentication.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172364190__fig_dc_vrp_ppp_cfg_002201), DeviceA and DeviceB are connected through LMP interfaces, and DeviceA is required to authenticate DeviceB in PAP mode.

**Figure 1** Networking diagram for configuring PAP authentication![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1 in this example represents Lmpif0/1/0.


  
![](figure/en-us_image_0000001399677229.png)

#### Precautions

None


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Adopt the AAA authentication scheme and add the username and password of DeviceB to the local user list of DeviceA.
2. Perform configuration on the LMP interface of DeviceA to enable DeviceA to authenticate DeviceB in PAP mode.
3. Configure a username and password on the LMP interface of DeviceB.

#### Data Preparation

To complete the configuration, you need the following data:

* Username and password of DeviceB
* Interface IP address of DeviceA
* Interface IP address of DeviceB

#### Procedure

1. Configure DeviceA.
   
   
   
   # Add the username and password of DeviceB to the local user list of DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] aaa
   [*DeviceA-aaa] local-user rtb password cipher YsHsjx_202206
   [*DeviceA-aaa] local-user rtb service-type ppp
   [*DeviceA-aaa] authentication-scheme default1  
   [*DeviceA-aaa-authen-default1] authentication-mode local
   [*DeviceA-aaa-authen-default1] commit
   [~DeviceA-aaa-authen-default1] quit
   [~DeviceA-aaa] quit
   ```
   
   # Configure an IP address for Lmpif0/1/0 and set the link-layer encapsulation protocol of this interface to PPP.
   
   ```
   [~DeviceA] interface Lmpif 0/1/0
   ```
   ```
   [~DeviceA-Lmpif0/1/0] ip address 10.110.0.1 255.255.255.0
   ```
   ```
   [*DeviceA-Lmpif0/1/0] link-protocol ppp
   ```
   
   # Configure DeviceA to authenticate DeviceB in PAP mode.
   
   ```
   [*DeviceA-Lmpif0/1/0] ppp authentication-mode pap
   ```
   ```
   [*DeviceA-Lmpif0/1/0] undo shutdown
   ```
   
   # Commit the configuration.
   
   ```
   [*DeviceA-Lmpif0/1/0] commit
   ```
2. Configure DeviceB.
   
   
   
   # Configure an IP address for Lmpif0/1/0 and set the link-layer encapsulation protocol of this interface to PPP.
   
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
   [~DeviceB] interface Lmpif0/1/0
   ```
   ```
   [~DeviceB-Lmpif0/1/0] ip address 10.110.0.2 255.255.255.0
   ```
   ```
   [*DeviceB-Lmpif0/1/0] link-protocol ppp
   ```
   
   # Configure DeviceB to send its username and password to DeviceA.
   
   ```
   [*DeviceB-Lmpif0/1/0] ppp pap local-user rtb password cipher YsHsjx_202206
   ```
   ```
   [*DeviceB-Lmpif0/1/0] undo shutdown
   ```
   
   # Commit the configuration.
   
   ```
   [*DeviceB-Lmpif0/1/0] commit
   ```
3. Verify the configuration.
   
   After the configuration is complete, run the **display interface** command on both DeviceA and DeviceB. The command output shows that the LCP status of both devices is **LCP opened**. The following example uses the command output on DeviceA.
   ```
   [~DeviceA] display interface Lmpif 0/1/0
   ```
   ```
   Lmpif0/1/0 current state : UP (ifindex: 15)
   ```
   ```
   Line protocol current state : UP
   ```
   ```
   Description:
   ```
   ```
   Route Port,The Maximum Transmit Unit is 1500
   ```
   ```
   Internet Address is 10.110.0.1/24
   ```
   ```
   Link layer protocol is PPP
   ```
   ```
   LCP opened, IPCP opened
   ```
   ```
   Current BW: 100 Mbits
   ```
   ```
   Statistics last cleared:never:
   ```
   ```
     Last 300 seconds input rate 0 bits/sec, 0 packets/sec 
   ```
   ```
     Last 300 seconds output rate 0 bits/sec, 0 packets/sec
   ```
   ```
     Input: 0 packets, 0 bytes
   ```
   ```
     Input error: 0 shortpacket, 0 longpacket, 0 CRC, 0 lostpacket
   ```
   ```
     Output: 0 packets, 0 bytes
   ```
   ```
     Output error: 0 lostpackets
   ```
   ```
     Output error: 0 overrunpackets, 0 underrunpackets
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
  interface Lmpif0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   link-protocol ppp
  ```
  ```
   ip address 10.110.0.1 255.255.255.0
  ```
  ```
   ppp authentication-mode pap
  ```
  ```
  #
  ```
  ```
  aaa
  ```
  ```
   local-user rtb password cipher @%@%j]v~7%f[#S'W>j9zzM)3,*!u@%@%
   local-user rtb service-type ppp
  ```
  ```
   #
   authentication-scheme default1  
    authentication-mode local
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
  interface Lmpif0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   link-protocol ppp
  ```
  ```
   ip address 10.110.0.2 255.255.255.0
  ```
  ```
   ppp pap local-user rtb password cipher @%@%j]v~7%f[#S'W>j9zzM)3,*!u@%@%
  ```
  ```
  #
  ```
  ```
  return
  ```
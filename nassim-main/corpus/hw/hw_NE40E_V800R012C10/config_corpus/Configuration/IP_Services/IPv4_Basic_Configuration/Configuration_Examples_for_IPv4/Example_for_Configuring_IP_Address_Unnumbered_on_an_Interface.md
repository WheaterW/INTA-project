Example for Configuring IP Address Unnumbered on an Interface
=============================================================

This section provides an example for configuring IP address unnumbered on an interface.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172364945__fig_dc_vrp_ipv4_cfg_002701), an enterprise builds its intranet through an integrated services digital network (ISDN). DeviceA and DeviceB connect to a local LAN through GE 0/1/0 and connect to each other over the ISDN through dialing interfaces GE 0/2/0. To save IP address resources, the dialing interfaces are configured to borrow IP addresses from GE 0/1/0.

**Figure 1** Configuring IP address unnumbered on an interface![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/0 and GE 0/2/0, respectively.


  
![](images/fig_dc_vrp_ipv4_cfg_002701.png)

#### Precautions

None


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IP addresses to be borrowed.
2. Configure interfaces to borrow IP addresses from other interfaces.

#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of the numbered interfaces
* Numbers of the numbered interfaces

#### Procedure

1. Configure DeviceA.
   
   
   
   # Configure an IP address for GE 0/1/0.
   
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
   [~DeviceA-GigabitEthernet0/1/0] ip address 172.16.10.1 255.255.255.0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] quit
   ```
   
   # Configure GE 0/2/0 to borrow the IP address from GE 0/1/0.
   
   ```
   [*DeviceA] interface GigabitEthernet 0/2/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] ip address unnumbered interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] undo shutdown
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] quit
   ```
2. Configure DeviceB.
   
   
   
   # Configure an IP address for GE 0/1/0.
   
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
   [~DeviceB-GigabitEthernet0/1/0] ip address 172.16.20.1 255.255.255.0
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] quit
   ```
   
   # Configure GE 0/2/0 to borrow the IP address from GE 0/1/0.
   
   ```
   [*DeviceB] interface GigabitEthernet 0/2/0
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0] ip address unnumbered interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0] undo shutdown
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0] quit
   ```
   
   # Configure a route to the Ethernet network segment of DeviceB.
   
   ```
   [*DeviceA] ip route-static 172.16.20.0 255.255.255.0 GigabitEthernet 0/2/0
   ```
   ```
   [*DeviceA] commit
   ```
3. Verify the configuration.
   
   
   
   # Ping the IP address of DeviceB's interface that directly connects to DeviceA from DeviceA. The ping operation is successful.
   
   ```
   [~DeviceA] ping 172.16.20.1
   ```
   ```
     PING 172.16.20.2: 56  data bytes, press CTRL_C to break
   ```
   ```
       Reply from 172.16.20.2: bytes=56 Sequence=1 ttl=255 time=25 ms
   ```
   ```
       Reply from 172.16.20.2: bytes=56 Sequence=2 ttl=255 time=25 ms
   ```
   ```
       Reply from 172.16.20.2: bytes=56 Sequence=3 ttl=255 time=26 ms
   ```
   ```
       Reply from 172.16.20.2: bytes=56 Sequence=4 ttl=255 time=26 ms
   ```
   ```
       Reply from 172.16.20.2: bytes=56 Sequence=5 ttl=255 time=26 ms
   ```
   ```
     --- 172.16.20.2 ping statistics ---
   ```
   ```
       5 packet(s) transmitted
   ```
   ```
       5 packet(s) received
   ```
   ```
       0.00% packet loss
   ```
   ```
       round-trip min/avg/max = 25/25/26 ms
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
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 172.16.10.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address unnumbered interface GigabitEthernet0/1/0
  ```
  ```
  #
  ```
  ```
  ip route-static 172.16.20.0 255.255.255.0 GigabitEthernet0/2/0
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
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 172.16.20.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address unnumbered interface GigabitEthernet0/1/0
  ```
  ```
  #
  ```
  ```
  ip route-static 172.16.10.0 255.255.255.0 GigabitEthernet0/2/0
  ```
  ```
  #
  ```
  ```
  return
  ```
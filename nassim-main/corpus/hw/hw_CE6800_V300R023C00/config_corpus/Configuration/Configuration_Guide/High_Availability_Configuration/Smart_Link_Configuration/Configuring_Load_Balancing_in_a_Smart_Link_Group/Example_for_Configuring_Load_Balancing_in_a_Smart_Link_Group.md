Example for Configuring Load Balancing in a Smart Link Group
============================================================

Example for Configuring Load Balancing in a Smart Link Group

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0000001130623728__fig55359209437), dual-uplink networking is used on the user side of the network to enhance network reliability. Multiple VLANs carry data traffic transmitted on the network. To maximize link utilization, the customer requires that data traffic be forwarded on both uplinks. Service interruption resulting from a link switchover must be within milliseconds.

#### 

**Figure 1** Network diagram of load balancing in a Smart Link group![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent 100GE 1/0/1 and 100GE 1/0/2, respectively.


  
![](figure/en-us_image_0000001176663281.png)


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Map VLAN 500 of which traffic needs to be transmitted through the secondary link to instance 10 on DeviceA.
2. Configure a Smart Link group on DeviceA, and add interface1 and interface2 to the Smart Link group.
3. Configure load balancing on DeviceA so that data traffic from the VLAN mapped to instance 10 is forwarded over the secondary link.
4. Enable the switchback function of the Smart Link group on DeviceA so that traffic is switched back to the original primary link when the link recovers.
5. Configure DeviceA to send Flush packets.
6. Configure interfaces of DeviceB, DeviceC, and DeviceD to receive Flush packets.
7. Enable the Smart Link group on DeviceA.

#### Procedure

1. Configure VLANs.
   
   # Create VLANs on DeviceA and configure related interfaces to allow packets of these VLANs to pass through. The configurations of DeviceB, DeviceC, and DeviceD are similar to the configuration of DeviceA. For detailed configurations, see the Configuration Scripts.
   
   ```
   <HUAWEI> system-view 
   [~HUAWEI] sysname DeviceA 
   [*HUAWEI] commit 
   [~DeviceA] vlan batch 10 100 500  
   [*DeviceA] interface 100ge1/0/1 
   [*DeviceA-100GE1/0/1] portswitch
   [*DeviceA-100GE1/0/1] port link-type trunk 
   [*DeviceA-100GE1/0/1] port trunk allow-pass vlan 10 100 500
   [*DeviceA-100GE1/0/1] stp disable 
   [*DeviceA-100GE1/0/1] quit 
   [*DeviceA] commit 
   [~DeviceA] interface 100ge 1/0/2 
   [*DeviceA-100GE1/0/2] portswitch
   [*DeviceA-100GE1/0/2] port link-type trunk 
   [*DeviceA-100GE1/0/2] port trunk allow-pass vlan 100 500
   [*DeviceA-100GE1/0/2] stp disable
   [*DeviceA-100GE1/0/2] quit 
   [*DeviceA] commit
   ```
2. Configure VLAN mapping on DeviceA.
   ```
   [~DeviceA] stp region-configuration 
   [*DeviceA-mst-region] instance 10 vlan 500 
   [*DeviceA-mst-region] quit 
   [*DeviceA] commit
   ```
3. Add STP-disabled uplink interfaces on DeviceA to the Smart Link group and specify them as the master and slave interfaces.
   ```
   [~DeviceA] smart-link group 1 
   [*DeviceA-smlk-group1] port 100ge 1/0/1 master 
   [*DeviceA-smlk-group1] port 100ge 1/0/2 slave 
   [*DeviceA-smlk-group1] commit
   ```
4. Configure load balancing on DeviceA.
   ```
   [~DeviceA-smlk-group1] load-balance instance 10 slave 
   [*DeviceA-smlk-group1] commit
   ```
5. Enable the switchback function on DeviceA and configure the WTR time.
   ```
   [*DeviceA-smlk-group1] restore enable 
   [*DeviceA-smlk-group1] timer wtr 120 
   [*DeviceA-smlk-group1] commit
   ```
6. Configure DeviceA to send Flush packets containing an HMAC-SHA256-encrypted password.
   ```
   [~DeviceA-smlk-group1] flush send control-vlan 10 password hmac-sha256 123 
   [*DeviceA-smlk-group1] commit
   ```
7. Configure devices to receive Flush packets.
   
   # Configure DeviceB to receive Flush packets containing an HMAC-SHA256-encrypted password.
   
   ```
   [~DeviceB] interface 100ge 1/0/1 
   [*DeviceB-100GE1/0/1] portswitch
   [*DeviceB-100GE1/0/1] stp disable 
   [*DeviceB-100GE1/0/1] smart-link flush receive control-vlan 10 password hmac-sha256 123
   [*DeviceB-100GE1/0/1] quit 
   [*DeviceB] commit 
   [~DeviceB] interface 100ge 1/0/2 
   [*DeviceB-100GE1/0/2] smart-link flush receive control-vlan 10 password hmac-sha256 123
   [*DeviceB-100GE1/0/2] quit 
   [*DeviceB] commit
   ```
   
   # Configure DeviceC to receive Flush packets containing an HMAC-SHA256-encrypted password.
   
   ```
   [~DeviceC] interface 100ge 1/0/1 
   [*DeviceC-100GE1/0/1] portswitch
   [*DeviceC-100GE1/0/1] stp disable 
   [*DeviceC-100GE1/0/1] smart-link flush receive control-vlan 10 password hmac-sha256 123 
   [*DeviceC-100GE1/0/1] quit 
   [*DeviceC] commit
   [~DeviceC] interface 100ge 1/0/2
   [*DeviceC-100GE1/0/2] smart-link flush receive control-vlan 10 password hmac-sha256 123
   [*DeviceC-100GE1/0/2] quit 
   [*DeviceC] commit
   ```
   
   # Configure DeviceD to receive Flush packets containing an HMAC-SHA256-encrypted password.
   
   ```
   [~DeviceD] interface 100ge 1/0/1
   [*DeviceD-100GE1/0/1] smart-link flush receive control-vlan 10 password hmac-sha256 123
   [*DeviceD-100GE1/0/1] quit 
   [*DeviceD] commit 
   [~DeviceD] interface 100ge 1/0/2
   [*DeviceD-100GE1/0/2] smart-link flush receive control-vlan 10 password hmac-sha256 123
   [*DeviceD-100GE1/0/2] quit 
   [*DeviceD] commit
   ```
8. Enable the Smart Link group on DeviceA.
   
   ```
   [~DeviceA-smlk-group1] smart-link enable 
   [*DeviceA-smlk-group1] commit 
   ```

#### Verifying the Configuration

# Run the **display smart-link group** command to view information about the Smart Link group on DeviceA. If the following information is displayed, the configuration is successful:
```
[~DeviceA] display smart-link group 1 
Smart Link group 1 information :  
Smart Link group: enabled
Wtr-time is: 120 sec.
Load-Balance Instance: --   
Protected-VLAN reference-instance: --    
DeviceID: 00e0-fc12-3456  
Control-VLAN ID: 10   
Member       Role    InstanceID  State      Flush Count  Last-Flush-Time   
-----------------------------------------------------------------------------------   
100GE1/0/1    Master           0  Active              0   0000/00/00 00:00:00 UTC+00:00
100GE1/0/1    Master          10  Inactive            0   0000/00/00 00:00:00 UTC+00:00
100GE1/0/2    Slave            0  Inactive            0   0000/00/00 00:00:00 UTC+00:00
100GE1/0/2    Slave           10  Active              0   0000/00/00 00:00:00 UTC+00:00
```

# Run the **shutdown** command to shut down interface 100GE 1/0/1. The command output shows that interface 100GE 1/0/1 is in the Inactive state, and interface 100GE 1/0/2 is in the Active state.

```
[~DeviceA] interface 100ge 1/0/1
[*DeviceA-100GE1/0/1] shutdown 
[*DeviceA-100GE1/0/1] commit 
[~DeviceA-100GE1/0/1] display smart-link group 1 
Smart Link group 1 information :   
Smart Link group: enabled   
Wtr-time is: 120 sec.   
Load-Balance Instance: --                                                                                                            
Protected-VLAN reference-instance: --   
DeviceID: 00e0-fc12-3456  
Control-VLAN ID: 10   
Member       Role    InstanceID  State      Flush Count  Last-Flush-Time   
------------------------------------------------------------------------------------   
100GE1/0/1    Master           0  Inactive            0   2020/03/22 00:00:00 UTC+00:00
100GE1/0/1    Master          10  Inactive            0   2020/03/22 00:00:00 UTC+00:00
100GE1/0/2    Slave            0  Active              1   2020/03/22 10:34:46 UTC+00:00
100GE1/0/2    Slave           10  Active              1   2020/03/22 10:34:46 UTC+00:00
```

# Run the **undo shutdown** command to enable interface 100GE 1/0/1.

```
[~DeviceA-100GE1/0/1] undo shutdown 
[*DeviceA-100GE1/0/1] commit
```

# Check the interface state after 120 seconds. The command output shows that interface 100GE 1/0/1 is in the Active state, and interface 100GE 1/0/2 is in the Inactive state.

```
[~DeviceA-100GE1/0/1] display smart-link group 1 
Smart Link group 1 information :   
Smart Link group: enabled   
Wtr-time is: 120 sec.   
Load-Balance Instance: --                                                                                                            
Protected-VLAN reference-instance: --   
DeviceID: 00e0-fc12-3456  Control-VLAN ID: 10   
Member       Role    InstanceID  State      Flush Count  Last-Flush-Time   
-----------------------------------------------------------------------------------   
100GE1/0/1    Master           0  Active              1   2020/03/22 10:35:46 UTC+00:00
100GE1/0/1    Master          10  Inactive            1   2020/03/22 10:35:46 UTC+00:00
100GE1/0/2    Slave            0  Inactive            1   2020/03/22 10:34:46 UTC+00:00
100GE1/0/2    Slave           10  Active              1   2020/03/22 10:34:46 UTC+00:00
```

#### Configuration Scripts

* DeviceA
  
  ```
  # 
  sysname DeviceA 
  # 
  vlan batch 10 100 500
  # 
  stp region-configuration  
   instance 10 vlan 500
  # 
  interface 100GE1/0/1
   
   port link-type trunk  
   port trunk allow-pass vlan 10 100 500  
   stp disable 
  # 
  interface 100GE1/0/2
   
   port link-type trunk  
   port trunk allow-pass vlan 10 100 500  
   stp disable 
  # 
  smart-link group 1  
   restore enable  
   smart-link enable  
   port 100GE1/0/1 master  
   port 100GE1/0/2 slave  
   timer wtr 120  
   flush send control-vlan 10 password hmac-sha256 %^%#c+p$W[eADi"zB!@-Nh"jtHO)L7YQ2VwcC27#D/%^%#
  # 
  return
  ```
* DeviceB
  
  ```
  # 
  sysname DeviceB 
  # 
  vlan batch 10 100 500 
  # 
  interface 100GE1/0/1
   
   port link-type trunk  
   port trunk allow-pass vlan 10 100 500 
   stp disable  
   smart-link flush receive control-vlan 10 password hmac-sha256 %^%#Ep7t@o-'kXRUn$Lwgf22l+{8Ryqof3i+6z&$V\</%^%# 
  # 
  interface 100GE1/0/2
   
   port link-type trunk  
   port trunk allow-pass vlan 10 100 500
   smart-link flush receive control-vlan 10 password hmac-sha256 %^%#iu+l&X\dP3}",:H'1F#PBIp`1a3GB'v0sUK]2zxO%^%# 
  # 
  return
  ```
* DeviceC
  ```
  # 
  sysname DeviceC 
  # 
  vlan batch 10 100 500 
  # 
  interface 100GE1/0/1
   
   port link-type trunk  
   port trunk allow-pass vlan 10 100 500  
   stp disable  
   smart-link flush receive control-vlan 10 password hmac-sha256 %^%#[:95Guh"OENC;];s3nN8K++m=^Bg*ZtRBRO0ZV66%^%# 
  # interface 100GE1/0/2
   
   port link-type trunk  
   port trunk allow-pass vlan 10 100 500  
   smart-link flush receive control-vlan 10 password hmac-sha256 %^%#yQWMQ1a{,`#C)IvAvt16MDIzYY!.\E#Q>6qE=%^%# 
  # 
  return
  ```
* DeviceD
  ```
  # 
  sysname DeviceD 
  # 
  vlan batch 10 100 500 
  # 
  interface 100GE1/0/1
   
   port link-type trunk  
   port trunk allow-pass vlan 10 100 500  
   smart-link flush receive control-vlan 10 password hmac-sha256 %^%#;Bw$EMeC,".A@u1Xd%CO];DdK'+'Q*Xi,0'M%46+%^%# 
  # 
  interface 100GE1/0/2
   
   port link-type trunk  
   port trunk allow-pass vlan 10 100 500  
   smart-link flush receive control-vlan 10 password hmac-sha256 %^%#wT5!@We"Pj1w*Ch$%-27+B.YD&+=H>(%!{s\'%^%# 
  # 
  return
  ```
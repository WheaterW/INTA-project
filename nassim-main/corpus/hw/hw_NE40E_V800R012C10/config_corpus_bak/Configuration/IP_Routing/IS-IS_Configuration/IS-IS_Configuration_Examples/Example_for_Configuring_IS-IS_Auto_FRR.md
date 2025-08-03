Example for Configuring IS-IS Auto FRR
======================================

Example_for_Configuring_IS-IS_Auto_FRR

#### Networking Requirements

If a fault occurs on a network, IS-IS Auto FRR fast switches traffic to a backup link before the route convergence, which prevents traffic interruption.

In [Figure 1](#EN-US_TASK_0172366111__fig_dc_vrp_isis_cfg_009201):

* IS-IS runs between four Routers.
* The four Routers are all Level-1-2 Routers.
* If DeviceC or Link T fails, it is required that the traffic forwarded by DeviceA be rapidly switched to the backup link.

**Figure 1** Configuring IS-IS Auto FRR  
![](figure/en-us_image_0256720277.png)

| Device Name | Interface | IP Address |
| --- | --- | --- |
| DeviceA | GE0/1/0 | 10.0.1.1/24 |
| GE0/2/0 | 10.1.1.1/24 |
| DeviceB | GE0/1/0 | 10.1.1.2/24 |
| GE0/2/0 | 10.2.1.1/24 |
| DeviceC | GE0/1/0 | 10.0.1.2/24 |
| GE0/2/0 | 10.3.1.1/24 |
| DeviceD | GE0/1/0 | 10.3.1.2/24 |
| GE0/2/0 | 10.2.1.2/24 |
| GE0/3/0 | 10.4.1.1/24 |



#### Precautions

To improve security, you are advised to configure IS-IS authentication. For details, see "Configuring IS-IS Authentication." IS-IS interface authentication is used as an example. For details, see Example for Configuring Basic IS-IS Functions.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable basic IS-IS functions on each Router.
2. Set a higher link cost (in compliance with the traffic protection inequality of IS-IS Auto FRR) on GE 0/2/0 of DeviceA, and ensure that Link T is preferentially selected.
3. Enable IS-IS Auto FRR on DeviceA that forwards the protected traffic.

#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of interfaces on each Router
* NET of each Router
* Level of each Router
* Costs of interfaces on each Router

#### Procedure

1. Configure IP addresses for interfaces. For configuration details, see [Configuration Files](#EN-US_TASK_0172366111__section_dc_vrp_cfg_00649405) in this section.
2. Configure basic IS-IS functions.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] isis 1
   ```
   ```
   [*DeviceA-isis-1] is-level level-1-2
   ```
   ```
   [*DeviceA-isis-1] network-entity 10.0000.0000.0001.00
   ```
   ```
   [*DeviceA-isis-1] quit
   ```
   ```
   [*DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] isis enable 1
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceA] interface gigabitethernet 0/2/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] isis enable 1
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/0] quit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] isis 1
   ```
   ```
   [*DeviceB-isis-1] is-level level-1-2
   ```
   ```
   [*DeviceB-isis-1] network-entity 10.0000.0000.0002.00
   ```
   ```
   [*DeviceB-isis-1] quit
   ```
   ```
   [*DeviceB] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] isis enable 1
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceB] interface gigabitethernet 0/2/0
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0] isis enable 1
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/2/0] quit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] isis 1
   ```
   ```
   [*DeviceC-isis-1] is-level level-1-2
   ```
   ```
   [*DeviceC-isis-1] network-entity 10.0000.0000.0003.00
   ```
   ```
   [*DeviceC-isis-1] quit
   ```
   ```
   [*DeviceC] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] isis enable 1
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceC] interface gigabitethernet 0/2/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] isis enable 1
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] commit
   ```
   ```
   [~DeviceC-GigabitEthernet0/2/0] quit
   ```
   
   # Configure DeviceD.
   
   ```
   [~DeviceD] isis 1
   ```
   ```
   [*DeviceD-isis-1] is-level level-1-2
   ```
   ```
   [*DeviceD-isis-1] network-entity 10.0000.0000.0004.00
   ```
   ```
   [*DeviceD-isis-1] quit
   ```
   ```
   [*DeviceD] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/0] isis enable 1
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceD] interface gigabitethernet 0/2/0
   ```
   ```
   [*DeviceD-GigabitEthernet0/2/0] isis enable 1
   ```
   ```
   [*DeviceD-GigabitEthernet0/2/0] commit
   ```
   ```
   [~DeviceD-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceD] interface gigabitethernet 0/3/0
   ```
   ```
   [*DeviceD-GigabitEthernet0/3/0] isis enable 1
   ```
   ```
   [*DeviceD-GigabitEthernet0/3/0] commit
   ```
   ```
   [~DeviceD-GigabitEthernet0/3/0] quit
   ```
3. Set the cost of Gigabit Ethernet 0/2/0 on DeviceA to 30, and then check routing information.
   
   
   
   # Configure the cost of GE 0/2/0 on DeviceA to 30.
   
   ```
   [~DeviceA] interface gigabitethernet 0/2/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/0] isis cost 30
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/0] quit
   ```
   # Check information about the link from DeviceA to DeviceD. IS-IS preferentially selects link T to transmit traffic forwarded by DeviceA because link T has the smallest cost.
   ```
   [~DeviceA] display isis route verbose 10.4.1.1
                                                                                   
                            Route information for ISIS(1)                          
                            -----------------------------                          
                                                                                   
                           ISIS(1) Level-1 Forwarding Table                        
                           --------------------------------    
      
   IPV4 Dest  : 10.4.1.0/24        Int. Cost : 30            Ext. Cost : NULL  
   Admin Tag  : -                  Src Count : 2             Flags     : A/-/L/-  
   Priority   : Low                Age       : 00:00:23                  
   NextHop    :                    Interface :               ExitIndex :           
       10.0.1.2                         GE0/1/0                   0x00000010     
        Flags: D-Direct, A-Added to URT, L-Advertised in LSPs, S-IGP Shortcut,
                                    U-Up/Down Bit Set, LP-Local Prefix-Sid  
        Protect Type: L-Link Protect, N-Node Protect
                                                                                   
                                                                                   
                           ISIS(1) Level-2 Forwarding Table                        
                           --------------------------------  
    
   IPV4 Dest  : 10.4.1.0/24        Int. Cost : 30            Ext. Cost : NULL  
   Admin Tag  : -                  Src Count : 2             Flags     : -/-/-/-  
   Priority   : Low                Age       : 00:00:00                  
   NextHop    :                    Interface :               ExitIndex :            
                                         -                    
        Flags: D-Direct, A-Added to URT, L-Advertised in LSPs, S-IGP Shortcut,
                                    U-Up/Down Bit Set, LP-Local Prefix-Sid
        Protect Type: L-Link Protect, N-Node Protect
   ```
4. Enable IS-IS Auto FRR.
   
   
   
   # Enable IS-IS Auto FRR on DeviceA.
   
   ```
   [~DeviceA] isis
   [~DeviceA-isis-1] frr
   [*DeviceA-isis-1-frr] loop-free-alternate
   [*DeviceA-isis-1-frr] commit
   [~DeviceA-isis-1-frr] quit
   [~DeviceA-isis-1] quit
   ```
5. Verify the configuration.
   
   
   
   # Check information about the route from DeviceA to DeviceD. The command output shows that IS-IS generates a backup route because IS-IS Auto FRR is enabled.
   
   ```
   [~DeviceA] display isis route verbose 10.4.1.1
                                                                                   
                            Route information for ISIS(1)                          
                            ----------------------------- 
                          ISIS(1) Level-1 Forwarding Table                        
                           --------------------------------      
                     
   IPV4 Dest  : 10.4.1.0/24        Int. Cost : 30            Ext. Cost : NULL  
   Admin Tag  : -                  Src Count : 2             Flags     : A/-/L/-  
   Priority   : Low                Age       : 00:00:52                  
   NextHop    :                    Interface :               ExitIndex :                
       10.0.1.2                         GE0/1/0                   0x00000010     
       (B)10.1.1.2                      GE0/2/0                   0x0000000f(N)  
        Flags: D-Direct, A-Added to URT, L-Advertised in LSPs, S-IGP Shortcut,
                                    U-Up/Down Bit Set, LP-Local Prefix-Sid  
        Protect Type: L-Link Protect, N-Node Protect  
                                                                                   
                                                                                   
                           ISIS(1) Level-2 Forwarding Table                        
                           --------------------------------    
                       
   IPV4 Dest  : 10.4.1.0/24        Int. Cost : 30            Ext. Cost : NULL  
   Admin Tag  : -                  Src Count : 2             Flags     : -/-/-/-/-  
   Priority   : Low                Age       : 00:00:00                 
   NextHop    :                    Interface :               ExitIndex :                 
                                         -                    
        Flags: D-Direct, A-Added to URT, L-Advertised in LSPs, S-IGP Shortcut,
                                    U-Up/Down Bit Set, LP-Local Prefix-Sid 
        Protect Type: L-Link Protect, N-Node Protect                           
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
  isis 1
  ```
  ```
   network-entity 10.0000.0000.0001.00
  ```
  ```
   frr
  ```
  ```
    loop-free-alternate level-1
  ```
  ```
    loop-free-alternate level-2
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet 0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.0.1.1 255.255.255.0
  ```
  ```
   isis enable 1
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet 0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.1.1 255.255.255.0
  ```
  ```
   isis enable 1
  ```
  ```
   isis cost 30
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
  isis 1
  ```
  ```
   network-entity 10.0000.0000.0002.00
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet 0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.1.2 255.255.255.0
  ```
  ```
   isis enable 1
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet 0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.2.1.1 255.255.255.0
  ```
  ```
   isis enable 1
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
  ```
  ```
  isis 1
  ```
  ```
   network-entity 10.0000.0000.0003.00
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet 0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.0.1.2 255.255.255.0
  ```
  ```
   isis enable 1
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet 0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.3.1.1 255.255.255.0
  ```
  ```
   isis enable 1
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceD configuration file
  
  ```
  #
  ```
  ```
  sysname DeviceD
  ```
  ```
  #
  ```
  ```
  isis 1
  ```
  ```
   network-entity 10.0000.0000.0004.00
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet 0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.3.1.2 255.255.255.0
  ```
  ```
   isis enable 1
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet 0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.2.1.2 255.255.255.0
  ```
  ```
   isis enable 1
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet 0/3/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.4.1.1 255.255.255.0
  ```
  ```
   isis enable 1
  ```
  ```
  #
  ```
  ```
  return
  ```
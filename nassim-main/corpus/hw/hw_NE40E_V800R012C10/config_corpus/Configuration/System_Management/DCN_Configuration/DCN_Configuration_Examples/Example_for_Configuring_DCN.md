Example for Configuring DCN
===========================

This section provides an example for configuring the data communication network (DCN) feature.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172361425__fig_dc_vrp_dcn_cfg_002201), the GNE is directly connected to an NMS and two NEs. A static route is configured for communication between the NMS and GNE. After the DCN function is configured, the NMS can manage the attached NEs through the GNE and automatically discover new NEs.

**Figure 1** Networking diagram for configuring DCN  
![](images/fig_dc_vrp_dcn_cfg_002201.png)

#### Precautions

Before configuring DCN, note the following:

* An NMS's IP address is a public IP address, and a GNE's NEIP address is a Layer 3 virtual private network (VPN) address. To implement address conversion, you must specify a GNE's interface that is connected to an NMS, bind the GNE's interface to a DCN VPN instance, and set an IP address for the GNE's interface.
* The binding operation must be performed before you set an IP address for the interface. Otherwise, this IP address will be deleted when you bind the interface to the DCN VPN instance.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable the DCN feature globally.
2. Bind the interface (connecting the GNE to the NMS) to a DCN VPN instance. Then set an IP address for the interface.
3. Configure a static route for communication between the NMS and GNE.
4. Configure the automatic NE report function on the GNE.

#### Data Preparation

To complete the configuration, you need the following data:

* Name of the DCN VPN instance![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  A DCN VPN instance named \_\_dcn\_vpn\_\_ is automatically generated when the DCN feature is enabled globally on the GNE.
  
  You can run the [**display ip vpn-instance**](cmdqueryname=display+ip+vpn-instance) command on the GNE to view the DCN VPN instance name.
* IP address of the interface connecting the GNE to the NMS

#### Procedure

1. Enable the DCN feature globally.
   
   
   
   # Enable the DCN feature globally. In this example, a GNE is used.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname gne
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~gne] dcn
   ```
   ```
   [*gne-dcn] ne-ip 10.1.1.2 16
   ```
   ```
   [*gne-dcn] quit
   ```
2. Bind the interface (connecting the GNE to the NMS) to DCN VPN instance \_\_dcn\_vpn\_\_. Then, set an IP address for the interface.
   
   
   ```
   [*gne] interface GigabitEthernet 0/1/0
   ```
   ```
   [*gne-GigabitEthernet0/1/0] ip binding vpn-instance __dcn_vpn__
   ```
   ```
   [*gne-GigabitEthernet0/1/0] ip address 172.16.1.2 16
   ```
   ```
   [*gne-GigabitEthernet0/1/0] commit
   ```
   ```
   [~gne-GigabitEthernet0/1/0] quit
   ```
3. Configure a static route for communication between the NMS and GNE. For configuration details, see "Configuration Files" in this section.
4. Configure the automatic NE report function on the GNE.
   
   
   
   # Enable the automatic NE report function on the GNE.
   
   ```
   [~gne] dcn
   ```
   ```
   [*gne-dcn] auto-report
   ```
   ```
   [*gne-GigabitEthernet0/1/0] commit
   ```
5. Verify the configuration.
   
   
   
   # View the configurations of the GNE.
   
   ```
   <gne> display dcn brief
   ```
   ```
   ------------------------------------------------
    NE-ID:               0x280FC
    NE-IP:               10.1.1.2
    Mask:                255.255.0.0
    DCN-Interface:       LoopBack2147483647
    Auto-Report:         Enable
   ------------------------------------------------
   ```

#### Configuration Files

* Configuration file of the GNE
  
  ```
  #                                                                               
  ip dcn vpn-instance __dcn_vpn__                                                 
  #                                                                               
  interface GigabitEthernet0/1/0                                                  
   undo shutdown                                                                  
   dcn                                                                            
   ip binding vpn-instance __dcn_vpn__                                            
   ip address 172.16.1.2 255.255.0.0                                             
  #                                                                               
  interface LoopBack2147483647                                                    
   description DCN loopback interface                                             
   ip binding vpn-instance __dcn_vpn__                                            
   ip address 10.1.1.2 255.255.0.0                                               
  #                                                                               
  ospf 65534 vpn-instance __dcn_vpn__                                             
   description DCN ospf create by default                                         
   opaque-capability enable                                                       
   vpn-instance-capability simple                                                 
   area 0.0.0.0                                                                   
    network 0.0.0.0 255.255.255.255                                               
  #                                                                               
  !The DCN function implements the capability of plug-and-play for this device.
  !A NE IP address based on the unique NE ID is automatically generated in VPN
  !of DCN. It is recommended that the NE IP address be changed to the planned 
  !one by running the ne-ip X.X.X.X <MASK> command after the device being online.
  dcn                                                                             
   auto-report                                                                    
   ne-ip 10.1.1.2 255.255.0.0
  #                                                                               
  return 
  ```
* Configuration files of NE1 and NE2
  
  ```
  #                                                                               
  interface GigabitEthernet0/1/1                                                  
   undo shutdown                                                                  
   dcn                                                                            
  #                                                                               
  interface LoopBack2147483647                                                    
   description DCN loopback interface                                             
   ip binding vpn-instance __dcn_vpn__                                            
   ip address 10.1.1.3 255.255.0.0                                               
  #                                                                               
  ospf 65534 vpn-instance __dcn_vpn__                                             
   description DCN ospf create by default                                         
   opaque-capability enable 
   hostname                                                       
   vpn-instance-capability simple                                                 
   area 0.0.0.0                                                                   
    network 0.0.0.0 255.255.255.255                                               
  #                                                                               
  !The DCN function implements the capability of plug-and-play for this device.
  !A NE IP address based on the unique NE ID is automatically generated in VPN
  !of DCN. It is recommended that the NE IP address be changed to the planned 
  !one by running the ne-ip X.X.X.X <MASK> command after the device being online.
  dcn                                                                             
  #                                                                               
  return
  ```
Example for Configuring DHCP Snooping in a QinQ Scenario
========================================================

Example for Configuring DHCP Snooping in a QinQ Scenario

#### Networking Requirements

As shown in [Figure 1](#EN-US_XTASK_0000001564000565__fig_dc_cfg_qinq_003001), two enterprises obtain IPv4 addresses through DHCP, and both of them have two branches. The offices of the two enterprises are connected to DeviceA and DeviceB of the ISP network. A non-Huawei device on the ISP network uses the TPID value of 0x9100 in the outer VLAN tag.

The requirements are as follows:

* Enterprise 1 and enterprise 2 use independently planned VLANs that do not affect each other.
* Traffic is transparently transmitted between each enterprise's branches through the ISP network. Users accessing the same service in each enterprise are allowed to communicate, and users accessing different services are isolated.
* The devices defend against DHCP attacks on the network and provide better services for DHCP users.

QinQ and DHCP snooping can be configured to meet the preceding requirements. VLAN 100 and VLAN 200 provided by the ISP network can be used to transmit traffic for enterprise 1 and enterprise 2, respectively. This enables communication within an enterprise while isolating the two enterprises from each other. To implement interworking with a non-Huawei device, change the TPID value in the outer VLAN tag on the interfaces of the Huawei devices connected to the non-Huawei device. Configure DHCP snooping on DeviceA and DeviceB to defend against DHCP attacks.
**Figure 1** Network diagram of configuring basic DHCP snooping functions in a QinQ scenario![](public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1, 2, and 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](figure/en-us_image_0000001564120473.png "Click to enlarge")


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create VLAN 100 and VLAN 200 on both DeviceA and DeviceB, configure the interfaces connected to enterprise devices as QinQ ones, and add them to VLAN 100 and VLAN 200. In this way, different outer VLAN tags are added for different services.
2. Add the interfaces of DeviceA and DeviceB connected to the ISP network to VLAN 100 and VLAN 200, allowing the packets from the two VLANs to pass through.
3. On the interfaces of DeviceA and DeviceB connected to the ISP network, set the TPID in the outer VLAN tag to the value used on the non-Huawei device, allowing DeviceA and DeviceB to interwork with the non-Huawei device.
4. Configure DHCP snooping on DeviceA and DeviceB to defend against DHCP attacks.![](public_sys-resources/note_3.0-en-us.png) 
   
   DHCP snooping can process DHCP messages with up to two VLAN tags. If DHCP snooping is configured to process messages with more than two VLAN tags, such messages will be discarded, negatively affecting user experience.


#### Procedure

1. Create VLANs.
   
   
   
   # Create VLAN 100 and VLAN 200 on DeviceA. The configuration of DeviceB is similar to that of DeviceA.
   
   ```
   <HUAWEI> system-view 
   [~HUAWEI] sysname DeviceA
   [*DeviceA] vlan batch 100 200
   [*DeviceA] commit
   ```
2. Configure interfaces as QinQ ones.
   
   
   
   # On DeviceA, configure 100GE 1/0/1 and 100GE 1/0/2 as QinQ interfaces, and set the default VLANs of 100GE 1/0/1 and 100GE 1/0/2 to VLAN 100 and VLAN 200, respectively.
   
   ```
   [~DeviceA] interface 100GE 1/0/1
   [*DeviceA-100GE1/0/1] port link-type dot1q-tunnel
   [*DeviceA-100GE1/0/1] port default vlan 100
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100GE 1/0/2
   [*DeviceA-100GE1/0/2] port link-type dot1q-tunnel
   [*DeviceA-100GE1/0/2] port default vlan 200
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```
3. Configure the interfaces of the devices connected to the ISP network.
   
   
   
   # Add 100GE 1/0/3 on DeviceA to VLAN 100 and VLAN 200.
   
   ```
   [~DeviceA] interface 100GE 1/0/3
   [*DeviceA-100GE1/0/3] port link-type trunk
   [*DeviceA-100GE1/0/3] port trunk allow-pass vlan 100 200
   ```
4. Configure the TPID value in the outer VLAN tag.
   
   
   
   # On DeviceA, set the TPID value in the outer VLAN tag to 0x9100.
   
   ```
   [*DeviceA-100GE1/0/3] qinq protocol 9100
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] commit
   ```
5. Configure DHCP snooping.
   
   
   
   # Enable DHCP snooping globally on DeviceA.
   
   ```
   [~DeviceA] dhcp enable 
   [*DeviceA] dhcp snooping enable
   [*DeviceA] commit
   ```
6. Enable DHCP snooping on the interfaces.
   
   
   
   # Enable DHCP snooping on the user-side interfaces of DeviceA.
   
   ```
   [~DeviceA] interface 100GE 1/0/1
   [*DeviceA-100GE1/0/1] dhcp snooping enable
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100GE 1/0/2
   [*DeviceA-100GE1/0/2] dhcp snooping enable
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```
7. Configure the interface as a trusted one.
   
   
   
   # Configure the interface connected to the DHCP server as a trusted one.
   
   ```
   [~DeviceA] interface 100GE 1/0/3
   [*DeviceA-100GE1/0/3] dhcp snooping trusted
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] commit
   ```
8. Verify the configuration.
   
   
   
   # Check the DHCP snooping configuration.
   
   ```
   [~DeviceA] display dhcp snooping configuration
   #                                                                               
   dhcp snooping enable                                                          
   #                                                                               
   interface 100GE1/0/1                                                  
    dhcp snooping enable                                                          
   #                                                                               
   interface 100GE1/0/2                                                  
    dhcp snooping enable                                                          
   #                                                                               
   interface 100GE1/0/3
    dhcp snooping trusted                                                          
   #
   ```
   
   # Check the information about the DHCP snooping binding table.
   
   ```
   [~DeviceA] display dhcp snooping user-bind all
   DHCP Dynamic Bind-table:
   Flags:O - outer vlan ,I - inner vlan   
   IP Address       MAC Address     VLAN(O/I)/(BD-VLAN)        Interface          Lease            
   ------------------------------------------------------------------------------------------------------- 
   10.1.1.141      00e0-fc12-3456    100 /--  /--              100GE1/0/1       2022.03.27-07:31
   10.1.1.137      00e0-fc12-3457    200 /--  /--              100GE1/0/2       2022.03.27-07:31
   ------------------------------------------------------------------------------------------------------- 
   Print count:           2          Total count:           2 
   ```
   
   In enterprise 1, use a PC in a VLAN of one branch to ping a PC in the same VLAN but of the other branch. If the ping operation is successful, internal users of enterprise 1 can communicate.
   
   Repeat this operation for enterprise 2. If the ping operation is successful, internal users of enterprise 2 can communicate.
   
   Next, use a PC in a VLAN of an enterprise 1 branch to ping a PC in the same VLAN but of an enterprise 2 branch. The ping operation should fail, indicating that the users in enterprise 1 and enterprise 2 are isolated.

#### Configuration Scripts

* DeviceA
  ```
  #
  sysname DeviceA
  #
  vlan batch 100 200
  #
  dhcp enable
  #
  dhcp snooping enable
  #
  interface 100GE1/0/1 
   port link-type dot1q-tunnel
   port default vlan 100
   dhcp snooping enable 
  #
  interface 100GE1/0/2
   port link-type dot1q-tunnel
   port default vlan 200
   dhcp snooping enable
  #
  interface 100GE1/0/3
   qinq protocol 9100
   port link-type trunk
   port trunk allow-pass vlan 100 200
   dhcp snooping trusted
  #
  return
  ```
* DeviceB
  ```
  #
  sysname DeviceA
  #
  vlan batch 100 200
  #
  dhcp enable
  #
  dhcp snooping enable
  #
  interface 100GE1/0/1 
   port link-type dot1q-tunnel
   port default vlan 100
   dhcp snooping enable 
  #
  interface 100GE1/0/2
   port link-type dot1q-tunnel
   port default vlan 200
   dhcp snooping enable
  #
  interface 100GE1/0/3
   qinq protocol 9100
   port link-type trunk
   port trunk allow-pass vlan 100 200
   dhcp snooping trusted
  #
  return
  ```
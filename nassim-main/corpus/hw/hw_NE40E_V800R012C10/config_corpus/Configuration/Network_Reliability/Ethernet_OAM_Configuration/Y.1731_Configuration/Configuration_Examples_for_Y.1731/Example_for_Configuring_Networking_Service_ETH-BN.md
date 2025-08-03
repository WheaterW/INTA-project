Example for Configuring Networking Service ETH-BN
=================================================

When routing devices connect to microwave devices, enable the ETH-BN receiving function to implement association with the microwave bandwidth. This section provides an example for configuring the ETH-BN receiving function for a VLAN.

#### Context

On the network shown in [Figure 1](#EN-US_TASK_0172362191__fig_dc_vrp_y1731_cfg_007801), the RTN links form a single chain, and no intermediate services are on the chain.

**Figure 1** Configuring the ETH-BN receiving function for a VLAN![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1 in this example represents GE 0/1/0.1


  
![](images/fig_dc_vrp_y1731_cfg_0078_01.png)

#### Data Preparation

To complete the configuration, you need the following data:

* MD name, MA name, and MEP ID for configuring basic CFM functions on CE1
* VLAN ID used in VLAN networking

#### Procedure

1. Configure a VLAN.
   
   
   
   Configure a VLAN connection between CE1 and RTNs (Device1, Device2, and Device3). For configuration details, see the section "VLAN Configuration" in *Configuration Guide - LAN Access and MAN Access*.
2. Configure CE1.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname CE1
   ```
   ```
   [*CE1] commit
   ```
   ```
   [~CE1] cfm enable
   ```
   ```
   [*CE1] cfm md md1
   ```
   ```
   [*CE1-md-md1] ma ma1
   ```
3. Configure the ETH-BN receiving function.
   
   
   ```
   [*CE1-md-md1-ma-ma1] mep mep-id 1 interface gigabitEthernet0/1/0.1 vlan 1 outward
   ```
   ```
   [*CE1-md-md1-ma-ma1] mep mep-id 1 eth-bn receive enable
   ```
4. Verify the configuration.
   
   
   
   After the configuration is complete, run the [**display y1731 eth-bn**](cmdqueryname=display+y1731+eth-bn) command on CE1 to check information about ETH-BN packets on the receive end.
   
   ```
   <CE1>display y1731 eth-bn md md1 ma ma1 mep 1
   ```
   ```
    Source MAC         : 00e0-fc12-7890
    Port ID            : 1
    Bandwidth          : 3(M)
   ```

#### Configuration Files

CE1 configuration file
```
#                                                                               
sysname CE1                                                                      
#                                                                               
cfm enable                                                                      
#
interface gigabitEthernet0/1/0.1
 vlan-type dot1q 1
#
cfm md md1                                                                      
 ma ma1                                                                         
  mep mep-id 1 interface GigabitEthernet0/1/0.1 vlan 1 outward                         
  mep mep-id 1 eth-bn receive enable   
#
```
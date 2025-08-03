Example for Configuring a DHCPv4 Server Based on a Global Address Pool (Using a Sub-interface)
==============================================================================================

Example for Configuring a DHCPv4 Server Based on a Global Address Pool (Using a Sub-interface)

#### Networking Requirements

IPv4 addresses of different network segments need to be obtained for services such as VoIP on different user planes. DHCPv4 clients that support the services use one MAC address to apply for IPv4 addresses of different network segments and differentiate the services based on VLAN IDs. Therefore, the DHCPv4 server must be able to allocate IPv4 addresses to users with the same MAC address but different VLAN IDs.

As shown in [Figure 1](#EN-US_TASK_0000001513046150__fig_dc_vrp_dhcp_server_cfg_002001), DeviceA functions as a DHCPv4 server to dynamically allocate IPv4 addresses to clients. When DeviceA receives a user packet with the tag of 100, it selects the address pool **huawei1** based on the gateway address 10.10.10.1/24; when DeviceA receives a user packet with the tag of 200, it selects the address pool **huawei2** based on the gateway address 10.10.20.1/24.

![](public_sys-resources/note_3.0-en-us.png) 

Currently, the DHCPv4 server can allocate addresses to users with the same MAC address only from different address pools.


**Figure 1** Network diagram of configuring a DHCPv4 server based on a global address pool (using a sub-interface)![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 1.1, and interface 1.2 represent 100GE 1/0/1, 100GE 1/0/1.1, and 100GE 1/0/1.2, respectively.


  
![](figure/en-us_image_0000001513046194.png)

#### Procedure

1. Enable DHCPv4.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] [commit](cmdqueryname=commit)
   [~DeviceA] dhcp enable
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
2. Configure global address pools.
   
   
   
   # Configure attributes for the address pool **huawei1**.
   
   ```
   [~DeviceA] ip pool huawei1
   [*DeviceA-ip-pool-huawei1] network 10.10.10.0 mask 24
   [*DeviceA-ip-pool-huawei1] gateway-list 10.10.10.1
   [*DeviceA-ip-pool-huawei1] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
   
   # Configure attributes for the address pool **huawei2**.
   
   ```
   [~DeviceA] ip pool huawei2
   [*DeviceA-ip-pool-huawei2] network 10.10.20.0 mask 24
   [*DeviceA-ip-pool-huawei2] gateway-list 10.10.20.1
   [*DeviceA-ip-pool-huawei2] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
3. Configure Layer 3 sub-interfaces.
   
   
   
   # Configure IPv4 addresses for Layer 3 sub-interfaces, and enable the DHCPv4 server function based on global address pools on the Layer 3 sub-interfaces.
   
   
   
   ```
   [~DeviceA] interface 100GE 1/0/1
   [~DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100GE 1/0/1.1
   [*DeviceA-100GE1/0/1.1] ip address 10.10.10.1 24
   [*DeviceA-100GE1/0/1.1] dot1q termination vid 100
   [*DeviceA-100GE1/0/1.1] dhcp select global
   [*DeviceA-100GE1/0/1.1] quit
   [*DeviceA] interface 100GE 1/0/1.2
   [*DeviceA-100GE1/0/1.2] ip address 10.10.20.1 24
   [*DeviceA-100GE1/0/1.2] dot1q termination vid 200
   [*DeviceA-100GE1/0/1.2] dhcp select global
   [*DeviceA-100GE1/0/1.2] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

# On DeviceA, run the [**display ip pool**](cmdqueryname=display+ip+pool) command to check IPv4 address configuration and allocation in address pools. The **Used** field displays the number of used IPv4 addresses in each address pool.

```
[~DeviceA] display ip pool name huawei1

  Pool-name        : huawei1                                                                                                        
  Pool-No          : 0                                                                                                              
  Lease            : 1 Days 0 Hours 0 Minutes                                                                                       
  Domain-name      : -                                                                                                              
  DNS-server0      : -                                                                                                              
  NBNS-server0     : -                                                                                                              
  Netbios-type     : -                                                                                                              
  Position         : Local                                                                                                          
  Status           : Unlocked                                                                                                       
  Gateway-0        : 10.10.10.1                                                                                                     
  Network          : 10.10.10.0                                                                                                     
  Mask             : 255.255.255.0                                                                                                  
  VPN instance     : --                                                                                                             
  Logging          : Disable                                                                                                        
  Conflicted address recycle interval: -                                                                                            
  Address Statistic: Total       :253       Used        :0                                                                          
                     Idle        :253       Expired     :0                                                                          
                     Conflict    :0         Disabled    :0
                                                                            

 -------------------------------------------------------------------------------------                                              
  Network section                                                                                                                   
         Start           End       Total    Used Idle(Expired) Conflict Disabled                                                    
 -------------------------------------------------------------------------------------                                              
      10.10.10.1    10.10.10.254     253       0        253(0)       0     0                                                        
 ------------------------------------------------------------------------------------- 
```
```
[~DeviceA] display ip pool name huawei2

  Pool-name        : huawei2                                                                                                        
  Pool-No          : 1                                                                                                              
  Lease            : 1 Days 0 Hours 0 Minutes                                                                                       
  Domain-name      : -                                                                                                              
  DNS-server0      : -                                                                                                              
  NBNS-server0     : -                                                                                                              
  Netbios-type     : -                                                                                                              
  Position         : Local                                                                                                          
  Status           : Unlocked                                                                                                       
  Gateway-0        : 10.10.20.1                                                                                                     
  Network          : 10.10.20.0                                                                                                     
  Mask             : 255.255.255.0                                                                                                  
  VPN instance     : --                                                                                                             
  Logging          : Disable                                                                                                        
  Conflicted address recycle interval: -                                                                                            
  Address Statistic: Total       :253       Used        :0                                                                          
                     Idle        :253       Expired     :0                                                                          
                     Conflict    :0         Disabled    :0 
                                                                           

 -------------------------------------------------------------------------------------                                              
  Network section                                                                                                                   
         Start           End       Total    Used Idle(Expired) Conflict Disabled                                                    
 -------------------------------------------------------------------------------------                                              
      10.10.20.1    10.10.20.254     253       0        253(0)       0     0                                                        
 -------------------------------------------------------------------------------------    
```
#### Configuration Scripts

DeviceA

```
#
sysname DeviceA
#
dhcp enable
#
ip pool huawei1
 gateway-list 10.10.10.1
 network 10.10.10.0 mask 255.255.255.0 
# 
ip pool huawei2
 gateway-list 10.10.20.1
 network 10.10.20.0 mask 255.255.255.0 
#
interface 100GE1/0/1
 undo portswitch
#
interface 100GE1/0/1.1
 ip address 10.10.10.1 255.255.255.0
 dot1q termination vid 100
 encapsulation dot1q-termination
 dhcp select global
#
interface 100GE1/0/1.2
 ip address 10.10.20.1 255.255.255.0
 dot1q termination vid 200
 encapsulation dot1q-termination
 dhcp select global
#
return
```
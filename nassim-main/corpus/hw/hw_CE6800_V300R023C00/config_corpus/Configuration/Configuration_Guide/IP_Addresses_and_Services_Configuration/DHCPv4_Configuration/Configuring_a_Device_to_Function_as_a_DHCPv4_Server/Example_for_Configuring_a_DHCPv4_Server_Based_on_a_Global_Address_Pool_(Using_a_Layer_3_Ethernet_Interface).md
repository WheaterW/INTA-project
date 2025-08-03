Example for Configuring a DHCPv4 Server Based on a Global Address Pool (Using a Layer 3 Ethernet Interface)
===========================================================================================================

Example for Configuring a DHCPv4 Server Based on a Global Address Pool (Using a Layer 3 Ethernet Interface)

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0000001564126229__dc_cfg_dhcp_104701), DeviceA functions as a DHCPv4 server; the PCs on network segment 10.1.1.0/24 are fixed terminals; network segment 10.1.2.0/24 is used for the terminals' temporary access. To facilitate unified management, the administrator requires the terminals to automatically obtain IPv4 addresses and the IPv4 address of the DNS server (if users need to access the network using domain names, a DNS server must be configured). A PC named Client\_1 requires a fixed IPv4 address of 10.1.1.100/24 to meet service requirements.

**Figure 1** Network diagram of configuring a DHCPv4 server based on a global address pool (using a Layer 3 Ethernet interface)![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent 100GE 1/0/1 and 100GE 1/0/2, respectively.


  
![](figure/en-us_image_0000001564126273.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Set an IPv4 address lease to 30 days for the PCs (Client\_1 to Client\_n) on network segment 10.1.1.0/24, and allocate a fixed IPv4 address of 10.1.1.100/24 to Client\_1 statically.
2. Set an IPv4 address lease to two days for the PCs (Client\_s to Client\_t) on network segment 10.1.2.0/24 for temporary access.


#### Procedure

1. Enable DHCPv4.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] [commit](cmdqueryname=commit)
   [~DeviceA] dhcp enable
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
2. Configure IPv4 addresses for interfaces.
   
   
   ```
   [~DeviceA] interface 100GE 1/0/1
   [~DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ip address 10.1.1.1 24
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100GE 1/0/2
   [*DeviceA-100GE1/0/2] undo portswitch
   [*DeviceA-100GE1/0/2] ip address 10.1.2.1 24
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
3. Configure global address pools.
   
   
   
   # Configure attributes for the address pool **pool1**.
   
   ```
   [~DeviceA] ip pool pool1
   [*DeviceA-ip-pool-pool1] network 10.1.1.0 mask 24
   [*DeviceA-ip-pool-pool1] gateway-list 10.1.1.1
   [*DeviceA-ip-pool-pool1] lease day 30
   [*DeviceA-ip-pool-pool1] domain-name huawei.com
   [*DeviceA-ip-pool-pool1] dns-list 10.1.3.1
   [*DeviceA-ip-pool-pool1] static-bind ip-address 10.1.1.100 mac-address 00e0-fc12-3456
   [*DeviceA-ip-pool-pool1] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
   
   # Configure attributes for the address pool **pool2**.
   
   ```
   [~DeviceA] ip pool pool2
   [*DeviceA-ip-pool-pool2] network 10.1.2.0 mask 24
   [*DeviceA-ip-pool-pool2] gateway-list 10.1.2.1
   [*DeviceA-ip-pool-pool2] lease day 2
   [*DeviceA-ip-pool-pool2] domain-name huawei.com
   [*DeviceA-ip-pool-pool2] dns-list 10.1.3.1
   [*DeviceA-ip-pool-pool2] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
4. Enable the DHCPv4 server function based on global address pools on Layer 3 Ethernet interfaces.
   
   
   ```
   [~DeviceA] interface 100GE 1/0/1
   [~DeviceA-100GE1/0/1] dhcp select global
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100GE 1/0/2
   [*DeviceA-100GE1/0/2] dhcp select global
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

# On DeviceA, run the [**display ip pool**](cmdqueryname=display+ip+pool) command to check IPv4 address configuration and allocation in address pools. The **Used** field displays the number of used IPv4 addresses in each address pool.

```
[~DeviceA] display ip pool name pool1

  Pool-name        : pool1                                                                                                          
  Pool-No          : 7                                                                                                              
  Lease            : 30 Days 0 Hours 0 Minutes                                                                                      
  Domain-name      : huawei.com                                                                                                     
  DNS-server0      : 10.1.3.1                                                                                                       
  NBNS-server0     : -                                                                                                              
  Netbios-type     : -                                                                                                              
  Position         : Local                                                                                                          
  Status           : Unlocked                                                                                                       
  Gateway-0        : 10.1.1.1                                                                                                       
  Network          : 10.1.1.0                                                                                                       
  Mask             : 255.255.255.0                                                                                                  
  VPN instance     : --                                                                                                             
  Logging          : Disable                                                                                                        
  Conflicted address recycle interval: -                                                                                            
  Address Statistic: Total       :253       Used        :1                                                                          
                     Idle        :252       Expired     :0                                                                          
                     Conflict    :0         Disabled    :0 
                                                                        

 -------------------------------------------------------------------------------------                                              
  Network section                                                                                                                   
         Start           End       Total    Used Idle(Expired) Conflict Disabled                                                    
 -------------------------------------------------------------------------------------                                              
        10.1.1.1      10.1.1.254     253       1        252(0)       0     0                                                        
 ------------------------------------------------------------------------------------- 
```
```
[~DeviceA] display ip pool name pool2

  Pool-name        : pool2                                                                                                          
  Pool-No          : 8                                                                                                              
  Lease            : 2 Days 0 Hours 0 Minutes                                                                                       
  Domain-name      : huawei.com                                                                                                     
  DNS-server0      : 10.1.3.1                                                                                                       
  NBNS-server0     : -                                                                                                              
  Netbios-type     : -                                                                                                              
  Position         : Local                                                                                                          
  Status           : Unlocked                                                                                                       
  Gateway-0        : 10.1.2.1                                                                                                       
  Network          : 10.1.2.0                                                                                                       
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
        10.1.2.1      10.1.2.254     253       0        253(0)       0     0                                                        
 -------------------------------------------------------------------------------------
```

# Check IPv4 address information on Client\_1. You can check that Client\_1 has obtained the IPv4 address 10.1.1.100/24.

# Check IPv4 address information on other DHCPv4 clients. You can check that the clients have obtained IPv4 addresses.

#### Configuration Scripts

DeviceA

```
#
sysname DeviceA
#
dhcp enable
#
ip pool pool1
 gateway-list 10.1.1.1 
 network 10.1.1.0 mask 255.255.255.0 
 static-bind ip-address 10.1.1.100 mac-address 00e0-fc12-3456 
 lease day 30 hour 0 minute 0 
 dns-list 10.1.3.1 
 domain-name huawei.com
# 
ip pool pool2
 gateway-list 10.1.2.1 
 network 10.1.2.0 mask 255.255.255.0 
 lease day 2 hour 0 minute 0 
 dns-list 10.1.3.1 
 domain-name huawei.com
#
interface 100GE1/0/1
 undo portswitch
 ip address 10.1.1.1 255.255.255.0
 dhcp select global
#
interface 100GE1/0/2
 undo portswitch
 ip address 10.1.2.1 255.255.255.0
 dhcp select global
#
return
```
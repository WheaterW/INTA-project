Example for Configuring a BOOTP Client
======================================

Example for Configuring a BOOTP Client

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0000001513046170__fig_dc_esap_cfg_001307), DeviceA functions as a BOOTP client and needs to obtain information such as an IPv4 address, DNS server address, and gateway address from DeviceB functioning as a DHCPv4 server.

**Figure 1** Network diagram of configuring a BOOTP client![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 represents 100GE 1/0/1.


  
![](figure/en-us_image_0000001563766565.png)

#### Procedure

1. Configure the BOOTP client function on DeviceA.
   
   
   
   # Create VLAN 10 and add 100GE 1/0/1 to VLAN 10.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] [commit](cmdqueryname=commit)
   [~DeviceA] vlan batch 10
   [*DeviceA] interface 100ge1/0/1
   [*DeviceA-100GE1/0/1] portswitch
   [*DeviceA-100GE1/0/1] port link-type trunk
   [*DeviceA-100GE1/0/1] port trunk allow-pass vlan 10
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
   
   # Enable the BOOTP client function on VLANIF 10.
   
   ```
   [~DeviceA] interface vlanif 10
   [*DeviceA-Vlanif10] ip address bootp-alloc
   [*DeviceA-Vlanif10] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
2. Create a global address pool on DeviceB and configure network parameters.
   1. Enable DHCPv4.
      
      
      ```
      <HUAWEI> system-view
      [~HUAWEI] sysname DeviceB
      [*HUAWEI] [commit](cmdqueryname=commit)
      [~DeviceB] dhcp enable
      [*DeviceB] dhcp server bootp
      [*DeviceB] [commit](cmdqueryname=commit)
      ```
   2. Create VLAN 10 and add 100GE 1/0/1 to VLAN 10.
      
      
      ```
      [~DeviceB] vlan batch 10
      [*DeviceB] interface 100ge 1/0/1
      [*DeviceB-100GE1/0/1] portswitch
      [*DeviceB-100GE1/0/1] port link-type trunk
      [*DeviceB-100GE1/0/1] port trunk allow-pass vlan 10
      [*DeviceB-100GE1/0/1] quit
      [*DeviceB] [commit](cmdqueryname=commit)
      ```
   3. Create an address pool and configure attributes for it.
      
      
      ```
      [~DeviceB] ip pool pool1
      [*DeviceB-ip-pool-pool1] network 192.168.1.0 mask 24
      [*DeviceB-ip-pool-pool1] gateway-list 192.168.1.126
      [*DeviceB-ip-pool-pool1] dns-list 192.168.1.2
      [*DeviceB-ip-pool-pool1] excluded-ip-address 192.168.1.1
      [*DeviceB-ip-pool-pool1] excluded-ip-address 192.168.1.2
      [*DeviceB-ip-pool-pool1] quit
      [*DeviceB] [commit](cmdqueryname=commit)
      ```
   4. Enable the DHCPv4 server function based on the global address pool on VLANIF 10.
      
      
      ```
      [~DeviceB] interface vlanif 10
      [*DeviceB-Vlanif10] ip address 192.168.1.1 24
      [*DeviceB-Vlanif10] dhcp select global
      [*DeviceB-Vlanif10] quit
      [*DeviceB] [commit](cmdqueryname=commit)
      ```

#### Verifying the Configuration

# After VLANIF 10 obtains an IPv4 address, run the [**display dhcp client**](cmdqueryname=display+dhcp+client) command on DeviceA to check the status of the BOOTP client.

```
[~DeviceA] display dhcp client
BOOTP client lease information on interface Vlanif10 :                          
 Current machine state         : Bound                                          
 Internet address assigned via : BOOTP                                          
 Physical address              : 00e0-fc12-3456                                 
 IP address                    : 192.168.1.254                                  
 Subnet mask                   : 255.255.255.0                                  
 Gateway ip address            : 192.168.1.126                                  
 Lease obtained at             : 2021-09-22 23:04:47                            
 DNS                           : 192.168.1.2           
```
# Run the [**display ip pool**](cmdqueryname=display+ip+pool) command on DeviceB to check the configuration of the global address pool.
```
[~DeviceB] display ip pool name pool1
  Pool-name      : pool1
  Pool-No        : 0
  Lease          : 1 Days 0 Hours 0 Minutes
  Domain-name    : 192.168.1.2
  DNS-server0    : -
  NBNS-server0   : -
  Netbios-type   : -
  Position       : Local
  Status           : Unlocked
  Gateway-0      : 192.168.1.126
  Network        : 192.168.1.0
  Mask           : 255.255.255.0
  VPN instance     : --
  Logging          : Disable
  Conflicted address recycle interval: -
  Address Statistic: Total       :253       Used        :1                      
                     Idle        :251       Expired     :0                      
                     Conflict    :0         Disabled    :1 
                       
                                                                                
 -----------------------------------------------------------------------------
         Start           End     Total  Used  Idle(Expired)  Conflict  Disabled
 -----------------------------------------------------------------------------
      10.20.20.1    10.20.20.254   253     1        251(0)         0        1
 -----------------------------------------------------------------------------    
```


#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  vlan batch 10
  #
  interface Vlanif10
   ip address bootp-alloc
  #
  interface 100GE1/0/1
   port link-type trunk
   port trunk allow-pass vlan 10
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  vlan batch 10
  #
  dhcp enable
  #
  dhcp server bootp
  #
  ip pool pool1
   gateway-list 192.168.1.126
   network 192.168.1.0 mask 255.255.255.0
   excluded-ip-address 192.168.1.1 192.168.1.2
   dns-list 192.168.1.2
  #
  interface Vlanif10
   ip address 192.168.1.1 255.255.255.0
   dhcp select global
  #
  interface 100GE1/0/1
   port link-type trunk
   port trunk allow-pass vlan 10
  #
  return
  ```
Example for Configuring a DHCPv4 Client
=======================================

Example for Configuring a DHCPv4 Client

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0000001563886121__fig_dc_cfg_dhcp_107101), DeviceA functions as a DHCPv4 client and needs to obtain information such as an IPv4 address, DNS server address, and gateway address from DeviceB functioning as a DHCPv4 server.

**Figure 1** Network diagram of configuring a DHCPv4 client![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 represents 100GE 1/0/1.


  
![](figure/en-us_image_0000001564126269.png)

#### Procedure

1. Configure the DHCPv4 client function on DeviceA.
   
   
   
   # Create VLAN 10 and add 100GE 1/0/1 to VLAN 10.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] [commit](cmdqueryname=commit)
   [~DeviceA] vlan batch 10
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] portswitch
   [*DeviceA-100GE1/0/1] port link-type trunk
   [*DeviceA-100GE1/0/1] port trunk allow-pass vlan 10
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
   
   # Enable the DHCPv4 client function on VLANIF 10.
   
   ```
   [~DeviceA] interface vlanif 10
   [*DeviceA-Vlanif10] ip address dhcp-alloc
   [*DeviceA-Vlanif10] quit
   ```
2. Create a global address pool on DeviceB and configure network parameters.
   1. Enable DHCPv4.
      
      
      ```
      <HUAWEI> system-view
      [~HUAWEI] sysname DeviceB
      [*HUAWEI] [commit](cmdqueryname=commit)
      [~DeviceB] dhcp enable
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
   3. Create an address pool and configure attributes for the pool.
      
      
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

# After VLANIF 10 obtains an IPv4 address, run the [**display dhcp client**](cmdqueryname=display+dhcp+client) command on DeviceA to check the status of the DHCPv4 client.

```
[~DeviceA] display dhcp client
DHCP client lease information on interface Vlanif10 :
 Current machine state         : Bound
 Internet address assigned via : DHCP
 Physical address              : 00e0-fc12-3456
 IP address                    : 192.168.1.254
 Subnet mask                   : 255.255.255.0
 Gateway ip address            : 192.168.1.126
 DHCP server                   : 192.168.1.1
 Lease obtained at             : 2021-09-26 20:30:39
 Lease expires at              : 2021-09-27 20:30:39
 Lease renews at               : 2020-09-27 08:30:39
 Lease rebinds at              : 2020-09-27 17:30:39
 Request option list           : 1 3 6 15 28 33 44 121 184  
 Class identifier              : huawei xxxx  
 Client identifier             : 00e0-fc12-1111
 DNS                           : 192.168.1.2   
```
# Run the [**display ip pool name pool1**](cmdqueryname=display+ip+pool+name+pool1) command on DeviceB to check IPv4 address allocation in the global address pool. The **Used** field value indicates the number of allocated IPv4 addresses.
```
[~DeviceB] display ip pool name pool1
  Pool-name        : pool1
  Pool-No          : 0
  Lease            : 1 Days 0 Hours 0 Minutes
  Domain-name      : -
  DNS-server0      : 192.168.1.2
  NBNS-server0     : -
  Netbios-type     : -
  Position         : Local
  Status           : Unlocked
  Gateway-0        : 192.168.1.126
  Network          : 192.168.1.0
  Mask             : 255.255.255.0
  VPN instance     : --
  Logging          : Disable
  Conflicted address recycle interval: -
  Address Statistic: Total       :253       Used        :1
                     Idle        :251       Expired     :0
                     Conflict    :0         Disabled     :1
  

 -------------------------------------------------------------------------------
  Network section
         Start           End     Total  Used  Idle(Expired)  Conflict  Disabled
 -------------------------------------------------------------------------------
     192.168.1.1   192.168.1.254     253       1        251(0)       0     1
 -------------------------------------------------------------------------------
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
   ip address dhcp-alloc
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
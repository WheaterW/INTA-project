Example for Configuring a DHCPv4 Server Based on an Interface Address Pool
==========================================================================

Example for Configuring a DHCPv4 Server Based on an Interface Address Pool

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0000001564126241__dc_cfg_dhcp_104701), DeviceA functions as a DHCPv4 server; the PCs on network segment 10.1.1.0/24 are fixed terminals; network segment 10.1.2.0/24 is used for the terminals' temporary access. To facilitate unified management, the administrator requires the terminals to automatically obtain IPv4 addresses and the IPv4 address of the DNS server (if users need to access the network using domain names, a DNS server must be configured). A PC named Client\_1 requires a fixed IPv4 address of 10.1.1.100/24 to meet service requirements.

**Figure 1** Network diagram of configuring a DHCPv4 server based on an interface address pool![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent 100GE 1/0/1 and 100GE 1/0/2, respectively.


  
![](figure/en-us_image_0000001563766553.png)

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
2. Add interfaces to VLANs.
   
   
   
   # Add 100GE 1/0/1 and 100GE 1/0/2 to VLAN 10 and VLAN 11, respectively.
   
   ```
   [~DeviceA] vlan batch 10 11
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] portswitch
   [*DeviceA-100GE1/0/1] port link-type access
   [*DeviceA-100GE1/0/1] port default vlan 10
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] portswitch
   [*DeviceA-100GE1/0/2] port link-type access
   [*DeviceA-100GE1/0/2] port default vlan 11
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
3. Configure IPv4 addresses for VLANIF interfaces.
   
   
   
   # Configure an IPv4 address for VLANIF 10.
   
   ```
   [~DeviceA] interface vlanif 10
   [*DeviceA-Vlanif10] ip address 10.1.1.1 24
   [*DeviceA-Vlanif10] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
   
   # Configure an IPv4 address for VLANIF 11.
   
   ```
   [~DeviceA] interface vlanif 11
   [*DeviceA-Vlanif11] ip address 10.1.2.1 24
   [*DeviceA-Vlanif11] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
4. Configure interface address pools.
   
   
   
   # Configure the clients connected to VLANIF 10 to obtain IPv4 addresses and other network parameters from the address pool on VLANIF 10.
   
   ```
   [~DeviceA] interface vlanif 10
   [~DeviceA-Vlanif10] dhcp select interface
   [*DeviceA-Vlanif10] dhcp server gateway-list 10.1.1.1
   [*DeviceA-Vlanif10] dhcp server lease day 30
   [*DeviceA-Vlanif10] dhcp server domain-name huawei.com
   [*DeviceA-Vlanif10] dhcp server dns-list 10.1.3.1
   [*DeviceA-Vlanif10] dhcp server static-bind ip-address 10.1.1.100 mac-address 00e0-fc12-3456
   [*DeviceA-Vlanif10] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
   
   # Configure the clients connected to VLANIF 11 to obtain IPv4 addresses and other network parameters from the address pool on VLANIF 11.
   
   ```
   [~DeviceA] interface vlanif 11
   [~DeviceA-Vlanif11] dhcp select interface
   [*DeviceA-Vlanif11] dhcp server gateway-list 10.1.2.1
   [*DeviceA-Vlanif11] dhcp server lease day 2
   [*DeviceA-Vlanif11] dhcp server domain-name huawei.com
   [*DeviceA-Vlanif11] dhcp server dns-list 10.1.3.1
   [*DeviceA-Vlanif11] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

# On DeviceA, run the [**display ip pool**](cmdqueryname=display+ip+pool) command to check IPv4 address configuration and allocation in address pools. The **Used** field displays the number of used IPv4 addresses in each address pool.

```
[~DeviceA] display ip pool interface vlanif10
  Pool-name        : Vlanif10
  Pool-No          : 0
  Lease            : 30 Days 0 Hours 0 Minutes
  Domain-name      : huawei.com
  DNS-server0      : 10.1.3.1
  NBNS-server0     : -
  Netbios-type     : -
  Position         : Interface
  Status           : Unlocked
  Gateway-0        : 10.1.1.1
  Network          : 10.1.1.0
  Mask             : 255.255.255.0
  VPN instance     : --
  Logging          : Disable
  Conflicted address recycle interval: -
  Address Statistic: Total       :253       Used        :100
                     Idle        :153       Expired     :0
                     Conflict    :0         Disabled     :0

 -------------------------------------------------------------------------------
  Network section
         Start           End       Total    Used Idle(Expired) Conflict Disabled
 -------------------------------------------------------------------------------
        10.1.1.1      10.1.1.254     253     100        153(0)       0     0
 -------------------------------------------------------------------------------
```
```
[~DeviceA] display ip pool interface vlanif11
  Pool-name        : Vlanif11
  Pool-No          : 1
  Lease            : 2 Days 0 Hours 0 Minutes
  Domain-name      : huawei.com
  DNS-server0      : 10.1.3.1
  NBNS-server0     : -
  Netbios-type     : -
  Position         : Interface
  Status           : Unlocked
  Gateway-0        : 10.1.2.1
  Network          : 10.1.2.0
  Mask             : 255.255.255.0
  VPN instance     : --
  Logging          : Disable
  Conflicted address recycle interval: -
  Address Statistic: Total       :253       Used        :3
                     Idle        :250       Expired     :0
                     Conflict    :0         Disabled     :0

 -------------------------------------------------------------------------------
  Network section
         Start           End       Total    Used Idle(Expired) Conflict Disabled
 -------------------------------------------------------------------------------
        10.1.2.1      10.1.1.254    253       3        250(0)       0     0
 -------------------------------------------------------------------------------
```

# Check IPv4 address information on Client\_1. You can check that Client\_1 has obtained the IPv4 address 10.1.1.100/24.

# Check IPv4 address information on other DHCPv4 clients. You can check that the clients have obtained IPv4 addresses.

#### Configuration Scripts

DeviceA

```
#
sysname DeviceA
#
vlan batch 10 11
#
dhcp enable
#
interface Vlanif10
 ip address 10.1.1.1 255.255.255.0
 dhcp select interface
 dhcp server gateway-list 10.1.1.1
 dhcp server static-bind ip-address 10.1.1.100 mac-address  00e0-fc12-3456
 dhcp server lease day 30 hour 0 minute 0
 dhcp server dns-list 10.1.3.1
 dhcp server domain-name huawei.com
#
interface Vlanif11
 ip address 10.1.2.1 255.255.255.0
 dhcp select interface
 dhcp server gateway-list 10.1.2.1
 dhcp server lease day 2 hour 0 minute 0
 dhcp server dns-list 10.1.3.1
 dhcp server domain-name huawei.com
#
interface 100GE1/0/1
 port default vlan 10
#
interface 100GE1/0/2
 port default vlan 11
#
return
```
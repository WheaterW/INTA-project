Example for Configuring DHCPv6 Snooping on a Layer 3 Device
===========================================================

Applications of DHCPv6 snooping on Layer 3 devices include IPv6/MAC spoofing attack defense.

#### Networking Requirements

As shown in [Figure 1](#EN-US_CONCEPT_0314612912__fig8310216184110), DHCPv6 snooping needs to be configured on the Layer 3 interface GE 0/1/0 of the DHCPv6 relay agent to allow DHCPv6 client access.

If a user goes offline unexpectedly after obtaining an IPv6 address, the system can automatically detect the logout, delete the corresponding DHCPv6 binding entry, and instruct the DHCPv6 server to release this IPv6 address. In addition, DHCPv6 snooping enabled on the DHCPv6 relay can prevent against IPv6/MAC spoofing attacks.

DHCPv6 client 1 uses a dynamically assigned IPv6 address, and DHCPv6 client 2 uses a statically assigned IPv6 address.

**Figure 1** Network diagram of configuring DHCPv6 snooping on a Layer 3 device![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent GE 0/1/0 and GE 0/2/0, respectively.


  
![](figure/en-us_image_0316480564.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IPv6 addresses for interfaces.
2. Enable DHCPv6 snooping in the system view and interface view.
3. Configure a DHCPv6 snooping binding table to check IPv6 packets against the binding table in order to prevent against IPv6/MAC spoofing attacks.
4. Enable association between ND probe and DHCPv6 snooping.

#### Procedure

1. Configure IPv6 addresses for interfaces.
   
   # Configure IPv6 addresses for GE 0/1/0 and GE 0/2/0.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DHCPv6-relay
   [*HUAWEI] commit
   [~DHCPv6-relay] interface gigabitethernet 0/1/0
   [~DHCPv6-relay-GigabitEthernet0/1/0] ipv6 enable
   [*DHCPv6-relay-GigabitEthernet0/1/0] ipv6 address 2001:db8:2::1/64
   [*DHCPv6-relay-GigabitEthernet0/1/0] commit
   [~DHCPv6-relay-GigabitEthernet0/1/0] quit
   [~DHCPv6-relay] interface gigabitethernet 0/2/0
   [~DHCPv6-relay-GigabitEthernet0/2/0] ipv6 enable
   [*DHCPv6-relay-GigabitEthernet0/2/0] ipv6 address 2001:db8:3::1/64
   [*DHCPv6-relay-GigabitEthernet0/2/0] commit
   [~DHCPv6-relay-GigabitEthernet0/2/0] quit
   ```
2. Enable DHCPv6 snooping.
   
   # Enable DHCPv6 snooping both globally and on an interface.
   
   ```
   [~DHCPv6-relay] dhcpv6 snooping enable
   [*DHCPv6-relay] interface gigabitethernet 0/1/0
   [*DHCPv6-relay-GigabitEthernet0/1/0] dhcpv6 snooping enable 
   [*DHCPv6-relay-GigabitEthernet0/1/0] commit
   [~DHCPv6-relay-GigabitEthernet0/1/0] quit
   ```
3. Configure the IPv6 packet check function and a DHCPv6 snooping binding entry.
   
   # Configure the IPv6 packet check function on the DHCPv6 client-side interface to prevent IPv6/MAC spoofing attacks.
   
   ```
   [~DHCPv6-relay] interface gigabitethernet 0/1/0
   [~DHCPv6-relay-GigabitEthernet0/1/0] dhcpv6 snooping check ipv6 enable
   [*DHCPv6-relay-GigabitEthernet0/1/0] commit
   [~DHCPv6-relay-GigabitEthernet0/1/0] quit
   ```
   
   # Configure a static binding entry.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   For users who use static IPv6 addresses, you need to configure static DHCPv6 snooping binding entries for them.
   
   ```
   [~DHCPv6-relay] interface gigabitethernet 0/1/0
   [~DHCPv6-relay-GigabitEthernet0/1/0] dhcpv6 snooping bind-table static ipv6-address 2001:db8:1::1 mac-address 00e0-fc12-3456
   [*DHCPv6-relay-GigabitEthernet0/1/0] commit
   ```
   
   # Configure a destination IPv6 address for the DHCPv6 packets on GE 0/1/0.
   
   ```
   [~DHCPv6-relay-GigabitEthernet0/1/0] dhcpv6 relay destination 2001:db8:3::2
   [*DHCPv6-relay-GigabitEthernet0/1/0] commit
   ```
4. Enable association between ND probe and DHCPv6 snooping.
   
   # Configure the system to perform ND probe for the IPv6 addresses that have reached the aging time in DHCPv6 snooping entries and do not exist in ND entries. If the system fails to detect a user within the specified number of probes, the system will delete the corresponding DHCPv6 snooping binding entry and instruct the DHCPv6 server to release the user's IPv6 address.
   
   ```
   [~DHCPv6-relay] dhcpv6 snooping nd-detect enable
   [*DHCPv6-relay] commit
   ```
5. Verify the configuration.
   
   # Run the **display dhcpv6 snooping interface** command to check whether the DHCPv6 snooping function is enabled.
   
   ```
   [~DHCPv6-relay] display dhcpv6 snooping interface gigabitethernet 0/1/0
    dhcpv6 snooping enable
    dhcpv6 snooping check ipv6 enable
    ipv6 total                   0             
   ```
   
   # Run the **display dhcpv6 snooping bind-table static** command to check information about the DHCPv6 snooping binding table.
   
   ```
   [~DHCPv6-relay] display dhcpv6 snooping bind-table static
   bind-table:
   ifname         vrf            p/cvlan    mac-address    ipv6-address           tp lease    
   ---------------------------------------------------------------------------------------
   GE0/1/0        --             0000/0000  00e0-fc12-3456 2001:DB8:1::1/128      S  0
   ---------------------------------------------------------------------------------------
   binditem count:      1                   binditem total count: 1 
   ```

#### Configuration Files

```
# 
sysname DHCPv6-relay 
# 
dhcpv6 snooping enable
dhcpv6 snooping nd-detect enable                                     
#
interface GigabitEthernet0/1/0 
 undo shutdown  
 ipv6 enable
 ipv6 address 2001:DB8:2::1/64 
 dhcpv6 snooping enable
 dhcpv6 snooping check ipv6 enable
 dhcpv6 relay destination 2001:DB8:3::2 
 dhcpv6 snooping bind-table static ipv6-address 2001:DB8:1::1 mac-address 00e0-fc12-3456
#                                   
interface GigabitEthernet0/2/0 
 undo shutdown 
 ipv6 enable
 ipv6 address 2001:DB8:3::1/64 
# 
return 
```
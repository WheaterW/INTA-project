Example for Configuring DHCP Snooping for a Layer 2 Device
==========================================================

DHCP snooping is used on Layer 2 devices to prevent bogus DHCP server attacks, man-in-the-middle attacks, IP/MAC spoofing attacks, attacks by changing the CHADDR value, attacks by sending bogus DHCP renew packets, and attacks by sending DHCP request packets.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172372033__fig_dc_vrp_dhcp-snooping_cfg_004601), a DHCP client is connected to DeviceA through VLAN 10. Configure DHCP snooping on the Layer 2 interfaces, GE0/1/0 and GE0/1/1, of DeviceA. Configure the interfaces connecting to DHCP clients as untrusted interfaces and the interface connecting to the DHCP relay agent as a trusted interface.

Configure DHCP snooping on DeviceA to prevent the following attacks:

* Bogus DHCP server attacks
* Man-in-the-middle attacks and IP/MAC address spoofing
* Denial of service (DoS) attacks by changing the CHADDR field value
* Attacks by sending bogus DHCP request packets for extending IP address lease

DHCP client 1 uses a dynamic IP address, and DHCP client 2 uses a static IP address.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent GE0/1/0, GE0/1/1, and GE0/1/2, respectively.


**Figure 1** Networking diagram for configuring DHCP snooping for a Layer 2 device  
![](images/fig_dc_vrp_dhcp-snooping_cfg_004601.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable DHCP snooping in the system view and VLAN view.
2. Configure trusted and untrusted interfaces to prevent bogus DHCP server attacks.
3. Configure the DHCP snooping binding table so that the device can check ARP, IP, and DHCP request packets to prevent man-in-the-middle attacks, IP/MAC address spoofing, and attacks by sending bogus DHCP request packets for extending IP address lease.
4. Enable CHADDR field check to prevent attacks that change CHADDR field values in packets.
5. Configure Option 82 to create a binding table containing accurate interface information.
6. Configure the device to report alarms to the Network Management System (NMS).
7. (Optional) Configure the whitelist function for DHCP snooping.

#### Data Preparation

To complete the configuration, you need the following data:

* ID of the VLAN to which the interface belongs
* Static IP address to which packets can be forwarded
* Threshold of reporting alarms to the NMS

#### Procedure

1. Enable DHCP snooping.
   
   
   
   # Enable DHCP snooping globally.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceA
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceA] dhcp snooping enable
   ```
   
   # Switch Layer 3 interfaces to Layer 2 interfaces.
   
   ```
   [~DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] portswitch
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] port default vlan 10
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] quit
   ```
   ```
   [~DeviceA] interface gigabitethernet 0/1/1
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1] portswitch
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] port default vlan 10
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1] quit
   ```
   ```
   [~DeviceA] interface gigabitethernet 0/1/2
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/2] portswitch
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] port default vlan 10
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/2] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the interfaces are Layer 2 ones, running the **portswitch** command is not required.
   
   # Enable DHCP snooping on the Layer 2 interfaces.
   
   ```
   [~DeviceA] vlan 10
   ```
   ```
   [*DeviceA-vlan10] port gigabitethernet 0/1/0
   ```
   ```
   [*DeviceA-vlan10] dhcp snooping enable interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceA-vlan10] port gigabitethernet 0/1/1
   ```
   ```
   [*DeviceA-vlan10] dhcp snooping enable interface gigabitethernet 0/1/1
   ```
   ```
   [*DeviceA-vlan10] port gigabitethernet 0/1/2
   ```
   ```
   [*DeviceA-vlan10] dhcp snooping enable interface gigabitethernet 0/1/2
   ```
   ```
   [*DeviceA-vlan10] commit
   ```
   ```
   [~DeviceA-vlan10] quit
   ```
2. Configure trusted interfaces.
   
   
   
   # Configure the interface connecting to the DHCP server as a trusted interface, and enable DHCP snooping on all the interfaces connecting to the DHCP client. (If the interface on the client side is not configured as a trusted interface, the default interface mode is untrusted after DHCP snooping is enabled on the interface.) This prevents bogus DHCP server attacks.
   
   ```
   [~DeviceA] vlan 10
   ```
   ```
   [*DeviceA-vlan10] dhcp snooping trusted interface gigabitethernet 0/1/2
   ```
   ```
   [*DeviceA-vlan10] commit
   ```
   ```
   [~DeviceA-vlan10] quit
   ```
3. Enable packet check and configure the DHCP snooping binding table.
   
   
   
   # Configure the device to check Address Resolution Protocol (ARP) and IP packets on the interface on the DHCP client side. This prevents man-in-the-middle attacks and IP/MAC address spoofing.
   
   ```
   [~DeviceA] vlan 10
   ```
   ```
   [*DeviceA-vlan10] dhcp snooping check arp enable interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceA-vlan10] dhcp snooping check arp enable interface gigabitethernet 0/1/1
   ```
   ```
   [*DeviceA-vlan10] dhcp snooping check ip enable interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceA-vlan10] dhcp snooping check ip enable interface gigabitethernet 0/1/1
   ```
   ```
   [*DeviceA-vlan10] commit
   ```
   ```
   [~DeviceA-vlan10] quit
   ```
   
   # Configure the device to check DHCP request packets on the interface on the DHCP client side. This prevents attacks in which the attacker sends bogus DHCP request packets for extending IP address lease.
   
   ```
   [~DeviceA] vlan 10
   ```
   ```
   [*DeviceA-vlan10] dhcp snooping check dhcp-request enable interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceA-vlan10] dhcp snooping check dhcp-request enable interface gigabitethernet 0/1/1
   ```
   ```
   [*DeviceA-vlan10] commit
   ```
   ```
   [~DeviceA-vlan10] quit
   ```
   
   # Configure the device to check packets containing the CHADDR field on the interface on the DHCP client side. This prevents DoS attacks in which the attacker changes the CHADDR field value.
   
   ```
   [~DeviceA] vlan 10
   ```
   ```
   [*DeviceA-vlan10] dhcp check chaddr enable interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceA-vlan10] dhcp check chaddr enable interface gigabitethernet 0/1/1
   ```
   ```
   [*DeviceA-vlan10] commit
   ```
   ```
   [~DeviceA-vlan10] quit
   ```
   
   # Configure static DHCP snooping binding table entries.
   
   For users using static IP addresses, static DHCP snooping binding table entries must be manually configured.
   
   ```
   [~DeviceA] vlan 10
   ```
   ```
   [*DeviceA-vlan10] dhcp snooping bind-table static ip-address 10.1.3.1 mac-address 00e0-fc5e-008a interface gigabitethernet 0/1/1
   ```
   ```
   [*DeviceA-vlan10] commit
   ```
   ```
   [~DeviceA-vlan10] quit
   ```
4. Configure Option 82 field insertion.
   
   
   
   # Enable Option 82 field insertion to set up dynamic binding table entries with accurate interface information.
   
   ```
   [~DeviceA] vlan 10
   ```
   ```
   [*DeviceA-vlan10] dhcp option82 insert enable interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceA-vlan10] dhcp option82 insert enable interface gigabitethernet 0/1/1
   ```
   ```
   [*DeviceA-vlan10] commit
   ```
   ```
   [~DeviceA-vlan10] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   To configure a Layer 2 device to strip the Option 82 field before sending DHCP Relay packets to the client, perform either of the following operations:
   
   * Enable Option 82 field insertion on the interfaces connecting to the client and server.
   * Enable DHCP snooping for the VLAN to which the interface connecting to the client belongs, and configure this interface as a trusted interface.
5. Configure the device to report alarms to the NMS.
   
   
   
   # Enable alarm reporting to the NMS.
   
   ```
   [~DeviceA] vlan 10
   ```
   ```
   [*DeviceA-vlan10] dhcp snooping alarm dhcp-reply enable interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceA-vlan10] dhcp snooping alarm dhcp-reply enable interface gigabitethernet 0/1/1
   ```
   ```
   [*DeviceA-vlan10] dhcp snooping alarm arp enable interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceA-vlan10] dhcp snooping alarm arp enable interface gigabitethernet 0/1/1
   ```
   ```
   [*DeviceA-vlan10] dhcp snooping alarm ip enable interface gigabitethernet 0/1/1
   ```
   ```
   [*DeviceA-vlan10] dhcp snooping alarm ip enable interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceA-vlan10] dhcp snooping alarm dhcp-chaddr enable interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceA-vlan10] dhcp snooping alarm dhcp-chaddr enable interface gigabitethernet 0/1/1
   ```
   ```
   [*DeviceA-vlan10] dhcp snooping alarm dhcp-request enable interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceA-vlan10] dhcp snooping alarm dhcp-request enable interface gigabitethernet 0/1/1
   ```
   ```
   [*DeviceA-vlan10] commit
   ```
   ```
   [~DeviceA-vlan10] quit
   ```
   
   # Configure the alarm thresholds.
   
   ```
   [~DeviceA] vlan 10
   ```
   ```
   [*DeviceA-vlan10] dhcp snooping alarm dhcp-reply threshold 10 interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceA-vlan10] dhcp snooping alarm dhcp-reply threshold 10 interface gigabitethernet 0/1/1
   ```
   ```
   [*DeviceA-vlan10] dhcp snooping alarm arp threshold 10 interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceA-vlan10] dhcp snooping alarm arp threshold 10 interface gigabitethernet 0/1/1
   ```
   ```
   [*DeviceA-vlan10] dhcp snooping alarm ip threshold 10 interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceA-vlan10] dhcp snooping alarm ip threshold 10 interface gigabitethernet 0/1/1
   ```
   ```
   [*DeviceA-vlan10] dhcp snooping alarm dhcp-chaddr threshold 10 interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceA-vlan10] dhcp snooping alarm dhcp-chaddr threshold 10 interface gigabitethernet 0/1/1
   ```
   ```
   [*DeviceA-vlan10] dhcp snooping alarm dhcp-request threshold 10 interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceA-vlan10] dhcp snooping alarm dhcp-request threshold 10 interface gigabitethernet 0/1/1
   ```
   ```
   [*DeviceA-vlan10] commit
   ```
   ```
   [~DeviceA-vlan10] quit
   ```
6. (Optional) Configure the whitelist function for DHCP snooping.
   
   
   
   # Create a whitelist.
   
   ```
   [~DeviceA] dhcp snooping packet whitelist whitelist1
   ```
   
   # Configure rules for the whitelist.
   
   ```
   [*DeviceA-dhcpsnp-whitelist-whitelist1] dhcp packet-rule 1 source-ip 1.1.1.1 255.255.255.0 destination-ip 2.2.2.2 255.255.255.0 source-port bootps destination-port bootpc
   ```
   ```
   [*DeviceA-dhcpsnp-whitelist-whitelist1] commit
   ```
   ```
   [~DeviceA-dhcpsnp-whitelist-whitelist1] quit
   ```
   
   # Apply the whitelist.
   
   ```
   [~DeviceA] dhcp snooping apply packet whitelist whitelist1
   ```
   ```
   [*DeviceA] commit
   ```
7. Verify the configuration.
   
   
   
   Run the **display dhcp snooping global** command on DeviceA. You can see that DHCP snooping is enabled in the system view and interface view. You can also view the statistics on the alarms sent to the NMS.
   
   ```
   [~DeviceA] display dhcp snooping global
   ```
   ```
    dhcp snooping enable
   ```
   ```
   [~DeviceA] display dhcp snooping vlan 10 interface gigabitethernet 0/1/0
   ```
   ```
   dhcp snooping enable interface GigabitEthernet0/1/0
    dhcp snooping check arp enable interface GigabitEthernet0/1/0
    dhcp snooping alarm arp enable interface GigabitEthernet0/1/0
    dhcp snooping alarm arp threshold 10 interface gigabitethernet 0/1/0
    dhcp snooping check ip enable interface GigabitEthernet0/1/0
    dhcp snooping alarm ip enable interface GigabitEthernet0/1/0
    dhcp snooping alarm ip threshold 10 interface gigabitethernet 0/1/0
    dhcp snooping alarm dhcp-reply enable interface GigabitEthernet0/1/0
    dhcp snooping alarm dhcp-reply threshold 10 interface GigabitEthernet0/1/0
    dhcp check chaddr enable interface gigabitethernet 0/1/0
    dhcp snooping alarm dhcp-chaddr enable interface GigabitEthernet0/1/0
    dhcp snooping alarm dhcp-chaddr threshold 10 interface GigabitEthernet0/1/0
    dhcp snooping check dhcp-request enable interface GigabitEthernet0/1/0
    dhcp snooping alarm dhcp-request enable interface GigabitEthernet0/1/0
    dhcp snooping alarm dhcp-request threshold 10 interface GigabitEthernet0/1/0
    arp total                  0
    ip total                   0
    dhcp-request total         0
    chaddr&src mac total       0
    dhcp-reply total           0
   ```
   ```
   [~DeviceA] display dhcp snooping vlan 10 interface gigabitethernet 0/1/1
   ```
   ```
   dhcp snooping enable interface GigabitEthernet0/1/1
    dhcp snooping check arp enable interface GigabitEthernet0/1/1
    dhcp snooping alarm arp enable interface GigabitEthernet0/1/1
    dhcp snooping alarm arp threshold 10 interface gigabitethernet 0/1/1 
    dhcp snooping check ip enable interface GigabitEthernet0/1/1
    dhcp snooping alarm ip enable interface GigabitEthernet0/1/1
    dhcp snooping alarm ip threshold 10 interface gigabitethernet 0/1/1 
    dhcp snooping alarm dhcp-reply enable interface GigabitEthernet0/1/1
    dhcp snooping alarm dhcp-reply threshold 10 interface GigabitEthernet0/1/1
    dhcp check chaddr enable interface GigabitEthernet0/1/1
    dhcp snooping alarm dhcp-chaddr enable interface GigabitEthernet0/1/1
    dhcp snooping alarm dhcp-chaddr threshold 10 interface GigabitEthernet0/1/1
    dhcp snooping check dhcp-request enable interface GigabitEthernet0/1/1
    dhcp snooping alarm dhcp-request enable interface GigabitEthernet0/1/1
    dhcp snooping alarm dhcp-request threshold 10 interface GigabitEthernet0/1/1
    arp total                  0
    ip total                   0
    dhcp-request total         0
    chaddr&src mac total       0
    dhcp-reply total           0
   ```
   ```
   [~DeviceA] display dhcp snooping vlan 10 interface gigabitethernet 0/1/2
   ```
   ```
    dhcp snooping enable interface GigabitEthernet0/1/2
    dhcp snooping trusted interface GigabitEthernet0/1/2
    arp total                  0
    ip total                   0
    dhcp-request total         0
    chaddr&src mac total       0
    dhcp-reply total           0
   ```
   ```
   [~DeviceA] display dhcp snooping bind-table static
   ```
   ```
   bind-table:
   ifname         vrf/vsi/bdid   p/cvlan   mac-address    ip-address      tp lease     
   -------------------------------------------------------------------------------
   GE0/1/1     --        0100/0000 00e0-fc5e-008a 010.001.003.001 S  0
   -------------------------------------------------------------------------------
   binditem count:      1                   binditem total count: 1
   
   ```
   ```
   [~DeviceA] display dhcp option82 vlan 10 interface gigabitethernet 0/1/0
   ```
   ```
    dhcp option82 insert enable interface GigabitEthernet0/1/0
   ```
   ```
   [~DeviceA] display dhcp option82 vlan 10 interface gigabitethernet 0/1/1
   ```
   ```
    dhcp option82 insert enable interface GigabitEthernet0/1/1
   ```

#### Configuration Files

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
vlan batch 10
```
```
#
```
```
dhcp snooping enable
```
```
#
```
```
dhcp snooping packet whitelist whitelist1
```
```
dhcp packet-rule 1 source-ip 1.1.1.1 255.255.255.0 destination-ip 2.2.2.2 255.255.255.0 source-port bootps destination-port bootpc
```
```
#
```
```
dhcp snooping apply packet whitelist whitelist1
```
```
#
```
```
vlan 10
 dhcp snooping alarm dhcp-reply threshold 1000
 dhcp check chaddr enable
 dhcp snooping alarm dhcp-chaddr enable
 dhcp snooping alarm dhcp-chaddr threshold 100
 dhcp snooping check dhcp-request enable
 dhcp snooping alarm dhcp-request enable
 dhcp snooping alarm dhcp-request threshold 100
 dhcp snooping enable interface GigabitEthernet0/1/0
 dhcp snooping check arp enable interface GigabitEthernet0/1/0
 dhcp snooping alarm arp enable interface GigabitEthernet0/1/0
 dhcp snooping alarm arp threshold 10 interface GigabitEthernet0/1/0
 dhcp snooping check ip enable interface GigabitEthernet0/1/0
 dhcp snooping alarm ip enable interface GigabitEthernet0/1/0
 dhcp snooping alarm ip threshold 10 interface GigabitEthernet0/1/0
 dhcp snooping alarm dhcp-reply enable interface GigabitEthernet0/1/0
 dhcp snooping alarm dhcp-reply threshold 10 interface GigabitEthernet0/1/0
 dhcp check chaddr enable interface GigabitEthernet0/1/0
 dhcp snooping alarm dhcp-chaddr enable interface GigabitEthernet0/1/0
 dhcp snooping alarm dhcp-chaddr threshold 10 interface GigabitEthernet0/1/0
 dhcp snooping check dhcp-request enable interface GigabitEthernet0/1/0
 dhcp snooping alarm dhcp-request enable interface GigabitEthernet0/1/0
 dhcp snooping alarm dhcp-request threshold 10 interface GigabitEthernet0/1/0
 dhcp snooping enable interface GigabitEthernet0/1/1
 dhcp snooping check arp enable interface GigabitEthernet0/1/1
 dhcp snooping alarm arp enable interface GigabitEthernet0/1/1
 dhcp snooping alarm arp threshold 10 interface GigabitEthernet0/1/1
 dhcp snooping check ip enable interface GigabitEthernet0/1/1
 dhcp snooping alarm ip enable interface GigabitEthernet0/1/1
 dhcp snooping alarm ip threshold 10 interface GigabitEthernet0/1/1
 dhcp snooping alarm dhcp-reply enable interface GigabitEthernet0/1/1
 dhcp snooping alarm dhcp-reply threshold 10 interface GigabitEthernet0/1/1
 dhcp check chaddr enable interface GigabitEthernet0/1/1
 dhcp snooping alarm dhcp-chaddr enable interface GigabitEthernet0/1/1
 dhcp snooping alarm dhcp-chaddr threshold 10 interface GigabitEthernet0/1/1
 dhcp snooping check dhcp-request enable interface GigabitEthernet0/1/1
 dhcp snooping alarm dhcp-request enable interface GigabitEthernet0/1/1
 dhcp snooping alarm dhcp-request threshold 10 interface GigabitEthernet0/1/1
 dhcp snooping enable interface GigabitEthernet0/1/2
 dhcp snooping trusted interface GigabitEthernet0/1/2
 dhcp check chaddr enable interface GigabitEthernet0/1/2
 dhcp snooping bind-table static ip-address 10.1.3.1 mac-address 00e0-fc5e-008a interface gigabitethernet 0/1/1
 dhcp option82 insert enable interface GigabitEthernet0/1/0
 dhcp option82 insert enable interface GigabitEthernet0/1/1
 dhcp option82 insert enable interface GigabitEthernet0/1/2
#                                                                     
```
```
interface GigabitEthernet0/1/0
```
```
 undo shutdown
```
```
 portswitch
```
```
 port default vlan 10
```
```
#
```
```
interface GigabitEthernet0/1/1
```
```
 undo shutdown
```
```
 portswitch
```
```
 port default vlan 10
```
```
#
```
```
interface GigabitEthernet0/1/2
```
```
 undo shutdown
```
```
 portswitch
```
```
 port default vlan 10
```
```
#
```
```
return
```
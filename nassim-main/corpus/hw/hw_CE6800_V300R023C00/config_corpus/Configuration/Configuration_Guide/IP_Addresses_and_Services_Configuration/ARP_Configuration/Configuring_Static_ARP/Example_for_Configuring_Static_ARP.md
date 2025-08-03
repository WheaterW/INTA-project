Example for Configuring Static ARP
==================================

Example for Configuring Static ARP

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001176663593__fig7672135224615), DeviceA is used to connect the departments of an enterprise, and each department is added to a different VLAN. Fixed IP addresses have been manually assigned to the file backup server and hosts in the president's office, and dynamic IP addresses have been assigned to hosts in the marketing and R&D departments using DHCP. In the marketing department, hosts can access the Internet and are often subject to ARP attacks. Attackers target DeviceA and modify its dynamic ARP entries, interrupting communication between hosts in the president's office and external devices, and preventing hosts in all departments from accessing the file backup server. The enterprise requires that static ARP entries be configured on DeviceA to ensure that the president's office and external devices can communicate securely and that all departments can access the file backup server.

**Figure 1** Network diagram of configuring static ARP![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](figure/en-us_image_0000001176743529.png "Click to enlarge")

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure static ARP entries for hosts in the president's office on DeviceA to prevent the ARP entries of the hosts from being modified by ARP attack messages. This ensures that hosts in the president's office and external devices can communicate securely.
2. Configure a static ARP entry for the file backup server on DeviceA to prevent the ARP entry of the file backup server from being modified by ARP attack messages. This ensures that all departments can access the file backup server.

#### Procedure

1. Create a VLAN on DeviceA and configure an IP address for each interface.
   
   
   
   # Create VLAN 10, add interface 1 to VLAN 10, and configure an IP address for VLANIF 10.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] [commit](cmdqueryname=commit)
   [~DeviceA] vlan batch 10
   [~DeviceA] interface 100GE1/0/1
   [~DeviceA-100GE1/0/1] portswitch
   [~DeviceA-100GE1/0/1] port link-type access
   [*DeviceA-100GE1/0/1] port default vlan 10
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface vlanif 1
   [*DeviceA-Vlanif10] ip address 10.164.1.20 24
   [*DeviceA-Vlanif10] quit
   ```
   
   # Configure an IP address for interface 2.
   
   ```
   [~DeviceA] interface 100GE1/0/2
   [~DeviceA-100GE1/0/2] undo portswitch
   [*DeviceA-100GE1/0/2] ip address 10.164.10.10 24
   [*DeviceA-100GE1/0/2] quit
   ```
   
   # Configure an IP address for interface 3.
   
   ```
   [~DeviceA] interface 100GE1/0/3
   [~DeviceA-100GE1/0/3] undo portswitch
   [*DeviceA-100GE1/0/3] ip address 10.164.20.1 24
   [*DeviceA-100GE1/0/3] quit
   ```
2. Configure static ARP entries on DeviceA.
   
   
   ```
   [~DeviceA] arp static 10.164.1.1 00e0-fc01-0001 vlan 10 interface 100GE1/0/1
   [~DeviceA] arp static 10.164.10.1 00e0-fc01-003a interface 100GE1/0/2
   ```

#### Verifying the Configuration

# Run the [**display arp static**](cmdqueryname=display+arp+static) command to check the configured static ARP entries.

#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  vlan batch 10
  #
  interface Vlanif10
   ip address 10.164.1.20 255.255.255.0
  #
  interface 100GE1/0/1
   port link-type access
   port default vlan 10
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.164.10.10 255.255.255.0
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 10.164.20.1 255.255.255.0
  #
  arp static 10.164.1.1 00e0-fc01-0001 vlan 10 interface 100GE1/0/1
  arp static 10.164.10.1 00e0-fc01-003a interface 100GE1/0/2
  #                                                                            
          
  return
  ```
Example for Configuring PIM-SM BSR Administrative Domains
=========================================================

Example for Configuring PIM-SM BSR Administrative Domains

#### Networking Requirements

On a PIM-SM network that uses dynamic RP election, it is required that BSR administrative domains be configured to allow C-BSRs to serve multicast groups in a specified group address range.

On the ISP network shown in [Figure 1](#EN-US_TASK_0000001130783624__fig_dc_vrp_multicast_cfg_003801), multicast services are deployed. An IGP has been deployed on the network, unicast services are running properly, and the network has been connected to the Internet. It is required that configurations be performed to allow user hosts to receive VOD information in multicast mode.

![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent 100GE1/0/1, 100GE1/0/2, and 100GE1/0/3, respectively.


**Figure 1** Networking diagram of configuring PIM-SM BSR administrative domains  
![](figure/en-us_image_0000001176743363.png)

#### Precautions

Note the following during the configuration:

* Unicast routes on the network must be reachable because multicast routing depends on unicast routing.
* Multicast routing must be enabled on all devices.
* PIM-SM must be enabled on the interfaces that connect devices, the interfaces that directly connect devices to multicast sources, and the interfaces that directly connect devices to hosts.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IP addresses and a unicast routing protocol for interfaces on each device.
2. Enable multicast routing on all devices to be used to provide multicast services.
3. Enable PIM-SM on all interfaces of each multicast device.
4. Enable IGMP on the interfaces that directly connect devices to hosts.
5. Configure the BSR administrative domain function on all devices to be used to provide multicast services.
6. Configure dynamic RP election and C-BSRs in the BSR administrative domain corresponding to a specific multicast group.
7. Configure a multicast boundary on edge interfaces.

#### Data Preparation

To complete the configuration, you need the following data:

* Multicast group addresses: 239.1.0.0/16 and 239.2.0.0/16
* Multicast source addresses: 192.168.1.2/24 and 192.168.7.2/24

#### Procedure

1. Assign an IP address to each device interface and configure a unicast routing protocol. For detailed configurations, see Configuration Scripts.
2. Enable the multicast function on all devices and PIM-SM on all the involved interfaces.
   
   
   
   # Enable the multicast function on all devices and PIM-SM on all the involved interfaces.
   
   ```
   [~DeviceA] multicast routing-enable
   [*DeviceA] interface 100GE 1/0/1
   [*DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] pim sm
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100GE 1/0/2
   [*DeviceA-100GE1/0/2] pim sm
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100GE 1/0/3
   [*DeviceA-100GE 1/0/3] undo portswitch
   [*DeviceA-100GE1/0/3] pim sm
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] commit
   ```
   
   The configurations of DeviceB, DeviceC, and DeviceD are similar to the configuration of DeviceA, and are not mentioned here.
3. Enable IGMP on the interfaces connected to hosts. The configuration details are not mentioned here.
4. Configure the BSR administrative domain function on all devices to be used to provide multicast services.
   
   
   ```
   [~DeviceA] pim
   [~DeviceA-pim] c-bsr admin-scope
   [*DeviceA-pim] quit
   [*DeviceA] commit
   ```
   
   The configurations of DeviceB, DeviceC, and DeviceD are similar to the configuration of DeviceA, and are not mentioned here.
5. Configure dynamic RP election and C-BSRs in the BSR administrative domain corresponding to a specific multicast group.
   
   
   
   # Perform the following steps on one or more devices in the PIM-SM domain to configure dynamic RP election.
   
   ```
   [~DeviceA] pim
   [~DeviceA-pim] c-bsr group 239.1.0.0 255.255.0.0
   [*DeviceA-pim] c-bsr LoopBack0
   [*DeviceA-pim] c-rp LoopBack0
   [*DeviceA-pim] quit
   [*DeviceA] commit
   ```
   
   The configuration of DeviceB is similar to the configuration of DeviceA, and is not mentioned here.
6. Configure a multicast boundary on edge interfaces.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] interface 100GE 1/0/2
   [~DeviceA-100GE 1/0/2] undo portswitch
   [*DeviceA-100GE1/0/2] multicast boundary 239.1.0.0 16
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA-] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] interface 100GE 1/0/2
   [~DeviceB-100GE 1/0/2] undo portswitch
   [*DeviceB-100GE1/0/2] multicast boundary 239.2.0.0 16
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] commit
   ```

#### Verifying the Configuration

# Run the **display pim bsr-info** command to check BSR information on each device. For example, BSR information on DeviceA and DeviceB is as follows:

```
<DeviceA> display pim bsr-info
VPN-Instance: public net
 Elected AdminScoped BSR Count: 1
 Elected BSR Address: 1.1.1.1
     Priority: 0
     Hash mask length: 30
     State: Elected
     Scope: 239.1.0.0/16
     Uptime: 01:03:41
     Next BSR message scheduled at: 00:00:21
     C-RP Count: 1
 Candidate AdminScoped BSR Count: 1
 Candidate BSR Address: 1.1.1.1
     Priority: 0
     Hash mask length: 30
     State: Elected
     Scope: 239.1.0.0/16
     Wait to be BSR: 0
```
```
<DeviceB> display pim bsr-info
VPN-Instance: public net
 Elected AdminScoped BSR Count: 1
 Elected BSR Address: 2.2.2.2
     Priority: 0
     Hash mask length: 30
     State: Elected
     Scope: 239.2.0.0/16
     Uptime: 00:44:34
     Next BSR message scheduled at: 00:00:27
     C-RP Count: 1
 Candidate AdminScoped BSR Count: 1
 Candidate BSR Address: 2.2.2.2
     Priority: 0
     Hash mask length: 30
     State: Elected
     Scope: 239.2.0.0/16
     Wait to be BSR: 0 
```

# Run the **display pim rp-info** command to check RP information on each device. The following example shows the RP information on DeviceA:

```
<DeviceA> display pim rp-info
VPN-Instance: public net
 PIM-SM BSR RP Number:1
 Group/MaskLen: 239.1.0.0/16
     RP: 1.1.1.1 (local)
     Priority: 0
     Uptime: 01:05:04
     Expires: 00:02:28 
```

# Run the **display pim routing-table** command to view the PIM routing table on each device. Receiver1 requires the multicast data sent by the multicast source 192.168.1.2 to the multicast group 239.1.0.1, and Receiver2 requires the multicast data sent by the multicast source 192.168.7.2 to the multicast group 239.2.0.1. A command output example is as follows:

```
<DeviceC> display pim routing-table
VPN-Instance: public net
 Total 1 (*, G) entry; 1 (S, G) entry

 (*, 239.1.0.1)
     RP: 1.1.1.1
     Protocol: pim-sm, Flag: WC
     UpTime: 00:00:03
     Upstream interface: 100GE1/0/3, Refresh time: 00:00:03
         Upstream neighbor: 192.168.3.1
         RPF prime neighbor: 192.168.3.1
     Downstream interface(s) information:
     Total number of downstreams: 1
        1: 100GE1/0/4
             Protocol: static, UpTime: 00:00:03, Expires: -

 (192.168.1.2, 239.1.0.1)
     RP: 1.1.1.1
     Protocol: pim-sm, Flag: SPT SG_RCVR
     UpTime: 00:04:10
     Upstream interface: 100GE1/0/3, Refresh time: 00:04:10
         Upstream neighbor: 192.168.3.1
         RPF prime neighbor: 192.168.3.1
     Downstream interface(s) information:
     Total number of downstreams: 1
        1: 100GE1/0/4
             Protocol: static, UpTime: 00:04:10, Expires: -
```
```
<DeviceD> display pim routing-table
VPN-Instance: public net
 Total 1 (*, G) entry; 1 (S, G) entry

 (*, 239.2.0.1)
     RP: 2.2.2.2
     Protocol: pim-sm, Flag: WC
     UpTime: 00:00:04
     Upstream interface: 100GE1/0/3, Refresh time: 00:00:04
         Upstream neighbor: 192.168.4.1
         RPF prime neighbor: 192.168.4.1
     Downstream interface(s) information:
     Total number of downstreams: 1
        1: 100GE1/0/4
             Protocol: static, UpTime: 00:00:04, Expires: -

 (192.168.7.2, 239.2.0.1)
     RP: 2.2.2.2
     Protocol: pim-sm, Flag: SPT SG_RCVR
     UpTime: 00:00:04
     Upstream interface: 100GE1/0/3, Refresh time: 00:00:04
         Upstream neighbor: 192.168.4.1
         RPF prime neighbor: 192.168.4.1
     Downstream interface(s) information:
     Total number of downstreams: 1
        1: 100GE1/0/4
             Protocol: static, UpTime: 00:00:04, Expires: -
```
#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  multicast routing-enable
  #
  isis 1
   network-entity 10.0000.0000.0001.00  
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.1.1 255.255.255.0
   pim sm
   isis enable 1
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.2.1 255.255.255.0
   pim sm
   multicast boundary 239.1.0.0 16
   isis enable 1
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 192.168.3.1 255.255.255.0
   pim sm
   isis enable 1
  #
  interface LoopBack0
   ip address 1.1.1.1 255.255.255.255
   pim sm
   isis enable 1 
  #
  pim
   c-bsr admin-scope
   c-bsr group 239.1.0.0 255.255.0.0
   c-bsr LoopBack0
   c-rp LoopBack0
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  multicast routing-enable  
  #
  isis 1
   network-entity 10.0000.0000.0002.00 
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.7.1 255.255.255.0
   pim sm
   isis enable 1 
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.2.2 255.255.255.0
   pim sm
   multicast boundary 239.2.0.0 16
   isis enable 1 
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 192.168.4.1 255.255.255.0
   pim sm
   isis enable 1
  #
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
   pim sm
   isis enable 1
  #
  pim
   c-bsr admin-scope
   c-bsr group 239.2.0.0 255.255.0.0
   c-bsr LoopBack1
   c-rp LoopBack1
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  multicast routing-enable
  #
  isis 1
   network-entity 10.0000.0000.0003.00  
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 192.168.3.2 255.255.255.0
   pim sm
   isis enable 1
  #
  interface 100GE1/0/4
   undo portswitch
   ip address 192.168.5.1 255.255.255.0
   pim sm
   igmp static-group 239.1.0.1 source 192.168.1.2
   isis enable 1     
  #
  pim
   c-bsr admin-scope
  #
  return 
  ```
* DeviceD
  
  ```
  #
  sysname DeviceD
  #
  multicast routing-enable
  #
  isis 1
   network-entity 10.0000.0000.0004.00 
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 192.168.4.2 255.255.255.0
   pim sm
   isis enable 1
  #
  interface 100GE1/0/4
   undo portswitch
   ip address 192.168.6.1 255.255.255.0
   pim sm
   igmp static-group 239.2.0.1 source 192.168.7.2
   isis enable 1        
  #
  pim
   c-bsr admin-scope
  #
  return
  ```
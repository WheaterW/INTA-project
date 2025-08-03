Example for Configuring VLAN-based Port Mirroring (1:N Scenario)
================================================================

Example for Configuring VLAN-based Port Mirroring (1:N Scenario)

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0000001226186793__fig_dc_ne_portmirror_cfg_002701), SwitchA forwards user packets from VLAN 10 and VLAN 20 to DeviceB. To monitor the packets forwarded by SwitchA from VLAN 10 to interface 2 on DeviceB, specify interface 1 on DeviceB as an observing port and configure port mirroring on interface 2. In this way, all the packets received by interface 2 are copied to interface 1 for analysis by HostD (the analyzer).

**Figure 1** Networking diagram for configuring port mirroring![](../../../../public_sys-resources/note_3.0-en-us.png) 

* The configurations in this example are performed on DeviceB and DeviceC, both of which can be HUAWEI NE40E-M2 series devices.
* Interfaces 1 through 3 in this example represent GE0/1/0, GE0/3/0, and GE0/3/1, respectively.

  
![](figure/en-us_image_0000001180947024.png)

| Device Name | Interface Number | Interface IP Address | Interface MAC Address |
| --- | --- | --- | --- |
| DeviceB | GE0/1/0 | 10.10.1.1/24 | - |
| DeviceB | GE0/3/0 | - | - |
| DeviceB | GE0/3/1 | 10.1.1.2/24 | - |
| DeviceC | GE0/1/0 | 10.1.1.1/24 | - |




#### Configuration Notes

Do not configure an interface as both an observing port and a mirrored port.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure GE0/1/0 on DeviceB as an observing port.
2. Configure GE0/3/0 on DeviceB as a mirrored port and enable port mirroring.

#### Data Preparation

To complete the configuration, you need the following data:

* Types and numbers of the observing port and mirrored port

#### Procedure

1. Configure IP addresses for interfaces and ensure that the corresponding routes are reachable. For configuration details, see [Configuration Files](#EN-US_TASK_0000001226186793__example1465079755213933) in this section.
2. Configure GE0/1/0 as an observing port.
   
   
   ```
   <DeviceB> system-view
   ```
   ```
   [~DeviceB] interface gigabitethernet0/1/0
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] port-observing observe-index 1
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] quit
   ```
3. Enable VLAN-based upstream port mirroring on GE0/3/0.
   
   
   ```
   [~DeviceB] vlan 10
   ```
   ```
   [*DeviceB-vlan10] commit
   ```
   ```
   [~DeviceB-vlan10] quit
   ```
   ```
   [~DeviceB] interface gigabitethernet0/3/0
   ```
   ```
   [~DeviceB-GigabitEthernet0/3/0] portswitch
   ```
   ```
   [*DeviceB-GigabitEthernet0/3/0] port default vlan 10
   ```
   ```
   [*DeviceB-GigabitEthernet0/3/0] port-mirroring inbound vlan 10
   ```
   ```
   [*DeviceB-GigabitEthernet0/3/0] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/3/0] quit
   ```
4. Specify the observing port for port mirroring.
   
   
   ```
   [~DeviceB] interface gigabitethernet0/3/0
   ```
   ```
   [~DeviceB-GigabitEthernet0/3/0] port-mirroring to observe-index 1
   ```
   ```
   [*DeviceB-GigabitEthernet0/3/0] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/3/0] quit
   ```
   
   After the preceding configuration is complete, all VLAN packets received by GE0/3/0 are mirrored to GE0/1/0.
5. Verify the configuration.
   
   
   
   Check mirroring information through the **ping** command or another traffic generation method. For example, if SwitchA sends 10 ping packets to GE0/3/0 on DeviceB, HostD is expected to receive all the packets sent by SwitchA.
   
   Check statistics about GE0/1/0 on DeviceB.
   
   ```
   <DeviceB> display interface gigabitethernet0/1/0
   ```
   ```
   GigabitEthernet0/1/0 current state : UP
   ```
   ```
   Line protocol current state : UP
   ```
   ```
   Description:XXXXXX, GigabitEthernet0/1/0 Interface
   ```
   ```
   Route Port,The Maximum Transmit Unit is 1500
   ```
   ```
   Internet protocol processing : disabled
   ```
   ```
   IP Sending Frames' Format is PKTFMT_ETHNT_2, Hardware address is 00e0-fc7d-a497
   ```
   ```
   The Vendor PN is HFBR-5710L
   ```
   ```
   Port BW: 1G, Transceiver max BW: 1G, Transceiver Mode: MultiMode
   ```
   ```
   WaveLength: 850nm, Transmission Distance: 550m
   ```
   ```
    Loopback:none, full-duplex mode, negotiation: disable, Pause Flowcontrol:Send and Receive Enable
   ```
   ```
   Statistics last cleared:never
   ```
   ```
       Last 300 seconds input rate: 0 bits/sec, 0 packets/sec
   ```
   ```
       Last 300 seconds output rate: 0 bits/sec, 0 packets/sec
   ```
   ```
       Input: 107628 bytes, 1016 packets
   ```
   ```
       Output: 107628 bytes, 1016 packets
   ```
   ```
       Input:
   ```
   ```
         Unicast: 0, Multicast: 0
   ```
   ```
         Broadcast: 0, JumboOctets: 0
   ```
   ```
         CRC: 0, Symbol: 0
   ```
   ```
         Overrun: 0 , InRangeLength: 0
   ```
   ```
         LongPacket: 0 , Jabber: 0, Alignment: 0
   ```
   ```
         Fragment: 0, Undersized Frame: 0
   ```
   ```
         RxPause: 0
   ```
   ```
       Output:
   ```
   ```
         Unicast: 10, Multicast: 0
   ```
   ```
         Broadcast: 0, Jumbo: 0
   ```
   ```
         Lost: 0, Overflow: 0, Underrun: 0
   ```
   ```
         TxPause: 0                                    
   ```

#### Configuration Files

* DeviceB configuration file
  
  ```
  #
  ```
  ```
   sysname DeviceB
  ```
  ```
   vlan 10
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/3/0
  ```
  ```
   portswitch
  ```
  ```
   port default vlan 10
  ```
  ```
   port-mirroring inbound vlan 10
  ```
  ```
   port-mirroring to observe-index 1
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/3/1
  ```
  ```
   ip address 10.1.1.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   ip address 10.10.1.1 255.255.255.0
  ```
  ```
   port-observing observe-index 1
  ```
  ```
  #
  ```
  ```
  return
  ```
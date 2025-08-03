Example for Configuring Port Mirroring (1:N Scenario)
=====================================================

Example_for_Configuring_Port_Mirroring_(1:N_Scenario)

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0281831761__fig_dc_ne_portmirror_cfg_002701), the switch forwards user packets from VLAN 10 and VLAN 20 to the Device. To monitor the packets forwarded by the switch to interface 1 on the Device, specify interface 2 and interface 3 on the Device as observing ports. In addition, specify interface 1 as a mirrored port and enable the port mirroring function for the traffic of VLAN 10. Then, map the mirrored port to the observing ports. In this way, all the packets of VLAN 10 received by interface 1 are copied to interface 2 and interface 3.

**Figure 1** Networking diagram for configuring port mirroring in a 1:N scenario![](../../../../public_sys-resources/note_3.0-en-us.png) 

* The configurations in this example are performed on the Device. The HUAWEI NE40E-M2 series can function as a Device.
* Interfaces 1 through 3 in this example represent GE0/1/0, GE0/2/0, and GE0/3/0, respectively.

  
![](figure/en-us_image_0281832655.png)

| Device Name | Interface Name | Interface IP Address |
| --- | --- | --- |
| Device | GE0/1/0 | - |
| Device | GE0/2/0 | 10.10.1.1/24 |
| Device | GE0/3/0 | 10.1.1.2/24 |




#### Configuration Notes

Do not configure an interface as both an observing port and a mirrored port.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure GE0/2/0 and GE0/3/0 on the Device as observing ports.
2. Configure GE0/1/0 on the Device as a mirrored port and enable the port mirroring function for the traffic of VLAN 10.
3. Map the mirrored port to the observing ports and enable mirroring analysis on GE0/1/0.

#### Data Preparation

To complete the configuration, you need the following data:

* Types and numbers of the observing ports and mirrored port

#### Procedure

1. Configure IP addresses for interfaces and ensure that the corresponding routes are reachable. For configuration details, see [Configuration Files](#EN-US_TASK_0281831761__example1465079755213933) in this section.
2. Configure GE0/2/0 and GE0/3/0 as observing ports.
   
   
   ```
   <Device> system-view
   [~Device] interface gigabitethernet0/2/0
   [~Device-GigabitEthernet0/2/0] port-observing observe-index 1
   [*Device-GigabitEthernet0/2/0] commit
   [~Device-GigabitEthernet0/2/0] quit
   [~Device] interface gigabitethernet0/3/0
   [~Device-GigabitEthernet0/3/0] port-observing observe-index 2
   [~Device-GigabitEthernet0/3/0] commit
   [~Device-GigabitEthernet0/3/0] quit
   ```
3. Enable VLAN-based upstream port mirroring on GE0/1/0.
   
   
   ```
   [~Device] vlan 10
   [*Device-vlan10] commit
   [~Device-vlan10] quit
   [~Device] interface gigabitethernet0/1/0
   [~Device-GigabitEthernet0/1/0] portswitch
   [*Device-GigabitEthernet0/1/0] port default vlan 10
   [*Device-GigabitEthernet0/1/0] port-mirroring inbound vlan 10
   [*Device-GigabitEthernet0/1/0] commit
   [~Device-GigabitEthernet0/1/0] quit
   ```
4. Map the mirrored port GE0/1/0 to the observing ports GE0/2/0 and GE0/3/0.
   
   
   ```
   [~Device] interface gigabitethernet0/1/0
   [~Device-GigabitEthernet0/1/0] port-mirroring to observe-index 1 2
   [*Device-GigabitEthernet0/1/0] commit
   [~Device-GigabitEthernet0/1/0] quit
   ```
   
   After the preceding configuration is complete, the packets of VLAN 10 received by GE0/1/0 are mirrored to GE0/2/0 and GE0/3/0.
5. Verify the configuration.
   
   
   
   For example, if the switch sends 10 packets with the VLAN ID being 10 to the mirrored port GE0/1/0 of the Device, check that the observing ports GE0/2/0 and GE0/3/0 can forward all the packets with the VLAN ID being 10 received by the mirrored port GE0/1/0. Run the **display interface** command to check packet statistics about GE0/2/0.
   
   ```
   <Device> display interface gigabitethernet0/2/0
   GigabitEthernet0/2/0 current state : UP
   Line protocol current state : UP
   Description:XXXXXX, GigabitEthernet0/2/0 Interface
   Route Port,The Maximum Transmit Unit is 1500
   Internet protocol processing : disabled
   IP Sending Frames' Format is PKTFMT_ETHNT_2, Hardware address is 00e0-fc7d-a497
   The Vendor PN is HFBR-5710L
   Port BW: 1G, Transceiver max BW: 1G, Transceiver Mode: MultiMode
   WaveLength: 850nm, Transmission Distance: 550m
    Loopback:none, full-duplex mode, negotiation: disable, Pause Flowcontrol:Send and Receive Enable
   Statistics last cleared:never
       Last 300 seconds input rate: 0 bits/sec, 0 packets/sec
       Last 300 seconds output rate: 0 bits/sec, 0 packets/sec
       Input: 560 bytes, 10 packets
       Output: 560 bytes, 10 packets
       Input:
         Unicast: 0, Multicast: 0
         Broadcast: 0, JumboOctets: 0
         CRC: 0, Symbol: 0
         Overrun: 0 , InRangeLength: 0
         LongPacket: 0 , Jabber: 0, Alignment: 0
         Fragment: 0, Undersized Frame: 0
         RxPause: 0
       Output:
         Unicast: 10, Multicast: 0
         Broadcast: 0, Jumbo: 0
         Lost: 0, Overflow: 0, Underrun: 0
         TxPause: 0  
   ```

#### Configuration Files

* Device configuration file
  
  ```
  #
   sysname Device
   vlan 10
  #
   interface GigabitEthernet0/1/0
   portswitch
   port default vlan 10
   port-mirroring inbound vlan 10
   port-mirroring to observe-index 1 2
  #
  interface GigabitEthernet0/2/0
   ip address 10.10.1.1 255.255.255.0
   port-observing observe-index 1
  #
  interface GigabitEthernet0/3/0
   ip address 10.1.1.2 255.255.255.0
   port-observing observe-index 2
  #
  return
  ```
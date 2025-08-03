Example for Configuring the Compatibility of the EtherType Field in the Outer Tag of QinQ Packets
=================================================================================================

This example shows how to configure the EtherType of an outer tag to enable the interworking between Huawei devices and non-Huawei devices.

#### Networking Requirements

PE2 is a Huawei device. PE1 and CE1 are non-Huawei devices. CE2 is a non-Huawei switch. [Figure 1](#EN-US_TASK_0172363293__en-us_task_0172363201_fig_dc_vrp_qinq_cfg_002501) shows the networking and the EtherType value in the outer tag of QinQ packets. In this situation, you can enable Huawei devices and non-Huawei devices to interwork with each other by setting the EtherType value in the outer tag of the interface on PE2.

**Figure 1** Networking of configuring the compatibility of the EtherType field in the outer tag of QinQ packets![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 and 2 represent GE0/1/0 and GE0/2/0, respectively.


  
![](figure/en-us_image_0000001556429561.png)

| Device Name | EtherType Value in the Outer Tag | Device Name | EtherType Value in the Outer Tag |
| --- | --- | --- | --- |
| PE1 | 0x9100 | CE1 | 0x8100 |
| PE2 | 0x8100 | CE2 | 0x9100 |




#### Configuration Roadmap

The configuration roadmap is as follows:

1. Switch PE2's interfaces connected to the CEs into Layer 2 interfaces to ensure Layer 2 connectivity.
2. Configure the compatibility of the EtherType field in the outer tag of QinQ packets on PE2's interface that connects to CE2 to ensure that the Huawei device and non-Huawei device can interwork with each other.

#### Data Preparation

To complete the configuration, you need the following data:

* Names of the physical interfaces through which PE2 connects to non-Huawei devices
* EtherType encapsulation value in the outer tag of non-Huawei devices

#### Procedure

1. Switch PE2's interfaces connected to CEs to Layer 2 interfaces.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname PE2
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~PE2] interface gigabitethernet 0/1/0
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] portswitch
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE2] interface gigabitethernet 0/2/0
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] portswitch
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] undo shutdown
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE2] commit
   ```
2. Configure the compatibility of the EtherType field in the outer tag of QinQ packets on the interface of PE2 that connects to CE2.
   
   
   ```
   [~PE2] interface gigabitethernet 0/1/0
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] qinq protocol 9100
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE2] commit
   ```
3. Verify the configuration.
   
   
   
   After the configurations are complete, run the [**display this**](cmdqueryname=display+this) command on GE 0/1/0 of PE2. The command output shows the information of the interface.
   
   Run the [**display interface**](cmdqueryname=display+interface) *interface-type interface-number* command on PE2. The command output shows the EtherType value of the outer VLAN tag.
   
   ```
   [~PE2] display interface gigabitethernet0/1/0
   ```
   ```
   GigabitEthernet0/1/0 current state : UP
   Line protocol current state : UP (ifindex: 12)
   Switch Port, TPID : 9100(Hex), The Maximum Transmit Unit is 1500
   Internet protocol processing : disabled
   IP Sending Frames' Format is PKTFMT_ETHNT_2, Hardware address is 00e0-fc12-3456
   Last physical up time   : 0000-00-00 00:00:00
   Last physical down time : 0000-00-00 00:00:00
   Current system time: 2012-06-28 03:59:19
   Statistics last cleared:never
       Last 300 seconds input rate: 0 bits/sec, 0 packets/sec
       Last 300 seconds output rate: 0 bits/sec, 0 packets/sec
       Input peak rate 0 bits/sec, Record time: -
       Output peak rate 0 bits/sec, Record time: -
       Input: 0 bytes, 0 packets
       Output: 0 bytes, 0 packets
       Input:
         Unicast: 0 packets, Multicast: 0 packets
         Broadcast: 0 packets, JumboOctets: 0 packets
         CRC: 0 packets, Symbol: 0 packets
         Overrun: 0 packets, InRangeLength: 0 packets
         LongPacket: 0 packets, Jabber: 0 packets, Alignment: 0 packets
         Fragment: 0 packets, Undersized Frame: 0 packets
         RxPause: 0 packets
       Output:
         Unicast: 0 packets, Multicast: 0 packets
         Broadcast: 0 packets, JumboOctets: 0 packets
         Lost: 0 packets, Overflow: 0 packets, Underrun: 0 packets
         System: 0 packets, Overruns: 0 packets
         TxPause: 0 packets
       Last 300 seconds input utility rate:  0.00%
       Last 300 seconds output utility rate: 0.00%
   ```

#### PE2 configuration file

```
#
 sysname PE2
#
interface GigabitEthernet 0/1/0
 portswitch
 undo shutdown
 qinq protocol 9100
#
interface GigabitEthernet 0/2/0
 portswitch
 undo shutdown
#
return
```
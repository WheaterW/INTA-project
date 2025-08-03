Example for Configuring Priority Mappings for VLAN Packets Based on BA Classification on Layer 2 Interfaces
===========================================================================================================

This section provides an example for configuring priority mappings for VLAN packets based on BA classification.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172371315__fig_dc_ne_qos_cfg_205401), SwitchA forwards VLAN packets from VLAN 10 to DeviceA. DeviceA maps the priorities of the VLAN packets to the priorities of IP packets based on the configured priority mappings in the DiffServ domain set on DeviceA. DeviceA then forwards the packets to the IP network.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

interface1 and interface2 in this example represent GE 0/1/0 and GE 0/2/0, respectively.


**Figure 1** Networking diagram for configuring priority mappings for VLAN packets based on BA classification on Layer 2 interfaces  
![](images/fig_dc_ne_qos_cfg_205401.png)  


#### Configuration Notes

When configuring priority mappings for VLAN packets based on BA classification on Layer 2 interfaces, pay attention to the following:

* Before running the **trust 8021p vlan** command on an interface, use the **trust upstream vlan** command to bind a DiffServ domain to the interface. Otherwise, the **trust 8021p vlan** configuration does not take effect.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a VLAN on DeviceA.
2. Configure the inbound interface of DeviceA to trust the priorities of packets from an upstream device.
3. Configure priority mappings based on BA classification on the inbound interface of DeviceA.
4. Configure priority mappings for packets on the outbound interface of DeviceA.

#### Data Preparation

To complete the configuration, you need the following data:

* VLAN ID
* 802.1p priorities, service classes and colors of the packets on the Router, and DSCP values of IP packets

#### Procedure

1. Configure a VLAN on DeviceA.
   
   
   
   # Create a VLAN.
   
   ```
   <DeviceA> system-view
   ```
   ```
   [~DeviceA] vlan batch 10
   ```
   ```
   [*DeviceA] commit
   ```
   ```
   [~DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] portswitch
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] port trunk allow-pass vlan 10
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] quit
   ```
2. Enable BA classification on the inbound interface GE 0/1/0 of DeviceA to map the priorities of VLAN packets to the priorities of IP packets according to the default mappings.
   
   
   ```
   [~DeviceA-GigabitEthernet0/1/0] trust upstream default vlan 10
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] trust 8021p vlan 10
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] quit
   ```
3. Configure priority mappings from VLAN packets to IP packets on the outbound interface GE 0/2/0 of DeviceA.
   
   
   ```
   [~DeviceA] diffserv domain default
   ```
   ```
   [*DeviceA-dsdomain-default] 8021p-inbound 2 phb ef green
   ```
   ```
   [*DeviceA-dsdomain-default] ip-dscp-outbound ef green map 34
   ```
   ```
   [*DeviceA-dsdomain-default] commit
   ```
   ```
   [~DeviceA-dsdomain-default] quit
   ```
   ```
   [~DeviceA] interface gigabitethernet 0/2/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] portswitch
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] port trunk allow-pass vlan 10
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] trust upstream default vlan 10
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] trust 8021p vlan 10
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/0] quit
   ```
   
   After the preceding configuration is complete, DeviceA maps the VLAN packets with the 802.1p priority of 2 from an upstream device to IP packets with the service class of EF and the packet color of green. DeviceA maps the other 802.1p priorities of VLAN packets to the corresponding DSCP values of IP packets based on the default mappings.
4. Verify the configuration.
   
   
   
   Run the **display port-queue statistics interface gigabitethernet 0/2/0 outbound** command on DeviceA. The statistics about AF2 packets are not displayed on the outbound interface. This is because the mapping from the 802.1p priority of 2 to the IP service priority of EF is configured on the inbound interface.
   
   ```
   <DeviceA> display port-queue statistics interface gigabitethernet 0/2/0 outbound
   ```
   ```
   GigabitEthernet0/2/0 outbound traffic statistics:
    [be]
    Current usage percentage of queue: 0
     Total pass:
                          1,003,905,621 packets,             90,351,505,260 bytes
     Total discard:
                                      0 packets,                          0 bytes
       Drop tail discard:
                                      0 packets,                          0 bytes
       Wred discard:
                                      0 packets,                          0 bytes
     Last 30 seconds pass rate:
                                      0 pps,                              0 bps
     Last 30 seconds discard rate:
                                      0 pps,                              0 bps
       Drop tail discard rate:
                                      0 pps,                              0 bps
       Wred discard rate:
                                      0 pps,                              0 bps
     buffer size:                    10 kbytes
     used buffer size:                0 kbytes
     Peak rate:
                             0000-00-00 00:00:00                          0 bps
    [af1]
    Current usage percentage of queue: 0
     Total pass:
                                      0 packets,                          0 bytes
     Total discard:
                                      0 packets,                          0 bytes
       Drop tail discard:
                                      0 packets,                          0 bytes
       Wred discard:
                                      0 packets,                          0 bytes
     Last 30 seconds pass rate:
                                      0 pps,                              0 bps
     Last 30 seconds discard rate:
                                      0 pps,                              0 bps
       Drop tail discard rate:
                                      0 pps,                              0 bps
       Wred discard rate:
                                      0 pps,                              0 bps
     buffer size:                    10 kbytes
     used buffer size:                0 kbytes
     Peak rate:
                             0000-00-00 00:00:00                          0 bps
    [af2]
    Current usage percentage of queue: 0
     Total pass:
                                      0 packets,                          0 bytes
     Total discard:
                                      0 packets,                          0 bytes
       Drop tail discard:
                                      0 packets,                          0 bytes
       Wred discard:
                                      0 packets,                          0 bytes
     Last 30 seconds pass rate:
                                      0 pps,                              0 bps
     Last 30 seconds discard rate:
                                      0 pps,                              0 bps
       Drop tail discard rate:
                                      0 pps,                              0 bps
       Wred discard rate:
                                      0 pps,                              0 bps
     buffer size:                    10 kbytes
     used buffer size:                0 kbytes
     Peak rate:
                             0000-00-00 00:00:00                          0 bps
    [af3]
    Current usage percentage of queue: 0
     Total pass:
                                      0 packets,                          0 bytes
     Total discard:
                                      0 packets,                          0 bytes
       Drop tail discard:
                                      0 packets,                          0 bytes
       Wred discard:
                                      0 packets,                          0 bytes
     Last 30 seconds pass rate:
                                      0 pps,                              0 bps
     Last 30 seconds discard rate:
                                      0 pps,                              0 bps
       Drop tail discard rate:
                                      0 pps,                              0 bps
       Wred discard rate:
                                      0 pps,                              0 bps
     buffer size:                    10 kbytes
     used buffer size:                0 kbytes
     Peak rate:
                             0000-00-00 00:00:00                          0 bps
    [af4]
    Current usage percentage of queue: 0
     Total pass:
                                      0 packets,                          0 bytes
     Total discard:
                                      0 packets,                          0 bytes
       Drop tail discard:
                                      0 packets,                          0 bytes
       Wred discard:
                                      0 packets,                          0 bytes
     Last 30 seconds pass rate:
                                      0 pps,                              0 bps
     Last 30 seconds discard rate:
                                      0 pps,                              0 bps
       Drop tail discard rate:
                                      0 pps,                              0 bps
       Wred discard rate:
                                      0 pps,                              0 bps
     buffer size:                    10 kbytes
     used buffer size:                0 kbytes
     Peak rate:
                             0000-00-00 00:00:00                          0 bps
    [ef]
    Current usage percentage of queue: 0
     Total pass:
                             27,167,382 packets,              3,477,424,896 bytes
     Total discard:
                                      0 packets,                          0 bytes
       Drop tail discard:
                                      0 packets,                          0 bytes
       Wred discard:
                                      0 packets,                          0 bytes
     Last 30 seconds pass rate:
                                844,397 pps,                    864,661,792 bps
     Last 30 seconds discard rate:
                                      0 pps,                              0 bps
       Drop tail discard rate:
                                      0 pps,                              0 bps
       Wred discard rate:
                                      0 pps,                              0 bps
     buffer size:                    10 kbytes
     used buffer size:                0 kbytes
     Peak rate:
                             0000-00-00 00:00:00                          0 bps
    [cs6]
    Current usage percentage of queue: 0
     Total pass:
                                    335 packets,                     25,502 bytes
     Total discard:
                                      0 packets,                          0 bytes
       Drop tail discard:
                                      0 packets,                          0 bytes
       Wred discard:
                                      0 packets,                          0 bytes
     Last 30 seconds pass rate:
                                      0 pps,                              0 bps
     Last 30 seconds discard rate:
                                      0 pps,                              0 bps
       Drop tail discard rate:
                                      0 pps,                              0 bps
       Wred discard rate:
                                      0 pps,                              0 bps
     buffer size:                    10 kbytes
     used buffer size:                0 kbytes
     Peak rate:
                             0000-00-00 00:00:00                          0 bps
    [cs7]
    Current usage percentage of queue: 0
     Total pass:
                                      0 packets,                          0 bytes
     Total discard:
                                      0 packets,                          0 bytes
       Drop tail discard:
                                      0 packets,                          0 bytes
       Wred discard:
                                      0 packets,                          0 bytes
     Last 30 seconds pass rate:
                                      0 pps,                              0 bps
     Last 30 seconds discard rate:
                                      0 pps,                              0 bps
       Drop tail discard rate:
                                      0 pps,                              0 bps
       Wred discard rate:
                                      0 pps,                              0 bps
     buffer size:                    10 kbytes
     used buffer size:                0 kbytes
     Peak rate:
                             0000-00-00 00:00:00                          0 bps
   ```

#### Configuration Files

DeviceA configuration file
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
diffserv domain default
```
```
 8021p-inbound 2 phb ef green
```
```
 ip-dscp-outbound ef green map 34
```
```
#
```
```
vlan 10
```
```
#
```
```
interface GigabitEthernet 0/1/0
```
```
 portswitch
```
```
 undo shutdown
```
```
 port trunk allow-pass vlan 10
```
```
 trust upstream default vlan 10
```
```
 trust 8021p vlan 10
```
```
#
```
```
interface GigabitEthernet0/2/0
```
```
 portswitch
```
```
 undo shutdown
```
```
 port trunk allow-pass vlan 10
```
```
 trust upstream default vlan 10
```
```
 trust 8021p vlan 10
```
```
#
```
```
return
```
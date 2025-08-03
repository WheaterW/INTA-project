Example for Configuring ARP Bidirectional Isolation and ARP VLAN CAR
====================================================================

This section provides an example for configuring ARP bidirectional isolation and ARP VLAN CAR. A configuration networking diagram is provided to help you understand the configuration procedure. The example provides the networking requirements, configuration roadmap, configuration procedure, and configuration files.

#### Networking Requirements

ARP is an open protocol and sets up IP-address-to-MAC-address mappings. When being used on an Ethernet network, ARP offers possibilities for malicious attackers because of its simplicity, openness, and lack of security measures. Attackers forge and send excessive ARP request and response packets to the Router. The ARP buffer of the Router has a limited storage capability, so that it will be incapable of caching legitimate ARP packets after being overflowed. ARP security enables the Router to process ARP request and reply packets separately, so that the Router can rapidly respond to ARP request packets. In addition, ARP security allows you to set a rate limit for ARP packets, so that excessive ARP packets will be discarded when the preset rate limit is reached.

As shown in [Figure 1](#EN-US_TASK_0000001348417002__fig_dc_ne_arpsec_cfg_501201), only the user-side interface is connected to the Layer 2 devices. Therefore, configure ARP bidirectional isolation and ARP VLAN CAR on the user-side interface GE 0/1/0.

**Figure 1** Network diagram of configuring ARP security![](../../../../public_sys-resources/note_3.0-en-us.png) 

* The configurations in this example are performed on Device.
* Interface 1 in this example represents GE 0/1/0.

  
![](figure/en-us_image_0000001398497245.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable ARP bidirectional isolation.
2. Configure the rate limit of packets to be sent to the CPU.

#### Data Preparation

To complete the configuration, you need the following data:

* Rate limit of ARP packets to be sent to the CPU

#### Procedure

1. Configure VLANs on the Router. The configuration details are not provided here.
2. Enable ARP bidirectional isolation.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname Device
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~Device] interface gigabitethernet 0/1/0
   ```
   ```
   [~Device-GigabitEthernet0/1/0] arp-safeguard enable
   ```
   ```
   [*Device-GigabitEthernet0/1/0] commit
   ```
3. Configure the rate limit of ARP packets on GE 0/1/0.
   
   
   ```
   [~Device-GigabitEthernet0/1/0] arp rate-limit 50
   ```
   ```
   [*Device-GigabitEthernet0/1/0] commit
   ```
   ```
   [~Device-GigabitEthernet0/1/0] quit
   ```
4. Verify the configuration.
   
   
   
   Check ARP bidirectional isolation statistics on the interface board in slot 1.
   
   ```
   <Device> display arp-safeguard statistics slot 1
   ```
   ```
   ArpRequest-Count : 23
   ArpReply-Count   : 23
   ArpToCp-Count    : 23
   ArpDrop-Count    : 23
   ```
   
   Check the rate limit of ARP packets on GE 0/1/0.
   
   ```
   <Device> display arp rate-limit interface gigabitethernet 0/1/0
   ```
   ```
    Interface: GigabitEthernet0/1/0
        arp rate-limit: 50 
   ```

#### Configuration Files

```
#
sysname Device
#
vlan 100
vlan 200
#
interface GigabitEthernet0/1/0
 undo shutdown
 portswitch
 port trunk allow-pass vlan 100 200
 arp-safeguard enable
 arp rate-limit 50
#
return
```
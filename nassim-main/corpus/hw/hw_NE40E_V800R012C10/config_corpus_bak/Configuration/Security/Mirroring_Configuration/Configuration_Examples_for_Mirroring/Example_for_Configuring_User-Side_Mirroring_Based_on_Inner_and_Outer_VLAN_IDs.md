Example for Configuring User-Side Mirroring Based on Inner and Outer VLAN IDs
=============================================================================

This section provides an example for configuring user-side mirroring based on inner and outer VLAN IDs in IPoEoQ access scenarios.

#### Networking Requirements

In the IPoEoQ access scenario shown in [Figure 1](#EN-US_TASK_0000001262916511__fig_dc_ne_ipox_cfg_008601), the networking requirements for user-side mirroring based on inner and outer VLAN IDs are as follows:

* The user accesses the network through GE0/1/2.2 on the device in IPoEoQ mode. LAN switch 1 tags user packets with VLAN 1 and VLAN 2, and LAN switch 2 tags user packets with QinQ 100.
* The user belongs to domain **isp1** and adopts binding authentication and RADIUS accounting.
* The RADIUS server address is 192.168.7.249. The authentication and accounting port numbers are 1812 and 1813, respectively. The standard RADIUS protocol is adopted. The shared key is **it-is-my-secret1**.
* The DNS server address is 192.168.7.252.
* To monitor the user packets that are sent from LAN switch 2 to interface 2 on the device and carry the termination tag 100/1, you need to configure interface 3 on the device as an observing port, and then configure user-side mirroring based on inner and outer VLAN IDs on interface 2. In this way, all the packets received by interface 2 are copied to interface 3 for analysis by HostD (the analyzer).

**Figure 1** Networking diagram for configuring user-side mirroring based on inner and outer VLAN IDs![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE0/1/1, GE0/1/2.2, and GE0/1/3, respectively.


  
![](figure/en-us_image_0000001819659188.png "Click to enlarge")

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure authentication and accounting schemes.
2. Configure a RADIUS server group.
3. Configure an address pool.
4. Configure an authentication domain.
5. Configure a BAS interface and an upstream interface.
6. Configure an observing port.
7. Configure a mirrored port for user-side mirroring based on inner and outer VLAN IDs and enable the mirroring function.
8. Configure an observing port for user-side mirroring based on inner and outer VLAN IDs.

#### Data Preparation

To complete the configuration, you need the following data:

* Authentication scheme name and authentication mode
* Accounting scheme name and accounting mode
* RADIUS server group name, and IP addresses and port numbers of the RADIUS authentication and accounting servers
* Address pool name, gateway address, and DNS server address
* Domain name
* BAS interface parameters
* Types and numbers of the observing port and user-side mirrored port

#### Procedure

1. Configure AAA schemes.
   
   
   
   # Configure an authentication scheme.
   
   ```
   <HUAWEI> system-view 
   ```
   ```
   [~HUAWEI] aaa
   ```
   ```
   [~HUAWEI-aaa] authentication-scheme auth1
   ```
   ```
   [*HUAWEI-aaa-authen-auth1] authentication-mode radius
   ```
   ```
   [*HUAWEI-aaa-authen-auth1] commit
   ```
   ```
   [~HUAWEI-aaa-authen-auth1] quit
   ```
   
   # Configure an accounting scheme.
   
   ```
   [~HUAWEI-aaa] accounting-scheme acct1
   ```
   ```
   [*HUAWEI-aaa-accounting-acct1] accounting-mode radius
   ```
   ```
   [*HUAWEI-aaa-accounting-acct1] commit
   ```
   ```
   [~HUAWEI-aaa-accounting-acct1] quit
   ```
   ```
   [~HUAWEI-aaa] quit
   ```
2. Configure a RADIUS server group.
   
   
   ```
   [~HUAWEI] radius-server group rd1
   ```
   ```
   [*HUAWEI-radius-rd1] radius-server authentication 192.168.7.249 1812 weight 0
   ```
   ```
   [*HUAWEI-radius-rd1] radius-server accounting 192.168.7.249 1813 weight 0
   ```
   ```
   [*HUAWEI-radius-rd1] commit
   ```
   ```
   [~HUAWEI-radius-rd1] radius-server shared-key-cipher it-is-my-secret1
   ```
   ```
   [*HUAWEI-radius-rd1] commit
   ```
   ```
   [~HUAWEI-radius-rd1] quit
   ```
3. Configure an address pool.
   
   
   ```
   [~HUAWEI] ip pool pool1 bas local
   ```
   ```
   [*HUAWEI-ip-pool-pool1] gateway 10.82.0.1 255.255.255.0
   ```
   ```
   [*HUAWEI-ip-pool-pool1] commit
   ```
   ```
   [*HUAWEI-ip-pool-pool1] section 0 10.82.0.2 10.82.0.200
   ```
   ```
   [~HUAWEI-ip-pool-pool1] dns-server 192.168.7.252
   ```
   ```
   [*HUAWEI-ip-pool-pool1] commit
   ```
   ```
   [~HUAWEI-ip-pool-pool1] quit
   ```
4. Configure an authentication domain.
   
   
   ```
   [~HUAWEI] aaa
   ```
   ```
   [~HUAWEI-aaa] domain isp1
   ```
   ```
   [*HUAWEI-aaa-domain-isp1] authentication-scheme auth1
   ```
   ```
   [*HUAWEI-aaa-domain-isp1] accounting-scheme acct1
   ```
   ```
   [*HUAWEI-aaa-domain-isp1] radius-server group rd1
   ```
   ```
   [*HUAWEI-aaa-domain-isp1] commit 
   ```
   ```
   [~HUAWEI-aaa-domain-isp1] ip-pool pool1
   ```
   ```
   [~HUAWEI-aaa-domain-isp1] quit
   ```
   ```
   [~HUAWEI-aaa] quit
   ```
5. Configure Ethernet interfaces.
   
   
   
   # Configure user-side VLANs.
   
   ```
   [~HUAWEI] interface GigabitEthernet 0/1/2.2
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/2.2] user-vlan 1 2 qinq 100
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/2.2-vlan-1-2-QinQ-100-100] commit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/2.2-vlan-1-2-QinQ-100-100] quit
   ```
   
   
   
   # Configure BAS.
   
   ```
   [~HUAWEI-GigabitEthernet0/1/2.2] bas
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/2.2-bas] access-type layer2-subscriber
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/2.2-bas] default-domain authentication isp1
   [*HUAWEI-GigabitEthernet0/1/2.2-bas] authentication-method bind
   [*HUAWEI-GigabitEthernet0/1/2.2-bas] commit
   [~HUAWEI-GigabitEthernet0/1/2.2-bas] quit
   [~HUAWEI-GigabitEthernet0/1/2.2] quit
   ```
   
   # Configure an upstream interface.
   
   ```
   [~HUAWEI] interface GigabitEthernet 0/1/1
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/1] ip address 192.168.7.1 255.255.255.0
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/1] commit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/1] quit
   ```
   ```
   [~HUAWEI] quit
   ```
6. Configure an observing port.
   
   
   ```
   [~HUAWEI] interface GigabitEthernet 0/1/3
   [~HUAWEI-GigabitEthernet0/1/3] ip address 192.168.7.2 255.255.255.0
   [*HUAWEI-GigabitEthernet0/1/3] port-observing observe-index 1
   [*HUAWEI-GigabitEthernet0/1/3] commit
   [~HUAWEI-GigabitEthernet0/1/3] quit
   ```
7. Configure an upstream mirrored port for user-side mirroring based on inner and outer VLAN IDs and enable the mirroring function.
   
   
   ```
   [~HUAWEI] interface GigabitEthernet 0/1/2.2
   [~HUAWEI-GigabitEthernet0/1/2.2] port-mirroring inbound pe-vid 100 ce-vid 1
   [*HUAWEI-GigabitEthernet0/1/2.2] commit
   [~HUAWEI-GigabitEthernet0/1/2.2] quit
   ```
8. Configure an observing port for user-side mirroring based on inner and outer VLAN IDs.
   
   
   ```
   [~HUAWEI] interface GigabitEthernet 0/1/2.2
   [~HUAWEI-GigabitEthernet0/1/2.2] port-mirroring to observe-index 1
   [*HUAWEI-GigabitEthernet0/1/2.2] commit
   [~HUAWEI-GigabitEthernet0/1/2.2] quit
   ```
9. Verify the configuration.
   
   
   
   After 10 packets that carry the termination tag 100/1 are sent from LAN switch 2 to the user-side mirrored port GE0/1/2.2 on the device, the observing port GE0/1/3 forwards all such packets received by the user-side mirrored port GE0/1/2.2. Run the **display interface** command to check packet statistics about GE0/1/3.
   
   ```
   <HUAWEI> display interface gigabitethernet0/1/3
   GigabitEthernet0/1/3 current state : UP
   Line protocol current state : UP
   Description:XXXXXX, GigabitEthernet0/1/3 Interface
   Route Port,The Maximum Transmit Unit is 1500
   Internet protocol processing : disabled
   IP Sending Frames' Format is XXXXXX_XXXXX_2, Hardware address is xxxx-xxxx-xxxx
   The Vendor PN is XXXX-XXXXX
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

```
#
sysname HUAWEI
#
radius-server group rd1
 radius-server shared-key-cipher %^%#clY:%[]x='-RMNJus[s/VJ:3YBq3<..|.{'xgbp+%^%#
 radius-server authentication 192.168.7.249 1812 weight 0
 radius-server accounting 192.168.7.249 1813 weight 0
 radius-server shared-key-cipher it-is-my-secret1
#
ip pool pool1 bas local
 gateway 10.82.0.1 255.255.255.0
 section 0 10.82.0.2 10.82.0.200
 dns-server 192.168.7.252
#
aaa
 #
 authentication-scheme auth1
 authentication-mode radius
 #
 accounting-scheme acct1
 accounting-mode radius
 #
 domain default0
 #
 domain default1
 #
 domain default_admin
 domain isp1
  authentication-scheme auth1
  accounting-scheme acct1
  radius-server group rd1
  ip-pool pool1
#
interface GigabitEthernet0/1/1
 ip address 192.168.7.1 255.255.255.0
#
interface GigabitEthernet0/1/2.2
 user-vlan 1 2 qinq 100
 bas
 #
  access-type layer2-subscriber default-domain authentication isp1
  authentication-method bind
#
 port-mirroring inbound pe-vid 100 ce-vid 1
 port-mirroring to observe-index 1
#
interface GigabitEthernet0/1/3
 ip address 192.168.7.2 255.255.255.0
 port-observing observe-index 1
#
return
```
Example for Configuring ARP Security
====================================

This example describes ARP security configuration procedures.

#### Networking Requirements

ARP is a basic link layer protocol that can be used on the Ethernet. It maps devices' IP addresses to MAC addresses. ARP is simple to use but does not have any security guarantee. Attackers may send forged ARP packets to attack networks, causing normal services to be interrupted and devices to break down. Therefore, carriers want to enhance backbone network security.

As shown in [Figure 1](#EN-US_TASK_0172371911__fig_dc_vrp_arp_cfg_201901), an Internet bar is connected to the Internet through the Device. ARP security needs to be configured on the Device to protect the Internet bar against ARP attacks.

**Figure 1** Networking diagram of configuring ARP security  
![](images/fig_dc_vrp_arp_cfg_201901.png)  


#### Precautions

None.


#### Configuration Roadmap

The configuration roadmap is as follows:

* Limit the ARP packet processing rate on interface boards. This effectively prevents devices from continuously processing a large number of invalid ARP packets (with destination IP addresses unable to be resolved) sent by attackers. Burdens on the devices' CPUs are relieved and valid packets can be properly processed on the devices.
* Limit the number of ARP entries on interfaces. This effectively prevents devices from processing invalid ARP packets with forged source IP addresses sent by attackers. The devices can then process valid ARP packets and generate valid ARP entries, ensuring proper data forwarding.
* Configure strict ARP entry learning on interfaces. This effectively prevents devices from receiving invalid ARP packets sent by attackers.

#### Data Preparation

To complete the configuration, you need the following data:

* Interface board slot number: 1; number of ARP packets that the interface board processes every second: 50
* Maximum number of ARP entries that an interface can learn: 20

#### Procedure

1. Configure the interface board in slot 1 to process 50 ARP packets to a specific destination every second.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI]  sysname Device
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~Device] arp speed-limit destination-ip maximum 50 slot 1
   ```
   ```
   [*Device] commit
   ```
2. Configure GE 0/1/0 to learn a maximum of 20 ARP entries and enable strict ARP entry learning on GE 0/1/0.
   
   
   ```
   [~Device] interface gigabitethernet 0/1/0
   ```
   ```
   [~Device-GigabitEthernet0/1/0] arp-limit maximum 20
   ```
   ```
   [*Device-GigabitEthernet0/1/0] arp learning strict force-enable
   ```
   ```
   [*Device-GigabitEthernet0/1/0] commit
   ```
   ```
   [~Device-GigabitEthernet0/1/0] quit
   ```
3. Verify the configuration.
   
   
   
   Use a tool to send gratuitous ARP packets to the Device. Run the **display arp** command on the Device. The command output shows that the Device has not learned the received gratuitous ARP packets.
   
   ```
   <Device> display arp all
   ```
   ```
   IP ADDRESS      MAC ADDRESS     EXPIRE(M) TYPE        INTERFACE   VPN-INSTANCE
   ```
   ```
                                             VLAN/CEVLAN PVC
   ```
   ```
   ------------------------------------------------------------------------------
   ```
   ```
   192.168.1.200   00e0-fc7f-7258            I -         GE0/1/0
   ```
   ```
   172.16.1.180    00e0-fc56-7741  9         D-0         GE0/2/0
   ```
   ```
   10.2.1.1        00e0-fc11-8894            I -         GE0/1/1
   ```
   ```
   10.1.1.1        00e0-fc39-f564            I -         GE0/2/1
   ```
   ```
   10.1.1.2        00e0-fc22-18d5  9         D-3         GE0/2/1
   ```
   ```
   ------------------------------------------------------------------------------
   ```
   ```
   Total:5         Dynamic:2       Static:0    Interface:3    Remote:0
   ```
   ```
   Redirect:0
   ```
   
   Run the **display arp speed-limit** command on the Device to view the configured ARP packet processing rate.
   
   ```
   <Device> display arp speed-limit destination-ip slot 1
   ```
   ```
   Slot     SuppressType    SuppressValue
   ```
   ```
    ---------------------------------------------------
   ```
   ```
    1        ARP          50
   ```

#### Configuration Files

```
#
sysname Device
arp speed-limit destination-ip maximum 50 slot 1 
#
interface GigabitEthernet0/1/0
 undo shutdown
 arp learning strict force-enable
 arp-limit maximum 20 
#
return
```
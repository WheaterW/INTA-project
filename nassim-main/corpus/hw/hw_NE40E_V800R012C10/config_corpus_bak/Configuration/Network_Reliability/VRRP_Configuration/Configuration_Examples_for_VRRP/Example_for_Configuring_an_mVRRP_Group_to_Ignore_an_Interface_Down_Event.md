Example for Configuring an mVRRP Group to Ignore an Interface Down Event
========================================================================

In this example, an mVRRP group is configured to ignore an interface Down event, allowing both the mVRRP group and a peer BFD session to be established between NPEs.

#### Networking Requirements

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The NE40E-M2K is used as an example.


A VRRP group is usually associated with a BFD session or an EFM session to rapidly implement an active/standby link switchover, improving link reliability. As showed in [Figure 1](#EN-US_TASK_0000001208660195__en-us_task_0172361808_fig_dc_vrp_vrrp_cfg_013401), VRRP association cannot be configured in the following scenarios:

* One carrier runs the VPLS aggregation network and the other one runs the access and core networks. A link BFD session cannot be established between NPE1 and PE1 or between NPE2 and PE2.
* On the VPLS aggregation network enabled with split horizon, PWs are established between PE1 and PE3 and between PE2 and PE3 and they cannot transmit traffic between NPE1 and NPE2. As a result, an mVRRP group or a peer BFD session cannot be established between NPE1 and NPE2.
* Two NPEs are directly connected.

**Figure 1** Configuring the mVRRP group to ignore an interface Down event![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE 0/1/1, GE 0/1/2, and GE 0/1/3, respectively.


  
![](images/fig_dc_vrp_vrrp_cfg_013401.png)  

| Device Name | Interface Name | IP Address and Mask |
| --- | --- | --- |
| CE1 | GE0/1/1.100 | 10.100.1.1/24 |
| GE0/1/1.101 | 10.101.1.1/24 |
| GE0/1/1.102 | 10.102.1.1/24 |
| GE0/1/1.103 | 10.103.1.1/24 |
| PE1 | GE0/1/2 | 172.16.34.3/24 |
| GE0/1/3 | 172.16.35.3/24 |
| LoopBack1 | 3.3.3.3/32 |
| PE2 | GE0/1/2 | 172.16.34.4/24 |
| GE0/1/3 | 172.16.45.4/24 |
| LoopBack1 | 4.4.4.4/32 |
| PE3 | GE0/1/1 | 172.16.35.5/24 |
| GE0/1/2 | 172.16.45.5/24 |
| LoopBack1 | 5.5.5.5/32 |
| NPE1 | Eth-Trunk1.1 | 10.1.1.254/24 |
| GE0/1/1.100 | 10.100.1.254/24 |
| GE0/1/1.101 | 10.101.1.254/24 |
| GE0/1/1.102 | 10.102.1.254/24 |
| GE0/1/1.103 | 10.103.1.254/24 |
| NPE2 | Eth-Trunk1.1 | 10.1.1.253/24 |
| GE0/1/1.100 | 10.100.1.253/24 |
| GE0/1/1.101 | 10.101.1.253/24 |
| GE0/1/1.102 | 10.102.1.253/24 |
| GE0/1/1.103 | 10.103.1.253/24 |

For the preceding scenarios, you can use the BFD sampling mode and configure an mVRRP group to ignore an interface Down event to implement a rapid master/backup VRRP switchover.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* Each NPE enabled with BFD sampling establishes a link BFD session with each CE.
* When an mVRRP group is configured to ignore an interface Down event, a VRRP-enabled interface directly changes its VRRP status to Master but not Initialize if the interface goes Down.

CEs are connected to QinQ termination sub-interfaces of NPEs on the VPLS aggregation network shown in [Figure 1](#EN-US_TASK_0000001208660195__en-us_task_0172361808_fig_dc_vrp_vrrp_cfg_013401).

On the NPEs, an mVRRP group and its service VRRP groups are configured and the mVRRP group tracks BFD sessions to rapidly perform a master/backup VRRP switchover.

The configurations on the NPEs are as follows:

* An Eth-Trunk link, an mVRRP group, and a peer BFD session are established between NPE1 and NPE2.
* Service VRRP groups are established on interfaces connecting NPE1 and NPE2 to the VPLS aggregation network.
* A link BFD session is established between each NPE and each CE. The mVRRP group tracks each link BFD session. The mVRRP group can rapidly perform a master/backup VRRP switchover if two or more link BFD sessions go Down.


#### Precautions

To improve security, you are advised to configure a VRRP security policy. For details, see "Example for Configuring a VRRP Group."

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure GE 0/1/1 on NPE1 and GE 0/1/1 on NPE2 to work in user termination mode.
2. Configure basic functions for the sub-interfaces for QinQ VLAN tag termination on NPE1 and NPE2 to ensure IP connectivity.
3. Configure multiple VRRP groups on the sub-interface for QinQ VLAN tag termination on each NPE to determine the active/standby status of links.
4. Specify a VRRP group as an mVRRP group on the sub-interface for QinQ VLAN tag termination on each NPE and bind service VRRP groups to the mVRRP group. This configuration allows the mVRRP group to determine the master/backup status of the sub-interfaces in service VRRP groups.
5. Configure a peer BFD session between NPEs to monitor the remote link between NPE1 and NPE2, and configure a link BFD session between each NPE and each CE to monitor the link between them.
6. Configure the mVRRP group to rapidly perform a master/backup VRRP switchover with the help of BFD sampling if two or more link BFD sessions tracked by the mVRRP group go Down.



#### Data Preparation

To complete the configuration, you need the following data:

* PE-VID, CE-VID, and IP address for each sub-interface for QinQ VLAN tag termination on each NPE
* mVRRP group ID: 10, virtual IP address: 10.1.1.1; service VRRP group ID: 100, virtual IP address: 10.100.1.200; service VRRP group ID: 101, virtual IP address: 10.101.1.200; service VRRP group ID: 102, virtual IP address: 10.102.1.200; service VRRP group ID: 103, virtual IP address: 10.103.1.200
* NPE1 data (Peer IP address: 10.1.1.253, outbound interface: GE0/1/1.1, source IP address: 10.1.1.254); NPE2 data (peer IP address: 10.1.1.254, outbound interface: GE0/1/1.1, source IP address: 10.1.1.253)
* Link BFD session parameters on each NPE and CE, including the peer IP address, outbound interface name, and source IP address


#### Procedure

1. Configure an Eth-Trunk interface on each NPE.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The following example provides only the configuration procedure on each NPE. For the procedure for configuring a link BFD session on each CE, see the chapter "BFD Configuration" in *HUAWEI NE40E-M2 series Universal Service Router Configuration Guide - Reliability*. For the procedure for configuring the VPLS on each CE, see the chapter "VPLS Configuration" in *HUAWEI NE40E-M2 series Universal Service Router Configuration Guide - VPN*.
   
   # Configure NPE1.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname NPE1
   [*HUAWEI] commit
   [~NPE1] interface Eth-Trunk 1
   [*NPE1-Eth-Trunk1] commit
   [~NPE1-Eth-Trunk1] quit
   [~NPE1] interface gigabitethernet0/1/2
   [~NPE1-GigabitEthernet0/1/2] undo shutdown
   [*NPE1-GigabitEthernet0/1/2] eth-trunk 1
   [*NPE1-GigabitEthernet0/1/2] commit
   [~NPE1-GigabitEthernet0/1/2] quit
   [~NPE1] interface gigabitethernet0/2/1
   [~NPE1-GigabitEthernet0/2/1] undo shutdown
   [*NPE1-GigabitEthernet0/2/1] eth-trunk 1
   [*NPE1-GigabitEthernet0/2/1] commit
   [~NPE1-GigabitEthernet0/2/1] quit
   ```
   
   # Configure NPE2.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname NPE2
   [*HUAWEI] commit
   [~NPE2] interface Eth-Trunk 1
   [*NPE2-Eth-Trunk1] commit
   [~NPE2-Eth-Trunk1] quit
   [~NPE2] interface gigabitethernet0/1/2
   [~NPE2-GigabitEthernet0/1/2] undo shutdown
   [*NPE2-GigabitEthernet0/1/2] eth-trunk 1
   [*NPE2-GigabitEthernet0/1/2] commit
   [~NPE2-GigabitEthernet0/1/2] quit
   [~NPE2] interface gigabitethernet0/2/1
   [~NPE2-GigabitEthernet0/2/1] undo shutdown
   [*NPE2-GigabitEthernet0/2/1] eth-trunk 1
   [*NPE2-GigabitEthernet0/2/1] commit
   [~NPE2-GigabitEthernet0/2/1] quit
   ```
2. Configure basic functions for sub-interfaces for QinQ VLAN tag termination.
   
   
   
   # Configure NPE1.
   
   ```
   [~NPE1] interface Eth-Trunk 1
   [*NPE1-Eth-Trunk1] undo shutdown
   [*NPE1-Eth-Trunk1] commit
   [~NPE1-Eth-Trunk1] quit
   [~NPE1] interface Eth-Trunk 1.1
   [*NPE1-Eth-Trunk1.1] control-vid 1 qinq-termination
   [*NPE1-Eth-Trunk1.1] qinq termination pe-vid 10 ce-vid 1 to 100
   [*NPE1-Eth-Trunk1.1] ip address 10.1.1.254 24
   [*NPE1-Eth-Trunk1.1] arp broadcast enable
   [*NPE1-Eth-Trunk1.1] commit
   [~NPE1-Eth-Trunk1.1] quit
   ```
   ```
   [~NPE1] interface gigabitethernet0/1/1
   [~NPE1-GigabitEthernet0/1/1] undo shutdown
   [*NPE1-GigabitEthernet0/1/1] commit
   [~NPE1-GigabitEthernet0/1/1] quit
   ```
   ```
   [~NPE1] interface gigabitethernet0/1/1.100
   [*NPE1-GigabitEthernet0/1/1.100] control-vid 100 qinq-termination
   [*NPE1-GigabitEthernet0/1/1.100] qinq termination pe-vid 10 ce-vid 101 to 200
   [*NPE1-GigabitEthernet0/1/1.100] ip address 10.100.1.254 24
   [*NPE1-GigabitEthernet0/1/1.100] arp broadcast enable
   [*NPE1-GigabitEthernet0/1/1.100] commit
   [~NPE1-GigabitEthernet0/1/1.100] quit
   [~NPE1] interface gigabitethernet0/1/1.101
   [*NPE1-GigabitEthernet0/1/1.101] control-vid 101 qinq-termination
   [*NPE1-GigabitEthernet0/1/1.101] qinq termination pe-vid 10 ce-vid 201 to 300
   [*NPE1-GigabitEthernet0/1/1.101] ip address 10.101.1.254 24
   [*NPE1-GigabitEthernet0/1/1.101] arp broadcast enable
   [*NPE1-GigabitEthernet0/1/1.101] commit
   [~NPE1-GigabitEthernet0/1/1.101] quit
   [~NPE1] interface gigabitethernet0/1/1.102
   [*NPE1-GigabitEthernet0/1/1.102] control-vid 102 qinq-termination
   [*NPE1-GigabitEthernet0/1/1.102] qinq termination pe-vid 10 ce-vid 301 to 400
   [*NPE1-GigabitEthernet0/1/1.102] ip address 10.102.1.254 24
   [*NPE1-GigabitEthernet0/1/1.102] arp broadcast enable
   [*NPE1-GigabitEthernet0/1/1.102] commit
   [~NPE1-GigabitEthernet0/1/1.102] quit
   [~NPE1] interface gigabitethernet0/1/1.103
   [*NPE1-GigabitEthernet0/1/1.103] control-vid 103 qinq-termination
   [*NPE1-GigabitEthernet0/1/1.103] qinq termination pe-vid 10 ce-vid 401 to 500
   [*NPE1-GigabitEthernet0/1/1.103] ip address 10.103.1.254 24
   [*NPE1-GigabitEthernet0/1/1.103] arp broadcast enable
   [*NPE1-GigabitEthernet0/1/1.103] commit
   [~NPE1-GigabitEthernet0/1/1.103] quit
   ```
   
   # Configure NPE2.
   
   ```
   [~NPE2] interface Eth-Trunk 1
   [*NPE2-Eth-Trunk1] quit
   [*NPE2] interface Eth-Trunk 1.1
   [*NPE2-Eth-Trunk1.1] control-vid 1 qinq-termination
   [*NPE2-Eth-Trunk1.1] qinq termination pe-vid 10 ce-vid 1 to 100
   [*NPE2-Eth-Trunk1.1] ip address 10.1.1.253 24
   [*NPE2-Eth-Trunk1.1] arp broadcast enable
   [*NPE2-Eth-Trunk1.1] commit
   [~NPE2-Eth-Trunk1.1] quit
   ```
   ```
   [~NPE2] interface gigabitethernet0/1/1
   [~NPE2-GigabitEthernet0/1/1] undo shutdown
   [*NPE2-GigabitEthernet0/1/1] commit
   [~NPE2-GigabitEthernet0/1/1] quit
   ```
   ```
   [~NPE2] interface gigabitethernet0/1/1.100
   [*NPE2-GigabitEthernet0/1/1.100] control-vid 100 qinq-termination
   [*NPE2-GigabitEthernet0/1/1.100] qinq termination pe-vid 10 ce-vid 101 to 200
   [*NPE2-GigabitEthernet0/1/1.100] ip address 10.100.1.253 24
   [*NPE2-GigabitEthernet0/1/1.100] arp broadcast enable
   [*NPE2-GigabitEthernet0/1/1.100] commit
   [~NPE2-GigabitEthernet0/1/1.100] quit
   [~NPE2] interface gigabitethernet0/1/1.101
   [*NPE2-GigabitEthernet0/1/1.101] control-vid 101 qinq-termination
   [*NPE2-GigabitEthernet0/1/1.101] qinq termination pe-vid 10 ce-vid 201 to 300
   [*NPE2-GigabitEthernet0/1/1.101] ip address 10.101.1.253 24
   [*NPE2-GigabitEthernet0/1/1.101] arp broadcast enable
   [*NPE2-GigabitEthernet0/1/1.101] commit
   [~NPE2-GigabitEthernet0/1/1.101] quit
   [~NPE2] interface gigabitethernet0/1/1.102
   [*NPE2-GigabitEthernet0/1/1.102] control-vid 102 qinq-termination
   [*NPE2-GigabitEthernet0/1/1.102] qinq termination pe-vid 10 ce-vid 301 to 400
   [*NPE2-GigabitEthernet0/1/1.102] ip address 10.102.1.253 24
   [*NPE2-GigabitEthernet0/1/1.102] arp broadcast enable
   [*NPE2-GigabitEthernet0/1/1.102] commit
   [~NPE2-GigabitEthernet0/1/1.102] quit
   [~NPE2] interface gigabitethernet0/1/1.103
   [*NPE2-GigabitEthernet0/1/1.103] control-vid 103 qinq-termination
   [*NPE2-GigabitEthernet0/1/1.103] qinq termination pe-vid 10 ce-vid 401 to 500
   [*NPE2-GigabitEthernet0/1/1.103] ip address 10.103.1.253 24
   [*NPE2-GigabitEthernet0/1/1.103] arp broadcast enable
   [*NPE2-GigabitEthernet0/1/1.103] commit
   [~NPE2-GigabitEthernet0/1/1.103] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After the IP address is assigned to each sub-interface for QinQ VLAN tag termination, run the **arp broadcast enable** command to ensure that the sub-interfaces can ping each other.
   
   After completing the configurations, run the **ping** command on each NPE to ping the other NPE's Eth-Trunk1.1 IP address. The command output shows that the ping is successful.
   
   The following example uses the command output on NPE1.
   
   ```
   [~NPE1] ping 10.1.1.253
     PING 10.1.1.253: 56  data bytes, press CTRL_C to break
       Reply from 10.1.1.253: bytes=56 Sequence=1 ttl=255 time=160 ms
       Reply from 10.1.1.253: bytes=56 Sequence=2 ttl=255 time=90 ms
       Reply from 10.1.1.253: bytes=56 Sequence=3 ttl=255 time=160 ms
       Reply from 10.1.1.253: bytes=56 Sequence=4 ttl=255 time=180 ms
       Reply from 10.1.1.253: bytes=56 Sequence=5 ttl=255 time=120 ms
   
     --- 10.1.1.253 ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max = 90/142/180 ms
   
   ```
   
   Split horizon configured on the VPLS network prevents data transmission between interfaces on NPEs. Therefore, the sub-interfaces on which service VRRP groups are configured on NPEs cannot ping each other. The following example uses the command output on GE 0/1/1.100 of NPE1.
   
   ```
   [~NPE1] ping 10.100.1.253
     PING 10.100.1.253: 56  data bytes, press CTRL_C to break
       Request time out
       Request time out
       Request time out
       Request time out
       Request time out
   
     --- 3.3.3.3 ping statistics ---
       5 packet(s) transmitted
       0 packet(s) received
       100.00% packet loss
   
   ```
   
   Each NPE can ping CEs on the same network segment, indicating that the links between NPEs and CEs are working properly. In the following examples, NPE1 and NPE2 can ping CE1.
   
   ```
   [~NPE1] ping 10.100.1.1
    PING 10.100.1.1: 56  data bytes, press CTRL_C to break
       Reply from 10.100.1.1: bytes=56 Sequence=1 ttl=255 time=180 ms
       Reply from 10.100.1.1: bytes=56 Sequence=2 ttl=255 time=160 ms
       Reply from 10.100.1.1: bytes=56 Sequence=3 ttl=255 time=150 ms
       Reply from 10.100.1.1: bytes=56 Sequence=4 ttl=255 time=150 ms
       Reply from 10.100.1.1: bytes=56 Sequence=5 ttl=255 time=120 ms
   
     --- 10.100.1.1 ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max = 120/152/180 ms
   
   [~NPE2] ping 10.100.1.1
   PING 10.100.1.1: 56  data bytes, press CTRL_C to break
       Reply from 10.100.1.1: bytes=56 Sequence=1 ttl=255 time=190 ms
       Reply from 10.100.1.1: bytes=56 Sequence=2 ttl=255 time=120 ms
       Reply from 10.100.1.1: bytes=56 Sequence=3 ttl=255 time=130 ms
       Reply from 10.100.1.1: bytes=56 Sequence=4 ttl=255 time=100 ms
       Reply from 10.100.1.1: bytes=56 Sequence=5 ttl=255 time=70 ms
   
     --- 10.100.1.1 ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max = 70/122/190 ms
   
   ```
3. Configure basic VRRP functions for the sub-interfaces for QinQ VLAN tag termination.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * This example provides a scenario in which one carrier runs the VPLS aggregation network and the other runs the access and core networks. In this scenario, the **ignore-if-down** parameter must be configured in the **admin-vrrp** command for the mVRRP group. This setting allows an interface on a device in the mVRRP group to change its VRRP status to Master if its directly connected interface on the other device in the mVRRP group goes Down.
   * If the **ignore-if-down** parameter is not configured and Eth-Trunk1.1 on NPE1 fails, Eth-Trunk1.1 on NPE2 also goes Down and changes its VRRP status from Backup to Initialize. The VRRP status change causes the mVRRP group on NPEs to fail to perform a rapid master/backup VRRP switchover.
   * Do not run the **shutdown** command on Eth-Trunk1.1 of NPE1 to simulate a link fault in the scenario described in this example. If this command is run, the VRRP status becomes Master on both NPE1 and NPE2 in the mVRRP group, causing service interruptions.
   * In other scenarios different from the scenario described in this example, do not use the **ignore-if-down** parameter in the command. If the **ignore-if-down** parameter is used, the state machine of the VRRP group is inconsistent with that defined in relevant standards.
   
   # Configure an mVRRP group with the VRID of 10 on Eth-Trunk1.1 of NPE1; enable the mVRRP group to ignore an interface Down event; configure common VRRP groups on sub-interfaces of GE 0/1/1.
   
   ```
   [~NPE1] interface Eth-Trunk 1.1
   [~NPE1-Eth-Trunk1.1] qinq vrrp pe-vid 10 ce-vid 100
   [*NPE1-Eth-Trunk1.1] vrrp vrid 10 virtual-ip 10.1.1.1
   [*NPE1-Eth-Trunk1.1] vrrp vrid 10 priority 120
   [*NPE1-Eth-Trunk1.1] admin-vrrp vrid 10 ignore-if-down
   [*NPE1-Eth-Trunk1.1] commit
   [~NPE1-Eth-Trunk1.1] quit
   ```
   ```
   [~NPE1] interface gigabitethernet0/1/1.100
   [~NPE1-GigabitEthernet0/1/1.100] qinq vrrp pe-vid 10 ce-vid 101
   [*NPE1-GigabitEthernet0/1/1.100] vrrp vrid 100 virtual-ip 10.100.1.200
   [*NPE1-GigabitEthernet0/1/1.100] commit
   [~NPE1-GigabitEthernet0/1/1.100] quit
   [~NPE1] interface gigabitethernet0/1/1.101
   [~NPE1-GigabitEthernet0/1/1.101] qinq vrrp pe-vid 10 ce-vid 201
   [*NPE1-GigabitEthernet0/1/1.101] vrrp vrid 101 virtual-ip 10.101.1.200
   [*NPE1-GigabitEthernet0/1/1.101] commit
   [~NPE1-GigabitEthernet0/1/1.101] quit
   [~NPE1] interface gigabitethernet0/1/1.102
   [~NPE1-GigabitEthernet0/1/1.102] qinq vrrp pe-vid 10 ce-vid 301
   [*NPE1-GigabitEthernet0/1/1.102] vrrp vrid 102 virtual-ip 10.102.1.200
   [*NPE1-GigabitEthernet0/1/1.102] commit
   [~NPE1-GigabitEthernet0/1/1.102] quit
   [~NPE1] interface gigabitethernet0/1/1.103
   [~NPE1-GigabitEthernet0/1/1.103] qinq vrrp pe-vid 10 ce-vid 401
   [*NPE1-GigabitEthernet0/1/1.103] vrrp vrid 103 virtual-ip 10.103.1.200
   [*NPE1-GigabitEthernet0/1/1.103] commit
   [~NPE1-GigabitEthernet0/1/1.103] quit
   ```
   
   # Configure an mVRRP group with the VRID of 10 on Eth-Trunk1.1 of NPE2; enable the mVRRP group to ignore an interface Down event; configure common VRRP groups on sub-interfaces of GE 0/1/1.
   
   ```
   [~NPE2] interface Eth-Trunk 1.1
   [~NPE2-Eth-Trunk1.1] qinq vrrp pe-vid 10 ce-vid 100
   [*NPE2-Eth-Trunk1.1] vrrp vrid 10 virtual-ip 10.1.1.1
   [*NPE2-Eth-Trunk1.1] admin-vrrp vrid 10 ignore-if-down
   [*NPE2-Eth-Trunk1.1] commit
   [~NPE2-Eth-Trunk1.1] quit
   ```
   ```
   [~NPE2] interface gigabitethernet0/1/1.100
   [~NPE2-GigabitEthernet0/1/1.100] qinq vrrp pe-vid 10 ce-vid 101
   [*NPE2-GigabitEthernet0/1/1.100] vrrp vrid 100 virtual-ip 10.100.1.200
   [*NPE2-GigabitEthernet0/1/1.100] commit
   [~NPE2-GigabitEthernet0/1/1.100] quit
   [~NPE2] interface gigabitethernet0/1/1.101
   [~NPE2-GigabitEthernet0/1/1.101] qinq vrrp pe-vid 10 ce-vid 201
   [*NPE2-GigabitEthernet0/1/1.101] vrrp vrid 101 virtual-ip 10.101.1.200
   [*NPE2-GigabitEthernet0/1/1.101] commit
   [~NPE2-GigabitEthernet0/1/1.101] quit
   [~NPE2] interface gigabitethernet0/1/1.102
   [~NPE2-GigabitEthernet0/1/1.102] qinq vrrp pe-vid 10 ce-vid 301
   [*NPE2-GigabitEthernet0/1/1.102] vrrp vrid 102 virtual-ip 10.102.1.200
   [*NPE2-GigabitEthernet0/1/1.102] commit
   [~NPE2-GigabitEthernet0/1/1.102] quit
   [~NPE2] interface gigabitethernet0/1/1.103
   [~NPE2-GigabitEthernet0/1/1.103] qinq vrrp pe-vid 10 ce-vid 401
   [*NPE2-GigabitEthernet0/1/1.103] vrrp vrid 103 virtual-ip 10.103.1.200
   [*NPE2-GigabitEthernet0/1/1.103] commit
   [~NPE2-GigabitEthernet0/1/1.103] quit
   ```
   
   After completing the configurations, run the **display vrrp brief** command on each NPE.
   
   The command output on NPE1 is as follows:
   * In mVRRP group 10, the value of the **State** field is **Master** and the value of the **Type** field is **Admin**.
   * In each common VRRP group, the value of the **State** field is **Master** and the value of the **Type** field is **Normal**.
   ```
   [~NPE1] display vrrp brief
   Total:5     Master:5    Backup:0    Non-active:0
   VRID   State      Interface        Type     Virtual IP       Master IP       Local IP
   ------------------------------------------------------------------------------------------
   10     Master     Eth-Trunk1.1     Admin    10.1.1.1       10.1.1.254 24    10.1.1.254 24 
   100    Master     GE0/1/1.100      Normal   10.100.1.200   10.100.1.254 24  10.100.1.254 24 
   101    Master     GE0/1/1.101      Normal   10.101.1.200   10.101.1.254 24  10.101.1.254 24 
   102    Master     GE0/1/1.102      Normal   10.102.1.200   10.102.1.254 24  10.102.1.254 24
   103    Master     GE0/1/1.103      Normal   10.103.1.200   10.103.1.254 24  10.103.1.254 24
   ```
   The command output on NPE2 is as follows:
   * In mVRRP group 10, the value of the **State** field is **Backup** and the value of the **Type** field is **Admin**.
   * In each common VRRP group, the value of the **State** field is **Master** and the value of the **Type** field is **Normal**.
   ```
   [~NPE2] display vrrp brief
   Total:5     Master:4    Backup:1    Non-active:0
   VRID   State      Interface        Type     Virtual IP      Master IP          Local IP
   ---------------------------------------------------------------------------------------------
   10     Backup     Eth-Trunk1.1     Admin    10.1.1.1      10.1.1.254 24       10.1.1.253 24 
   100    Master     GE0/1/1.100      Normal   10.100.1.200  10.100.1.253 24     10.100.1.253 24 
   101    Master     GE0/1/1.101      Normal   10.101.1.200  10.101.1.253 24     10.101.1.253 24 
   102    Master     GE0/1/1.102      Normal   10.102.1.200  10.102.1.253 24     10.102.1.253 24 
   103    Master     GE0/1/1.103      Normal   10.103.1.200  10.103.1.253 24     10.103.1.253 24 
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Split horizon configured on the VPLS aggregation network prevents traffic transmission between interfaces on NPEs. Therefore, the sub-interfaces on which common VRRP groups are configured on NPEs cannot exchange VRRP packets, causing the VRRP status to be Master on both NPE1 and NPE2 in each common VRRP group.
4. Bind each common VRRP group to the mVRRP group so that the common VRRP groups become service VRRP groups.
   
   
   
   # Configure NPE1.
   
   ```
   [~NPE1] interface gigabitethernet0/1/1.100
   [*NPE1-GigabitEthernet0/1/1.100] vrrp vrid 100 track admin-vrrp interface Eth-Trunk1.1 vrid 10 unflowdown
   [*NPE1-GigabitEthernet0/1/1.100] commit
   [~NPE1-GigabitEthernet0/1/1.100] quit
   [~NPE1] interface gigabitethernet0/1/1.101
   [*NPE1-GigabitEthernet0/1/1.101] vrrp vrid 101 track admin-vrrp interface Eth-Trunk1.1 vrid 10 unflowdown
   [*NPE1-GigabitEthernet0/1/1.101] commit
   [~NPE1-GigabitEthernet0/1/1.101] quit
   [~NPE1] interface gigabitethernet0/1/1.102
   [*NPE1-GigabitEthernet0/1/1.102] vrrp vrid 102 track admin-vrrp interface Eth-Trunk1.1 vrid 10 unflowdown
   [*NPE1-GigabitEthernet0/1/1.102] commit
   [~NPE1-GigabitEthernet0/1/1.102] quit
   [~NPE1] interface gigabitethernet0/1/1.103
   [*NPE1-GigabitEthernet0/1/1.103] vrrp vrid 103 track admin-vrrp interface Eth-Trunk1.1 vrid 10 unflowdown
   [*NPE1-GigabitEthernet0/1/1.103] commit
   [~NPE1-GigabitEthernet0/1/1.103] quit
   ```
   
   # Configure NPE2.
   
   ```
   [~NPE2] interface gigabitethernet0/1/1.100
   [*NPE2-GigabitEthernet0/1/1.100] vrrp vrid 100 track admin-vrrp interface Eth-Trunk1.1 vrid 10 unflowdown
   [*NPE2-GigabitEthernet0/1/1.100] commit
   [~NPE2-GigabitEthernet0/1/1.100] quit
   [~NPE2] interface gigabitethernet0/1/1.101
   [*NPE2-GigabitEthernet0/1/1.101] vrrp vrid 101 track admin-vrrp interface Eth-Trunk1.1 vrid 10 unflowdown
   [*NPE2-GigabitEthernet0/1/1.101] commit
   [~NPE2-GigabitEthernet0/1/1.101] quit
   [~NPE2] interface gigabitethernet0/1/1.102
   [*NPE2-GigabitEthernet0/1/1.102] vrrp vrid 102 track admin-vrrp interface Eth-Trunk1.1 vrid 10 unflowdown
   [*NPE2-GigabitEthernet0/1/1.102] commit
   [~NPE2-GigabitEthernet0/1/1.102] quit
   [~NPE2] interface gigabitethernet0/1/1.103
   [*NPE2-GigabitEthernet0/1/1.103] vrrp vrid 103 track admin-vrrp interface Eth-Trunk1.1 vrid 10 unflowdown
   [*NPE2-GigabitEthernet0/1/1.103] commit
   [~NPE2-GigabitEthernet0/1/1.103] quit
   ```
   
   After completing the configurations, run the **display vrrp brief** command on each NPE.
   
   The command output on NPE1 is as follows:
   * In mVRRP group 10, the value of the **State** field is **Master** and the value of the **Type** field is **Admin**.
   * In each service VRRP group, the value of the **State** field is **Master** and the value of the **Type** field is **Member**.
   ```
   [~NPE1] display vrrp brief
   Total:5     Master:5    Backup:0    Non-active:0
   VRID   State      Interface        Type     Virtual IP       Master IP        Local IP
   ----------------------------------------------------------------------------------------------
   10     Master     Eth-Trunk1.1     Admin    10.1.1.1       10.1.1.254 24    10.1.1.254 24 
   100    Master     GE0/1/1.100      Normal   10.100.1.200   10.100.1.254 24  10.100.1.254 24 
   101    Master     GE0/1/1.101      Normal   10.101.1.200   10.101.1.254 24  10.101.1.254 24 
   102    Master     GE0/1/1.102      Normal   10.102.1.200   10.102.1.254 24  10.102.1.254 24
   103    Master     GE0/1/1.103      Normal   10.103.1.200   10.103.1.254 24  10.103.1.254 24
   ```
   The command output on NPE2 is as follows:
   * In mVRRP group 10, the value of the **State** field is **Backup** and the value of the **Type** field is **Admin**.
   * In each service VRRP group, the value of the **State** field is **Backup** and the value of the **Type** field is **Member**.
   ```
   [~NPE2] display vrrp brief
   Total:5     Master:0    Backup:5    Non-active:0
   VRID   State      Interface        Type     Virtual IP       Master IP         Local IP
   ----------------------------------------------------------------------------------------------
   10     Backup     Eth-Trunk1.1     Admin    10.1.1.1       10.1.1.254 24       10.1.1.253 24
   100    Backup     GE0/1/1.100      Member   10.100.1.200   10.100.1.254 24     10.100.1.253 24
   101    Backup     GE0/1/1.101      Member   10.101.1.200   10.101.1.253 24     10.102.1.253 24
   102    Backup     GE0/1/1.102      Member   10.102.1.200   10.102.1.254 24     10.102.1.253 24
   103    Backup     GE0/1/1.103      Member   10.103.1.200   10.103.1.254 24     10.103.1.253 24
   ```
   
   The command output shows that the service VRRP groups have been bound to the mVRRP group and their statuses are correct.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The service VRRP groups bound to the mVRRP group do not send VRRP packets, and the mVRRP group determines the VRRP statuses of devices in the service VRRP groups.
5. Configure basic BFD functions.
   
   
   
   # Configure a peer BFD session between NPE1 and NPE2, and configure a link BFD session between each NPE and each CE.
   
   # Configure NPE1.
   
   ```
   [~NPE1] bfd
   [*NPE1-bfd] commit
   [~NPE1-bfd] quit
   [~NPE1] bfd peer1 bind peer-ip 10.1.1.253 interface Eth-Trunk 1.1 source-ip 10.1.1.254 auto
   [*NPE1-bfd-session-peer1] commit
   [~NPE1-bfd-session-peer1] quit
   ```
   ```
   [~NPE1] bfd link1 bind peer-ip 10.100.1.1 interface gigabitethernet0/1/1.100 source-ip 10.100.1.254 auto
   [*NPE1-bfd-session-link1] commit
   [~NPE1-bfd-session-link1] quit
   [~NPE1] bfd link2 bind peer-ip 10.101.1.1 interface gigabitethernet0/1/1.101 source-ip 10.101.1.254 auto
   [*NPE1-bfd-session-link2] commit
   [~NPE1-bfd-session-link2] quit
   [~NPE1] bfd link3 bind peer-ip 10.102.1.1 interface gigabitethernet0/1/1.102 source-ip 10.102.1.254 auto
   [*NPE1-bfd-session-link3] commit
   [~NPE1-bfd-session-link3] quit
   [~NPE1] bfd link4 bind peer-ip 10.103.1.1 interface gigabitethernet0/1/1.103 source-ip 10.103.1.254 auto
   [*NPE1-bfd-session-link4] commit
   [~NPE1-bfd-session-link4] quit
   ```
   
   # Configure NPE2.
   
   ```
   [~NPE2] bfd
   [*NPE2-bfd] commit
   [~NPE2-bfd] quit
   [~NPE2] bfd peer1 bind peer-ip 10.1.1.254 interface Eth-Trunk 1.1 source-ip 10.1.1.253 auto
   [*NPE2-bfd-session-peer1] commit
   [~NPE2-bfd-session-peer1] quit
   ```
   ```
   [~NPE2] bfd link1 bind peer-ip 10.100.1.1 interface gigabitethernet0/1/1.100 source-ip 10.100.1.253 auto
   [*NPE2-bfd-session-link1] commit
   [~NPE2-bfd-session-link1] quit
   [~NPE2] bfd link2 bind peer-ip 10.101.1.1 interface gigabitethernet0/1/1.101 source-ip 10.101.1.253 auto
   [*NPE2-bfd-session-link2] commit
   [~NPE2-bfd-session-link2] quit
   [~NPE2] bfd link3 bind peer-ip 10.102.1.1 interface gigabitethernet0/1/1.102 source-ip 10.102.1.253 auto
   [*NPE2-bfd-session-link3] commit
   [~NPE2-bfd-session-link3] quit
   [~NPE2] bfd link4 bind peer-ip 10.103.1.1 interface gigabitethernet0/1/1.103 source-ip 10.103.1.253 auto
   [*NPE2-bfd-session-link4] commit
   [~NPE2-bfd-session-link4] quit
   ```
   
   After completing the configurations and configuring BFD on each CE, run the **display bfd configuration all** command on each NPE. The command output shows that the value of the **Commit** field is **True**.
   
   # The following example uses the command output on NPE1.
   
   ```
   [~NPE1] display bfd configuration all
   --------------------------------------------------------------------------------
   CFG Name        CFG Type       LocalDiscr MIndex    SessNum  Commit   AdminDown 
   --------------------------------------------------------------------------------
   peer1           S_AUTO_IF      8192       4096      1        True     False
   link1           S_AUTO_IF      8193       4097      1        True     False
   link2           S_AUTO_IF      8194       4098      1        True     False
   link3           S_AUTO_IF      8195       4099      1        True     False
   link4           S_AUTO_IF      8196       4100      1        True     False
   --------------------------------------------------------------------------------
        Total Commit/Uncommit CFG Number : 5/0
   ```
   
   Run the **display bfd session all** command on each NPE to view the BFD session status. The command output shows that the value of the **State** field is **Up**.
   
   # The following example uses the command output on NPE1.
   
   ```
   [~NPE1] display bfd session all
   (w): State in WTR 
   (*): State is invalid
   --------------------------------------------------------------------------------
   Local  Remote PeerIpAddr      State     Type      InterfaceName                 
   --------------------------------------------------------------------------------
   8192  8192    10.1.1.253      Up        S_AUTO_IF   Eth-Trunk1.1                 
   8193  8192    10.100.1.1      Up        S_AUTO_IF   GigabitEthernet0/1/1.100
   8194  8193    10.101.1.1      Up        S_AUTO_IF   GigabitEthernet0/1/1.101
   8195  8194    10.102.1.1      Up        S_AUTO_IF   GigabitEthernet0/1/1.102
   8196  8195    10.103.1.1      Up        S_AUTO_IF   GigabitEthernet0/1/1.103
   --------------------------------------------------------------------------------
   Total UP/DOWN Session Number : 5/0
   ```
6. Configure the mVRRP group to track each link BFD session to allow BFD sampling to help rapidly trigger a master/backup VRRP switchover.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The configuration is performed only for the mVRRP group on Eth-Trunk1.1 of each NPE, because service VRRP groups have been bound to the mVRRP group.
   
   # Configure NPE1.
   
   ```
   [~NPE1] interface Eth-Trunk 1.1
   [*NPE1-Eth-Trunk1.1] vrrp vrid 10 track bfd-session session-name peer1 peer
   [*NPE1-Eth-Trunk1.1] vrrp vrid 10 track bfd-session session-name link1 link
   [*NPE1-Eth-Trunk1.1] vrrp vrid 10 track bfd-session session-name link2 link
   [*NPE1-Eth-Trunk1.1] vrrp vrid 10 track bfd-session session-name link3 link
   [*NPE1-Eth-Trunk1.1] vrrp vrid 10 track bfd-session session-name link4 link
   [*NPE1-Eth-Trunk1.1] vrrp vrid 10 track link-bfd down-number 2
   [*NPE1-Eth-Trunk1.1] commit
   [~NPE1-Eth-Trunk1.1] quit
   ```
   
   # Configure NPE2.
   
   ```
   [~NPE2] interface Eth-Trunk 1.1
   [*NPE2-Eth-Trunk1.1] vrrp vrid 10 track bfd-session session-name peer1 peer
   [*NPE2-Eth-Trunk1.1] vrrp vrid 10 track bfd-session session-name link1 link
   [*NPE2-Eth-Trunk1.1] vrrp vrid 10 track bfd-session session-name link2 link
   [*NPE2-Eth-Trunk1.1] vrrp vrid 10 track bfd-session session-name link3 link
   [*NPE2-Eth-Trunk1.1] vrrp vrid 10 track bfd-session session-name link4 link
   [*NPE2-Eth-Trunk1.1] vrrp vrid 10 track link-bfd down-number 2
   [*NPE2-Eth-Trunk1.1] commit
   [~NPE2-Eth-Trunk1.1] quit
   ```
   
   After completing the configurations, run the **display vrrp interface** command on each NPE. The command output shows that the mVRRP group has been bound to one peer BFD session and four link BFD sessions and that all BFD sessions are Up.
   
   ```
   [~NPE1] display vrrp interface Eth-Trunk 1.1
   ```
   ```
   Eth-Trunk1.1 | Virtual Router 10
   State             : Master
   Virtual IP        : 10.1.1.1
   Master IP         : 10.1.1.254           
   Local IP          : 10.1.1.254
   PriorityRun       : 120
   PriorityConfig    : 120
   MasterPriority    : 120
   Preempt           : YES      Delay Time : 0
   TimerRun          : 1
   TimerConfig       : 1
   Auth Type         : NONE
   Virtual Mac       : 0000-5e00-0101
   Passive Mode      : NO
   Check TTL         : YES
   Config Type       : admin-vrrp
   Backup-forward    : disabled
   Config track link-bfd down-number : 2
   Track BFD         : link1         type : link
   BFD-session state : UP
   Track BFD         : link2         type : link
   BFD-session state : UP
   Track BFD         : link3         type : link
   BFD-session state : UP
   Track BFD         : link4         type : link
   BFD-session state : UP
   Track BFD         : peer1         type : peer
   BFD-session state : UP
   Create Time       : 2013-03-11 12:58:02
   Last Change Time  : 2013-03-11 12:58:07
   ```
   ```
   [~NPE2] display vrrp interface Eth-Trunk 1.1
   ```
   ```
   Eth-Trunk1.1 | Virtual Router 10
   State             : Backup
   Virtual IP        : 10.1.1.1
   Master IP         : 10.1.1.254  
   Local IP          : 10.1.1.253
   PriorityRun       : 100
   PriorityConfig    : 100
   MasterPriority    : 120
   Preempt           : YES   Delay Time : 0
   TimerRun          : 1
   TimerConfig       : 1
   Auth Type         : NONE
   Virtual Mac       :  0000-5e00-0102
   Passive Mode      : NO
   Check TTL         : YES
   Config Type       : admin-vrrp
   Backup-forward    : disabled
   Config track link-bfd down-number : 2
   Track BFD         : link1         type : link
   BFD-session state : UP
   Track BFD         : link2         type : link
   BFD-session state : UP
   Track BFD         : link3         type : link
   BFD-session state : UP
   Track BFD         : link4         type : link
   BFD-session state : UP
   Track BFD         : peer1         type : peer
   BFD-session state : UP
   Create Time       : 2013-03-11 12:58:02 
   Last Change Time  : 2013-03-11 12:58:07
   ```
7. Verify the configuration.
   
   
   
   After completing the configurations, run the [**display vrrp brief**](cmdqueryname=display+vrrp+brief) command on each NPE.
   
   The command output on NPE1 is as follows:
   * In mVRRP group 10, the value of the **State** field is **Master** and the value of the **Type** field is **Admin**.
   * In each service VRRP group, the value of the **State** field is **Master** and the value of the **Type** field is **Member**.
   ```
   [~NPE1] display vrrp brief
   Total:5     Master:5    Backup:0    Non-active:0
   VRID   State     Interface        Type     Virtual IP        Master IP        Local IP
   ----------------------------------------------------------------------------------------------
   10     Master     Eth-Trunk1.1     Admin    10.1.1.1       10.1.1.254 24    10.1.1.254 24 
   100    Master     GE0/1/1.100      Normal   10.100.1.200   10.100.1.254 24  10.100.1.254 24 
   101    Master     GE0/1/1.101      Normal   10.101.1.200   10.101.1.254 24  10.101.1.254 24 
   102    Master     GE0/1/1.102      Normal   10.102.1.200   10.102.1.254 24  10.102.1.254 24
   103    Master     GE0/1/1.103      Normal   10.103.1.200   10.103.1.254 24  10.103.1.254 24
   ```
   The command output on NPE2 is as follows:
   * In mVRRP group 10, the value of the **State** field is **Backup** and the value of the **Type** field is **Admin**.
   * In each service VRRP group, the value of the **State** field is **Backup** and the value of the **Type** field is **Member**.
   ```
   [~NPE2] display vrrp brief
   Total:5     Master:0    Backup:5    Non-active:0
   VRID   State     Interface        Type     Virtual IP        Master IP        Local IP
   ----------------------------------------------------------------------------------------------------
   ```
   ```
   10     Backup     Eth-Trunk1.1     Admin    10.1.1.1       10.1.1.254 24       10.1.1.253 24
   100    Backup     GE0/1/1.100      Member   10.100.1.200   10.100.1.254 24     10.100.1.253 24
   101    Backup     GE0/1/1.101      Member   10.101.1.200   10.101.1.253 24     10.102.1.253 24
   102    Backup     GE0/1/1.102      Member   10.102.1.200   10.102.1.254 24     10.102.1.253 24
   103    Backup     GE0/1/1.103      Member   10.103.1.200   10.103.1.254 24     10.103.1.253 24
   ```
   
   Run the **shutdown** command on GE 0/1/1.100 of NPE1 to simulate a fault in the link between NPE1 and CE1.
   
   ```
   [~NPE1] interface gigabitethernet0/1/1.100
   [*NPE1-GigabitEthernet0/1/1.100] shutdown
   [*NPE1-GigabitEthernet0/1/1.100] commit
   [~NPE1-GigabitEthernet0/1/1.100] quit
   ```
   
   Run the **display bfd session all** command on NPE1. The command output shows that the link BFD session between NPE1 and CE1 goes Down.
   
   ```
   [~NPE1] display bfd session all
   (w): State in WTR 
   (*): State is invalid
   --------------------------------------------------------------------------------
   Local   Remote   PeerIpAddr     State    Type         InterfaceName
   --------------------------------------------------------------------------------
   8192    8192     10.1.1.253     Up       S_AUTO_IF    Eth-Trunk1.1
   8193    0        10.100.1.1     Down    S_AUTO_IF    GigabitEthernet0/1/1.100
   8194    8193     10.101.1.1     Up       S_AUTO_IF    GigabitEthernet0/1/1.101
   8195    8194     10.102.1.1     Up       S_AUTO_IF    GigabitEthernet0/1/1.102
   8196    8195     10.103.1.1     Up       S_AUTO_IF    GigabitEthernet0/1/1.103
   --------------------------------------------------------------------------------
   Total UP/DOWN Session Number : 4/1 
   ```
   
   In this configuration example, if two or more link BFD sessions go Down, the mVRRP group rapidly performs a master/backup VRRP switchover.
   
   Because only one link BFD session went Down, the mVRRP group does not perform a master/backup VRRP switchover. Run the **display vrrp brief** command on each NPE.
   
   The command output on NPE1 is as follows:
   * In mVRRP group 10, the value of the **State** field is **Master** and the value of the **Type** field is **Admin**.
   * In service VRRP group 100, the value of the **State** field is **Initialize** and the value of the **Type** field is **Member**.
   * In other service VRRP groups, the value of the **State** field is **Master** and the value of the **Type** field is **Member**.
   ```
   [~NPE1] display vrrp brief
   Total:5     Master:4    Backup:0    Non-active:1
   VRID   State     Interface        Type     Virtual IP            Master IP        Local IP
   -------------------------------------------------------------------------------------------
   10     Master        Eth-Trunk1.1      Admin     10.1.1.1       10.1.1.254 24    10.1.1.254 24 
   100    Initialize    GE0/1/1.100       Member    10.100.1.200   -               10.100.1.254 24                 
   101    Master        GE0/1/1.101       Member    10.101.1.200   10.101.1.254 24  10.101.1.254 24 
   102    Master        GE0/1/1.102       Member    10.102.1.200   10.102.1.254 24  10.102.1.254 24
   103    Master        GE0/1/1.103       Member    10.103.1.200   10.103.1.254 24  10.103.1.254 24
   ```
   The command output on NPE2 is as follows:
   * In mVRRP group 10, the value of the **State** field is **Backup** and the value of the **Type** field is **Admin**.
   * In each service VRRP group, the value of the **State** field is **Backup** and the value of the **Type** field is **Member**.
   ```
   [~NPE2] display vrrp brief
   Total:5     Master:0    Backup:5    Non-active:0 
   VRID   State      Interface        Type      Virtual IP      Master IP        Local IP
   ------------------------------------------------------------------------------------------------
   10     Backup     GE0/1/1.1     Admin       10.1.1.254        10.1.1.253 24
   100    Backup     GE0/1/1.100      Member   10.100.1.200   10.100.1.254 24     10.100.1.253 24
   101    Backup     GE0/1/1.101      Member   10.101.1.200   10.101.1.253 24     10.102.1.253 24
   102    Backup     GE0/1/1.102      Member   10.102.1.200   10.102.1.254 24     10.102.1.253 24
   103    Backup     GE0/1/1.103      Member   10.103.1.200   10.103.1.254 24     10.103.1.253 24
   ```
   
   Run the **shutdown** command on GE 0/1/1.101 of NPE1 to simulate a fault in the link between NPE1 and CE2.
   
   ```
   [~NPE1] interface gigabitethernet0/1/1.101
   [*NPE1-GigabitEthernet0/1/1.101] shutdown
   [*NPE1-GigabitEthernet0/1/1.101] commit
   [~NPE1-GigabitEthernet0/1/1.101] quit
   ```
   
   Run the **display bfd session all** command on NPE1. The command output shows that the link BFD session between NPE1 and CE2 goes Down.
   
   ```
   [~NPE1] display bfd session all
   (w): State in WTR 
   (*): State is invalid
   --------------------------------------------------------------------------------
   Local  Remote PeerIpAddr      State     Type        InterfaceName
   --------------------------------------------------------------------------------
   8192   8192   10.1.1.253      Up        S_AUTO_IF   Eth-Trunk1.1
   8193   0      10.100.1.1      Down      S_AUTO_IF   GigabitEthernet0/1/1.100
   8194   0      10.101.1.1      Down     S_AUTO_IF   GigabitEthernet0/1/1.101
   8195   8194   10.102.1.1      Up        S_AUTO_IF   GigabitEthernet0/1/1.102
   8196   8195   10.103.1.1      Up        S_AUTO_IF   GigabitEthernet0/1/1.103
   --------------------------------------------------------------------------------
   Total UP/DOWN Session Number : 3/2
   ```
   
   In this configuration example, if two or more link BFD sessions go Down, the mVRRP group rapidly performs a master/backup VRRP switchover.
   
   Because two link BFD sessions went Down, the mVRRP group performs a master/backup VRRP switchover. Run the [**display vrrp brief**](cmdqueryname=display+vrrp+brief) command on each NPE.
   
   The command output on NPE1 is as follows:
   * In mVRRP group 10, the value of the **State** field is **Initialize** and the value of the **Type** field is **Admin**.
   * In each service VRRP group, the value of the **State** field is **Initialize** and the value of the **Type** field is **Member**.
   ```
   [~NPE1] display vrrp brief
   Total:5     Master:0    Backup:0    Non-active:5
   VRID   State         Interface        Type      Virtual IP      Master IP        Local IP
   ---------------------------------------------------------------------------------------------------
   10     Initialize    Eth-Trunk1.1     Admin     10.1.1.1      -                10.1.1.254 24
   100    Initialize    GE0/1/1.100      Member    10.100.1.200  -               10.100.1.254 24 
   101    Initialize    GE0/1/1.101      Member    10.101.1.200 10.101.1.254 24  10.101.1.254 24 
   102    Initialize    GE0/1/1.102      Member    10.102.1.200 10.102.1.254 24  10.102.1.254 24
   103    Initialize    GE0/1/1.103      Member    10.103.1.200 10.103.1.254 24  10.103.1.254 24
   ```
   The command output on NPE2 is as follows:
   * In mVRRP group 10, the value of the **State** field is **Master** and the value of the **Type** field is **Admin**.
   * In each service VRRP group, the value of the **State** field is **Master** and the value of the **Type** field is **Member**.
   ```
   [~NPE2] display vrrp brief
   Total:5     Master:5    Backup:0    Non-active:0
   VRID   State      Interface         Type     Virtual IP      Master IP           Local IP
   ---------------------------------------------------------------------------------------------------------
   10     Master     Eth-Trunk1.1      Admin    10.1.1.1       10.1.1.253 24       10.1.1.253 24
   100    Master     GE0/1/1.100       Member   10.100.1.200   10.100.1.253 24     10.100.1.253 24
   101    Master     GE0/1/1.101       Member   10.101.1.200   10.102.1.253 24     10.102.1.253 24
   102    Master     GE0/1/1.102       Member   10.102.1.200   10.102.1.253 24     10.102.1.253 24
   103    Master     GE0/1/1.103       Member   10.103.1.200   10.103.1.253 24     10.103.1.253 24
   ```
   
   Run the **undo shutdown** command on GE 0/1/1.100 and GE 0/1/1.101 of NPE1 to simulate fault recovery between NPE1 and CE1 and between NPE1 and CE2.
   
   ```
   [~NPE1] interface gigabitethernet0/1/1.100
   [*NPE1-GigabitEthernet0/1/1.100] undo shutdown
   [*NPE1-GigabitEthernet0/1/1.100] commit
   [~NPE1-GigabitEthernet0/1/1.100] quit
   [~NPE1] interface gigabitethernet0/1/1.101
   [*NPE1-GigabitEthernet0/1/1.101] undo shutdown
   [*NPE1-GigabitEthernet0/1/1.101] commit
   [~NPE1-GigabitEthernet0/1/1.101] quit
   ```
   
   Run the **display bfd session all** command on NPE1. The command output shows that the link BFD session between NPE1 and each CE goes Up.
   
   ```
   [~NPE1] display bfd session all
   (w): State in WTR 
   (*): State is invalid
   --------------------------------------------------------------------------------
   Local  Remote PeerIpAddr     State     Type        InterfaceName                 
   --------------------------------------------------------------------------------
   8192  8192   10.1.1.253      Up        S_AUTO_IF   Eth-Trunk1.1                 
   8193  8192   10.100.1.1      Up       S_AUTO_IF   GigabitEthernet0/1/1.100     
   8194  8193   10.101.1.1      Up       S_AUTO_IF   GigabitEthernet0/1/1.101     
   8195  8194   10.102.1.1      Up        S_AUTO_IF   GigabitEthernet0/1/1.102     
   8196  8195   10.103.1.1      Up        S_AUTO_IF   GigabitEthernet0/1/1.103     
   --------------------------------------------------------------------------------
   Total UP/DOWN Session Number : 5/0
   ```
   
   A VRRP switchback has been performed and the VRRP statuses of NPE1 and NPE2 in each VRRP group have been restored. Run the [**display vrrp brief**](cmdqueryname=display+vrrp+brief) command on each NPE.
   
   The command output on NPE1 is as follows:
   * In mVRRP group 10, the value of the **State** field is **Master** and the value of the **Type** field is **Admin**.
   * In each service VRRP group, the value of the **State** field is **Master** and the value of the **Type** field is **Member**.
   ```
   [~NPE1] display vrrp brief
   Total:5     Master:5    Backup:0    Non-active:0
   VRID   State      Interface        Type     Virtual IP      Master IP           Local IP
   ```
   ```
   ------------------------------------------------------------------------------------------------------------------
   10     Master     Eth-Trunk1.1     Admin    10.1.1.1       10.1.1.254 24    10.1.1.254 24 
   100    Master     GE0/1/1.100      Normal   10.100.1.200   10.100.1.254 24  10.100.1.254 24 
   101    Master     GE0/1/1.101      Normal   10.101.1.200   10.101.1.254 24  10.101.1.254 24 
   102    Master     GE0/1/1.102      Normal   10.102.1.200   10.102.1.254 24  10.102.1.254 24
   103    Master     GE0/1/1.103      Normal   10.103.1.200   10.103.1.254 24  10.103.1.254 24
   ```
   The command output on NPE2 is as follows:
   * In mVRRP group 10, the value of the **State** field is **Backup** and the value of the **Type** field is **Admin**.
   * In each service VRRP group, the value of the **State** field is **Backup** and the value of the **Type** field is **Member**.
   ```
   [~NPE2] display vrrp brief
   Total:5     Master:0    Backup:5    Non-active:0
   VRID   State      Interface        Type     Virtual IP      Master IP           Local IP
   ------------------------------------------------------------------------------------------------------------------
   ```
   ```
   10     Backup     Eth-Trunk1.1     Admin    10.1.1.1       10.1.1.254 24       10.1.1.253 24
   100    Backup     GE0/1/1.100      Member   10.100.1.200   10.100.1.254 24     10.100.1.253 24
   101    Backup     GE0/1/1.101      Member   10.101.1.200   10.101.1.253 24     10.102.1.253 24
   102    Backup     GE0/1/1.102      Member   10.102.1.200   10.102.1.254 24     10.102.1.253 24
   103    Backup     GE0/1/1.103      Member   10.103.1.200   10.103.1.254 24     10.103.1.253 24
   ```

#### Configuration Files

* NPE1 configuration file
  
  ```
  #
  sysname NPE1
  #
  bfd
  #
  interface Eth-Trunk1 
  #
  interface Eth-Trunk1.1
   control-vid 1 qinq-termination
   qinq termination pe-vid 10 ce-vid 1 to 100
   qinq vrrp pe-vid 10 ce-vid 100
   ip address 10.1.1.254 255.255.255.0
   vrrp vrid 10 virtual-ip 10.1.1.1
   admin-vrrp vrid 10 ignore-if-down
   vrrp vrid 10 priority 120
   vrrp vrid 10 track bfd-session session-name link1 link
   vrrp vrid 10 track bfd-session session-name link2 link
   vrrp vrid 10 track bfd-session session-name link3 link
   vrrp vrid 10 track bfd-session session-name link4 link
   vrrp vrid 10 track bfd-session session-name peer1 peer
   vrrp vrid 10 track link-bfd down-number 2
   arp broadcast enable
  #
  interface GigabitEthernet0/1/1
   undo shutdown
  #
  interface GigabitEthernet0/1/1.100
   control-vid 100 qinq-termination
   qinq termination pe-vid 10 ce-vid 101 to 200
   qinq vrrp pe-vid 10 ce-vid 101
   ip address 10.100.1.254 255.255.255.0
   vrrp vrid 100 virtual-ip 10.100.1.200
   vrrp vrid 100 track admin-vrrp interface Eth-Trunk1.1 vrid 10 unflowdown
   arp broadcast enable
  #
  interface GigabitEthernet0/1/1.101
   control-vid 101 qinq-termination
   qinq termination pe-vid 10 ce-vid 201 to 300
   qinq vrrp pe-vid 10 ce-vid 201
   ip address 10.101.1.254 255.255.255.0
   vrrp vrid 101 virtual-ip 10.101.1.200
   vrrp vrid 101 track admin-vrrp interface Eth-Trunk1.1 vrid 10 unflowdown
   arp broadcast enable
  #
  interface GigabitEthernet0/1/1.102
   control-vid 102 qinq-termination
   qinq termination pe-vid 10 ce-vid 301 to 400
   qinq vrrp pe-vid 10 ce-vid 301
   ip address 10.102.1.254 255.255.255.0
   vrrp vrid 102 virtual-ip 10.102.1.200
   vrrp vrid 102 track admin-vrrp interface Eth-Trunk1.1 vrid 10 unflowdown
   arp broadcast enable
  #
  interface GigabitEthernet0/1/1.103
   control-vid 103 qinq-termination
   qinq termination pe-vid 10 ce-vid 401 to 500
   qinq vrrp pe-vid 10 ce-vid 401
   ip address 10.103.1.254 255.255.255.0
   vrrp vrid 103 virtual-ip 10.103.1.200
   vrrp vrid 103 track admin-vrrp interface Eth-Trunk1.1 vrid 10 unflowdown
   arp broadcast enable
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   eth-trunk 1
  #
  interface GigabitEthernet0/2/1
   undo shutdown
   eth-trunk 1
  #
  bfd link1 bind peer-ip 10.100.1.1 interface GigabitEthernet0/1/1.100 source-ip 10.100.1.254 auto
  #
  bfd link2 bind peer-ip 10.101.1.1 interface GigabitEthernet0/1/1.101 source-ip 10.101.1.254 auto
  #
  bfd link3 bind peer-ip 10.102.1.1 interface GigabitEthernet0/1/1.102 source-ip 10.102.1.254 auto
  #
  bfd link4 bind peer-ip 10.103.1.1 interface GigabitEthernet0/1/1.103 source-ip 10.103.1.254 auto
  #
  bfd peer1 bind peer-ip 10.1.1.253 interface Eth-Trunk1.1 source-ip 10.1.1.254 auto
  #
  return
  ```
* NPE2 configuration file
  
  ```
  #
  sysname NPE2
  #
  bfd
  #
  interface Eth-Trunk1 
  #
  interface Eth-Trunk1.1
   control-vid 1 qinq-termination
   qinq termination pe-vid 10 ce-vid 1 to 100
   qinq vrrp pe-vid 10 ce-vid 100
   ip address 10.1.1.253 255.255.255.0
   vrrp vrid 10 virtual-ip 10.1.1.1
   admin-vrrp vrid 10 ignore-if-down
   vrrp vrid 10 track bfd-session session-name link1 link
   vrrp vrid 10 track bfd-session session-name link2 link
   vrrp vrid 10 track bfd-session session-name link3 link
   vrrp vrid 10 track bfd-session session-name link4 link
   vrrp vrid 10 track bfd-session session-name peer1 peer
   vrrp vrid 10 track link-bfd down-number 2
   arp broadcast enable
  #
  interface GigabitEthernet0/1/1
   undo shutdown
  #
  interface GigabitEthernet0/1/1.100
   control-vid 100 qinq-termination
   qinq termination pe-vid 10 ce-vid 101 to 200
   qinq vrrp pe-vid 10 ce-vid 101
   ip address 10.100.1.253 255.255.255.0
   vrrp vrid 100 virtual-ip 10.100.1.200
   vrrp vrid 100 track admin-vrrp interface Eth-Trunk1.1 vrid 10 unflowdown
   arp broadcast enable
  #
  interface GigabitEthernet0/1/1.101
   control-vid 101 qinq-termination
   qinq termination pe-vid 10 ce-vid 201 to 300
   qinq vrrp pe-vid 10 ce-vid 201
   ip address 10.101.1.253 255.255.255.0
   vrrp vrid 101 virtual-ip 10.101.1.200
   vrrp vrid 101 track admin-vrrp interface Eth-Trunk1.1 vrid 10 unflowdown
   arp broadcast enable
  #
  interface GigabitEthernet0/1/1.102
   control-vid 102 qinq-termination
   qinq termination pe-vid 10 ce-vid 301 to 400
   qinq vrrp pe-vid 10 ce-vid 301
   ip address 10.102.1.253 255.255.255.0
   vrrp vrid 102 virtual-ip 10.102.1.200
   vrrp vrid 102 track admin-vrrp interface Eth-Trunk1.1 vrid 10 unflowdown
   arp broadcast enable
  #
  interface GigabitEthernet0/1/1.103
   control-vid 103 qinq-termination
   qinq termination pe-vid 10 ce-vid 401 to 500
   qinq vrrp pe-vid 10 ce-vid 401
   ip address 10.103.1.253 255.255.255.0
   vrrp vrid 103 virtual-ip 10.103.1.200
   vrrp vrid 103 track admin-vrrp interface Eth-Trunk1.1 vrid 10 unflowdown
   arp broadcast enable
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   eth-trunk 1
  #
  interface GigabitEthernet0/2/1
   undo shutdown
   eth-trunk 1
  #
  bfd link1 bind peer-ip 10.100.1.1 interface GigabitEthernet0/1/1.100 source-ip 10.100.1.253 auto
  #
  bfd link2 bind peer-ip 10.101.1.1 interface GigabitEthernet0/1/1.101 source-ip 10.101.1.253 auto
  #
  bfd link3 bind peer-ip 10.102.1.1 interface GigabitEthernet0/1/1.102 source-ip 10.102.1.253 auto
  #
  bfd link4 bind peer-ip 10.103.1.1 interface GigabitEthernet0/1/1.103 source-ip 10.103.1.253 auto
  #
  bfd peer1 bind peer-ip 10.1.1.254 interface Eth-Trunk1.1 source-ip 10.1.1.253 auto
  #
  return
  
  ```
* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  mpls lsr-id 3.3.3.3
  #
  mpls
  #
  mpls l2vpn
  #
  vsi ldp1 static
   pwsignal ldp
    vsi-id 100
    peer 5.5.5.5
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/2
  
   undo shutdown
   ip address 172.16.34.3 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/1
   undo shutdown
  #
  interface GigabitEthernet0/1/1.1
   vlan-type dot1q 10
   l2 binding vsi ldp1
  #
  interface GigabitEthernet0/1/3
   undo shutdown
   ip address 172.16.35.3 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 3.3.3.3 255.255.255.255
  #
  ospf 1
   area 0.0.0.0
    network 3.3.3.3 0.0.0.0
    network 172.16.34.0 0.0.0.255
    network 172.16.35.0 0.0.0.255
  #
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  mpls lsr-id 4.4.4.4
  #
  mpls
  #
  mpls l2vpn
  #
  vsi ldp1 static
   pwsignal ldp
    vsi-id 100
    peer 5.5.5.5
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 172.16.34.4 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/1
   undo shutdown
  #
  interface GigabitEthernet0/1/1.1
   vlan-type dot1q 10
   l2 binding vsi ldp1
  #
  interface GigabitEthernet0/1/3
   undo shutdown
   ip address 172.16.45.4 255.255.255.0
   mpls
   mpls ldp
  interface LoopBack1
   ip address 4.4.4.4 255.255.255.255
  #
  ospf 1
   area 0.0.0.0
    network 4.4.4.4 0.0.0.0
    network 172.16.34.0 0.0.0.255
    network 172.16.45.0 0.0.0.255
  #
  return
  ```
* PE3 configuration file
  
  ```
  #
  sysname PE3
  #
  mpls lsr-id 5.5.5.5
  #
  mpls
  #
  mpls l2vpn
  #
  vsi ldp1 static
   pwsignal ldp
    vsi-id 100
    peer 3.3.3.3
    peer 4.4.4.4
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
  #
  interface GigabitEthernet0/1/0.1
   vlan-type dot1q 10
   l2 binding vsi ldp1
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 172.16.35.5 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 172.16.45.5 255.255.255.0
   mpls
   mpls ldp
  #
  ip address 5.5.5.5 255.255.255.255
  #
  ospf 1
   area 0.0.0.0
    network 5.5.5.5 0.0.0.0
    network 172.16.35.0 0.0.0.255
    network 172.16.45.0 0.0.0.255
  #
  return
  ```
* CE1 configuration file
  
  ```
  #
  sysname CE1
  #
  bfd
  # 
  interface GigabitEthernet0/1/1
   undo shutdown
  #
  interface GigabitEthernet0/1/1.100
   control-vid 100 qinq-termination
   qinq termination pe-vid 10 ce-vid 110
   ip address 10.100.1.1 255.255.255.0
   arp broadcast enable
  #
  interface GigabitEthernet0/1/1.101
   control-vid 101 qinq-termination
   qinq termination pe-vid 10 ce-vid 210
   ip address 10.101.1.1 255.255.255.0
   arp broadcast enable
  #
  interface GigabitEthernet0/1/1.102
   control-vid 102 qinq-termination
   qinq termination pe-vid 10 ce-vid 310
   ip address 10.102.1.1 255.255.255.0
   arp broadcast enable
  #
  interface GigabitEthernet0/1/1.103
   control-vid 103 qinq-termination
   qinq termination pe-vid 10 ce-vid 410
   ip address 10.103.1.1 255.255.255.0
   arp broadcast enable
  #
  bfd link11 bind peer-ip 10.100.1.254 interface GigabitEthernet0/1/1.100 source-ip 10.100.1.1 auto
  #
  bfd link12 bind peer-ip 10.101.1.254 interface GigabitEthernet0/1/1.101 source-ip 10.101.1.1 auto
  #
  bfd link13 bind peer-ip 10.102.1.254 interface GigabitEthernet0/1/1.102 source-ip 10.102.1.1 auto
  #
  bfd link14 bind peer-ip 10.103.1.254 interface GigabitEthernet0/1/1.103 source-ip 10.103.1.1 auto
  #
  bfd link21 bind peer-ip 10.100.1.253 interface GigabitEthernet0/1/1.100 source-ip 10.100.1.1 auto
  #
  bfd link22 bind peer-ip 10.101.1.253 interface GigabitEthernet0/1/1.101 source-ip 10.101.1.1 auto
  #
  bfd link23 bind peer-ip 10.102.1.253 interface GigabitEthernet0/1/1.102 source-ip 10.102.1.1 auto
  #
  bfd link24 bind peer-ip 10.103.1.253 interface GigabitEthernet0/1/1.103 source-ip 10.103.1.1 auto
  #
  return
  ```
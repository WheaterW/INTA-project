Example for Associating a VRRP Group with BFD Sessions Using BFD Sampling
=========================================================================

In this example, a VRRP group is used together with BFD sampling when link BFD sessions cannot be established between NPEs and PEs.

#### Networking Requirements

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The NE40E-M2K is used as an example.

A VRRP group is usually associated with a BFD session to rapidly perform an active/standby link switchover, improving link reliability. On the network shown in [Figure 1](#EN-US_TASK_0000001163660194__en-us_task_0172361817_fig_dc_vrp_vrrp_cfg_012901), CEs connect to sub-interfaces for QinQ VLAN tag termination on NPEs across a VPLS aggregation network. On the NPEs, an mVRRP group and its service VRRP groups are configured. The mVRRP group tracks BFD sessions to perform a rapid master/backup VRRP switchover. A peer BFD session is established between the NPEs. Because the VPLS aggregation network is run by a carrier different from the carrier running the access and core networks, a link BFD session cannot be established between NPE1 and PE1 or between NPE2 and PE2.

To improve link reliability in this scenario, use the BFD sampling mode.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Each NPE enabled with BFD sampling establishes a link BFD session with each CE.


The configurations on NPEs are described as follows:

* An mVRRP group, service VRRP groups, and a peer BFD session are established on interfaces connecting NPE1 and NPE2 to the VPLS aggregation network.
* A link BFD session is established between each NPE and each CE. The mVRRP group tracks each link BFD session. The mVRRP group can rapidly perform a master/backup VRRP switchover if two or more link BFD sessions go Down.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE 0/1/1, GE 0/1/2, and GE 0/1/3, respectively.



**Figure 1** Associating a VRRP group with BFD sessions using BFD sampling  
![](images/fig_dc_vrp_vrrp_cfg_012901.png)  

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
| NPE1 | GE0/1/1.1 | 10.1.1.254/24 |
| GE0/1/1.100 | 10.100.1.254/24 |
| GE0/1/1.101 | 10.101.1.254/24 |
| GE0/1/1.102 | 10.102.1.254/24 |
| GE0/1/1.103 | 10.103.1.254/24 |
| NPE2 | GE0/1/1.1 | 10.1.1.253/24 |
| GE0/1/1.100 | 10.100.1.253/24 |
| GE0/1/1.101 | 10.101.1.253/24 |
| GE0/1/1.102 | 10.102.1.253/24 |
| GE0/1/1.103 | 10.103.1.253/24 |



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
* VRRP groups on NPEs:
  + Backup group 10, with a virtual IP address of 10.1.1.1.
  + Backup group 100, with a virtual IP address of 10.100.1.200.
  + Backup group 101, with a virtual IP address of 10.101.1.200.
  + Backup group 102, with a virtual IP address of 10.102.1.200.
  + Backup group 103, with a virtual IP address of 10.103.1.200.Backup group 10 functions as an mVRRP group, and the others function as service VRRP groups.
* Binding between the service VRRP groups and the mVRRP group so that the mVRRP group determines the master and backup states of the service VRRP groups
* Peer BFD session parameters on each NPE (peer IP address of 10.1.1.253, outbound interface of GE 0/1/1.1, and source IP address of 10.1.1.254 on NPE1; peer IP address of 10.1.1.254, outbound interface of GE 0/1/1.1, and source IP address of 10.1.1.253 on NPE2)
* Link BFD session parameters on each NPE and CE, including the peer IP address, outbound interface name, and source IP address

#### Procedure

1. Configure basic functions for sub-interfaces for QinQ VLAN tag termination.
   
   
   
   The following example provides only the configuration procedure on each NPE. For the procedure for configuring a link BFD session on each CE, see the chapter "BFD Configuration" in *HUAWEI NE40E-M2 seriesUniversal Service Router Configuration Guide - Reliability*. For the procedure for configuring the VPLS on each CE, see the chapter "VPLS Configuration" in *HUAWEI NE40E-M2 seriesUniversal Service Router Configuration Guide - VPN*.
   
   # Configure NPE1.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname NPE1
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~NPE1] interface gigabitethernet0/1/1
   ```
   ```
   [~NPE1-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1] commit
   ```
   ```
   [~NPE1-GigabitEthernet0/1/1] quit
   ```
   ```
   [~NPE1] interface gigabitethernet0/1/1.1
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.1] control-vid 1 qinq-termination
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.1] qinq termination pe-vid 10 ce-vid 1 to 100
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.1] ip address 10.1.1.254 24
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.1] arp broadcast enable
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.1] commit
   ```
   ```
   [~NPE1-GigabitEthernet0/1/1.1] quit
   ```
   ```
   [~NPE1] interface gigabitethernet0/1/1.100
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.100] control-vid 100 qinq-termination
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.100] qinq termination pe-vid 10 ce-vid 101 to 200
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.100] ip address 10.100.1.254 24
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.100] arp broadcast enable
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.100] commit
   ```
   ```
   [~NPE1-GigabitEthernet0/1/1.100] quit
   ```
   ```
   [~NPE1] interface gigabitethernet0/1/1.101
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.101] control-vid 101 qinq-termination
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.101] qinq termination pe-vid 10 ce-vid 201 to 300
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.101] ip address 10.101.1.254 24
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.101] arp broadcast enable
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.101] commit
   ```
   ```
   [~NPE1-GigabitEthernet0/1/1.101] quit
   ```
   ```
   [~NPE1] interface gigabitethernet0/1/1.102
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.102] control-vid 102 qinq-termination
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.102] qinq termination pe-vid 10 ce-vid 301 to 400
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.102] ip address 10.102.1.254 24
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.102] arp broadcast enable
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.102] commit
   ```
   ```
   [~NPE1-GigabitEthernet0/1/1.102] quit
   ```
   ```
   [~NPE1] interface gigabitethernet0/1/1.103
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.103] control-vid 103 qinq-termination
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.103] qinq termination pe-vid 10 ce-vid 401 to 500
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.103] ip address 10.103.1.254 24
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.103] arp broadcast enable
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.103] commit
   ```
   ```
   [~NPE1-GigabitEthernet0/1/1.103] quit
   ```
   
   # Configure NPE2.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname NPE2
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~NPE2] interface gigabitethernet0/1/1
   ```
   ```
   [~NPE2-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*NPE2-GigabitEthernet0/1/1] commit
   ```
   ```
   [~NPE2-GigabitEthernet0/1/1] quit
   ```
   ```
   [~NPE2] interface gigabitethernet0/1/1.1
   ```
   ```
   [*NPE2-GigabitEthernet0/1/1.1] control-vid 1 qinq-termination
   ```
   ```
   [*NPE2-GigabitEthernet0/1/1.1] qinq termination pe-vid 10 ce-vid 1 to 100
   ```
   ```
   [*NPE2-GigabitEthernet0/1/1.1] ip address 10.1.1.253 24
   ```
   ```
   [*NPE2-GigabitEthernet0/1/1.1] arp broadcast enable
   ```
   ```
   [*NPE2-GigabitEthernet0/1/1.1] commit
   ```
   ```
   [~NPE2-GigabitEthernet0/1/1.1] quit
   ```
   ```
   [~NPE2] interface gigabitethernet0/1/1.100
   ```
   ```
   [*NPE2-GigabitEthernet0/1/1.100] control-vid 100 qinq-termination
   ```
   ```
   [*NPE2-GigabitEthernet0/1/1.100] qinq termination pe-vid 10 ce-vid 101 to 200
   ```
   ```
   [*NPE2-GigabitEthernet0/1/1.100] ip address 10.100.1.253 24
   ```
   ```
   [*NPE2-GigabitEthernet0/1/1.100] arp broadcast enable
   ```
   ```
   [*NPE2-GigabitEthernet0/1/1.100] commit
   ```
   ```
   [~NPE2-GigabitEthernet0/1/1.100] quit
   ```
   ```
   [~NPE2] interface gigabitethernet0/1/1.101
   ```
   ```
   [*NPE2-GigabitEthernet0/1/1.101] control-vid 101 qinq-termination
   ```
   ```
   [*NPE2-GigabitEthernet0/1/1.101] qinq termination pe-vid 10 ce-vid 201 to 300
   ```
   ```
   [*NPE2-GigabitEthernet0/1/1.101] ip address 10.101.1.253 24
   ```
   ```
   [*NPE2-GigabitEthernet0/1/1.101] arp broadcast enable
   ```
   ```
   [*NPE2-GigabitEthernet0/1/1.101] commit
   ```
   ```
   [~NPE2-GigabitEthernet0/1/1.101] quit
   ```
   ```
   [~NPE2] interface gigabitethernet0/1/1.102
   ```
   ```
   [*NPE2-GigabitEthernet0/1/1.102] control-vid 102 qinq-termination
   ```
   ```
   [*NPE2-GigabitEthernet0/1/1.102] qinq termination pe-vid 10 ce-vid 301 to 400
   ```
   ```
   [*NPE2-GigabitEthernet0/1/1.102] ip address 10.102.1.253 24
   ```
   ```
   [*NPE2-GigabitEthernet0/1/1.102] arp broadcast enable
   ```
   ```
   [*NPE2-GigabitEthernet0/1/1.102] commit
   ```
   ```
   [~NPE2-GigabitEthernet0/1/1.102] quit
   ```
   ```
   [~NPE2] interface gigabitethernet0/1/1.103
   ```
   ```
   [*NPE2-GigabitEthernet0/1/1.103] control-vid 103 qinq-termination
   ```
   ```
   [*NPE2-GigabitEthernet0/1/1.103] qinq termination pe-vid 10 ce-vid 401 to 500
   ```
   ```
   [*NPE2-GigabitEthernet0/1/1.103] ip address 10.103.1.253 24
   ```
   ```
   [*NPE2-GigabitEthernet0/1/1.103] arp broadcast enable
   ```
   ```
   [*NPE2-GigabitEthernet0/1/1.103] commit
   ```
   ```
   [~NPE2-GigabitEthernet0/1/1.103] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After the IP address is assigned to each sub-interface for QinQ VLAN tag termination, run the [**arp broadcast enable**](cmdqueryname=arp+broadcast+enable) command to ensure that the sub-interfaces can ping each other.
   
   After completing the configurations, run the [**ping**](cmdqueryname=ping) command on the sub-interface for QinQ VLAN tag termination on each NPE to ping another sub-interface for QinQ VLAN tag termination on the same network segment. The command output shows that the ping is successful.
2. Configure basic VRRP functions for the sub-interfaces for QinQ VLAN tag termination.
   
   
   
   # Configure an mVRRP group with the VRID of 10 on GE 0/1/1.1 and configure common VRRP groups on other sub-interfaces of NPE1.
   
   ```
   [~NPE1] interface gigabitethernet0/1/1.1
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.1] qinq vrrp pe-vid 10 ce-vid 100
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.1] vrrp vrid 10 virtual-ip 10.1.1.1
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.1] vrrp vrid 10 priority 120
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.1] admin-vrrp vrid 10
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.1] commit
   ```
   ```
   [~NPE1-GigabitEthernet0/1/1.1] quit
   ```
   ```
   [~NPE1] interface gigabitethernet0/1/1.100
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.100] qinq vrrp pe-vid 10 ce-vid 101
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.100] vrrp vrid 100 virtual-ip 10.100.1.200
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.100] commit
   ```
   ```
   [~NPE1-GigabitEthernet0/1/1.100] quit
   ```
   ```
   [~NPE1] interface gigabitethernet0/1/1.101
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.101] qinq vrrp pe-vid 10 ce-vid 201
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.101] vrrp vrid 101 virtual-ip 10.101.1.200
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.101] commit
   ```
   ```
   [~NPE1-GigabitEthernet0/1/1.101] quit
   ```
   ```
   [~NPE1] interface gigabitethernet0/1/1.102
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.102] qinq vrrp pe-vid 10 ce-vid 301
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.102] vrrp vrid 102 virtual-ip 10.102.1.200
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.102] commit
   ```
   ```
   [~NPE1-GigabitEthernet0/1/1.102] quit
   ```
   ```
   [~NPE1] interface gigabitethernet0/1/1.103
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.103] qinq vrrp pe-vid 10 ce-vid 401
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.103] vrrp vrid 103 virtual-ip 10.103.1.200
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.103] commit
   ```
   ```
   [~NPE1-GigabitEthernet0/1/1.103] quit
   ```
   
   # Configure an mVRRP group with the VRID of 10 on GE 0/1/1.1 and configure common VRRP groups on other sub-interfaces of NPE2.
   
   ```
   [~NPE2] interface gigabitethernet0/1/1.1
   ```
   ```
   [*NPE2-GigabitEthernet0/1/1.1] qinq vrrp pe-vid 10 ce-vid 100
   ```
   ```
   [*NPE2-GigabitEthernet0/1/1.1] vrrp vrid 10 virtual-ip 10.1.1.1
   ```
   ```
   [*NPE2-GigabitEthernet0/1/1.1] admin-vrrp vrid 10
   ```
   ```
   [*NPE2-GigabitEthernet0/1/1.1] commit
   ```
   ```
   [~NPE2-GigabitEthernet0/1/1.1] quit
   ```
   ```
   [~NPE2] interface gigabitethernet0/1/1.100
   ```
   ```
   [*NPE2-GigabitEthernet0/1/1.100] qinq vrrp pe-vid 10 ce-vid 101
   ```
   ```
   [*NPE2-GigabitEthernet0/1/1.100] vrrp vrid 100 virtual-ip 10.100.1.200
   ```
   ```
   [*NPE2-GigabitEthernet0/1/1.100] commit
   ```
   ```
   [~NPE2-GigabitEthernet0/1/1.100] quit
   ```
   ```
   [~NPE2] interface gigabitethernet0/1/1.101
   ```
   ```
   [*NPE2-GigabitEthernet0/1/1.101] qinq vrrp pe-vid 10 ce-vid 201
   ```
   ```
   [*NPE2-GigabitEthernet0/1/1.101] vrrp vrid 101 virtual-ip 10.101.1.200
   ```
   ```
   [*NPE2-GigabitEthernet0/1/1.101] commit
   ```
   ```
   [~NPE2-GigabitEthernet0/1/1.101] quit
   ```
   ```
   [~NPE2] interface gigabitethernet0/1/1.102
   ```
   ```
   [*NPE2-GigabitEthernet0/1/1.102] qinq vrrp pe-vid 10 ce-vid 301
   ```
   ```
   [*NPE2-GigabitEthernet0/1/1.102] vrrp vrid 102 virtual-ip 10.102.1.200
   ```
   ```
   [*NPE2-GigabitEthernet0/1/1.102] commit
   ```
   ```
   [~NPE2-GigabitEthernet0/1/1.102] quit
   ```
   ```
   [~NPE2] interface gigabitethernet0/1/1.103
   ```
   ```
   [*NPE2-GigabitEthernet0/1/1.103] qinq vrrp pe-vid 10 ce-vid 401
   ```
   ```
   [*NPE2-GigabitEthernet0/1/1.103] vrrp vrid 103 virtual-ip 10.103.1.200
   ```
   ```
   [*NPE2-GigabitEthernet0/1/1.103] commit
   ```
   ```
   [~NPE2-GigabitEthernet0/1/1.103] quit
   ```
   
   After completing the configurations, run the **display vrrp** command on each NPE.
   
   The command output on NPE1 is as follows:
   * In mVRRP group 10, the value of the **State** field is **Master** and the value of the **Type** field is **Admin**.
   * In each common VRRP group, the value of the **State** field is **Master** and the value of the **Type** field is **Normal**.
   ```
   [~NPE1] display vrrp brief
   ```
   ```
   Total:5     Master:5    Backup:0    Non-active:0    
   VRID   State       Interface        Type    Virtual IP       Master IP       Local IP
   -------------------------------------------------------------------------------------------------
   10     Master     GE0/1/1.1        Admin   10.1.1.1       10.1.1.254 24    10.1.1.254 24
   100    Master      GE0/1/1.100      Normal  10.100.1.200    10.100.1.254 24  10.100.1.254 24
   101    Master      GE0/1/1.101      Normal  10.101.1.200    10.101.1.254 24  10.101.1.254 24
   102    Master      GE0/1/1.102      Normal  10.102.1.200    10.102.1.253 24  10.102.1.253 24
   103    Master      GE0/1/1.103      Normal  10.103.1.200    10.103.1.254 24  10.103.1.254 24
   ```
   The command output on NPE2 is as follows:
   * In mVRRP group 10, the value of the **State** field is **Backup** and the value of the **Type** field is **Admin**.
   * In each common VRRP group, the value of the **State** field is **Backup** and the value of the **Type** field is **Normal**.
   ```
   [~NPE2] display vrrp brief
   ```
   ```
   Total:5     Master:0    Backup:5    Non-active:0    
   VRID   State       Interface        Type    Virtual IP     Master IP       Local IP
   --------------------------------------------------------------------------------------------------
   10     Backup     GE0/1/1.1        Admin   10.1.1.1      10.1.1.254 24    10.1.1.253 24
   100    Backup      GE0/1/1.100      Normal  10.100.1.200  10.100.1.254 24  10.100.1.253 24
   101    Backup      GE0/1/1.101      Normal  10.101.1.200  10.101.1.254 24  10.101.1.253 24
   102    Backup      GE0/1/1.102      Normal  10.102.1.200  10.102.1.254 24  10.102.1.253 24
   103    Backup      GE0/1/1.103      Normal  10.103.1.200  10.103.1.254 24  10.103.1.253 24
   ```
3. Bind each common VRRP group to the mVRRP group so that the common VRRP groups become service VRRP groups.
   
   
   
   # Configure NPE1.
   
   ```
   [~NPE1] interface gigabitethernet0/1/1.100
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.100] vrrp vrid 100 track admin-vrrp interface gigabitethernet0/1/1.1 vrid 10 unflowdown
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.100] commit
   ```
   ```
   [~NPE1-GigabitEthernet0/1/1.100] quit
   ```
   ```
   [~NPE1] interface gigabitethernet0/1/1.101
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.101] vrrp vrid 101 track admin-vrrp interface gigabitethernet0/1/1.1 vrid 10 unflowdown
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.101] commit
   ```
   ```
   [~NPE1-GigabitEthernet0/1/1.101] quit
   ```
   ```
   [~NPE1] interface gigabitethernet0/1/1.102
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.102] vrrp vrid 102 track admin-vrrp interface gigabitethernet0/1/1.1 vrid 10 unflowdown
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.102] commit
   ```
   ```
   [~NPE1-GigabitEthernet0/1/1.102] quit
   ```
   ```
   [~NPE1] interface gigabitethernet0/1/1.103
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.103] vrrp vrid 103 track admin-vrrp interface gigabitethernet0/1/1.1 vrid 10 unflowdown
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.103] commit
   ```
   ```
   [~NPE1-GigabitEthernet0/1/1.103] quit
   ```
   
   # Configure NPE2.
   
   ```
   [~NPE2] interface gigabitethernet0/1/1.100
   ```
   ```
   [*NPE2-GigabitEthernet0/1/1.100] vrrp vrid 100 track admin-vrrp interface gigabitethernet0/1/1.1 vrid 10 unflowdown
   ```
   ```
   [*NPE2-GigabitEthernet0/1/1.100] commit
   ```
   ```
   [~NPE2-GigabitEthernet0/1/1.100] quit
   ```
   ```
   [~NPE2] interface gigabitethernet0/1/1.101
   ```
   ```
   [*NPE2-GigabitEthernet0/1/1.101] vrrp vrid 101 track admin-vrrp interface gigabitethernet0/1/1.1 vrid 10 unflowdown
   ```
   ```
   [*NPE2-GigabitEthernet0/1/1.101] commit
   ```
   ```
   [~NPE2-GigabitEthernet0/1/1.101] quit
   ```
   ```
   [~NPE2] interface gigabitethernet0/1/1.102
   ```
   ```
   [*NPE2-GigabitEthernet0/1/1.102] vrrp vrid 102 track admin-vrrp interface gigabitethernet0/1/1.1 vrid 10 unflowdown
   ```
   ```
   [*NPE2-GigabitEthernet0/1/1.102] commit
   ```
   ```
   [~NPE2-GigabitEthernet0/1/1.102] quit
   ```
   ```
   [~NPE2] interface gigabitethernet0/1/1.103
   ```
   ```
   [*NPE2-GigabitEthernet0/1/1.103] vrrp vrid 103 track admin-vrrp interface gigabitethernet0/1/1.1 vrid 10 unflowdown
   ```
   ```
   [*NPE2-GigabitEthernet0/1/1.103] commit
   ```
   ```
   [~NPE2-GigabitEthernet0/1/1.103] quit
   ```
   
   After completing the configurations, run the **display vrrp** command on each NPE.
   
   The command output on NPE1 is as follows:
   * In mVRRP group 10, the value of the **State** field is **Master** and the value of the **Type** field is **Admin**.
   * In each service VRRP group, the value of the **State** field is **Master** and the value of the **Type** field is **Member**.
   ```
   [~NPE1] display vrrp brief
   ```
   ```
   Total:5     Master:5    Backup:0    Non-active:0    
   VRID   State       Interface         Type    Virtual IP         Master IP       Local IP
   ------------------------------------------------------------------------------------------
   ```
   ```
   10     Master     GE0/1/1.1        Admin   10.1.1.1       10.1.1.254 24    10.1.1.254 24
   100    Master      GE0/1/1.100      Normal  10.100.1.200    10.100.1.254 24  10.100.1.254 24
   101    Master      GE0/1/1.101      Normal  10.101.1.200    10.101.1.254 24  10.101.1.254 24
   102    Master      GE0/1/1.102      Normal  10.102.1.200    10.102.1.253 24  10.102.1.253 24
   103    Master      GE0/1/1.103      Normal  10.103.1.200    10.103.1.254 24  10.103.1.254 24
   ```
   The command output on NPE2 is as follows:
   * In mVRRP group 10, the value of the **State** field is **Backup** and the value of the **Type** field is **Admin**.
   * In each service VRRP group, the value of the **State** field is **Backup** and the value of the **Type** field is **Member**.
   ```
   [~NPE2] display vrrp brief
   ```
   ```
   Total:5     Master:0    Backup:5    Non-active:0    
   VRID   State       Interface         Type    Virtual IP    Master IP       Local IP
   ```
   ```
   --------------------------------------------------------------------------------------------------
   10     Backup     GE0/1/1.1        Admin   10.1.1.1      10.1.1.254 24    10.1.1.253 24
   100    Backup      GE0/1/1.100      Normal  10.100.1.200  10.100.1.254 24  10.100.1.253 24
   101    Backup      GE0/1/1.101      Normal  10.101.1.200  10.101.1.254 24  10.101.1.253 24
   102    Backup      GE0/1/1.102      Normal  10.102.1.200  10.102.1.254 24  10.102.1.253 24
   103    Backup      GE0/1/1.103      Normal  10.103.1.200  10.103.1.254 24  10.103.1.253 24
   ```
   
   The command output shows that the service VRRP groups have been successfully bound to the mVRRP group and their statuses are correct.
4. Configure basic BFD functions.
   
   
   
   # Configure a peer BFD session between NPE1 and NPE2, and configure a link BFD session between each NPE and each CE.
   
   # Configure NPE1.
   
   ```
   [~NPE1] bfd
   ```
   ```
   [~NPE1-bfd] quit
   ```
   ```
   [~NPE1] bfd peer1 bind peer-ip 10.1.1.253 interface gigabitethernet0/1/1.1 source-ip 10.1.1.254 auto
   ```
   ```
   [*NPE1-bfd-session-peer1] commit
   ```
   ```
   [~NPE1-bfd-session-peer1] quit
   ```
   ```
   [~NPE1] bfd link1 bind peer-ip 10.100.1.1 interface gigabitethernet0/1/1.100 source-ip 10.100.1.254 auto
   ```
   ```
   [*NPE1-bfd-session-link1] commit
   ```
   ```
   [~NPE1-bfd-session-link1] quit
   ```
   ```
   [~NPE1] bfd link2 bind peer-ip 10.101.1.1 interface gigabitethernet0/1/1.101 source-ip 10.101.1.254 auto
   ```
   ```
   [*NPE1-bfd-session-link2] commit
   ```
   ```
   [~NPE1-bfd-session-link2] quit
   ```
   ```
   [~NPE1] bfd link3 bind peer-ip 10.102.1.1 interface gigabitethernet0/1/1.102 source-ip 10.102.1.254 auto
   ```
   ```
   [*NPE1-bfd-session-link3] commit
   ```
   ```
   [~NPE1-bfd-session-link3] quit
   ```
   ```
   [~NPE1] bfd link4 bind peer-ip 10.103.1.1 interface gigabitethernet0/1/1.103 source-ip 10.103.1.254 auto
   ```
   ```
   [*NPE1-bfd-session-link4] commit
   ```
   ```
   [~NPE1-bfd-session-link4] quit
   ```
   
   # Configure NPE2.
   
   ```
   [~NPE2] bfd
   ```
   ```
   [~NPE2-bfd] quit
   ```
   ```
   [~NPE2] bfd peer1 bind peer-ip 10.1.1.254 interface gigabitethernet0/1/1.1 source-ip 10.1.1.253 auto
   ```
   ```
   [*NPE2-bfd-session-peer1] commit
   ```
   ```
   [~NPE2-bfd-session-peer1] quit
   ```
   ```
   [~NPE2] bfd link1 bind peer-ip 10.100.1.1 interface gigabitethernet0/1/1.100 source-ip 10.100.1.253 auto
   ```
   ```
   [*NPE2-bfd-session-link1] commit
   ```
   ```
   [~NPE2-bfd-session-link1] quit
   ```
   ```
   [~NPE2] bfd link2 bind peer-ip 10.101.1.1 interface gigabitethernet0/1/1.101 source-ip 10.101.1.253 auto
   ```
   ```
   [*NPE2-bfd-session-link2] commit
   ```
   ```
   [~NPE2-bfd-session-link2] quit
   ```
   ```
   [~NPE2] bfd link3 bind peer-ip 10.102.1.1 interface gigabitethernet0/1/1.102 source-ip 10.102.1.253 auto
   ```
   ```
   [*NPE2-bfd-session-link3] commit
   ```
   ```
   [~NPE2-bfd-session-link3] quit
   ```
   ```
   [~NPE2] bfd link4 bind peer-ip 10.103.1.1 interface gigabitethernet0/1/1.103 source-ip 10.103.1.253 auto
   ```
   ```
   [*NPE2-bfd-session-link4] commit
   ```
   ```
   [~NPE2-bfd-session-link4] quit
   ```
   
   # Run the **display bfd session all** command on each NPE to view the BFD session status. The command output shows that the value of the **State** field is **Up**.
   
   # The following example uses the command output on NPE1.
   
   ```
   [~NPE1] display bfd session all
   (w): State in WTR 
   (*): State is invalid
   --------------------------------------------------------------------------------
   Local  Remote PeerIpAddr      State     Type      InterfaceName                 
   --------------------------------------------------------------------------------
   8192  8192   10.1.1.253      Up        S_AUTO_IF   GigabitEthernet0/1/1.1       
   8193  8192   10.100.1.1      Up        S_AUTO_IF   GigabitEthernet0/1/1.100     
   8194  8193   10.101.1.1      Up        S_AUTO_IF   GigabitEthernet0/1/1.101     
   8195  8194   10.102.1.1      Up        S_AUTO_IF   GigabitEthernet0/1/1.102     
   8196  8195   10.103.1.1      Up        S_AUTO_IF   GigabitEthernet0/1/1.103     
   --------------------------------------------------------------------------------
        Total UP/DOWN Session Number : 5/0
   ```
5. Configure the mVRRP group to track each link BFD session to allow BFD sampling to help rapidly trigger a master/backup VRRP switchover.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The configuration is performed only for the mVRRP group on GE 0/1/1.1 of each NPE, because service VRRP groups have been bound to the mVRRP group.
   
   # Configure NPE1.
   
   ```
   [~NPE1] interface gigabitethernet0/1/1.1
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.1] vrrp vrid 10 track bfd-session session-name peer1 peer
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.1] vrrp vrid 10 track bfd-session session-name link1 link
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.1] vrrp vrid 10 track bfd-session session-name link2 link
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.1] vrrp vrid 10 track bfd-session session-name link3 link
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.1] vrrp vrid 10 track bfd-session session-name link4 link
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.1] vrrp vrid 10 track link-bfd down-number 2
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.1] commit
   ```
   ```
   [~NPE1-GigabitEthernet0/1/1.1] quit
   ```
   
   # Configure NPE2.
   
   ```
   [~NPE2] interface gigabitethernet0/1/1.1
   ```
   ```
   [*NPE2-GigabitEthernet0/1/1.1] vrrp vrid 10 track bfd-session session-name peer1 peer
   ```
   ```
   [*NPE2-GigabitEthernet0/1/1.1] vrrp vrid 10 track bfd-session session-name link1 link
   ```
   ```
   [*NPE2-GigabitEthernet0/1/1.1] vrrp vrid 10 track bfd-session session-name link2 link
   ```
   ```
   [*NPE2-GigabitEthernet0/1/1.1] vrrp vrid 10 track bfd-session session-name link3 link
   ```
   ```
   [*NPE2-GigabitEthernet0/1/1.1] vrrp vrid 10 track bfd-session session-name link4 link
   ```
   ```
   [*NPE2-GigabitEthernet0/1/1.1] vrrp vrid 10 track link-bfd down-number 2
   ```
   ```
   [*NPE2-GigabitEthernet0/1/1.1] commit
   ```
   ```
   [~NPE2-GigabitEthernet0/1/1.1] quit
   ```
   
   After completing the configurations, run the **display vrrp** command on each NPE. The command output shows that allowable maximum number of tracked link BFD sessions in the Down state is **2**, that the mVRRP group has been bound to one peer BFD session and four link BFD sessions, and that the status of each BFD session is **UP**.
   
   ```
   [~NPE1] display vrrp interface gigabitethernet0/1/1.1 verbose
   ```
   ```
   GigabitEthernet0/1/1.1 | Virtual Router 10
   State                             : Master
   Virtual IP                        : 10.1.1.1
   Master IP                         : 10.1.1.254
   Local IP                          : 10.1.1.254             
   PriorityRun                       : 120
   PriorityConfig                    : 120
   MasterPriority                    : 120
   Preempt                           : YES              Delay Time : 0s
   Hold Multiplier                   : 4
   TimerRun                          : 1s
   TimerConfig                       : 1s
   Auth Type                         : NONE
   Virtual MAC                       : 0000-5e00-0101
   Passive Mode      : NO
   Check TTL                         : YES
   Config Type                       : admin-vrrp
   Backup-forward    : disabled
   Config track link-bfd down-number : 2
   Track BFD                         : link1            Type: Link
   BFD-session State                 : UP
   Track BFD                         : link2            Type: Link
   BFD-session State                 : UP
   Track BFD                         : link3            Type: Link
   BFD-session State                 : UP
   Track BFD                         : link4            Type: Link
   BFD-session State                 : UP
   Track BFD                         : peer1            Type: Peer
   BFD-session State                 : UP
   Create Time                       : 2010-06-22 17:33:00
   Last Change Time                  : 2010-06-22 17:33:06
   ```
   ```
   [~NPE2] display vrrp interface gigabitethernet0/1/1.1
   ```
   ```
   GigabitEthernet0/1/1.1 | Virtual Router 10
   State                             : Backup
   Virtual IP                        : 10.1.1.1
   Master IP                         : 10.1.1.254
   Local IP                          : 10.1.1.253 
   PriorityRun                       : 100
   PriorityConfig                    : 100
   MasterPriority                    : 120
   Preempt                           : YES              Delay Time : 0s
   Hold Multiplier                   : 4
   TimerRun                          : 1s
   TimerConfig                       : 1s
   Auth Type                         : NONE
   Virtual MAC                       : 0000-5e00-0102
   Passive Mode      : NO
   Check TTL                         : YES
   Config Type                       : admin-vrrp
   Backup-forward    : disabled
   Config track link-bfd down-number : 2
   Track BFD                         : link1            Type: Link
   BFD-session State                 : UP
   Track BFD                         : link2            Type: Link
   BFD-session State                 : UP
   Track BFD                         : link3            Type: Link
   BFD-session State                 : UP
   Track BFD                         : link4            Type: Link
   BFD-session State                 : UP
   Track BFD                         : peer1            Type: Peer
   BFD-session State                 : UP
   Create Time                       : 2010-06-22 17:35:00
   Last Change Time                  : 2010-06-22 17:35:06
   ```
6. Verify the configuration.
   
   
   
   # Run the **shutdown** command on GE 0/1/1.100 of NPE1 to simulate a fault in the link between NPE1 and CE1.
   
   ```
   [~NPE1] interface gigabitethernet0/1/1.100
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.100] shutdown
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.100] commit
   ```
   ```
   [~NPE1-GigabitEthernet0/1/1.100] quit
   ```
   
   Run the **display bfd session all** command on NPE1. The command output shows that the link BFD session between NPE1 and CE1 goes Down.
   
   ```
   [~NPE1] display bfd session all
   ```
   ```
   (w): State in WTR 
   (*): State is invalid
   --------------------------------------------------------------------------------
   Local  Remote PeerIpAddr      State     Type        InterfaceName
   --------------------------------------------------------------------------------
   8192  8192   10.1.1.253      Up        S_AUTO_IF   GigabitEthernet0/1/1.1
   8193  0      10.100.1.1      Down      S_AUTO_IF   GigabitEthernet0/1/1.100
   8194  8193   10.101.1.1      Up        S_AUTO_IF   GigabitEthernet0/1/1.101
   8195  8194   10.102.1.1      Up        S_AUTO_IF   GigabitEthernet0/1/1.102
   8196  8195   10.103.1.1      Up        S_AUTO_IF   GigabitEthernet0/1/1.103
   --------------------------------------------------------------------------------
        Total UP/DOWN Session Number : 4/1 
   ```
   
   In this configuration example, if two or more link BFD sessions go Down, the mVRRP group rapidly performs a master/backup VRRP switchover.
   
   Because only one link BFD session went Down, the mVRRP group does not perform a master/backup VRRP switchover. Run the [**display vrrp brief**](cmdqueryname=display+vrrp+brief) command on each NPE.
   
   The command output on NPE1 is as follows:
   * In mVRRP group 10, the value of the **State** field is **Master** and the value of the **Type** field is **Admin**.
   * In service VRRP group 100, the value of the **State** field is **Initialize** and the value of the **Type** field is **Member**.
   * In other service VRRP groups, the value of the **State** field is **Master** and the value of the **Type** field is **Member**.
   ```
   [~NPE1] display vrrp brief
   ```
   ```
   Total:5     Master:4    Backup:0    Non-active:1    
   VRID   State       Interface         Type    Virtual IP      Master IP       Local IP
   ```
   ```
   10     Master     GE0/1/1.1        Admin   10.1.1.1        10.1.1.254 24    10.1.1.254 24
   100    Initialize      GE0/1/1.100  Normal  10.100.1.200    -               10.100.1.254 24
   101    Master      GE0/1/1.101      Normal  10.101.1.200    10.101.1.254 24  10.101.1.254 24
   102    Master      GE0/1/1.102      Normal  10.102.1.200    10.102.1.253 24  10.102.1.253 24
   103    Master      GE0/1/1.103      Normal  10.103.1.200    10.103.1.254 24  10.103.1.254 24
   ```
   The command output on NPE2 is as follows:
   * In mVRRP group 10, the value of the **State** field is **Backup** and the value of the **Type** field is **Admin**.
   * In each service VRRP group, the value of the **State** field is **Backup** and the value of the **Type** field is **Member**.
   ```
   [~NPE2] display vrrp brief
   ```
   ```
   Total:5     Master:0    Backup:5    Non-active:0    
   ```
   ```
   VRID   State       Interface        Type    Virtual IP     Master IP       Local IP
   --------------------------------------------------------------------------------------------------
   10     Backup     GE0/1/1.1        Admin   10.1.1.1      10.1.1.254 24    10.1.1.253 24
   100    Backup      GE0/1/1.100      Normal  10.100.1.200  10.100.1.254 24  10.100.1.253 24
   101    Backup      GE0/1/1.101      Normal  10.101.1.200  10.101.1.254 24  10.101.1.253 24
   102    Backup      GE0/1/1.102      Normal  10.102.1.200  10.102.1.254 24  10.102.1.253 24
   103    Backup      GE0/1/1.103      Normal  10.103.1.200  10.103.1.254 24  10.103.1.253 24
   ```
   
   Run the **shutdown** command on GE 0/1/1.101 of NPE1 to simulate a fault in the link between NPE1 and CE2.
   
   ```
   [~NPE1] interface gigabitethernet0/1/1.101
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.101] shutdown
   ```
   ```
   [*NPE1-GigabitEthernet0/1/1.101] commit
   ```
   ```
   [~NPE1-GigabitEthernet0/1/1.101] quit
   ```
   
   Run the **display bfd session all** command on NPE1. The command output shows that the link BFD session between NPE1 and CE2 goes Down.
   
   ```
   [~NPE1] display bfd session all
   ```
   ```
   (w): State in WTR 
   (*): State is invalid
   --------------------------------------------------------------------------------
   Local  Remote PeerIpAddr      State     Type      InterfaceName
   --------------------------------------------------------------------------------
   8192  8192   10.1.1.253      Up        S_AUTO_IF   GigabitEthernet0/1/1.1       
   8193  0      10.100.1.1      Down      S_AUTO_IF   GigabitEthernet0/1/1.100     
   8194  0      10.101.1.1      Down      S_AUTO_IF   GigabitEthernet0/1/1.101     
   8195  8194   10.102.1.1      Up        S_AUTO_IF   GigabitEthernet0/1/1.102     
   8196  8195   10.103.1.1      Up        S_AUTO_IF   GigabitEthernet0/1/1.103
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
   ```
   ```
   Total:5     Master:0    Backup:0    Non-active:5    
   VRID   State       Interface         Type    Virtual IP        Master IP       Local IP
   -----------------------------------------------------------------------------------------
   10     Initialize  GE0/1/1.1         Admin   10.1.1.1        -              10.1.1.254 24
   100    Initialize  GE0/1/1.100       Member  10.100.1.200    -              10.100.1.254 24
   101    Initialize  GE0/1/1.101       Member  10.101.1.200    -              10.101.1.254 24
   102    Initialize  GE0/1/1.102       Member  10.102.1.200    -               10.102.1.254 24
   103    Initialize  GE0/1/1.103       Member  10.103.1.200    -               10.103.1.254 24
   ```
   The command output on NPE2 is as follows:
   * In mVRRP group 10, the value of the **State** field is **Master** and the value of the **Type** field is **Admin**.
   * In each service VRRP group, the value of the **State** field is **Master** and the value of the **Type** field is **Member**.
   ```
   [~NPE2] display vrrp brief
   ```
   ```
   Total:5     Master:5    Backup:0    Non-active:0    
   VRID   State       Interface         Type    Virtual IP     Master IP       Local IP
   --------------------------------------------------------------------------------------------
   10     Master      GE0/1/1.1         Admin   10.1.1.1    10.1.1.253 24     10.1.1.253 24
   100    Master      GE0/1/1.100       Member  10.100.1.200 10.100.1.253 24   10.100.1.253 24
   101    Master      GE0/1/1.101       Member  10.101.1.200 10.101.1.253 24   10.101.1.253 24
   102    Master      GE0/1/1.102       Member  10.102.1.200 10.102.1.253 24   10.102.1.253 24
   103    Master      GE0/1/1.103       Member  10.103.1.200 10.102.1.253 24   10.102.1.253 24
   ```
   
   Run the **undo shutdown** command on GE 0/1/1.100 and GE 0/1/1.101 of NPE1 to simulate fault recovery between NPE1 and CE1 and between NPE1 and CE2.
   
   The command output shows that the link BFD session between NPE1 and each CE goes Up. Run the **display bfd session all** command on NPE1.
   
   ```
   [~NPE1] display bfd session all
   ```
   ```
   (w): State in WTR 
   (*): State is invalid
   --------------------------------------------------------------------------------
   Local  Remote PeerIpAddr      State     Type        InterfaceName
   --------------------------------------------------------------------------------
   8192  8192   10.1.1.253      Up        S_AUTO_IF   GigabitEthernet0/1/1.1
   8193  8192   10.100.1.1      Up        S_AUTO_IF   GigabitEthernet0/1/1.100
   8194  8193   10.101.1.1      Up        S_AUTO_IF   GigabitEthernet0/1/1.101
   8195  8194   10.102.1.1      Up        S_AUTO_IF   GigabitEthernet0/1/1.102
   8196  8195   10.103.1.1      Up        S_AUTO_IF   GigabitEthernet0/1/1.103
   --------------------------------------------------------------------------------
   Total UP/DOWN Session Number : 5/0
   ```
   
   The VRRP status on the NPE is restored.
   
   The command output on NPE1 is as follows:
   * In mVRRP group 10, the value of the **State** field is **Master** and the value of the **Type** field is **Admin**.
   * In each service VRRP group, the value of the **State** field is **Master** and the value of the **Type** field is **Member**.
   ```
   [~NPE1] display vrrp brief
   ```
   The command output on NPE2 is as follows:
   * In mVRRP group 10, the value of the **State** field is **Backup** and the value of the **Type** field is **Admin**.
   * In each service VRRP group, the value of the **State** field is **Backup** and the value of the **Type** field is **Member**.
   ```
   [~NPE2] display vrrp brief
   ```
   ```
   Total:5     Master:0    Backup:5    Non-active:0  
   VRID   State       Interface        Type    Virtual IP     Master IP       Local IP
   --------------------------------------------------------------------------------------------------
   10     Backup     GE0/1/1.1        Admin   10.1.1.1      10.1.1.254 24    10.1.1.253 24
   100    Backup      GE0/1/1.100      Normal  10.100.1.200  10.100.1.254 24  10.100.1.253 24
   101    Backup      GE0/1/1.101      Normal  10.101.1.200  10.101.1.254 24  10.101.1.253 24
   102    Backup      GE0/1/1.102      Normal  10.102.1.200  10.102.1.254 24  10.102.1.253 24
   103    Backup      GE0/1/1.103      Normal  10.103.1.200  10.103.1.254 24  10.103.1.253 24
   ```

#### Configuration Files

* NPE1 configuration file
  
  ```
  #
  sysname NPE1
  #
  bfd
  #
  interface GigabitEthernet0/1/1
   undo shutdown
  #
  interface GigabitEthernet0/1/1.1
   encapsulation qinq-termination
   control-vid 1 qinq-termination
   qinq termination pe-vid 10 ce-vid 1 to 100
   qinq vrrp pe-vid 10 ce-vid 100
   ip address 10.1.1.254 255.255.255.0
   vrrp vrid 10 virtual-ip 10.1.1.1
   admin-vrrp vrid 10
   vrrp vrid 10 priority 120
   vrrp vrid 10 track bfd-session session-name link1 link
   vrrp vrid 10 track bfd-session session-name link2 link
   vrrp vrid 10 track bfd-session session-name link3 link
   vrrp vrid 10 track bfd-session session-name link4 link
   vrrp vrid 10 track bfd-session session-name peer1 peer
   
   vrrp vrid 10 track link-bfd down-number 2
   
   arp broadcast enable
  #
  interface GigabitEthernet0/1/1.100
   encapsulation qinq-termination
   control-vid 100 qinq-termination
   qinq termination pe-vid 10 ce-vid 101 to 200
   qinq vrrp pe-vid 10 ce-vid 101
   ip address 10.100.1.254 255.255.255.0
   vrrp vrid 100 virtual-ip 10.100.1.200
   vrrp vrid 100 track admin-vrrp interface GigabitEthernet0/1/1.1 vrid 10 unflowdown
   arp broadcast enable
  #
  interface GigabitEthernet0/1/1.101
   encapsulation qinq-termination
   control-vid 101 qinq-termination
   qinq termination pe-vid 10 ce-vid 201 to 300
   qinq vrrp pe-vid 10 ce-vid 201
   ip address 10.101.1.254 255.255.255.0
   vrrp vrid 101 virtual-ip 10.101.1.200
   vrrp vrid 101 track admin-vrrp interface GigabitEthernet0/1/1.1 vrid 10 unflowdown
   arp broadcast enable
  #
  interface GigabitEthernet0/1/1.102
   encapsulation qinq-termination
   control-vid 102 qinq-termination
   qinq termination pe-vid 10 ce-vid 301 to 400
   qinq vrrp pe-vid 10 ce-vid 301
   ip address 10.102.1.254 255.255.255.0
   vrrp vrid 102 virtual-ip 10.102.1.200
   vrrp vrid 102 track admin-vrrp interface GigabitEthernet0/1/1.1 vrid 10 unflowdown
   arp broadcast enable
  #
  interface GigabitEthernet0/1/1.103
   encapsulation qinq-termination
   control-vid 103 qinq-termination
   qinq termination pe-vid 10 ce-vid 401 to 500
   qinq vrrp pe-vid 10 ce-vid 401
   ip address 10.103.1.254 255.255.255.0
   vrrp vrid 103 virtual-ip 10.103.1.200
   vrrp vrid 103 track admin-vrrp interface GigabitEthernet0/1/1.1 vrid 10 unflowdown
   arp broadcast enable
  #
  bfd link1 bind peer-ip 10.100.1.1 interface GigabitEthernet0/1/1.100 source-ip 10.100.1.254 auto
  #
  bfd link2 bind peer-ip 10.101.1.1 interface GigabitEthernet0/1/1.101 source-ip 10.101.1.254 auto
  #
  bfd link3 bind peer-ip 10.102.1.1 interface GigabitEthernet0/1/1.102 source-ip 10.102.1.254 auto
  #
  bfd link4 bind peer-ip 10.103.1.1 interface GigabitEthernet0/1/1.103 source-ip 10.103.1.254 auto
  #
  bfd peer1 bind peer-ip 10.1.1.253 interface GigabitEthernet0/1/1.1 source-ip 10.1.1.254 auto
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
  interface GigabitEthernet0/1/1
   undo shutdown
  #
  interface GigabitEthernet0/1/1.1
   encapsulation qinq-termination
   control-vid 1 qinq-termination
   qinq termination pe-vid 10 ce-vid 1 to 100
   qinq vrrp pe-vid 10 ce-vid 100
   ip address 10.1.1.253 255.255.255.0
   vrrp vrid 10 virtual-ip 10.1.1.1
   admin-vrrp vrid 10
   vrrp vrid 10 track bfd-session session-name link1 link
   vrrp vrid 10 track bfd-session session-name link2 link
   vrrp vrid 10 track bfd-session session-name link3 link
   vrrp vrid 10 track bfd-session session-name link4 link
   vrrp vrid 10 track bfd-session session-name peer1 peer
   vrrp vrid 10 track link-bfd down-number 2
   arp broadcast enable
  #
  interface GigabitEthernet0/1/1.100
   encapsulation qinq-termination
   control-vid 100 qinq-termination
   qinq termination pe-vid 10 ce-vid 101 to 200
   qinq vrrp pe-vid 10 ce-vid 101
   ip address 10.100.1.253 255.255.255.0
   vrrp vrid 100 virtual-ip 10.100.1.200
   vrrp vrid 100 track admin-vrrp interface GigabitEthernet0/1/1.1 vrid 10 unflowdown
   arp broadcast enable
  #
  interface GigabitEthernet0/1/1.101
   encapsulation qinq-termination
   control-vid 101 qinq-termination
   qinq termination pe-vid 10 ce-vid 201 to 300
   qinq vrrp pe-vid 10 ce-vid 201
   ip address 10.101.1.253 255.255.255.0
   vrrp vrid 101 virtual-ip 10.101.1.200
   vrrp vrid 101 track admin-vrrp interface GigabitEthernet0/1/1.1 vrid 10 unflowdown
   arp broadcast enable
  #
  interface GigabitEthernet0/1/1.102
   encapsulation qinq-termination
   control-vid 102 qinq-termination
   qinq termination pe-vid 10 ce-vid 301 to 400
   qinq vrrp pe-vid 10 ce-vid 301
   ip address 10.102.1.253 255.255.255.0
   vrrp vrid 102 virtual-ip 10.102.1.200
   vrrp vrid 102 track admin-vrrp interface GigabitEthernet0/1/1.1 vrid 10 unflowdown
   arp broadcast enable
  #
  interface GigabitEthernet0/1/1.103
   encapsulation qinq-termination
   control-vid 103 qinq-termination
   qinq termination pe-vid 10 ce-vid 401 to 500
   qinq vrrp pe-vid 10 ce-vid 401
   ip address 10.103.1.253 255.255.255.0
   vrrp vrid 103 virtual-ip 10.103.1.200
   vrrp vrid 103 track admin-vrrp interface GigabitEthernet0/1/1.1 vrid 10 unflowdown
   arp broadcast enable
  #
  bfd link1 bind peer-ip 10.100.1.1 interface GigabitEthernet0/1/1.100 source-ip 10.100.1.253 auto
  #
  bfd link2 bind peer-ip 10.101.1.1 interface GigabitEthernet0/1/1.101 source-ip 10.101.1.253 auto
  #
  bfd link3 bind peer-ip 10.102.1.1 interface GigabitEthernet0/1/1.102 source-ip 10.102.1.253 auto
  #
  bfd link4 bind peer-ip 10.103.1.1 interface GigabitEthernet0/1/1.103 source-ip 10.103.1.253 auto
  #
  bfd peer1 bind peer-ip 10.1.1.254 interface GigabitEthernet0/1/1.1 source-ip 10.1.1.253 auto
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
    peer 4.4.4.4
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
    peer 3.3.3.3
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
  #
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
  interface GigabitEthernet0/1/3
   undo shutdown
  #
  interface GigabitEthernet0/1/3.1
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
  interface LoopBack1
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
   encapsulation qinq-termination
   qinq termination pe-vid 10 ce-vid 110
   ip address 10.100.1.1 255.255.255.0
   arp broadcast enable
  #
  interface GigabitEthernet0/1/1.101
   encapsulation qinq-termination
   qinq termination pe-vid 10 ce-vid 210
   ip address 10.101.1.1 255.255.255.0
   arp broadcast enable
  #
  interface GigabitEthernet0/1/1.102
   encapsulation qinq-termination
   qinq termination pe-vid 10 ce-vid 310
   ip address 10.102.1.1 255.255.255.0
   arp broadcast enable
  #
  interface GigabitEthernet0/1/1.103
   encapsulation qinq-termination
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
Example for Configuring MLD Based on QinQ Termination
=====================================================

This section provides an example for configuring MLD based on QinQ termination.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172368012__fig_dc_vrp_l2mc_cfg_003401), Device A is connected to Device B and Switch A.

Host 1 and Host 2 are connected to Device A through Switch A. An MLD message sent from Switch A to Device A carries double VLAN tags and is transmitted to the multicast network through a QinQ VLAN tag termination sub-interface.

After MLD is enabled on Device A's GE 0/1/0, Host 1 and Host 2 can obtain traffic sent by the multicast source.

**Figure 1** Configuring MLD based on QinQ termination![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/0 and GE 0/1/1, respectively.


  
![](images/fig_dc_vrp_l2mc_cfg_qinq_snooping.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable IPv6 multicast on Device A.
2. Enable IPv6 PIM-SM on Device A's GE 0/1/1.
3. Configure QinQ termination on Device A's GE 0/1/0.1, and enable IPv6 PIM-SM and MLD on the sub-interface.

#### Data Preparation

To complete the configuration, you need the following data:

* VLAN tags on the sub-interface for QinQ VLAN tag termination on DeviceA (containing the two Layer 2 VLAN tags 1 and 2 used by switch A to access DeviceA)

#### Procedure

1. Enable IPv6 multicast on Device A.
   
   
   ```
   <~HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceA
   ```
   ```
   [~HUAWEI] commit
   ```
   ```
   [~DeviceA] multicast ipv6 routing-enable 
   ```
   ```
   [*DeviceA] commit
   ```
2. Configure an IPv6 address for Device A's GE 0/1/1 and enable IPv6 PIM-SM.
   
   
   ```
   [~DeviceA] interface GigabitEthernet0/1/1
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1] ipv6 enable
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] ipv6 address 2001:db8:6::1/64
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] pim ipv6 sm
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1] quit
   ```
3. Configure QinQ termination on Device A's GE 0/1/0.1, and enable IPv6 PIM-SM and MLD on the sub-interface.
   
   
   ```
   [~DeviceA] interface GigabitEthernet0/1/0.1
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0.1] encapsulation qinq-termination
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0.1] qinq termination pe-vid 1 to 4 ce-vid 1 to 4
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0.1] ipv6 enable
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0.1] ipv6 address 2001:db8:7::2/64
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0.1] pim ipv6 sm
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0.1] commit
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0.1] quit
   ```
4. Verify the configuration.
   
   
   
   # Run the **display pim ipv6 routing-table** command on Device A. The command output shows that multicast traffic for MLD based on QinQ termination is normally sent.
   
   ```
   VPN-Instance: public net
     Total 1 (*, G) entry; 1 (S, G) entry
      (*, FF17::1)
         RP: NULL
         Protocol: pim-sm, Flag: WC NIIF 
         UpTime: 00:00:33
        Upstream interface: NULL, Refresh time: 00:00:33
            Upstream neighbor: NULL
             RPF prime neighbor: NULL
         Downstream interface(s) information:
         Total number of downstreams: 1
            1:GigabitEthernet0/1/0.1
                 Protocol: mld, UpTime: 00:00:33, Expires: -
      (2001:db8:5::1, FF17::1)
         RP: NULL
         Protocol: pim-sm, Flag: SPT LOC ACT 
         UpTime: 00:00:22
        Upstream interface: GigabitEthernet0/1/1, Refresh time: 00:00:22
            Upstream neighbor: NULL
             RPF prime neighbor: NULL
         Downstream interface(s) information:
         Total number of downstreams: 1
            1:GigabitEthernet0/1/0.1
                 Protocol: pim-sm, UpTime: 00:00:22, Expires: -
   ```

#### Configuration Files

* Device A configuration file
  
  ```
  #
  sysname DeviceA
  #
   multicast ipv6 routing-enable
   #
   interface GigabitEthernet0/1/0
    undo shutdown
   #
   interface GigabitEthernet0/1/0.1
    ipv6 enable
    ipv6 address 2001:db8:7::2/64
    encapsulation qinq-termination
    qinq termination pe-vid 1 to 4 ce-vid 1 to 4
    pim ipv6 sm
    mld enable
   #
   interface GigabitEthernet0/1/1
    undo shutdown
    ipv6 enable
    ipv6 address 2001:db8:6::1/64
    pim ipv6 sm
   #
   ipv6 route-static 2001:db8:5:: 64  2001:db8:6::2
   #
   return
  ```
Example for Configuring a MAC Address Learning Limit Rule in a VSI
==================================================================

Configuring a MAC address learning limit rule for a Virtual Switching Instance (VSI) can control the number of access users in the VSI. When the number of MAC addresses learned in this VSI reaches the maximum number, no new MAC addresses can be learned. You can also configure the system to discard packets to defend against MAC address attacks and therefore improve network security.

#### Networking Requirements

Networks with poor security management, such as community networks, are vulnerable to hackers' MAC address attacks. The capacity of a MAC address table is limited. When hackers forge a large number of packets with different source MAC addresses and send the packets to a device, the MAC address table of the device will be filled up. Even if the device can receive valid packets, it cannot learn the source MAC addresses of the packets.

As shown in [Figure 1](#EN-US_TASK_0172362758__fig_dc_vrp_mac_cfg_002001), user network 1 accesses the VPLS network through S1, and user network 2 accesses the VPLS network through S2. A VSI named huawei is created on the VPLS network. A MAC address learning limit rule is configured for the VSI to control the number of users in this VSI and defend against MAC address attacks.

**Figure 1** Networking for configuring a MAC address learning limit rule in a VSI  
![](figure/en-us_image_0000001671749649.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create a VSI.
2. Configure a MAC address learning limit rule for the VSI.

#### Data Preparation

To complete the configuration, you need the following data:

* VSI name
* Maximum number of MAC addresses that can be learned

#### Procedure

1. Create a VSI.
   
   
   
   # Create a VSI named huawei.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname PE1
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~PE1] vsi huawei static
   ```
2. Configure a MAC address learning limit rule for the VSI.
   
   
   
   # Configure a MAC address learning limit rule for the VSI: A maximum of 300 MAC addresses can be learned; the packets received after the maximum number of MAC addresses have been learned are immediately discarded.
   
   ```
   [*PE1-vsi-huawei] mac-limit maximum 300 rate 100 action discard
   ```
   ```
   [*PE1-vsi-huawei] commit
   ```
   ```
   [~PE1-vsi-huawei] quit
   ```
3. Verify the configuration.
   
   
   
   Run the [**display mac-limit**](cmdqueryname=display+mac-limit) command in any view to check whether the MAC address learning limit rule is configured successfully.
   
   ```
   [*PE1] display mac-limit
   ```
   ```
   MAC limit is enabled
   Total MAC limit rule count : 1
   
   PORT                   VLAN/BD/VSI/EVPN      SLOT Maximum Rate(ms) Action  Alarm
   ----------------------------------------------------------------------------
   -                      huawei                -    300     100      discard disable
   ```

#### Configuration Files

```
#
sysname PE1
#
vsi huawei static
 mac-limit maximum 300 rate 100 action discard
#  
return
```
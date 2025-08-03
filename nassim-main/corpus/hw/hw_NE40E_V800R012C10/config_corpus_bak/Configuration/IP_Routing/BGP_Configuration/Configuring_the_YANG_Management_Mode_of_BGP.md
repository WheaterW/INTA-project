Configuring the YANG Management Mode of BGP
===========================================

In YANG management mode of BGP, BGP instance configurations can be delivered using the YANG model.

#### Usage Scenario

To manage BGP configurations using NETCONF YANG, you need to configure the YANG management mode of BGP on the device first. Alternatively, you can enable the leaf node (XPath: /bgp:bgp/bgp:global/bgp:yang-enable) globally through the YANG model file. This section describes the configuration on the device.


#### Procedure

1. Run the **system-view** command to enter the system view.
2. Run the **bgp yang-mode enable** command to configure the YANG management mode of the BGP VPN instance.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Running the **bgp yang-mode enable** command changes the configurations of BGP VPN instances and corresponding peers (and peer groups). For example:
   
   Example 1 (including part 1 and part 2):
   
   Part 1: For example, before the **bgp yang-mode enable** command is run, the configurations on the device are as follows:
   
   ```
   [~HUAWEI-bgp]display this 
   #
   bgp 100
    #
    ipv4-family unicast
     undo synchronization
    #
    ipv4-family vpn-instance abc
     peer 3.3.3.4 as-number 100
    #
    ipv4-family vpn-instance vrf1
     group a internal
     peer 1.1.1.1 as-number 100
     peer 1.1.1.1 group a 
   ```
   
   Part 2: After the **bgp yang-mode enable** command is run, the configurations on the device are changed as follows:
   
   ```
   [~HUAWEI-bgp]display this 
   # 
   bgp 100 
    # 
    ipv4-family unicast 
     undo synchronization
    # 
    vpn-instance abc //A BGP-VPN instance is added.
     peer 3.3.3.4 as-number 100   //The VPN instance-level command configuration in the BGP-VPN instance IPv4 address family view is migrated to the new BGP-VPN instance view.
    #
    ipv4-family vpn-instance abc
     peer 3.3.3.4 enable  //The address-family level command is added to the BGP-VPN instance IPv4 address family view.
    #
    vpn-instance vrf1
     group a internal //The VPN instance-level command configuration in the BGP-VPN instance IPv4 address family view is migrated to the new BGP-VPN instance view.
     peer 1.1.1.1 as-number 100 //The VPN instance-level command configuration in the BGP-VPN instance IPv4 address family view is migrated to the new BGP-VPN instance view.
     peer 1.1.1.1 group a //The VPN instance-level command configuration in the BGP-VPN instance IPv4 address family view is migrated to the new BGP-VPN instance view.
    #
    ipv4-family vpn-instance vrf1
   peer a enable //The address-family level command is added to the BGP-VPN instance IPv4 address family view.
     peer 1.1.1.1 enable //The address-family level command is added to the BGP-VPN instance IPv4 address family view.
     peer 1.1.1.1 group a enable //The address-family level command is added to the BGP-VPN instance IPv4 address family view.
   ```
   * After the **bgp yang-mode enable** command is run, the configurations shown in part 1 of example 1 cannot be performed.
   * After the **bgp yang-mode enable** command is run, if a BGP-VPN instance is deleted, all the configurations in the instance are deleted accordingly.
   
   Example 2: Example 2 is based on example 1. In this example, peer groups of the same name and in the same BGP VPN instance are changed.
   
   Before the **bgp yang-mode enable** command is run, the configurations on a deviceare as follows:
   
   ```
   [~HUAWEI-bgp]display this 
   # 
   bgp 100 
    # 
    ipv4-family unicast 
     undo synchronization 
    # 
    ipv4-family vpn-instance vrf1 
     group ML internal 
     peer ML password simple 11 
    # 
    ipv6-family vpn-instance vrf1 
     group ML internal 
     peer ML connect-interface LoopBack1
   ```
   
   After the **bgp yang-mode enable** command is run, the configurations on the device are changed as follows:
   
   ```
   [~HUAWEI-bgp]display this  
   # 
   bgp 100 
    # 
    ipv4-family unicast 
     undo synchronization 
    # 
    vpn-instance vrf1 
     group ML internal               
     peer ML password simple 11         
     group ML2019531105624 internal     //In this example, the name of the peer group changes from ML to ML2019531105624.
     peer ML2019531105624 connect-interface LoopBack1     //In this example, the name of the peer group changes from ML to ML2019531105624. 
    # 
    ipv4-family vpn-instance vrf1 
     peer ML enable 
    #  
    ipv6-family vpn-instance vrf1 
     peer ML2019531105624 enable
     
   ```
3. Run the **commit** command to commit the configuration.
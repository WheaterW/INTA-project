Example for Configuring Adaptive Routing
========================================

Example for Configuring Adaptive Routing

#### Networking Requirements

In the dragonfly topology shown in [Figure 1](#EN-US_TASK_0000001512830854__fig1562517576313), adaptive routing is enabled to improve network throughput and resilience and reduce network latency.

There are three groups in this dragonfly topology. Each group has five network nodes, each of which is connected to two compute nodes, to the other four network nodes in the group, and to the network nodes in the other two groups.

**Figure 1** Network diagram of adaptive routing in a dragonfly topology![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, interface3, interface4, interface5, and interface6 represent 100GE1/0/1, 100GE1/0/2, 100GE1/0/3, 100GE1/0/4, 100GE1/0/5, and 100GE1/0/6, respectively.


  
![](figure/en-us_image_0000001513150438.png)

**Table 1** Interface address table (The configurations of all devices are similar. DeviceA1 is used as an example, and only the interfaces and addresses related to DeviceA1 are listed. For the local port configurations, the local ports connecting DeviceA1, DeviceA2, and DeviceA3 in GroupA are used as an example.)
| Device | Interface Role | Interface Name | IP Address |
| --- | --- | --- | --- |
| DeviceA1 | Layer 3 sub-interface of the global port connected to DeviceB1 | 100GE1/0/1.104 | 172.16.1.1/24 |
| Layer 3 sub-interface of the global port connected to DeviceC1 | 100GE1/0/2.107 | 172.17.1.1/24 |
| Min sub-interface of the local port connected to DeviceA2 | 100GE1/0/3.102 | 10.12.1.1/24 |
| Non-min sub-interface of the local port connected to DeviceA2 | 100GE1/0/3.1020 | 10.12.2.1/24 |
| Min sub-interface of the local port connected to DeviceA3 | 100GE1/0/4.103 | 10.13.1.1/24 |
| Non-min sub-interface of the local port connected to DeviceA3 | 100GE1/0/4.1030 | 10.13.2.1/24 |
| access port | 100GE1/0/5 | 192.168.11.1/24 |
| access port | 100GE1/0/6 | 192.168.12.1/24 |
| Loopback interface | LoopBack0 | 1.1.1.1/32 |
| DeviceA2 | Min sub-interface of the local port connected to DeviceA1 | 100GE1/0/3.201 | 10.12.1.2/24 |
| Non-min sub-interface of the local port connected to DeviceA1 | 100GE1/0/3.2010 | 10.12.2.2/24 |
| DeviceA3 | Min sub-interface of the local port connected to DeviceA1 | 100GE1/0/3.301 | 10.13.1.3/24 |
| Non-min sub-interface of the local port connected to DeviceA1 | 100GE1/0/3.3010 | 10.13.2.3/24 |
| DeviceB1 | Layer 3 sub-interface of the global port connected to DeviceA1 | 100GE1/0/1.401 | 172.16.1.4/24 |
| DeviceC1 | Layer 3 sub-interface of the global port connected to DeviceA1 | 100GE1/0/1.701 | 172.17.1.7/24 |



#### Precautions

* The adaptive routing function can be configured only in the dragonfly topology and takes effect only when other devices in the topology are correctly configured.
* Routing policy parameters must be set by following the rule that the cost of a route within a group and between groups increments by 1 and 1000, respectively, each time the route is advertised to a new hop. In addition, you must correctly use the corresponding routing policy when configuring BGP routes and cannot modify other parameters except the policy name. If you change the policy name, you must also change the corresponding policy name used in the BGP route configuration.
* Devices in the same group must belong to the same AS, meaning they must have the same AS number. Devices in different groups must belong to different ASs, meaning they must have different AS numbers. The AS number ranges from 4200000000 to 4200000210.
* All devices on the network must be configured as RRs, and devices in the same group must have different RR cluster IDs.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure VPN instances and interfaces, including the Mix VPN instance, Non-min VPN instance, access port, local port, and global port.
2. Configure routing policies:
   * Policy for importing public network routes to the routing table of the Mix VPN instance
   * Policy for importing public network routes to the routing table of the Non-min VPN instance
   * Policy for importing routes from the Non-min VPN instance to the routing table of the Mix VPN instance
   * Policy for advertising EBGP routes of the public network instance
   * Policies for advertising and receiving IBGP routes of the public network instance
   * Policies for advertising and receiving IBGP routes of the Non-min VPN instance
3. Configure BGP route processing:
   * Configure the device to import direct routes in the Mix VPN instance to the public network routing table.
   * Configure route advertisement and reception for the public network instance.
   * Configure route import, advertisement, and reception for the Non-min VPN instance.
   * Configure route import for the Mix VPN instance.
   * Configure load balancing.
4. Configure adaptive routing. This includes configuring the dragonfly profile and enabling adaptive routing.


#### Procedure

1. Configure VPN instances and interfaces. The following uses DeviceA1 as an example. The configurations of other devices are similar to the configuration of DeviceA1, and are not provided here.
   
   
   
   # Configure a Mix VPN instance on DeviceA1.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA1
   [*HUAWEI] commit
   [~DeviceA1] ip vpn-instance mix_vrf
   [*DeviceA1-vpn-instance-mix_vrf] ipv4-family
   [*DeviceA1-vpn-instance-mix_vrf-af-ipv4] route-distinguisher 1:1
   [*DeviceA1-vpn-instance-mix_vrf-af-ipv4] quit
   [*DeviceA1-vpn-instance-mix_vrf] quit
   [*DeviceA1] commit
   ```
   
   # Configure a Non-min VPN instance on DeviceA1.
   
   ```
   [~DeviceA1] ip vpn-instance nonmin_vrf
   [*DeviceA1-vpn-instance-nonmin_vrf] ipv4-family
   [*DeviceA1-vpn-instance-nonmin_vrf-af-ipv4] route-distinguisher 2:1
   [*DeviceA1-vpn-instance-nonmin_vrf-af-ipv4] vpn-target 2:1 export-extcommunity
   [*DeviceA1-vpn-instance-nonmin_vrf-af-ipv4] vpn-target 2:1 import-extcommunity
   [*DeviceA1-vpn-instance-nonmin_vrf-af-ipv4] quit
   [*DeviceA1-vpn-instance-nonmin_vrf] quit
   [*DeviceA1] commit
   ```
   
   # Configure a global port on DeviceA1.
   
   ```
   [~DeviceA1] interface 100ge 1/0/1
   [*DeviceA1-100GE1/0/1] undo portswitch
   [*DeviceA1-100GE1/0/1] quit
   [*DeviceA1] commit
   [~DeviceA1] interface 100ge 1/0/1.104
   [*DeviceA1-100GE1/0/1.104] description min_port_of_global_link
   [*DeviceA1-100GE1/0/1.104] ip address 172.16.1.1 255.255.255.0
   [*DeviceA1-100GE1/0/1.104] dot1q termination vid 10
   [*DeviceA1-100GE1/0/1.104] quit
   [*DeviceA1] commit
   [~DeviceA1] interface 100ge 1/0/2
   [*DeviceA1-100GE1/0/2] undo portswitch
   [*DeviceA1-100GE1/0/2] quit
   [*DeviceA1] commit
   [~DeviceA1] interface 100ge 1/0/2.107
   [*DeviceA1-100GE1/0/2.107] description min_port_of_global_link
   [*DeviceA1-100GE1/0/2.107] ip address 172.17.1.1 255.255.255.0
   [*DeviceA1-100GE1/0/2.107] dot1q termination vid 10
   [*DeviceA1-100GE1/0/2.107] quit
   [*DeviceA1] commit
   ```
   
   # Configure a local port on DeviceA1.
   
   ```
   [~DeviceA1] interface 100ge 1/0/3
   [*DeviceA1-100GE1/0/3] undo portswitch
   [*DeviceA1-100GE1/0/3] quit
   [*DeviceA1] commit
   [~DeviceA1] interface 100ge 1/0/3.102
   [*DeviceA1-100GE1/0/3.102] description min_port_of_local_link
   [*DeviceA1-100GE1/0/3.102] ip address 10.12.1.1 255.255.255.0
   [*DeviceA1-100GE1/0/3.102] dot1q termination vid 10
   [*DeviceA1-100GE1/0/3.102] quit
   [*DeviceA1] commit
   [~DeviceA1] interface 100ge 1/0/3.1020
   [*DeviceA1-100GE1/0/3.1020] description nonmin_port_of_local_link
   [*DeviceA1-100GE1/0/3.1020] ip binding vpn-instance nonmin_vrf
   [*DeviceA1-100GE1/0/3.1020] ip address 10.12.2.1 255.255.255.0
   [*DeviceA1-100GE1/0/3.1020] dot1q termination vid 20
   [*DeviceA1-100GE1/0/3.1020] quit
   [*DeviceA1] commit
   [~DeviceA1] interface 100ge 1/0/4
   [*DeviceA1-100GE1/0/4] undo portswitch
   [*DeviceA1-100GE1/0/4] quit
   [*DeviceA1] commit
   [~DeviceA1] interface 100ge 1/0/4.103
   [*DeviceA1-100GE1/0/4.103] description min_port_of_local_link
   [*DeviceA1-100GE1/0/4.103] ip address 10.13.1.1 255.255.255.0
   [*DeviceA1-100GE1/0/4.103] dot1q termination vid 10
   [*DeviceA1-100GE1/0/4.103] quit
   [*DeviceA1] commit
   [~DeviceA1] interface 100ge 1/0/4.1030
   [*DeviceA1-100GE1/0/4.1030] description nonmin_port_of_local_link
   [*DeviceA1-100GE1/0/4.1030] ip binding vpn-instance nonmin_vrf
   [*DeviceA1-100GE1/0/4.1030] ip address 10.13.2.1 255.255.255.0
   [*DeviceA1-100GE1/0/4.1030] dot1q termination vid 20
   [*DeviceA1-100GE1/0/4.1030] quit
   [*DeviceA1] commit
   ```
   
   # Configure an access port on DeviceA1.
   
   ```
   [~DeviceA1] interface 100ge 1/0/5
   [*DeviceA1-100GE1/0/5] undo portswitch
   [*DeviceA1-100GE1/0/5] description access_port
   [*DeviceA1-100GE1/0/5] ip binding vpn-instance mix_vrf
   [*DeviceA1-100GE1/0/5] ip address 192.168.11.1 255.255.255.0
   [*DeviceA1-100GE1/0/5] quit
   [*DeviceA1] commit
   [~DeviceA1] interface 100ge 1/0/6
   [*DeviceA1-100GE1/0/6] undo portswitch
   [*DeviceA1-100GE1/0/6] description access_port
   [*DeviceA1-100GE1/0/6] ip binding vpn-instance mix_vrf
   [*DeviceA1-100GE1/0/6] ip address 192.168.12.1 255.255.255.0
   [*DeviceA1-100GE1/0/6] quit
   [*DeviceA1] commit
   ```
   
   # Configure a loopback interface on DeviceA1.
   
   ```
   [~DeviceA1] interface loopback 0
   [*DeviceA1-LoopBack0] ip binding vpn-instance mix_vrf
   [*DeviceA1-LoopBack0] ip address 1.1.1.1 255.255.255.255
   [*DeviceA1-LoopBack0] quit
   [*DeviceA1] commit
   ```
2. Configure routing policies.
   
   
   
   # On DeviceA1, configure a policy named **rp\_importrib\_min2mix** to import public network routes to the routing table of the Mix VPN instance.
   
   ```
   [~DeviceA1] route-policy rp_importrib_min2mix deny node 5
   [*DeviceA1-route-policy] if-match cost 2
   [*DeviceA1-route-policy] quit
   [*DeviceA1] route-policy rp_importrib_min2mix permit node 10
   [*DeviceA1-route-policy] if-match cost greater-equal 1 less-equal 2999
   [*DeviceA1-route-policy] quit
   ```
   
   # On DeviceA1, configure a policy named **rp\_importrib\_min2nonmin** to import public network routes to the routing table of the Non-min VPN instance.
   
   ```
   [*DeviceA1] route-policy rp_importrib_min2nonmin permit node 5
   [*DeviceA1-route-policy] if-match cost 1
   [*DeviceA1-route-policy] quit
   [*DeviceA1] route-policy rp_importrib_min2nonmin permit node 10
   [*DeviceA1-route-policy] if-match cost greater-equal 2000 less-equal 2999
   [*DeviceA1-route-policy] quit
   ```
   
   #On DeviceA1, configure a policy named **rp\_importrib\_nonmin2mix** to import routes from the Non-min VPN instance to the routing table of the Mix VPN instance.
   
   ```
   [*DeviceA1] route-policy rp_importrib_nonmin2mix permit node 5
   [*DeviceA1-route-policy] if-match cost greater-equal 2000 less-equal 2999
   [*DeviceA1-route-policy] quit
   [*DeviceA1] route-policy rp_importrib_nonmin2mix permit node 10
   [*DeviceA1-route-policy] if-match cost greater-equal 2 less-equal 999
   [*DeviceA1-route-policy] quit
   ```
   
   # On DeviceA1, configure a policy named **rp\_minvrf\_ebgp\_export** to advertise the EBGP routes of the public network instance.
   
   ```
   [*DeviceA1] route-policy rp_minvrf_ebgp_export deny node 5
   [*DeviceA1-route-policy] if-match cost greater-equal 2000 less-equal 4294967295
   [*DeviceA1-route-policy] quit
   [*DeviceA1] route-policy rp_minvrf_ebgp_export permit node 10
   [*DeviceA1-route-policy] if-match cost greater-equal 0 less-equal 1999
   [*DeviceA1-route-policy] apply cost + 1000
   [*DeviceA1-route-policy] quit
   ```
   
   # On DeviceA1, configure a policy named **rp\_minvrf\_ibgp\_export** to advertise the IBGP routes of the public network instance.
   
   ```
   [*DeviceA1] route-policy rp_minvrf_ibgp_export deny node 5
   [*DeviceA1-route-policy] if-match cost 2
   [*DeviceA1-route-policy] quit
   [*DeviceA1] route-policy rp_minvrf_ibgp_export deny node 10
   [*DeviceA1-route-policy] if-match cost greater-equal 2000 less-equal 4294967295
   [*DeviceA1-route-policy] if-match route-type ibgp
   [*DeviceA1-route-policy] quit
   [*DeviceA1] route-policy rp_minvrf_ibgp_export permit node 15
   [*DeviceA1-route-policy] if-match cost greater-equal 0 less-equal 1999
   [*DeviceA1-route-policy] apply cost + 1
   [*DeviceA1-route-policy] quit
   ```
   
   # On DeviceA1, configure a policy named **rp\_minvrf\_ibgp\_import** to receive the IBGP routes of the public network instance.
   
   ```
   [*DeviceA1] route-policy rp_minvrf_ibgp_import permit node 5
   [*DeviceA1-route-policy] apply ip-address next-hop peer-address
   [*DeviceA1-route-policy] quit
   ```
   
   # On DeviceA1, configure a policy named **rp\_nonmin\_vrf\_ibgp\_export** to advertise the IBGP routes of the Non-min VPN instance.
   
   ```
   [*DeviceA1] route-policy rp_nonmin_vrf_ibgp_export deny node 5
   [*DeviceA1-route-policy] if-match cost 2
   [*DeviceA1-route-policy] quit
   [*DeviceA1] route-policy rp_nonmin_vrf_ibgp_export permit node 10
   [*DeviceA1-route-policy] if-match cost greater-equal 2000 less-equal 2999
   [*DeviceA1-route-policy] if-match route-type ebgp
   [*DeviceA1-route-policy] apply cost + 1
   [*DeviceA1-route-policy] quit
   [*DeviceA1] route-policy rp_nonmin_vrf_ibgp_export permit node 15
   [*DeviceA1-route-policy] if-match cost 1
   [*DeviceA1-route-policy] if-match route-type ibgp
   [*DeviceA1-route-policy] apply cost + 1
   [*DeviceA1-route-policy] quit
   ```
   
   # On DeviceA1, configure a policy named **rp\_nonmin\_vrf\_ibgp\_import** to receive the IBGP routes of the Non-min VPN instance.
   
   ```
   [*DeviceA1] route-policy rp_nonmin_vrf_ibgp_import permit node 5
   [*DeviceA1-route-policy] apply ip-address next-hop peer-address
   [*DeviceA1-route-policy] quit
   [*DeviceA1] commit
   ```
3. Configure BGP route processing.
   
   
   
   # Configure DeviceA1 to import direct routes in the Mix VPN instance to the public network routing table.
   
   ```
   [~DeviceA1] ip import-rib vpn-instance mix_vrf protocol direct
   ```
   
   # Configure routes for the public network instance on DeviceA1.
   
   ```
   [*DeviceA1] bgp 4200000001
   [*DeviceA1-bgp] router-id 1.1.1.1
   [*DeviceA1-bgp] group minvrf_ebgp_group external
   [*DeviceA1-bgp] peer 172.16.1.4 as-number 4200000002
   [*DeviceA1-bgp] peer 172.16.1.4 group minvrf_ebgp_group 
   [*DeviceA1-bgp] peer 172.17.1.7 as-number 4200000003
   [*DeviceA1-bgp] peer 172.17.1.7 group minvrf_ebgp_group
   [*DeviceA1-bgp] group minvrf_ibgp_group internal
   [*DeviceA1-bgp] peer 10.12.1.2 as-number 4200000001
   [*DeviceA1-bgp] peer 10.12.1.2 group minvrf_ibgp_group
   [*DeviceA1-bgp] peer 10.13.1.3 as-number 4200000001
   [*DeviceA1-bgp] peer 10.13.1.3 group minvrf_ibgp_group
   [*DeviceA1-bgp] commit
   [~DeviceA1-bgp] ipv4-family unicast
   [*DeviceA1-bgp-af-ipv4] maximum load-balancing 128
   [*DeviceA1-bgp-af-ipv4] reflector cluster-id 1
   [*DeviceA1-bgp-af-ipv4] reflect change-path-attribute
   [*DeviceA1-bgp-af-ipv4] network 1.1.1.1 255.255.255.255
   [*DeviceA1-bgp-af-ipv4] network 192.168.11.0 255.255.255.0
   [*DeviceA1-bgp-af-ipv4] network 192.168.12.0 255.255.255.0
   [*DeviceA1-bgp-af-ipv4] auto-frr
   [*DeviceA1-bgp-af-ipv4] peer minvrf_ebgp_group route-policy rp_minvrf_ebgp_export export
   [*DeviceA1-bgp-af-ipv4] peer minvrf_ibgp_group route-policy rp_minvrf_ibgp_import import
   [*DeviceA1-bgp-af-ipv4] peer minvrf_ibgp_group route-policy rp_minvrf_ibgp_export export
   [*DeviceA1-bgp-af-ipv4] peer minvrf_ibgp_group reflect-client
   [*DeviceA1-bgp-af-ipv4] quit
   [*DeviceA1-bgp] commit
   ```
   
   # Configure routes for the Non-min VPN instance on DeviceA1.
   
   ```
   [~DeviceA1-bgp] ipv4-family vpn-instance nonmin_vrf
   [*DeviceA1-bgp-nonmin_vrf] import-rib public valid-route route-policy rp_importrib_min2nonmin
   [*DeviceA1-bgp-nonmin_vrf] maximum load-balancing 128
   [*DeviceA1-bgp-nonmin_vrf] group nonmin_vrf_ibgp_group internal
   [*DeviceA1-bgp-nonmin_vrf] peer 10.12.2.2 as-number 4200000001
   [*DeviceA1-bgp-nonmin_vrf] peer 10.12.2.2 group nonmin_vrf_ibgp_group
   [*DeviceA1-bgp-nonmin_vrf] peer 10.13.2.3 as-number 4200000001
   [*DeviceA1-bgp-nonmin_vrf] peer 10.13.2.3 group nonmin_vrf_ibgp_group
   [*DeviceA1-bgp-nonmin_vrf] peer nonmin_vrf_ibgp_group route-policy rp_nonmin_vrf_ibgp_import import
   [*DeviceA1-bgp-nonmin_vrf] peer nonmin_vrf_ibgp_group route-policy rp_nonmin_vrf_ibgp_export export
   [*DeviceA1-bgp-nonmin_vrf] quit
   [*DeviceA1] commit
   ```
   
   # Configure routes for the Mix VPN instance on DeviceA1.
   
   ```
   [~DeviceA1-bgp] ipv4-family vpn-instance mix_vrf
   [*DeviceA1-bgp-mix_vrf] maximum load-balancing 32
   [*DeviceA1-bgp-mix_vrf] load-balancing as-path-ignore
   [*DeviceA1-bgp-mix_vrf] load-balancing eibgp
   [*DeviceA1-bgp-mix_vrf] load-balancing med-ignore
   [*DeviceA1-bgp-mix_vrf] load-balancing adaptive-routing
   [*DeviceA1-bgp-mix_vrf] import-rib public valid-route route-policy rp_importrib_min2mix
   [*DeviceA1-bgp-mix_vrf] import-rib vpn-instance nonmin_vrf valid-route route-policy rp_importrib_nonmin2mix
   [*DeviceA1-bgp-mix_vrf] quit
   [*DeviceA1-bgp] commit
   ```
   
   # Configure dynamic load balancing for an ECMP on DeviceA1.
   
   ```
   [~DeviceA1] load-balance ecmp
   [*DeviceA1-ecmp] ecmp mode eligible flowlet-gap-time 9000
   [*DeviceA1-ecmp] quit
   [*DeviceA1] commit
   ```
4. Configure adaptive routing.
   
   
   
   # Configure a dragonfly profile on DeviceA1.
   
   ```
   [~DeviceA1] dragonfly profile default
   [*DeviceA1-dragonfly-profile-default] abs-pfc priority 3 4 5 enable    //This command is required only on the CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, and CE8850-HAM.
   [*DeviceA1-dragonfly-profile-default] adjust original-dscp 26 to priority 4 dscp 32
   [*DeviceA1-dragonfly-profile-default] adjust original-dscp 32 to priority 5 dscp 40
   [*DeviceA1-dragonfly-profile-default] quit
   [*DeviceA1] commit
   ```
   
   # Specify the priority queues for which PFC is to be enabled in the PFC profile.
   
   ```
   [~DeviceA] qos buffer headroom-pool size 4 mbytes slot 1      //This command is required only on the CE8855 and CE8851-32CQ4BQ.
   [*DeviceA1] dcb pfc
   [*DeviceA1-dcb-pfc-default] priority 3 4 5
   [*DeviceA1-dcb-pfc-default] quit
   [*DeviceA1] commit
   ```
   
   # Configure PFC on the global port and local port. (This step is required only on the CE8855 and CE8851-32CQ4BQ.)
   
   ```
   [~DeviceA1] interface 100ge 1/0/1
   [*DeviceA1-100GE1/0/1] dcb pfc enable mode manual
   [*DeviceA1-100GE1/0/1] quit
   [*DeviceA1] interface 100ge 1/0/2
   [*DeviceA1-100GE1/0/2] dcb pfc enable mode manual
   [*DeviceA1-100GE1/0/2] quit
   [*DeviceA1] interface 100ge 1/0/3
   [*DeviceA1-100GE1/0/3] dcb pfc enable mode manual
   [*DeviceA1-100GE1/0/3] quit
   [*DeviceA1] interface 100ge 1/0/4
   [*DeviceA1-100GE1/0/4] dcb pfc enable mode manual
   [*DeviceA1-100GE1/0/4] quit
   [*DeviceA1] commit
   ```
   
   # Configure PFC on the access port.
   
   ```
   [~DeviceA1] interface 100ge 1/0/5
   [*DeviceA1-100GE1/0/5] dcb pfc enable mode manual
   [*DeviceA1-100GE1/0/5] quit
   [*DeviceA1] interface 100ge 1/0/6
   [*DeviceA1-100GE1/0/6] dcb pfc enable mode manual
   [*DeviceA1-100GE1/0/6] quit
   [*DeviceA1] commit
   ```
   
   # Enable adaptive routing on DeviceA1 and both its global port and local port, and configure the roles of the interfaces in the direct topology.
   
   ```
   [~DeviceA1] adaptive-routing enable
   [*DeviceA1] interface 100ge 1/0/1
   [*DeviceA1-100GE1/0/1] adaptive-routing enable dragonfly-role global
   [*DeviceA1-100GE1/0/1] quit
   [*DeviceA1] interface 100ge 1/0/2
   [*DeviceA1-100GE1/0/2] adaptive-routing enable dragonfly-role global
   [*DeviceA1-100GE1/0/2] quit
   [*DeviceA1] interface 100ge 1/0/3
   [*DeviceA1-100GE1/0/3] adaptive-routing enable dragonfly-role local
   [*DeviceA1-100GE1/0/3] quit
   [*DeviceA1] interface 100ge 1/0/4
   [*DeviceA1-100GE1/0/4] adaptive-routing enable dragonfly-role local
   [*DeviceA1-100GE1/0/4] quit
   [*DeviceA1] commit
   ```

#### Verifying the Configuration

* For the CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, and CE8850-HAM:

# Display information about the configured dragonfly profile on DeviceA1.

```
[~DeviceA1] display dragonfly profile default
ABS-PFC Info: 
  ABS-PFC Enable Priority: 3 4 5 
  ABS-PFC Threshold(KB): 0 
Adjust Info: 
  O/N: Original/New 
  ----------------
  Priority   Dscp
  O/N        O/N
  ---------------- 
  3/4        26/32 
  4/5        32/40 
  ----------------
Adaptive-Routing Info:  
  -------------------------------------------------------------------- 
  Bandwidth-Level(High/Low)   Buffer-Level(High/Low)   Tx-Interval(ms) 
  -------------------------------------------------------------------- 
  6/3                         6/3                      500  
  --------------------------------------------------------------------
```

# Display the configuration delivery status of adaptive routing on DeviceA1.

```
[~DeviceA1] display adaptive-routing configuration status
Global Status: Enable                                               
Dragonfly Info:                                                     
  ------------------------------------------------------------------
  Interface    Role    Profile  Adaptive-Routing   ABS-PFC    Adjust
  ------------------------------------------------------------------
  100GE1/0/1   Global  default  Normal             Normal     Normal
  100GE1/0/2   Global  default  Normal             Normal     Normal
  100GE1/0/3   Local   default  Normal             Normal     Normal
  100GE1/0/4   Local   default  Normal             Normal     Normal
  ------------------------------------------------------------------
```

* For the CE8855 and CE8851-32CQ4BQ:

# Display information about the configured dragonfly profile on DeviceA1.

```
[~DeviceA1] display dragonfly profile default
Adjust Info: 
  O/N: Original/New 
  ----------------
  Priority   Dscp
  O/N        O/N
  ---------------- 
  3/4        26/32 
  4/5        32/40 
  ----------------
Adaptive-Routing Info:  
  -------------------------------------------------------------------- 
  Bandwidth-Level(High/Low)   Buffer-Level(High/Low)   Tx-Interval(ms) 
  -------------------------------------------------------------------- 
  6/3                         6/3                      500  
  --------------------------------------------------------------------
```

# Display the configuration delivery status of adaptive routing on DeviceA1.

```
[~DeviceA1] display adaptive-routing configuration status
Global Status: Enable                                               
Dragonfly Info:                                                     
  -------------------------------------------------------
  Interface    Role    Profile  Adaptive-Routing   Adjust
  -------------------------------------------------------
  100GE1/0/1   Global  default  Normal             Normal
  100GE1/0/2   Global  default  Normal             Normal
  100GE1/0/3   Local   default  Normal             Normal
  100GE1/0/4   Local   default  Normal             Normal
  -------------------------------------------------------
```

#### Configuration Scripts

DeviceA1

```
#
sysname DeviceA1
#
adaptive-routing enable
#
dcb pfc
 priority 3 4 5
#
qos buffer headroom-pool size 4 mbytes slot 1      //This command is required only on the CE8855 and CE8851-32CQ4BQ.
#
ip vpn-instance mix_vrf
 ipv4-family
  route-distinguisher 1:1
#
ip vpn-instance nonmin_vrf
 ipv4-family
  route-distinguisher 2:1
  vpn-target 2:1 export-extcommunity
  vpn-target 2:1 import-extcommunity
#
ip import-rib vpn-instance mix_vrf protocol direct
#
interface 100GE1/0/1
 undo portswitch
 adaptive-routing enable dragonfly-role global
 dcb pfc enable mode manual    //This command is required only on the CE8855 and CE8851-32CQ4BQ.
#
interface 100GE1/0/1.104
 description min_port_of_global_link
 ip address 172.16.1.1 255.255.255.0
 encapsulation dot1q-termination
 dot1q termination vid 10
#
interface 100GE1/0/2
 undo portswitch
 adaptive-routing enable dragonfly-role global
 dcb pfc enable mode manual    //This command is required only on the CE8855 and CE8851-32CQ4BQ.
#
interface 100GE1/0/2.107
 description min_port_of_global_link
 ip address 172.17.1.1 255.255.255.0
 encapsulation dot1q-termination
 dot1q termination vid 10
#
interface 100GE1/0/3
 undo portswitch
 adaptive-routing enable dragonfly-role local
 dcb pfc enable mode manual    //This command is required only on the CE8855 and CE8851-32CQ4BQ.
#
interface 100GE1/0/3.102
 description min_port_of_local_link
 ip address 10.12.1.1 255.255.255.0
 encapsulation dot1q-termination
 dot1q termination vid 10
#
interface 100GE1/0/3.1020
 description nonmin_port_of_local_link
 ip binding vpn-instance nonmin_vrf
 ip address 10.12.2.1 255.255.255.0
 encapsulation dot1q-termination
 dot1q termination vid 20
#
interface 100GE1/0/4
 undo portswitch
 adaptive-routing enable dragonfly-role local
 dcb pfc enable mode manual    //This command is required only on the CE8855 and CE8851-32CQ4BQ.
#
interface 100GE1/0/4.103
 description min_port_of_local_link
 ip address 10.13.1.1 255.255.255.0
 encapsulation dot1q-termination
 dot1q termination vid 10
#
interface 100GE1/0/4.1030
 description nonmin_port_of_local_link
 ip binding vpn-instance nonmin_vrf
 ip address 10.13.2.1 255.255.255.0
 encapsulation dot1q-termination
 dot1q termination vid 20
#
interface 100GE1/0/5
 undo portswitch
 description access_port
 ip binding vpn-instance mix_vrf
 ip address 192.168.11.1 255.255.255.0
 dcb pfc enable mode manual
#
interface 100GE1/0/6
 undo portswitch
 description access_port
 ip binding vpn-instance mix_vrf
 ip address 192.168.12.1 255.255.255.0
 dcb pfc enable mode manual
#
interface LoopBack0
 ip binding vpn-instance mix_vrf
 ip address 1.1.1.1 255.255.255.255
#
bgp 4200000001
 router-id 1.1.1.1
 group minvrf_ebgp_group external
 peer 172.16.1.4 as-number 4200000002
 peer 172.16.1.4 group minvrf_ebgp_group
 peer 172.17.1.7 as-number 4200000003
 peer 172.17.1.7 group minvrf_ebgp_group
 group minvrf_ibgp_group internal
 peer 10.12.1.2 as-number 4200000001
 peer 10.12.1.2 group minvrf_ibgp_group
 peer 10.13.1.3 as-number 4200000001
 peer 10.13.1.3 group minvrf_ibgp_group
 #
 ipv4-family unicast
  reflector cluster-id 1
  reflect change-path-attribute
  network 1.1.1.1 255.255.255.255
  network 192.168.11.0 255.255.255.0
  network 192.168.12.0 255.255.255.0
  maximum load-balancing 128
  auto-frr
  peer minvrf_ebgp_group enable
  peer minvrf_ebgp_group route-policy rp_minvrf_ebgp_export export
  peer 172.16.1.4 enable
  peer 172.16.1.4 group minvrf_ebgp_group
  peer 172.17.1.7 enable
  peer 172.17.1.7 group minvrf_ebgp_group
  peer minvrf_ibgp_group enable
  peer minvrf_ibgp_group route-policy rp_minvrf_ibgp_import import
  peer minvrf_ibgp_group route-policy rp_minvrf_ibgp_export export
  peer minvrf_ibgp_group reflect-client
  peer 10.12.1.2 enable
  peer 10.12.1.2 group minvrf_ibgp_group
  peer 10.13.1.3 enable
  peer 10.13.1.3 group minvrf_ibgp_group
 #
 ipv4-family vpn-instance mix_vrf
  load-balancing med-ignore
  load-balancing adaptive-routing
  maximum load-balancing 32
  load-balancing as-path-ignore
  load-balancing eibgp
  import-rib public valid-route route-policy rp_importrib_min2mix
  import-rib vpn-instance nonmin_vrf valid-route route-policy rp_importrib_nonmin2mix
 #
 ipv4-family vpn-instance nonmin_vrf
  maximum load-balancing 128
  import-rib public valid-route route-policy rp_importrib_min2nonmin
  group nonmin_vrf_ibgp_group internal
  peer 10.12.2.2 as-number 4200000001
  peer 10.12.2.2 group nonmin_vrf_ibgp_group
  peer 10.13.2.3 as-number 4200000001
  peer 10.13.2.3 group nonmin_vrf_ibgp_group
  peer nonmin_vrf_ibgp_group route-policy rp_nonmin_vrf_ibgp_import import
  peer nonmin_vrf_ibgp_group route-policy rp_nonmin_vrf_ibgp_export export
#
route-policy rp_importrib_min2mix deny node 5
 if-match cost 2
#
route-policy rp_importrib_min2mix permit node 10
 if-match cost greater-equal 1 less-equal 2999
#
route-policy rp_importrib_min2nonmin permit node 5
 if-match cost 1
#
route-policy rp_importrib_min2nonmin permit node 10
 if-match cost greater-equal 2000 less-equal 2999
#
route-policy rp_importrib_nonmin2mix permit node 5
 if-match cost greater-equal 2000 less-equal 2999
#
route-policy rp_importrib_nonmin2mix permit node 10
 if-match cost greater-equal 2 less-equal 999
#
route-policy rp_minvrf_ebgp_export deny node 5
 if-match cost greater-equal 2000 less-equal 4294967295
#
route-policy rp_minvrf_ebgp_export permit node 10
 if-match cost greater-equal 0 less-equal 1999
 apply cost + 1000
#
route-policy rp_minvrf_ibgp_export deny node 5
 if-match cost 2
#
route-policy rp_minvrf_ibgp_export deny node 10
 if-match cost greater-equal 2000 less-equal 4294967295
 if-match route-type ibgp
#
route-policy rp_minvrf_ibgp_export permit node 15
 if-match cost greater-equal 0 less-equal 1999
 apply cost + 1
#
route-policy rp_minvrf_ibgp_import permit node 5
 apply ip-address next-hop peer-address
#
route-policy rp_nonmin_vrf_ibgp_export deny node 5
 if-match cost 2
#
route-policy rp_nonmin_vrf_ibgp_export permit node 10
 if-match cost greater-equal 2000 less-equal 2999
 if-match route-type ebgp
 apply cost + 1
#
route-policy rp_nonmin_vrf_ibgp_export permit node 15
 if-match cost 1
 if-match route-type ibgp
 apply cost + 1
#
route-policy rp_nonmin_vrf_ibgp_import permit node 5
 apply ip-address next-hop peer-address
#
dragonfly profile default
 abs-pfc priority 3 4 5 enable    //This command is required only on the CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, and CE8850-HAM.
 adjust original-dscp 26 to priority 4 dscp 32
 adjust original-dscp 32 to priority 5 dscp 40
#
load-balance ecmp
 ecmp mode eligible flowlet-gap-time 9000
#
return
```
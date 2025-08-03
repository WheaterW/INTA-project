Example for Configuring QPPB (BGP)
==================================

This section provides an example for configuring QPPB (BGP).

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172371445__fig_dc_ne_qos_cfg_203801), DeviceB advertises BGP routes with community attributes to DeviceA, and DeviceA matches the community attributes against the community list, associates traffic behaviors with QoS local IDs for the matched routes, and applies a QPPB local policy to the traffic transmitted along the routes.

Traffic is sent from DeviceB to DeviceC by passing through DeviceA. DeviceB functions as a BGP route sender, and DeviceA functions as a BGP route receiver. It is required that source-based QPPB be applied to the incoming traffic on DeviceA.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent GE 0/1/0 and GE 0/2/0, respectively.


**Figure 1** Networking diagram for configuring QPPB  
![](images/fig_dc_ne_qos_cfg_203801.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure basic BGP functions.
2. Configure a routing policy to set community attributes for the routes to be advertised and advertise routes on DeviceB.
3. Configure a routing policy on DeviceA to match the community attributes against the community list, and associate traffic behaviors with QoS local IDs for the matched routes.
4. Apply the QPPB local policy to the inbound interface of DeviceA.

#### Data Preparation

To complete the configuration, you need the following data:

* IP address of each interface
* Routing policy name, matching rule, and route attribute
* QPPB local policy name

#### Procedure

1. Configure basic BGP functions on DeviceA and DeviceB.
   
   
   
   # Configure loopback interfaces on DeviceA and DeviceB.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceA
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceA] interface loopback 0
   ```
   ```
   [*DeviceA-LoopBack0] ip address 1.1.1.1 255.255.255.255
   ```
   ```
   [*DeviceA-LoopBack0] commit
   ```
   ```
   [~DeviceA-LoopBack0] return
   ```
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceB
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceB] interface loopback 0
   ```
   ```
   [*DeviceB-LoopBack0] ip address 2.2.2.2 255.255.255.255
   ```
   ```
   [*DeviceB-LoopBack0] commit
   ```
   ```
   [~DeviceB-LoopBack0] return
   ```
   
   # Configure interfaces connecting DeviceA and DeviceB and interfaces connecting DeviceA and DeviceC.
   
   ```
   <DeviceA> system-view
   ```
   ```
   [~DeviceA] interface GigabitEthernet 0/2/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/0] undo shutdown
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/0] ip address 10.10.1.1 255.255.255.0
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/0] quit
   ```
   ```
   [~DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] ip address 10.20.1.2 255.255.255.0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] return
   ```
   ```
   <DeviceB> system-view
   ```
   ```
   [~DeviceB] interface GigabitEthernet 0/2/0
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] ip address 10.10.1.2 255.255.255.0
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] return
   ```
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceC
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceC] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceC-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [~DeviceC-GigabitEthernet0/1/0] ip address 10.20.1.1 255.255.255.0
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceC-GigabitEthernet0/1/0] return
   ```
   
   # Enable OSPF to advertise route information containing the interface addresses.
   
   ```
   <DeviceA> system-view
   ```
   ```
   [~DeviceA] ospf
   ```
   ```
   [*DeviceA-ospf-1] area 0
   ```
   ```
   [*DeviceA-ospf-1-area-0.0.0.0] network 1.1.1.1 0.0.0.0
   ```
   ```
   [*DeviceA-ospf-1-area-0.0.0.0] network 10.10.1.0 0.0.0.255
   ```
   ```
   [*DeviceA-ospf-1-area-0.0.0.0] network 10.20.1.0 0.0.0.255
   ```
   ```
   [*DeviceA-ospf-1-area-0.0.0.0] commit
   ```
   ```
   [~DeviceA-ospf-1-area-0.0.0.0] return
   ```
   ```
   <DeviceB> system-view
   ```
   ```
   [~DeviceB] ospf
   ```
   ```
   [*DeviceB-ospf] area 0
   ```
   ```
   [*DeviceB-ospf-1-area-0.0.0.0] network 2.2.2.2 0.0.0.0
   ```
   ```
   [*DeviceB-ospf-1-area-0.0.0.0] network 10.10.1.0 0.0.0.255
   ```
   ```
   [*DeviceB-ospf-1-area-0.0.0.0] commit
   ```
   ```
   [~DeviceB-ospf-1-area-0.0.0.0] return
   ```
   ```
   <DeviceC> system-view
   ```
   ```
   [~DeviceC] ospf
   ```
   ```
   [*DeviceC-ospf] area 0
   ```
   ```
   [*DeviceC-ospf-1-area-0.0.0.0] network 10.20.1.0 0.0.0.255
   ```
   ```
   [*DeviceC-ospf-1-area-0.0.0.0] commit
   ```
   ```
   [~DeviceC-ospf-1-area-0.0.0.0] return
   ```
   
   # Configure BGP and set up an EBGP peer relationship between DeviceA and DeviceB.
   
   ```
   <DeviceA> system-view
   ```
   ```
   [~DeviceA] bgp 100
   ```
   ```
   [*DeviceA-bgp] peer 2.2.2.2 as-number 200
   ```
   ```
   [*DeviceA-bgp] peer 2.2.2.2 ebgp-max-hop 2
   ```
   ```
   [*DeviceA-bgp] peer 2.2.2.2 connect-interface loopback 0
   ```
   ```
   [*DeviceA-bgp] import-route direct
   ```
   ```
   [*DeviceA-bgp] commit
   ```
   ```
   [~DeviceA-bgp] return
   ```
   ```
   <DeviceB> system-view
   ```
   ```
   [~DeviceB] bgp 200
   ```
   ```
   [*DeviceB-bgp] peer 1.1.1.1 as-number 100
   ```
   ```
   [*DeviceB-bgp] peer 1.1.1.1 ebgp-max-hop 2
   ```
   ```
   [*DeviceB-bgp] peer 1.1.1.1 connect-interface loopback 0
   ```
   ```
   [*DeviceB-bgp] import-route direct
   ```
   ```
   [*DeviceB-bgp] commit
   ```
   ```
   [~DeviceB-bgp] return
   ```
   
   # Configure BGP and set up an IBGP peer relationship between DeviceA and DeviceC.
   
   ```
   <DeviceA> system-view
   ```
   ```
   [~DeviceA] bgp 100
   ```
   ```
   [*DeviceA-bgp] peer 10.20.1.1 as-number 100
   ```
   ```
   [*DeviceA-bgp] import-route direct
   ```
   ```
   [*DeviceA-bgp] commit
   ```
   ```
   [~DeviceA-bgp] quit
   ```
   ```
   <DeviceC> system-view
   ```
   ```
   [~DeviceC] bgp 100
   ```
   ```
   [*DeviceC-bgp] peer 10.20.1.2 as-number 100
   ```
   ```
   [*DeviceC-bgp] import-route direct
   ```
   ```
   [*DeviceC-bgp] commit
   ```
   ```
   [~DeviceC-bgp] quit
   ```
   
   After the configuration is complete, DeviceA can communicate with DeviceB and DeviceC.
2. Configure and apply a routing policy on DeviceB.
   
   
   
   # Configure an IP prefix on DeviceB.
   
   ```
   <DeviceB> system-view
   ```
   ```
   [~DeviceB] ip ip-prefix bb permit 10.10.1.0 24
   ```
   ```
   [*DeviceB] commit
   ```
   ```
   [~DeviceB] return
   ```
   
   # Configure a routing policy on DeviceB.
   
   ```
   <DeviceB> system-view
   ```
   ```
   [~DeviceB] route-policy aa permit node 10
   ```
   ```
   [*DeviceB-route-policy] if-match ip-prefix bb
   ```
   ```
   [*DeviceB-route-policy] apply community 10:10
   ```
   ```
   [*DeviceB-route-policy] commit
   ```
   ```
   [~DeviceB-route-policy] return
   ```
   
   # Configure a policy for advertising routes through BGP on DeviceB.
   
   ```
   <DeviceB> system-view
   ```
   ```
   [~DeviceB] bgp 200
   ```
   ```
   [*DeviceB-bgp] peer 1.1.1.1 route-policy aa export
   ```
   ```
   [*DeviceB-bgp] peer 1.1.1.1 advertise-community
   ```
   ```
   [*DeviceB-bgp] commit
   ```
   ```
   [~DeviceB-bgp] return
   ```
3. Configure a policy for receiving routes on DeviceA, and apply traffic behaviors to the route that matches the route attribute.
   
   
   
   # Configure a traffic behavior.
   
   ```
   [~DeviceA] traffic behavior dd
   ```
   ```
   [*DeviceA-behavior-dd] remark dscp af11
   ```
   ```
   [*DeviceA-behavior-dd] commit
   ```
   ```
   [~DeviceA-behavior-dd] return
   ```
   
   # Configure a routing policy and apply the traffic behavior to the route that matches the route attribute.
   
   ```
   <DeviceA> system-view
   ```
   ```
   [~DeviceA] ip community-filter 10 permit 10:10
   ```
   ```
   [*DeviceA] route-policy aa permit node 10
   ```
   ```
   [*DeviceA-route-policy] if-match community-filter 10
   ```
   ```
   [*DeviceA-route-policy] apply qos-local-id 1
   ```
   ```
   [*DeviceA-route-policy] commit
   ```
   ```
   [~DeviceA-route-policy] return
   ```
   
   # Configure a QPPB local policy on DeviceA.
   
   ```
   <DeviceA> system-view
   ```
   ```
   [~DeviceA] qppb local-policy ac
   ```
   ```
   [*DeviceA-localpolicy-ac] qos-local-id 1 behavior dd
   ```
   ```
   [*DeviceA-localpolicy-ac] commit
   ```
   ```
   [~DeviceA-localpolicy-ac] return
   ```
   
   # Apply the routing policy to the routes sent from DeviceB on DeviceA.
   
   ```
   <DeviceA> system-view
   ```
   ```
   [~DeviceA] bgp 100
   ```
   ```
   [*DeviceA-bgp] peer 2.2.2.2 route-policy aa import
   ```
   ```
   [*DeviceA-bgp] commit
   ```
   ```
   [~DeviceA-bgp] return
   ```
4. Apply the QPPB local policy to the incoming traffic on DeviceA.
   
   
   ```
   <DeviceA> system-view
   ```
   ```
   [~DeviceA] interface GigabitEthernet 0/2/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/0] qppb-policy ac source inbound
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/0] return
   ```
5. Verify the configuration.
   
   
   
   # Display the QPPB local policy information on DeviceA.
   
   ```
   <~DeviceA> display qppb local-policy configuration ac
   ```
   ```
   qppb local-policy: ac
    statistics disable
    service-class outbound disable
    is-used yes
    qos-local-id 1 behavior dd 
   ```

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  sysname DeviceA
  #
  traffic behavior dd
   remark dscp af11
  #
  qppb local-policy ac
   qos-local-id 1 behavior dd
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.20.1.2 255.255.255.0
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.10.1.1 255.255.255.0
   qppb-policy ac source inbound
  #
  interface LoopBack0
   ip address 1.1.1.1 255.255.255.255
  #
  bgp 100
   peer 2.2.2.2 as-number 200
   peer 2.2.2.2 ebgp-max-hop 2
   peer 2.2.2.2 connect-interface LoopBack0
   peer 10.20.1.1 as-number 100
  #
  ipv4-family unicast
    undo synchronization
    import-route direct
    peer 2.2.2.2 enable
    peer 2.2.2.2 route-policy aa import
    peer 10.20.1.1 enable     
  #
  ospf 1
   area 0.0.0.0
    network 1.1.1.1 0.0.0.0
    network 10.10.1.0 0.0.0.255
    network 10.20.1.0 0.0.0.255
  #
  ip community-filter 10 index 10 permit 10:10
  # 
  route-policy aa permit node 10
   if-match community-filter 10
   apply qos-local-id 1
  #
  return
  ```
* DeviceB configuration file
  
  ```
  #
  ```
  ```
  sysname DeviceB
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.10.1.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface LoopBack0
  ```
  ```
   ip address 2.2.2.2 255.255.255.255
  ```
  ```
  #
  ```
  ```
  bgp 200
  ```
  ```
   peer 1.1.1.1 as-number 100
  ```
  ```
   peer 1.1.1.1 ebgp-max-hop 2
  ```
  ```
   peer 1.1.1.1 connect-interface LoopBack0
  ```
  ```
   #
  ```
  ```
   ipv4-family unicast
  ```
  ```
    undo synchronization
  ```
  ```
    import-route direct
  ```
  ```
    peer 1.1.1.1 enable
  ```
  ```
    peer 1.1.1.1 route-policy aa export
  ```
  ```
    peer 1.1.1.1 advertise-community
  ```
  ```
    quit
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 2.2.2.2 0.0.0.0
  ```
  ```
    network 10.10.1.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  route-policy aa permit node 10
  ```
  ```
   if-match ip-prefix bb
  ```
  ```
   apply community 10:10
  ```
  ```
  #
  ```
  ```
  ip ip-prefix bb index 10 permit 10.10.1.0 24
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceC configuration file
  
  ```
  #
  ```
  ```
  sysname DeviceC
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.20.1.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  bgp 100
  ```
  ```
   peer 10.20.1.2 as-number 100
  ```
  ```
   #
  ```
  ```
   ipv4-family unicast
  ```
  ```
    undo synchronization
  ```
  ```
    import-route direct
  ```
  ```
    peer 10.20.1.2 enable
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 10.20.1.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  return
  ```
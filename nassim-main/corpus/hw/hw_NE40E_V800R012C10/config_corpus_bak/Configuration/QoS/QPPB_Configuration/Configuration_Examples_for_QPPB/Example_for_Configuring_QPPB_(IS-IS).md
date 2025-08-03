Example for Configuring QPPB (IS-IS)
====================================

This section provides an example for configuring QPPB (IS-IS).

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172371448__fig_dc_ne_qos_cfg_5097), IS-IS neighbor relationships are established between DeviceA and DeviceB, and DeviceB advertises IS-IS routes with community attributes to DeviceA. A QPPB local policy is applied to traffic passing through DeviceA. DeviceB functions as an IS-IS route sender, and DeviceA functions as an IS-IS route receiver.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 represents GE 0/1/0.


**Figure 1** Networking diagram for configuring QPPB  
![](images/fig_dc_ne_qos_cfg_5097.png)  


#### Precautions

None


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a routing policy on DeviceA to match the community attributes against the community list, and associate traffic behaviors with QoS local IDs for the matched routes.
2. Configure basic IS-IS functions.
3. Apply the QPPB local policy to the inbound interface of DeviceA.

#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of interfaces
* Routing policy name, matching rule, and route attribute
* QPPB local policy name

#### Procedure

1. Assign an IP address to each interface.
   
   
   
   Assign an IP address to each interface based on [Figure 1](#EN-US_TASK_0172371448__fig_dc_ne_qos_cfg_5097).
2. Configure a policy for receiving routes on DeviceA, and apply traffic behaviors to the route that matches the route attribute.
   
   
   
   # Configure a routing policy on DeviceA.
   
   ```
   <DeviceA> system-view
   ```
   ```
   [~DeviceA] route-policy ac permit node 123
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
3. Configure basic IS-IS functions.
   
   
   
   # Configure DeviceA.
   
   ```
   <DeviceA> system-view
   ```
   ```
   [~DeviceA] isis 1
   ```
   ```
   [*DeviceA-isis-1] is-level level-1
   ```
   ```
   [*DeviceA-isis-1] network-entity 10.0000.0000.0001.00
   ```
   ```
   [*DeviceA-isis-1] cost-style wide
   ```
   ```
   [*DeviceA-isis-1] filter-policy route-policy ac import
   ```
   ```
   [*DeviceA-isis-1] traffic-eng level-1
   ```
   ```
   [*DeviceA-isis-1] quit
   ```
   ```
   [*DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] isis enable 1
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] quit
   ```
   
   # Configure DeviceB.
   
   ```
   <DeviceB> system-view
   ```
   ```
   [~DeviceB] isis 1
   ```
   ```
   [*DeviceB-isis-1] network-entity 10.0000.0000.0002.00
   ```
   ```
   [*DeviceB-isis-1] cost-style wide
   ```
   ```
   [*DeviceB-isis-1] quit
   ```
   ```
   [*DeviceB] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] isis enable 1
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] quit
   ```
4. Apply the QPPB local policy to the inbound interface of DeviceA.
   
   
   ```
   [~DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] qppb-policy ac source inbound
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] quit
   ```
5. Verify the configuration.
   
   
   
   # Display the QPPB local policy information on DeviceA.
   
   ```
   [~DeviceA] display qppb local-policy configuration ac
   ```
   ```
   qppb local-policy: ac
    statistics disable
    service-class outbound disable 
    is-used yes
    qos-local-id 1 behavior dd 
   ```

#### Configuration Files

* DeviceA configuration file.
  
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
  isis 1
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0001.00
   filter-policy route-policy ac import
   traffic-eng level-1
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.10.1.1 255.255.255.0
   isis enable 1
   qppb-policy ac source inbound
  #
  route-policy ac permit node 123
   apply qos-local-id 1
  #
  return
  ```
* DeviceB configuration file.
  
  ```
  #
  sysname DeviceB
  #
  isis 1
   cost-style wide
   network-entity 10.0000.0000.0002.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.10.1.2 255.255.255.0
   isis enable 1
  #
  return
  ```
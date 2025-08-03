Example for Configuring Priority-based Shaping for a GQ
=======================================================

This section provides an example for configuring priority-based shaping for a GQ.

#### Networking Requirements

Assume that there are N QinQ users. Use users **test1** and **test2** as an example. The PE VLAN ID and CE VLAN ID of user **test1** are 1 and 100 respectively, and the PE VLAN ID and CE VLAN ID of user **test2** are 1 and 200 respectively. The bandwidths of the EF and BE queues are respectively 1 Mbit/s and 100 Mbit/s for user **test1** and are respectively 2 Mbit/s and 200 Mbit/s for user **test2**. It is required that the bandwidth be guaranteed for priority-specific queues of all users and the traffic rate be restricted to 5 Mbit/s for EF queues of all users in the GQ and to 600 Mbit/s for BE queues of all users in the GQ.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, Sub-interface1.1, Sub-interface1.2, and Interface2 represent GigabitEthernet0/1/0.1, GigabitEthernet0/1/0.2, and GigabitEthernet0/2/0, respectively.


**Figure 1** Configuring priority-based shaping for a GQ  
![](images/dc_ne_qos_cfg_5105_01.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure flow WRED objects.
2. Configure scheduling algorithms and parameters for the user **test1** flow queue.
3. Configure scheduling algorithms and parameters for the user **test2** flow queue.
4. Configure priority mapping and shaping values for the GQ.
5. Configure user-queue scheduling parameters for user **test1**.
6. Configure user-queue scheduling parameters for user **test2**.
7. Configure a QoS profile for user **test1** on the outbound interface of the Router.
8. Configure a QoS profile for user **test2** on the outbound interface of the Router.

#### Data Preparation

To complete the configuration, you need the following data:

* Scheduling algorithms and related parameters for flow queues
* Shaping values for a group queue
* Applied interface

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* HQoS must be applied to outgoing packets on an interface.
* The **cir** *cir-value* must be set to 0.
* The configuration of priority-based shaping for a GQ can be bound to a priority-based FQ profile only.


#### Procedure

1. Configure a WRED object referenced by a flow queue.
   
   
   * # Configure flow WRED **test1**.
     
     ```
     <HUAWEI> system-view
     ```
     ```
     [~HUAWEI] flow-wred test1
     ```
     ```
     [*HUAWEI-flow-wred-test1] commit
     ```
     ```
     [~HUAWEI-flow-wred-test1] return
     ```
   * # Configure flow WRED **test2**.
     
     ```
     <HUAWEI> system-view
     ```
     ```
     [~HUAWEI] flow-wred test2
     ```
     ```
     [*HUAWEI-flow-wred-test2] commit
     ```
     ```
     [~HUAWEI-flow-wred-test2] return
     ```
2. Configure scheduling algorithms and parameters for the flow queues.
   
   
   * Configure scheduling algorithms and parameters for the user **test1** flow queue.
     
     ```
     <HUAWEI> system-view
     ```
     ```
     [~HUAWEI] flow-queue test1 priority-mode
     ```
     ```
     [*HUAWEI-flow-queue-template-test1] queue ef priority 1 flow-wred test1 shaping 1000
     ```
     ```
     [*HUAWEI-flow-queue-template-test1] queue be priority 2 flow-wred test1 shaping 100000
     ```
     ```
     [*HUAWEI-flow-queue-template-test1] commit
     ```
     ```
     [~HUAWEI-flow-queue-template-test1] return
     ```
   * Configure scheduling algorithms and parameters for the user **test2** flow queue.
     
     ```
     <HUAWEI> system-view
     ```
     ```
     [~HUAWEI] flow-queue test2 priority-mode
     ```
     ```
     [*HUAWEI-flow-queue-template-test2] queue ef priority 1 flow-wred test2 shaping 2000
     ```
     ```
     [*HUAWEI-flow-queue-template-test2] queue be priority 2 flow-wred test2 shaping 200000
     ```
     ```
     [*HUAWEI-flow-queue-template-test2] commit
     ```
     ```
     [~HUAWEI-flow-queue-template-test2] return
     ```
3. Configure priority mapping and shaping values for the GQ.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] user-group-queue test priority-mode
   ```
   ```
   [*HUAWEI-user-group-queue-test] priority 1 shaping 5000 outbound
   ```
   ```
   [*HUAWEI-user-group-queue-test] priority 2 shaping 600000 outbound
   ```
   ```
   [*HUAWEI-user-group-queue-test] commit
   ```
   ```
   [~HUAWEI-user-group-queue-test] return
   ```
4. Configure user-queue scheduling parameters.
   
   
   * Configure user-queue scheduling parameters for user **test1**.
     
     ```
     <HUAWEI> system-view
     ```
     ```
     [~HUAWEI] qos-profile test1
     ```
     ```
     [*HUAWEI-qos-profile-test1] user-queue cir 0 pir 2000000 flow-queue test1 user-group-queue test outbound
     ```
     ```
     [*HUAWEI-qos-profile-test1] commit
     ```
     ```
     [~HUAWEI-qos-profile-test1] return
     ```
   * Configure user-queue scheduling parameters for user **test2**.
     
     ```
     <HUAWEI> system-view
     ```
     ```
     [~HUAWEI] qos-profile test2
     ```
     ```
     [*HUAWEI-qos-profile-test2] user-queue cir 0 pir 2000000 flow-queue test2 user-group-queue test outbound
     ```
     ```
     [*HUAWEI-qos-profile-test2] commit
     ```
     ```
     [~HUAWEI-qos-profile-test2] return
     ```
5. Apply the configuration to an interface.
   
   
   * Create a QinQ sub-interface, configure QinQ termination for the sub-interface, and apply the user **test1** configuration to interface 0/1/0.1.
     
     ```
     <HUAWEI> system-view
     ```
     ```
     [~HUAWEI] interface gigabitethernet 0/1/0.1
     ```
     ```
     [*HUAWEI-GigabitEthernet0/1/0.1] encapsulation qinq-termination
     ```
     ```
     [*HUAWEI-GigabitEthernet0/1/0.1] qinq termination pe-vid 1 ce-vid 100
     ```
     ```
     [*HUAWEI-GigabitEthernet0/1/0.1] ip address 10.10.1.1 255.255.255.0
     ```
     ```
     [*HUAWEI-GigabitEthernet0/1/0.1] qos-profile test1 outbound pe-vid 1 ce-vid 100
     ```
     ```
     [*HUAWEI-GigabitEthernet0/1/0.1] commit
     ```
     ```
     [~HUAWEI-GigabitEthernet0/1/0.1] quit
     ```
   * Create a QinQ sub-interface, configure QinQ termination for the sub-interface, and apply the user **test2** configuration to interface 0/1/0.2.
     
     ```
     <HUAWEI> system-view
     ```
     ```
     [~HUAWEI] interface gigabitethernet 0/1/0.2
     ```
     ```
     [*HUAWEI-GigabitEthernet0/1/0.2] encapsulation qinq-termination
     ```
     ```
     [*HUAWEI-GigabitEthernet0/1/0.2] qinq termination pe-vid 1 ce-vid 200
     ```
     ```
     [*HUAWEI-GigabitEthernet0/1/0.2] ip address 10.10.2.1 255.255.255.0
     ```
     ```
     [*HUAWEI-GigabitEthernet0/1/0.2] qos-profile test2 outbound pe-vid 1 ce-vid 200
     ```
     ```
     [*HUAWEI-GigabitEthernet0/1/0.2] commit
     ```
     ```
     [~HUAWEI-GigabitEthernet0/1/0.2] quit
     ```

#### Configuration Files

HUAWEI configuration file
```
#
```
```
 sysname HUAWEI
```
```
#
```
```
flow-wred test1
```
```
#
```
```
flow-wred test2
```
```
#
```
```
flow-queue test1 priority-mode
```
```
 queue ef priority 1 flow-wred test1 shaping 1000
```
```
 queue be priority 2 flow-wred test1 shaping 100000
```
```
#
```
```
flow-queue test2 priority-mode
```
```
 queue ef priority 1 flow-wred test2 shaping 2000
```
```
 queue be priority 2 flow-wred test2 shaping 200000
```
```
#
```
```
user-group-queue test priority-mode
```
```
 priority 1 shaping 5000 outbound
```
```
 priority 2 shaping 600000 outbound
```
```
#
```
```
qos-profile test1
```
```
 user-queue cir 0 pir 2000000 flow-queue test1 user-group-queue test outbound
```
```
#
```
```
qos-profile test2
```
```
 user-queue cir 0 pir 2000000 flow-queue test2 user-group-queue test outbound
```
```
#
```
```
interface GigabitEthernet0/1/0.1  
```
```
 encapsulation qinq-termination
```
```
 qinq termination pe-vid 1 ce-vid 100 
```
```
 ip address 10.10.1.1 255.255.255.0
```
```
 qos-profile test1 outbound pe-vid 1 ce-vid 100
```
```
#
```
```
interface GigabitEthernet0/1/0.2  
```
```
 encapsulation qinq-termination
```
```
 qinq termination pe-vid 1 ce-vid 200 
```
```
 ip address 10.10.2.1 255.255.255.0
```
```
 qos-profile test2 outbound pe-vid 1 ce-vid 200
```
```
#
```
```
return
```
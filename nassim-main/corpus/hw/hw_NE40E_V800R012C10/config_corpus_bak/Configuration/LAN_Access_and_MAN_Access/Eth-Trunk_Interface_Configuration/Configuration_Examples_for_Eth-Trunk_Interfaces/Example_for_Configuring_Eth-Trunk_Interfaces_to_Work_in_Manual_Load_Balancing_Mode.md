Example for Configuring Eth-Trunk Interfaces to Work in Manual Load Balancing Mode
==================================================================================

In manual load balancing mode, traffic can be evenly distributed among all the member interfaces. You can also set different weights for the member interfaces so that uneven load balancing can be carried out. That means, certain interfaces that have greater weights transmit more traffic.

#### Context

You can bundle multiple Ethernet interfaces into a logical Eth-Trunk interface (link aggregation group) to increase bandwidth, improve link reliability, and implement load balancing.

On the network shown in [Figure 1](#EN-US_TASK_0172362932__fig_dc_vrp_ethtrunk_cfg_002201), user group 1 communicates with user group 2. To allow traffic to be load-balanced among links, you can create Eth-Trunk interfaces on PE1 and PE2 and configure the Eth-Trunk interfaces to work in manual load balancing mode.

**Figure 1** Eth-Trunk interfaces in manual load balancing mode![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE 0/1/1, GE 0/2/1, and GE 0/3/1, respectively.


  
![](images/fig_dc_vrp_ethtrunk_cfg_002201.png)

#### Precautions

After an Eth-Trunk interface is created, it works in manual load balancing mode by default. You can adopt the default working mode.

If the Eth-Trunk interface has been configured to work in another mode, you can run the [**mode**](cmdqueryname=mode) command to configure the Eth-Trunk interface to work in manual load balancing mode.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create an Eth-Trunk interface in manual load balancing mode on each PE to implement link aggregation.
2. Add Ethernet interfaces to each Eth-Trunk interface and set a load balancing weight for each member interface to increase bandwidth and implement load balancing.

#### Data Preparation

To complete the configuration, you need the following data:

* Eth-Trunk interface ID
* Type and number of the member interface of the Eth-Trunk interface

Default value of every parameter of the Eth-Trunk interface


#### Procedure

1. Create an Eth-Trunk interface.
   
   
   
   # Configure PE1.
   
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
   [~PE1] interface eth-trunk 1
   ```
   ```
   [*PE1-Eth-Trunk1] commit
   ```
   ```
   [~PE1-Eth-Trunk1] quit
   ```
   
   # Configure PE2.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname PE2
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~PE2] interface eth-trunk 1
   ```
   ```
   [*PE2-Eth-Trunk1] commit
   ```
   ```
   [~PE2-Eth-Trunk1] quit
   ```
2. Add Ethernet interfaces to the Eth-Trunk interfaces and configure a load balancing weight for every member interface.
   
   
   
   # Configure PE1.
   
   ```
   [*PE1] interface gigabitethernet 0/1/1
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] eth-trunk 1
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/2/1
   ```
   ```
   [*PE1-GigabitEthernet0/2/1] undo shutdown
   ```
   ```
   [*PE1-GigabitEthernet0/2/1] eth-trunk 1
   ```
   ```
   [*PE1-GigabitEthernet0/2/1] distribute-weight 3
   ```
   ```
   [*PE1-GigabitEthernet0/2/1] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/3/1
   ```
   ```
   [*PE1-GigabitEthernet0/3/1] undo shutdown
   ```
   ```
   [*PE1-GigabitEthernet0/3/1] eth-trunk 1
   ```
   ```
   [*PE1-GigabitEthernet0/3/1] commit
   ```
   ```
   [~PE1-GigabitEthernet0/3/1] quit
   ```
   
   # Configure PE2.
   
   ```
   [*PE2] interface gigabitethernet 0/1/1
   ```
   ```
   [*PE2-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*PE2-GigabitEthernet0/1/1] eth-trunk 1
   ```
   ```
   [*PE2-GigabitEthernet0/1/1] quit
   ```
   ```
   [*PE2] interface gigabitethernet 0/2/1
   ```
   ```
   [*PE2-GigabitEthernet0/2/1] undo shutdown
   ```
   ```
   [*PE2-GigabitEthernet0/2/1] eth-trunk 1
   ```
   ```
   [*PE2-GigabitEthernet0/2/1] distribute-weight 3
   ```
   ```
   [*PE2-GigabitEthernet0/2/1] quit
   ```
   ```
   [*PE2] interface gigabitethernet 0/3/1
   ```
   ```
   [*PE2-GigabitEthernet0/3/1] undo shutdown
   ```
   ```
   [*PE2-GigabitEthernet0/3/1] eth-trunk 1
   ```
   ```
   [*PE2-GigabitEthernet0/3/1] commit
   ```
   ```
   [~PE2-GigabitEthernet0/3/1] quit
   ```
3. Verify the configuration.
   
   
   
   Run the [**display trunkmembership eth-trunk**](cmdqueryname=display+trunkmembership+eth-trunk) command in any view. The command output shows the weight of every member interface of the Eth-Trunk interface, manual load balancing mode and up state of the Eth-Trunk interface. Use the command output on PE1 as an example.
   
   ```
   [*PE1] display trunkmembership eth-trunk 1
   ```
   ```
   Trunk ID: 1
   used status: VALID
   TYPE: ethernet
   Working Mode : Normal
   Number Of Ports in Trunk = 3
   Number Of Up Ports in Trunk = 3
   operate status: up
   
   Interface GigabitEthernet0/1/1, valid, operate up, weight 1,
   Interface GigabitEthernet0/2/1, valid, operate up, weight 3,
   Interface GigabitEthernet0/3/1, valid, operate up, weight 1,
   ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  interface Eth-Trunk1
   #
  interface GigabitEthernet0/1/1
   undo shutdown
   eth-trunk 1
  #
  interface GigabitEthernet0/2/1
   undo shutdown
   eth-trunk 1
   distribute-weight 3
  #
  interface GigabitEthernet0/3/1
   undo shutdown
   eth-trunk 1
  #
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  interface Eth-Trunk1
   #
  interface GigabitEthernet0/1/1
   undo shutdown
   eth-trunk 1
  #
  interface GigabitEthernet0/2/1
   undo shutdown
   eth-trunk 1
   distribute-weight 3
  #
  interface GigabitEthernet0/3/1
   undo shutdown
   eth-trunk 1
  admin
  return
  ```
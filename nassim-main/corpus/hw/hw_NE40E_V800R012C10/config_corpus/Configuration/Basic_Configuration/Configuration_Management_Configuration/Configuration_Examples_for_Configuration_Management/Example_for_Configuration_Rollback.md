Example for Configuration Rollback
==================================

This section provides an example for configuration rollback where a user detects an IP address configuration error and expects system configurations to roll back to what they were before the IP addresses were configured.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172360025__fig_dc_vrp_cfgm_cfg_004501), a user logs in to the Router and configures IP addresses for interfaces on the Router. After the IP addresses of interfaces are configured, the user detects an IP address planning error and expects to reconfigure the IP addresses of interfaces. Traditionally speaking, the user must delete the IP addresses one by one and reconfigure them.

Configuration rollback simplifies configuration restoration. Configuration rollback allows the user to easily roll system configurations back to what they were before the IP addresses were configured.

**Figure 1** Configuration rollback![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 4 in this example represent GE 0/1/0, GE 0/1/1, GE 0/1/2, and GE 0/1/3, respectively.


  
![](images/fig_dc_vrp_cfgm_cfg_004501.png)  


#### Precautions

None


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IP addresses for interfaces on the Router.
2. Check information about configuration rollback points and configuration changes at the most recent configuration rollback points.
3. Perform configuration rollback by selecting a configuration rollback point to which system configurations are expected to roll back or the number of configuration rollback points that a configuration rollback operation is expected to undergo.

#### Data Preparation

To complete the configuration, you need the following data:

* GE 0/1/0, GE 0/1/1, GE 0/1/2, and GE 0/1/3 on the Router
* IP addresses for the preceding interfaces: 10.0.0.1/30, 10.0.1.1/30, 10.0.2.1/30, and 10.0.3.1/30

#### Procedure

1. Configure IP addresses for GE 0/1/0, GE 0/1/1, GE 0/1/2, and GE 0/1/3 on the Router.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] interface gigabitethernet 0/1/0
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/0] ip address 10.0.0.1 30
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/0] quit
   ```
   ```
   [*HUAWEI] interface gigabitethernet 0/1/1
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/1] ip address 10.0.1.1 30
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/1] quit
   ```
   ```
   [*HUAWEI] interface gigabitethernet 0/1/2
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/2] ip address 10.0.2.1 30
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/2] quit
   ```
   ```
   [*HUAWEI] interface gigabitethernet 0/1/3
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/3] ip address 10.0.3.1 30
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/3] quit
   ```
   ```
   [*HUAWEI] commit description IP address
   ```
   ```
   [~HUAWEI] quit
   ```
2. Check information about configuration rollback points and the differences between the previous and current configurations.
   
   
   
   # Display information about configuration rollback points.
   
   ```
   <HUAWEI> display configuration commit list verbose
   ```
   ```
   1) CommitId: 1000000006
           Label: -
           User: root
           User-Intf: VTY 1
           Type: CLI
           TimeStamp: 2012-06-29 15:55:20
           Description: IP address 
   
   2) CommitId: 1000000005
           Label: -
           User: root
           User-Intf: VTY 0
           Type: CLI
           TimeStamp: 2012-06-29 11:04:05
           Description: 
   
   3) CommitId: 1000000004
           Label: -
           User: root
           User-Intf: VTY 0
           Type: CLI
           TimeStamp: 2012-06-29 09:57:34
           Description: 
   
   4) CommitId: 1000000003
           Label: -
           User: root
           User-Intf: VTY 0
           Type: CLI
           TimeStamp: 2012-06-29 09:57:21
           Description: 
   
   5) CommitId: 1000000002
           Label: -
           User: anonymous
           User-Intf: CON 1023
           Type: CLI
           TimeStamp: 2012-06-28 16:31:48
           Description: 
   
   6) CommitId: 1000000001
           Label: -
           User: anonymous
           User-Intf: CON 1023
           Type: CLI
           TimeStamp: 2012-06-28 16:31:48
           Description:
   ```
   
   # Display the configuration changes at the most recent configuration rollback point.
   
   ```
   <HUAWEI> display configuration commit changes last 1
   ```
   ```
   Building configuration
   
     #
     interface GigabitEthernet0/1/0
   +  ip address 10.0.0.1 255.255.255.252
     #
     interface GigabitEthernet0/1/1
   +  ip address 10.0.1.1 255.255.255.252
     #
     interface GigabitEthernet0/1/2
   +  ip address 10.0.2.1 255.255.255.252
     #
     interface GigabitEthernet0/1/3
   +  ip address 10.0.3.1 255.255.255.252
     #
   ```
3. Perform configuration rollback.
   
   
   
   # Roll system configurations back to what they were before the most recent configuration rollback point was created.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In this example, the [**rollback configuration last 1**](cmdqueryname=rollback+configuration+last+1) command has the same return result as the [**rollback configuration to commit-id 1000000005**](cmdqueryname=rollback+configuration+to+commit-id+1000000005) command, both indicating that system configurations are rolled back to what they were before configuration rollback point 6 was generated.
   
   ```
   <HUAWEI> rollback configuration last 1
   ```
   
   # After the configuration rollback operation is complete, check whether a configuration rollback point has been generated.
   
   ```
   <HUAWEI> display configuration commit list verbose
   ```
   ```
   1) CommitId: 1000000007
           Label: -
           User: root
           User-Intf: VTY 1
           Type: ROLLBACK
           TimeStamp: 2012-06-29 15:58:22
           Description: 
   
   2) CommitId: 1000000006
           Label: -
           User: root
           User-Intf: VTY 1
           Type: CLI
           TimeStamp: 2012-06-29 15:55:20
           Description: IP address 
   
   3) CommitId: 1000000005
           Label: -
           User: root
           User-Intf: VTY 0
           Type: CLI
           TimeStamp: 2012-06-29 11:04:05
           Description: 
   
   4) CommitId: 1000000004
           Label: -
           User: root
           User-Intf: VTY 0
           Type: CLI
           TimeStamp: 2012-06-29 09:57:34
           Description: 
   
   5) CommitId: 1000000003
           Label: -
           User: root
           User-Intf: VTY 0
           Type: CLI
           TimeStamp: 2012-06-29 09:57:21
           Description: 
   
   6) CommitId: 1000000002
           Label: -
           User: anonymous
           User-Intf: CON 1023
           Type: CLI
           TimeStamp: 2012-06-28 16:31:48
           Description: 
   
   7) CommitId: 1000000001
           Label: -
           User: anonymous
           User-Intf: CON 1023
           Type: CLI
           TimeStamp: 2012-06-28 16:31:48
           Description: 
   ```
4. Verify the configuration.
   
   
   
   # Check that the configuration rollback operation is successful.
   
   ```
   <HUAWEI> display current-configuration interface
   ```
   ```
   #
   interface GigabitEthernet0/1/0
    undo shutdown
   #
   interface GigabitEthernet0/1/1
    undo shutdown
   #
   interface GigabitEthernet0/1/2
    undo shutdown
   #
   interface GigabitEthernet0/1/3
    undo shutdown
   #
   ```

#### Configuration Files

None.
Example for Configuring an NQA Test Group
=========================================

You can monitor the status of multiple links by binding an NQA test group to multiple NQA test instances.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0000001414302185__fig_dc_vrp_network-monitor_feature_008601), default routes are configured on DeviceA to import traffic from DeviceC to DeviceB1 and DeviceB2. The default routes are associated with an NQA test group that is bound to ICMP test instances **test1** and **test2** on DeviceA.

**Figure 1** NQA test group detection![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent GE 0/1/1 and GE 0/1/2, respectively.


  
![](figure/en-us_image_0000001363281364.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure NQA test instances and start the tests.
2. Configure an NQA test group.
3. Bind the NQA test group to test instances.

#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of DeviceB1 and DeviceB2.

#### Procedure

1. Configure NQA test instances and start the tests.
   
   
   ```
   <DeviceA> system-view
   ```
   ```
   [~DeviceA] nqa test-instance admin1 test1
   ```
   ```
   [~DeviceA-nqa-admin1-test1] test-type icmp
   ```
   ```
   [*DeviceA-nqa-admin1-test1] destination-address ipv4 10.1.1.1
   ```
   ```
   [*DeviceA-nqa-admin1-test1] frequency 15
   ```
   ```
   [*DeviceA-nqa-admin1-test1] start now
   ```
   ```
   [*DeviceA-nqa-admin1-test1] commit
   ```
   ```
   [~DeviceA-nqa-admin1-test1] quit
   ```
   ```
   [~DeviceA] nqa test-instance admin2 test2
   ```
   ```
   [~DeviceA-nqa-admin2-test2] test-type icmp
   ```
   ```
   [*DeviceA-nqa-admin2-test2] destination-address ipv4 10.2.2.2
   ```
   ```
   [*DeviceA-nqa-admin2-test2] frequency 15
   ```
   ```
   [*DeviceA-nqa-admin2-test2] start now
   ```
   ```
   [*DeviceA-nqa-admin2-test2] commit
   ```
   ```
   [~DeviceA-nqa-admin2-test2] quit
   ```
2. Configure an NQA test group.
   
   
   ```
   [~DeviceA] nqa group group1
   ```
   ```
   [*DeviceA-nqa-group-group1] operator and
   ```
   ```
   [*DeviceA-nqa-group-group1] description this is an nqa group
   ```
   ```
   [*DeviceA-nqa-group-group1] commit
   ```
3. Bind the NQA test group to test instances.
   
   
   ```
   [~DeviceA-nqa-group-group1] nqa test-instance admin1 test1
   ```
   ```
   [*DeviceA-nqa-group-group1] nqa test-instance admin2 test2
   ```
   ```
   [*DeviceA-nqa-group-group1] commit
   ```
   ```
   [~DeviceA-nqa-group-group1] quit
   ```
4. Verify the configuration. 
   
   
   ```
   [~DeviceA] display nqa group
   ```
   ```
   NQA-group information:
   ------------------------------------------------------------------------
   NQA-group group1
   Status: DOWN       Operator: AND     
   ------------------------------------------------------------------------
   Admin-name                       Test-name                        Status
   ------------------------------------------------------------------------
   admin1                           test1                            DOWN    
   admin2                           test2                            DOWN    
   ```

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  sysname DeviceA
  #
  interface GigabitEthernet0/1/1
   ip address 192.168.1.1 255.255.255.0
  #
  interface GigabitEthernet0/1/2
   ip address 192.168.1.2 255.255.255.0
  #
  nqa test-instance admin1 test1
   test-type icmp
   destination-address ipv4 10.1.1.1
   frequency 15
   start now
  #
  nqa test-instance admin2 test2
   test-type icmp
   destination-address ipv4 10.2.2.2
   frequency 15
   start now
  #
  nqa group group1
   description this is an nqa group
   operator and
   nqa test-instance admin1 test1
   nqa test-instance admin2 test2
  #
  return
  ```
* DeviceB1 configuration file
  ```
  #
  sysname DeviceB1
  #
  interface GigabitEthernet0/1/1
   ip address 10.1.1.1 255.255.255.0
  #
  return
  ```
* DeviceB2 configuration file
  ```
  #
  sysname DeviceB2
  #
  interface GigabitEthernet0/1/1
   ip address 10.2.2.2 255.255.255.0
  #
  return
  ```
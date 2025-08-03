Example for Configuring LLDP in a Single-Neighbor Networking Scenario
=====================================================================

Example for Configuring LLDP in a Single-Neighbor Networking Scenario

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000002056421438__fig103091844183012), DeviceA and DeviceB are directly connected, the NMS has reachable routes to DeviceA and DeviceB, and SNMP is configured on the devices and NMS.

A network administrator wants to obtain link communication information between DeviceA and DeviceB, and alarms of device function changes to learn details about the network topology and configuration conflicts.

**Figure 1** Single-neighbor networking  
![](figure/en-us_image_0000002092540037.png)
![](public_sys-resources/note_3.0-en-us.png) 

In this example, each LLDP interface represents 100GE1/0/1.



#### Configuration Roadmap

To obtain the link communication information between DeviceA and DeviceB from the NMS, configure LLDP on the devices. The configuration roadmap is as follows:

1. Enable LLDP globally on DeviceA and DeviceB.
2. Configure management IP addresses for DeviceA and DeviceB.


#### Procedure

1. Configure IP addresses and routing protocols for interfaces, as shown in [Figure 1](#EN-US_TASK_0000002056421438__fig103091844183012). For details, see Configuration Scripts.
2. Enable LLDP globally on DeviceA and DeviceB.
   
   # Configure DeviceA.
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] lldp enable
   [~DeviceA] commit
   ```
   
   # Configure DeviceB.
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] lldp enable
   [~DeviceB] commit
   ```
3. Configure management IP addresses for DeviceA and DeviceB.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The IP address specified in the [**lldp management-address**](cmdqueryname=lldp+management-address) command is the IP address of the LLDP interface. For details about how to configure an IP address for an LLDP interface, see Configuration Scripts.
   
   
   # Configure DeviceA.
   ```
   [~DeviceA] lldp management-address 10.10.10.1
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   ```
   [~DeviceB] lldp management-address 10.10.10.2
   [*DeviceB] commit
   ```
4. (Optional) Configure LLDP parameters for DeviceA and DeviceB. These parameters include the interval and delay for sending LLDP packets.
   
   # Configure DeviceA.
   ```
   [~DeviceA] lldp transmit interval 60
   [*DeviceA] lldp transmit delay 9
   [*DeviceA] commit
   ```
   
   The configuration of DeviceB is similar to that of DeviceA. For details, see Configuration Scripts.
5. (Optional) Enable the LLDP trap function for DeviceA and DeviceB and configure a delay for the devices to send LLDP traps.
   
   # Configure DeviceA.
   ```
   [~DeviceA] snmp-agent trap enable feature-name lldp
   [~DeviceA] lldp trap-interval 10
   [*DeviceA] commit
   ```
   
   The configuration of DeviceB is similar to that of DeviceA. For details, see Configuration Scripts.
6. Verify the configuration.
   
   # Check neighbor information of DeviceA.
   ```
   [~DeviceA] display lldp neighbor brief
   Local Interface         Exptime(s) Neighbor Interface      Neighbor Device      
   ------------------------------------------------------------------------------- 
   100GE1/0/1               115       100GE1/0/1                DeviceB
   ```
   
   # Check neighbor information of DeviceB.
   ```
   [~DeviceB] display lldp neighbor brief
   Local Interface         Exptime(s) Neighbor Interface      Neighbor Device      
   ------------------------------------------------------------------------------- 
   100GE1/0/1               115       100GE1/0/1                DeviceA
   ```

#### Configuration Scripts

* DeviceA
  
  ```
  #
   sysname DeviceA
  #
  lldp enable
  lldp transmit interval 60
  lldp transmit delay 9
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.10.10.1 255.255.255.0
  #
   
  lldp management-address  10.10.10.1
  snmp-agent trap enable feature-name lldp
  lldp trap-interval 10
  #
  return
  ```
* DeviceB
  
  ```
  #
   sysname DeviceB
  #
  lldp enable
  lldp transmit interval 60
  lldp transmit delay 9
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.10.10.2 255.255.255.0
  #
   
  lldp management-address  10.10.10.2
  snmp-agent trap enable feature-name lldp
  lldp trap-interval 10
  #
  return
  ```
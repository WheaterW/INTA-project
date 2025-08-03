Example for Configuring MSTP Multi-Process
==========================================

Example for Configuring MSTP Multi-Process

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001366159869__en-us_task_0000001130783108_fig17195027193012), DeviceA and DeviceB, as PE devices, are connected to CE devices, forming multiple access rings. DeviceA, CE1, and CE2 are in a ring; DeviceB, CE5, and CE6 are in another ring; DeviceA, DeviceB, CE3, and CE4 are in the third ring.

In this case, MSTP multi-process can be deployed to allow each access ring to calculate a spanning tree independently.

**Figure 1** Network diagram of MSTP multi-process![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, interface 3, interface 4, and interface 5 represent 100GE 1/0/1, 100GE 1/0/2, 100GE 1/0/3, 100GE 1/0/4, and 100GE 1/0/5, respectively.


  
![](figure/en-us_image_0000001176742841.png)

#### Procedure

1. Configure basic MSTP functions, add devices to an MST region, and create instances.
   
   
   
   # Add DeviceA to an MST region and create instances.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] stp region-configuration
   [~DeviceA-mst-region] region-name RG1
   [*DeviceA-mst-region] instance 1 vlan 2 to 100
   [*DeviceA-mst-region] instance 2 vlan 101 to 200
   [*DeviceA-mst-region] instance 3 vlan 201 to 300
   [*DeviceA-mst-region] quit
   [*DeviceA] commit
   ```
   
   # Add DeviceB to the MST region and create instances.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] stp region-configuration
   [~DeviceB-mst-region] region-name RG1
   [*DeviceB-mst-region] instance 1 vlan 2 to 100
   [*DeviceB-mst-region] instance 2 vlan 101 to 200
   [*DeviceB-mst-region] instance 3 vlan 201 to 300
   [*DeviceB-mst-region] quit
   [*DeviceB] commit
   ```
2. Enable MSTP on DeviceA and DeviceB.
   
   
   
   By default, STP, RSTP, or MSTP is enabled on a device. You can run the [**stp enable**](cmdqueryname=stp+enable) command in the system view to enable this function if it is disabled.
3. Create multiple MSTP processes on the devices and add ports to the processes.
   
   
   
   # On DeviceA, create process 1 and process 2, and add 100GE 1/0/3 and 100GE 1/0/4 to process 1 and 100GE 1/0/2 to process 2.
   
   ```
   [~DeviceA] stp process 1
   [*DeviceA-mst-process-1] quit
   [*DeviceA] stp process 2
   [*DeviceA-mst-process-2] quit
   [*DeviceA] interface 100ge 1/0/4
   [*DeviceA-100GE1/0/4] portswitch
   [*DeviceA-100GE1/0/4] stp binding process 1
   [*DeviceA-100GE1/0/4] quit
   [*DeviceA] interface 100ge 1/0/3
   [*DeviceA-100GE1/0/3] stp binding process 1
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] portswitch
   [*DeviceA-100GE1/0/2] stp binding process 2
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```
   
   # On DeviceB, create process 2 and process 3, and add 100GE 1/0/3 and 100GE 1/0/4 to process 3 and 100GE 1/0/2 to process 2.
   
   ```
   [~DeviceB] stp process 2
   [*DeviceB-mst-process-2] quit
   [*DeviceB] stp process 3
   [*DeviceB-mst-process-3] quit
   [*DeviceB] interface 100ge 1/0/4
   [*DeviceB-100GE1/0/4] portswitch
   [*DeviceB-100GE1/0/4] stp binding process 3
   [*DeviceB-100GE1/0/4] quit
   [*DeviceB] interface 100ge 1/0/3
   [*DeviceB-100GE1/0/3] portswitch
   [*DeviceB-100GE1/0/3] stp binding process 3
   [*DeviceB-100GE1/0/3] quit
   [*DeviceB] interface 100ge 1/0/2
   [*DeviceB-100GE1/0/2] portswitch
   [*DeviceB-100GE1/0/2] stp binding process 2
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] commit
   ```
4. Configure a shared link.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] portswitch
   [~DeviceA-100GE1/0/1] stp binding process 2 link-share
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] interface 100ge 1/0/1
   [~DeviceB-100GE1/0/1] portswitch
   [~DeviceB-100GE1/0/1] stp binding process 2 link-share
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] commit
   ```
5. Enable MSTP for processes.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] stp process 1
   [~DeviceA-mst-process-1] stp enable
   [*DeviceA-mst-process-1] quit
   [*DeviceA] stp process 2
   [*DeviceA-mst-process-2] stp enable
   [*DeviceA-mst-process-2] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] stp process 3
   [~DeviceB-mst-process-3] stp enable
   [*DeviceB-mst-process-3] quit
   [*DeviceB] stp process 2
   [*DeviceB-mst-process-2] stp enable
   [*DeviceB-mst-process-2] quit
   [*DeviceB] commit
   ```
6. Configure other functions.
   
   
   
   # On DeviceA, configure priorities and root protection.
   
   ```
   [~DeviceA] stp process 1
   [~DeviceA-mst-process-1] stp instance 0 root primary
   [*DeviceA-mst-process-1] stp instance 1 root primary
   [*DeviceA-mst-process-1] quit
   [*DeviceA] stp process 2
   [*DeviceA-mst-process-2] stp instance 0 root primary
   [*DeviceA-mst-process-2] stp instance 2 root primary
   [*DeviceA-mst-process-2] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] portswitch
   [*DeviceA-100GE1/0/2] stp root-protection
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```
   
   # On DeviceB, configure priorities and root protection.
   
   ```
   [~DeviceB] stp process 3
   [~DeviceB-mst-process-3] stp instance 0 root primary
   [*DeviceB-mst-process-3] stp instance 3 root primary
   [*DeviceB-mst-process-3] quit
   [*DeviceB] stp process 2
   [*DeviceB-mst-process-2] stp instance 0 root secondary
   [*DeviceB-mst-process-2] stp instance 2 root secondary
   [*DeviceB-mst-process-2] quit
   [*DeviceB] interface 100ge 1/0/2
   [*DeviceB] portswitch
   [*DeviceB-100GE1/0/2] stp root-protection
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] commit
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   * In each ring, the CE devices have lower MSTP process priorities than the PE device.
   * For DeviceA and DeviceB in the dual-access ring, you are recommended to configure them as the primary or a secondary root bridge in different instances.
   
   # On DeviceA, enable shared link protection for the MSTP process.
   
   ```
   [~DeviceA] stp process 2
   [~DeviceA-mst-process-2] stp link-share-protection
   [*DeviceA-mst-process-2] quit
   [*DeviceA] commit
   ```
   
   # On DeviceB, enable shared link protection for the MSTP process.
   
   ```
   [~DeviceB] stp process 2
   [~DeviceB-mst-process-2] stp link-share-protection
   [*DeviceB-mst-process-2] quit
   [*DeviceB] commit
   ```
7. Create VLANs and add ports to the VLANs.
   
   
   
   # On DeviceA, create VLANs 2 to 200, and add 100GE 1/0/3 and 100GE 1/0/4 to VLANs 2 to 100 and 100GE 1/0/1 and 100GE 1/0/2 to VLANs 101 to 200.
   
   ```
   [~DeviceA] vlan batch 2 to 200
   [*DeviceA] interface 100ge 1/0/3
   [*DeviceB-100GE1/0/3] portswitch
   [*DeviceA-100GE1/0/3] port link-type trunk
   [*DeviceA-100GE1/0/3] port trunk allow-pass vlan 2 to 100
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] interface 100ge 1/0/4
   [*DeviceA-100GE1/0/4] portswitch
   [*DeviceA-100GE1/0/4] port link-type trunk
   [*DeviceA-100GE1/0/4] port trunk allow-pass vlan 2 to 100
   [*DeviceA-100GE1/0/4] quit
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] portswitch
   [*DeviceA-100GE1/0/1] port link-type trunk 
   [*DeviceA-100GE1/0/1] port trunk allow-pass vlan 101 to 200
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] portswitch
   [*DeviceA-100GE1/0/2] port link-type trunk 
   [*DeviceA-100GE1/0/2] port trunk allow-pass vlan 101 to 200
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```
   
   # On DeviceB, create VLANs 101 to 300, and add 100GE 1/0/3 and 100GE 1/0/4 to VLANs 201 to 300 and 100GE 1/0/1 and 100GE 1/0/2 to VLANs 101 to 200.
   
   ```
   [~DeviceB] vlan batch 101 to 300
   [*DeviceB] interface 100ge 1/0/3
   [*DeviceB-100GE1/0/3] portswitch
   [*DeviceB-100GE1/0/3] port link-type trunk
   [*DeviceB-100GE1/0/3] port trunk allow-pass vlan 201 to 300
   [*DeviceB-100GE1/0/3] quit
   [*DeviceB] interface 100ge 1/0/4
   [*DeviceB-100GE1/0/4] portswitch
   [*DeviceB-100GE1/0/4] port link-type trunk
   [*DeviceB-100GE1/0/4] port trunk allow-pass vlan 201 to 300
   [*DeviceB-100GE1/0/4] quit
   [*DeviceB] interface 100ge 1/0/1
   [*DeviceB-100GE1/0/1] portswitch
   [*DeviceB-100GE1/0/1] port link-type trunk
   [*DeviceB-100GE1/0/1] port trunk allow-pass vlan 101 to 200
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] interface 100ge 1/0/2
   [*DeviceB-100GE1/0/2] portswitch
   [*DeviceB-100GE1/0/2] port link-type trunk
   [*DeviceB-100GE1/0/2] port trunk allow-pass vlan 101 to 200
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] commit
   ```

#### Verifying the Configuration

* Run the [**display stp interface brief**](cmdqueryname=display+stp+interface+brief) command on DeviceA.
  
  # 100GE 1/0/4 is a designated port in the CIST of MSTP process 1 and in instance 1.
  
  ```
  [~DeviceA] display stp process 1 interface 100ge 1/0/4 brief
   MSTID      Port                    Role  STP State       Protection
     0        100GE1/0/4              DESI  FORWARDING      NONE
     1        100GE1/0/4              DESI  FORWARDING      NONE
  ```
  
  # 100GE 1/0/2 is a designated port in the CIST of MSTP process 2 and in instance 2.
  
  ```
  [~DeviceA] display stp process 2 interface 100ge 1/0/2 brief
   MSTID      Port                    Role  STP State       Protection
     0        100GE1/0/2              DESI  FORWARDING      ROOT
     2        100GE1/0/2              DESI  FORWARDING      ROOT
  ```
* Run the [**display stp interface brief**](cmdqueryname=display+stp+interface+brief) command on DeviceB.
  
  # 100GE 1/0/4 is a designated port in the CIST of MSTP process 3 and in instance 3.
  
  ```
  [~DeviceB] display stp process 3 interface 100ge 1/0/4 brief
   MSTID      Port                    Role  STP State       Protection
     0        100GE1/0/4              DESI  FORWARDING      NONE
     3        100GE1/0/4              DESI  FORWARDING      NONE
  ```
  
  # 100GE 1/0/2 is a designated port in the CIST of MSTP process 2 and in instance 2.
  
  ```
  [~DeviceB] display stp process 2 interface 100ge 1/0/2 brief
   MSTID      Port                    Role  STP State       Protection
     0        100GE1/0/2              DESI  FORWARDING      ROOT
     2        100GE1/0/2              DESI  FORWARDING      ROOT
  ```

#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  vlan batch 2 to 200
  #
  stp region-configuration
   region-name RG1
   instance 1 vlan 2 to 100
   instance 2 vlan 101 to 200
   instance 3 vlan 201 to 300
  #
  stp process 1
   stp instance 0 root primary
   stp instance 1 root primary
   stp enable
  stp process 2
   stp instance 0 root primary
   stp instance 2 root primary
   stp link-share-protection
   stp enable
  #
  interface 100GE1/0/1
   port link-type trunk
   port trunk allow-pass vlan 101 to 200
   stp binding process 2 link-share
  #
  interface 100GE1/0/2
   port link-type trunk
   port trunk allow-pass vlan 101 to 200
   stp binding process 2
   stp root-protection
  #
  interface 100GE1/0/3
   port link-type trunk
   port trunk allow-pass vlan 2 to 100
   stp binding process 1
  #
  interface 100GE1/0/4
   port link-type trunk
   port trunk allow-pass vlan 2 to 100
   stp binding process 1
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  vlan batch 101 to 300
  #
  stp region-configuration
   region-name RG1
   instance 1 vlan 2 to 100
   instance 2 vlan 101 to 200
   instance 3 vlan 201 to 300
  #
  stp process 2
   stp instance 0 root secondary
   stp instance 2 root secondary
   stp link-share-protection
   stp enable
  stp process 3
   stp instance 0 root primary
   stp instance 3 root primary
   stp enable
  #
  interface 100GE1/0/1
   port link-type trunk
   port trunk allow-pass vlan 101 to 200
   stp binding process 2 link-share
  #
  interface 100GE1/0/2
   port link-type trunk
   port trunk allow-pass vlan 101 to 200
   stp binding process 2
   stp root-protection
  #
  interface 100GE1/0/3
   port link-type trunk
   port trunk allow-pass vlan 201 to 300
   stp binding process 3
  #
  interface 100GE1/0/4
   port link-type trunk
   port trunk allow-pass vlan 201 to 300
   stp binding process 3
  #
  return
  ```
Example for Configuring MSTP
============================

Example for Configuring MSTP

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001315390982__en-us_task_0000001176662865_fig1591461911549), there is a loop between DeviceA, DeviceB, DeviceC, and DeviceD. In this case, MSTP can be deployed on the network to break the loop, avoid broadcast storms and MAC address flapping, and implement load balancing for traffic of VLANs 2 to 10 and VLANs 11 to 20.

**Figure 1** Network diagram of MSTP![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](figure/en-us_image_0000001176662901.png)

#### Procedure

1. Configure the same MST region **RG1** on DeviceA, DeviceB, DeviceC, and DeviceD and create MSTI 1 and MSTI 2.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   Two devices belong to the same MST region when they have the same MST region name, VLAN-to-MSTI mappings, and revision level of the MST region.
   
   A VLAN can be mapped to only one MSTI. If you map a VLAN to multiple MSTIs, only the latest one will take effect.
   
   # Configure an MST region on DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] stp region-configuration
   [~DeviceA-mst-region] region-name RG1
   [*DeviceA-mst-region] instance 1 vlan 2 to 10
   [*DeviceA-mst-region] instance 2 vlan 11 to 20
   [*DeviceA-mst-region] quit
   [*DeviceA] commit
   ```
   
   # Configure an MST region on DeviceB.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] stp region-configuration
   [~DeviceB-mst-region] region-name RG1
   [*DeviceB-mst-region] instance 1 vlan 2 to 10
   [*DeviceB-mst-region] instance 2 vlan 11 to 20
   [*DeviceB-mst-region] quit
   [*DeviceB] commit
   ```
   
   # Configure an MST region on DeviceC.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceC
   [*HUAWEI] commit
   [~DeviceC] stp region-configuration
   [~DeviceC-mst-region] region-name RG1
   [*DeviceC-mst-region] instance 1 vlan 2 to 10
   [*DeviceC-mst-region] instance 2 vlan 11 to 20
   [*DeviceC-mst-region] quit
   [*DeviceC] commit
   ```
   
   # Configure an MST region on DeviceD.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceD
   [*HUAWEI] commit
   [~DeviceD] stp region-configuration
   [~DeviceD-mst-region] region-name RG1
   [*DeviceD-mst-region] instance 1 vlan 2 to 10
   [*DeviceD-mst-region] instance 2 vlan 11 to 20
   [*DeviceD-mst-region] quit
   [*DeviceD] commit
   ```
2. In the MST region **RG1**, configure the root bridge and a secondary root bridge in MSTI 1 and MSTI 2.
   
   
   
   # Configure DeviceA as the root bridge in MSTI 1.
   
   ```
   [~DeviceA] stp instance 1 root primary
   [*DeviceA] commit
   ```
   
   # Configure DeviceB as a secondary root bridge in MSTI 1.
   
   ```
   [~DeviceB] stp instance 1 root secondary
   [*DeviceB] commit
   ```
   
   # Configure DeviceB as the root bridge in MSTI 2.
   
   ```
   [~DeviceB] stp instance 2 root primary
   [*DeviceB] commit
   ```
   
   # Configure DeviceA as a secondary root bridge in MSTI 2.
   
   ```
   [~DeviceA] stp instance 2 root secondary
   [*DeviceA] commit
   ```
3. Configure the same path cost calculation method for all devices on the network. For the ports to be blocked in MSTI 1 and MSTI 2, set the path costs to be greater than the default value.
   
   
   
   # Configure DeviceA to use the Huawei legacy standard to calculate the path cost.
   
   ```
   [~DeviceA] stp pathcost-standard legacy
   [*DeviceA] commit
   ```
   
   # Configure DeviceB to use the Huawei legacy standard to calculate the path cost.
   
   ```
   [~DeviceB] stp pathcost-standard legacy
   [*DeviceB] commit
   ```
   
   # Configure DeviceC to use the Huawei legacy standard to calculate the path cost, and set the path cost of 100GE 1/0/2 in MSTI 2 to 20000.
   
   ```
   [~DeviceC] stp pathcost-standard legacy
   [*DeviceC] interface 100ge 1/0/2
   [*DeviceC-100GE1/0/2] portswitch
   [*DeviceC-100GE1/0/2] stp instance 2 cost 20000
   [*DeviceC-100GE1/0/2] quit
   [*DeviceC] commit
   ```
   
   # Configure DeviceD to use the Huawei legacy standard to calculate the path cost, and set the path cost of 100GE 1/0/2 in MSTI 1 to 20000.
   
   ```
   [~DeviceD] stp pathcost-standard legacy
   [*DeviceD] interface 100ge 1/0/2
   [*DeviceD-100GE1/0/2] portswitch
   [*DeviceD-100GE1/0/2] stp instance 1 cost 20000
   [*DeviceD-100GE1/0/2] quit
   [*DeviceD] commit
   ```
4. Enable MSTP globally.
   
   
   
   By default, STP, RSTP, or MSTP is enabled on a device. You can run the [**stp enable**](cmdqueryname=stp+enable) command in the system view to enable this function if it is disabled.
5. Disable MSTP on the interfaces connected to terminals.
   
   
   
   # Disable MSTP on 100GE 1/0/1 of DeviceC.
   
   ```
   [~DeviceC] interface 100ge 1/0/1
   [~DeviceC-100GE1/0/1] portswitch
   [~DeviceC-100GE1/0/1] stp disable
   [*DeviceC-100GE1/0/1] quit
   [*DeviceC] commit
   ```
   
   # Disable MSTP on 100GE 1/0/1 of DeviceD.
   
   ```
   [~DeviceD] interface 100ge 1/0/1
   [~DeviceD-100GE1/0/1] portswitch
   [~DeviceD-100GE1/0/1] stp disable
   [*DeviceD-100GE1/0/1] quit
   [*DeviceD] commit
   ```
6. Configure protection functions. For example, configure root protection for the designated ports of the root bridge in each MSTI.
   
   
   
   # Enable root protection on 100GE 1/0/1 of DeviceA.
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] portswitch
   [*DeviceA-100GE1/0/1] stp root-protection
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
   
   # Enable root protection on 100GE 1/0/1 of DeviceB.
   
   ```
   [~DeviceB] interface 100ge 1/0/1
   [*DeviceB-100GE1/0/1] portswitch
   [*DeviceB-100GE1/0/1] stp root-protection
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] commit
   ```
7. Create VLANs and add interfaces to the VLANs.
   
   
   
   # Create VLANs 2 to 20 on DeviceA and add 100GE 1/0/1 and 100GE 1/0/2 on DeviceA to the VLANs.
   
   ```
   [~DeviceA] vlan batch 2 to 20
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] portswitch
   [*DeviceA-100GE1/0/1] port link-type trunk
   [*DeviceA-100GE1/0/1] port trunk allow-pass vlan 2 to 20
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] portswitch
   [*DeviceA-100GE1/0/2] port link-type trunk
   [*DeviceA-100GE1/0/2] port trunk allow-pass vlan 2 to 20
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```
   
   # Create VLANs 2 to 20 on DeviceB and add 100GE 1/0/1 and 100GE 1/0/2 on DeviceB to the VLANs.
   
   ```
   [~DeviceB] vlan batch 2 to 20
   [*DeviceB] interface 100ge 1/0/1
   [*DeviceB-100GE1/0/1] portswitch
   [*DeviceB-100GE1/0/1] port link-type trunk
   [*DeviceB-100GE1/0/1] port trunk allow-pass vlan 2 to 20
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] interface 100ge 1/0/2
   [*DeviceB-100GE1/0/2] portswitch
   [*DeviceB-100GE1/0/2] port link-type trunk
   [*DeviceB-100GE1/0/2] port trunk allow-pass vlan 2 to 20
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] commit
   ```
   
   # Create VLANs 2 to 20 on DeviceC and add 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3 on DeviceC to the VLANs.
   
   ```
   [~DeviceC] vlan batch 2 to 20
   [*DeviceC] interface 100ge 1/0/1
   [*DeviceC-100GE1/0/1] portswitch
   [*DeviceC-100GE1/0/1] port link-type access
   [*DeviceC-100GE1/0/1] port default vlan 2
   [*DeviceC-100GE1/0/1] quit
   [*DeviceC] interface 100ge 1/0/2
   [*DeviceC-100GE1/0/2] portswitch
   [*DeviceC-100GE1/0/2] port link-type trunk
   [*DeviceC-100GE1/0/2] port trunk allow-pass vlan 2 to 20
   [*DeviceC-100GE1/0/2] quit
   [*DeviceC] interface 100ge 1/0/3
   [*DeviceC-100GE1/0/3] portswitch
   [*DeviceC-100GE1/0/3] port link-type trunk
   [*DeviceC-100GE1/0/3] port trunk allow-pass vlan 2 to 20
   [*DeviceC-100GE1/0/3] quit
   [*DeviceC] commit
   ```
   
   # Create VLANs 2 to 20 on DeviceD and add 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3 on DeviceD to the VLANs.
   
   ```
   [~DeviceD] vlan batch 2 to 20
   [*DeviceD] interface 100ge 1/0/1
   [*DeviceD-100GE1/0/1] portswitch
   [*DeviceD-100GE1/0/1] port link-type access
   [*DeviceD-100GE1/0/1] port default vlan 11
   [*DeviceD-100GE1/0/1] quit
   [*DeviceD] interface 100ge 1/0/2
   [*DeviceD-100GE1/0/2] portswitch
   [*DeviceD-100GE1/0/2] port link-type trunk
   [*DeviceD-100GE1/0/2] port trunk allow-pass vlan 2 to 20
   [*DeviceD-100GE1/0/2] quit
   [*DeviceD] interface 100ge 1/0/3
   [*DeviceD-100GE1/0/3] portswitch
   [*DeviceD-100GE1/0/3] port link-type trunk
   [*DeviceD-100GE1/0/3] port trunk allow-pass vlan 2 to 20
   [*DeviceD-100GE1/0/3] quit
   [*DeviceD] commit
   ```

#### Verifying the Configuration

After these configurations have been completed and the network topology becomes stable, perform the following operations to verify the configuration. MSTI 1 and MSTI 2 are used as examples. You do not need to check the interface status in MSTI 0.

# Run the [**display stp brief**](cmdqueryname=display+stp+brief) command on DeviceA to check the port role and status. In MSTI 1, 100GE 1/0/2 and 100GE 1/0/1 on DeviceA are designated ports because DeviceA is the root bridge. In MSTI 2, 100GE 1/0/1 on DeviceA is the designated port and 100GE 1/0/2 on DeviceA is the root port.

```
[~DeviceA] display stp brief
 MSTID  Port             Role  STP State       Protection  Cost       Edged
     0  100GE1/0/1       DESI  forwarding      root           2       disable
     0  100GE1/0/2       DESI  forwarding      none           2       disable
     1  100GE1/0/1       DESI  forwarding      root           2       disable
     1  100GE1/0/2       DESI  forwarding      none           2       disable
     2  100GE1/0/1       DESI  forwarding      root           2       disable
     2  100GE1/0/2       ROOT  forwarding      none           2       disable
```

# Run the [**display stp brief**](cmdqueryname=display+stp+brief) command on DeviceB to check the port role and status. In MSTI 2, 100GE 1/0/1 and 100GE 1/0/2 on DeviceB are designated ports because DeviceB is the root bridge. In MSTI 1, 100GE 1/0/1 on DeviceB is the designated port and 100GE 1/0/2 on DeviceB is the root port.

```
[~DeviceB] display stp brief
 MSTID  Port             Role  STP State       Protection  Cost       Edged
     0  100GE1/0/1       DESI  forwarding      root           2       disable
     0  100GE1/0/2       ROOT  forwarding      none           2       disable
     1  100GE1/0/1       DESI  forwarding      root           2       disable
     1  100GE1/0/2       ROOT  forwarding      none           2       disable
     2  100GE1/0/1       DESI  forwarding      root           2       disable
     2  100GE1/0/2       DESI  forwarding      none           2       disable
```

# Run the [**display stp interface brief**](cmdqueryname=display+stp+interface+brief) command on DeviceC to check the port role and status. 100GE 1/0/3 on DeviceC is the root port in MSTI 1 and MSTI 2. 100GE 1/0/2 on DeviceC is the blocked port in MSTI 2 and is the designated port in MSTI 1.

```
[~DeviceC] display stp interface 100ge 1/0/3 brief
 MSTID  Port             Role  STP State       Protection  Cost       Edged
     0  100GE1/0/3       ROOT  forwarding      none           2       disable
     1  100GE1/0/3       ROOT  forwarding      none           2       disable
     2  100GE1/0/3       ROOT  forwarding      none           2       disable
```
```
[~DeviceC] display stp interface 100ge 1/0/2 brief
 MSTID  Port             Role  STP State       Protection  Cost       Edged
     0  100GE1/0/2       DESI  forwarding      none           2       disable
     1  100GE1/0/2       DESI  forwarding      none           2       disable
     2  100GE1/0/2       ALTE  discarding      none       20000       disable
```

# Run the [**display stp interface brief**](cmdqueryname=display+stp+interface+brief) command on DeviceD to check the port role and status. 100GE 1/0/3 on DeviceD is the root port in MSTI 1 and MSTI 2. 100GE 1/0/2 on DeviceD is the blocked port in MSTI 1 and is the designated port in MSTI 2.

```
[~DeviceD] display stp interface 100ge 1/0/3 brief
 MSTID  Port             Role  STP State       Protection  Cost       Edged
     0  100GE1/0/3       ALTE  discarding      none           2       disable
     1  100GE1/0/3       ROOT  forwarding      none           2       disable
     2  100GE1/0/3       ROOT  forwarding      none           2       disable
```
```
[~DeviceD] display stp interface 100ge 1/0/2 brief
 MSTID  Port             Role  STP State       Protection  Cost       Edged
     0  100GE1/0/2       ROOT  forwarding      none           2       disable
     1  100GE1/0/2       ALTE  discarding      none       20000       disable
     2  100GE1/0/2       DESI  forwarding      none           2       disable
```

#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  vlan batch 2 to 20
  #
  stp instance 1 root primary
  stp instance 2 root secondary
  stp pathcost-standard legacy
  #
  stp region-configuration
   region-name RG1
   instance 1 vlan 2 to 10
   instance 2 vlan 11 to 20
  #
  interface 100GE1/0/1
   port link-type trunk
   port trunk allow-pass vlan 2 to 20
   stp root-protection
  #
  interface 100GE1/0/2
   port link-type trunk
   port trunk allow-pass vlan 2 to 20
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  vlan batch 2 to 20
  #
  stp instance 1 root secondary
  stp instance 2 root primary
  stp pathcost-standard legacy
  #
  stp region-configuration
   region-name RG1
   instance 1 vlan 2 to 10
   instance 2 vlan 11 to 20
  #
  interface 100GE1/0/1
   port link-type trunk
   port trunk allow-pass vlan 2 to 20
   stp root-protection
  #
  interface 100GE1/0/2
   port link-type trunk
   port trunk allow-pass vlan 2 to 20
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  vlan batch 2 to 20
  #
  stp pathcost-standard legacy
  #
  stp region-configuration
   region-name RG1
   instance 1 vlan 2 to 10
   instance 2 vlan 11 to 20
  #
  interface 100GE1/0/1
   port link-type access
   port default vlan 2
   stp disable
  #
  interface 100GE1/0/2
   port link-type trunk
   port trunk allow-pass vlan 2 to 20
   stp instance 2 cost 20000
  #
  interface 100GE1/0/3
   port link-type trunk
   port trunk allow-pass vlan 2 to 20
  #
  return
  ```
* DeviceD
  
  ```
  #
  sysname DeviceD
  #
  vlan batch 2 to 20
  #
  stp pathcost-standard legacy
  #
  stp region-configuration
   region-name RG1
   instance 1 vlan 2 to 10
   instance 2 vlan 11 to 20
  #
  interface 100GE1/0/1
   port link-type access
   port default vlan 11
   stp disable
  #
  interface 100GE1/0/2
   port link-type trunk
   port trunk allow-pass vlan 2 to 20
   stp instance 1 cost 20000
  #
  interface 100GE1/0/3
   port link-type trunk
   port trunk allow-pass vlan 2 to 20
  #
  return
  ```
Example for Configuring Basic VBST Functions
============================================

Example for Configuring Basic VBST Functions

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001513168314__fig15719124213546), DeviceC and DeviceD are dual-homed to DeviceA and DeviceB, respectively, forming a ring network. DeviceC transmits traffic from VLAN 10 and VLAN 20, and DeviceD transmits traffic from VLAN 20 and VLAN 30. The customer wants to deploy VBST on such a network to fulfill the following requirements: Service traffic in each VLAN is correctly forwarded and service traffic from different VLANs is load balanced to improve link efficiency.

**Figure 1** VBST networking![](public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1, 2, 3, 4, and 5 represent 100GE 1/0/1, 100GE 1/0/2, 100GE 1/0/3, 100GE 1/0/4, and 100GE 1/0/5 respectively.


  
![](figure/en-us_image_0000001513048370.png)

#### Procedure

1. Create required VLANs on devices.
   
   
   
   # Create VLAN 10, VLAN 20, and VLAN 30 on DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] vlan batch 10 20 30
   [*DeviceA] commit
   ```
   
   # Create VLAN 10, VLAN 20, and VLAN 30 on DeviceB.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] vlan batch 10 20 30
   [*DeviceB] commit
   ```
   
   # Create VLAN 10 and VLAN 20 on DeviceC.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceC
   [*HUAWEI] commit
   [~DeviceC] vlan batch 10 20
   [*DeviceC] commit
   ```
   
   # Create VLAN 20 and VLAN 30 on DeviceD.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceD
   [*HUAWEI] commit
   [~DeviceD] vlan batch 20 30
   [*DeviceD] commit
   ```
2. Add interfaces to VLANs.
   
   
   
   # On DeviceA, add 100GE 1/0/1 to VLAN 10, VLAN 20, and VLAN 30, 100GE 1/0/2 to VLAN 20 and VLAN 30, and 100GE 1/0/3 to VLAN 10 and VLAN 20.
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] portswitch
   [~DeviceA-100GE1/0/1] port link-type trunk
   [*DeviceA-100GE1/0/1] port trunk allow-pass vlan 10 20 30
   [*DeviceA-100GE1/0/1] undo port trunk allow-pass vlan 1
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] portswitch
   [*DeviceA-100GE1/0/2] port link-type trunk
   [*DeviceA-100GE1/0/2] port trunk allow-pass vlan 20 30
   [*DeviceA-100GE1/0/2] undo port trunk allow-pass vlan 1
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100ge 1/0/3
   [*DeviceA-100GE1/0/3] portswitch
   [*DeviceA-100GE1/0/3] port link-type trunk
   [*DeviceA-100GE1/0/3] port trunk allow-pass vlan 10 20
   [*DeviceA-100GE1/0/3] undo port trunk allow-pass vlan 1
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] commit
   ```
   
   #On DeviceB, add 100GE 1/0/1 to VLAN 10, VLAN 20, and VLAN 30, 100GE 1/0/2 to VLAN 10 and VLAN 20, and 100GE 1/0/3 to VLAN 20 and VLAN 30.
   
   ```
   [~DeviceB] interface 100ge 1/0/1
   [~DeviceB-100GE1/0/1] portswitch
   [~DeviceB-100GE1/0/1] port link-type trunk
   [*DeviceB-100GE1/0/1] port trunk allow-pass vlan 10 20 30
   [*DeviceB-100GE1/0/1] undo port trunk allow-pass vlan 1
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] interface 100ge 1/0/2
   [*DeviceB-100GE1/0/2] portswitch
   [*DeviceB-100GE1/0/2] port link-type trunk
   [*DeviceB-100GE1/0/2] port trunk allow-pass vlan 10 20
   [*DeviceB-100GE1/0/2] undo port trunk allow-pass vlan 1
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] interface 100ge 1/0/3
   [*DeviceB-100GE1/0/3] portswitch
   [*DeviceB-100GE1/0/3] port link-type trunk
   [*DeviceB-100GE1/0/3] port trunk allow-pass vlan 20 30
   [*DeviceB-100GE1/0/3] undo port trunk allow-pass vlan 1
   [*DeviceB-100GE1/0/3] quit
   [*DeviceB] commit
   ```
   
   #On DeviceC, add 100GE 1/0/2 to VLAN 10 and VLAN 20, 100GE 1/0/3 to VLAN 10 and VLAN 20, 100GE 1/0/4 to VLAN 10, and 100GE 1/0/5 to VLAN 20.
   
   ```
   [~DeviceC] interface 100ge 1/0/2
   [~DeviceC-100GE1/0/2] portswitch
   [~DeviceC-100GE1/0/2] port link-type trunk
   [*DeviceC-100GE1/0/2] port trunk allow-pass vlan 10 20
   [*DeviceC-100GE1/0/2] undo port trunk allow-pass vlan 1
   [*DeviceC-100GE1/0/2] quit
   [*DeviceC] interface 100ge 1/0/3
   [*DeviceC-100GE1/0/3] portswitch
   [*DeviceC-100GE1/0/3] port link-type trunk
   [*DeviceC-100GE1/0/3] port trunk allow-pass vlan 10 20
   [*DeviceC-100GE1/0/3] undo port trunk allow-pass vlan 1
   [*DeviceC-100GE1/0/3] quit
   [*DeviceC] interface 100ge 1/0/4
   [*DeviceC-100GE1/0/4] portswitch
   [*DeviceC-100GE1/0/4] port link-type access
   [*DeviceC-100GE1/0/4] port default vlan 10
   [*DeviceC-100GE1/0/4] quit
   [*DeviceC] interface 100ge 1/0/5
   [*DeviceC-100GE1/0/5] portswitch
   [*DeviceC-100GE1/0/5] port link-type access
   [*DeviceC-100GE1/0/5] port default vlan 20
   [*DeviceC-100GE1/0/5] quit
   [*DeviceC] commit
   ```
   
   #On DeviceD, add 100GE 1/0/2 to VLAN 20 and VLAN 30, 100GE 1/0/3 to VLAN 20 and VLAN 30, 100GE 1/0/4 to VLAN 20, and 100GE 1/0/5 to VLAN 30.
   
   ```
   [~DeviceD] interface 100ge 1/0/2
   [~DeviceD-100GE1/0/2] portswitch
   [~DeviceD-100GE1/0/2] port link-type trunk
   [*DeviceD-100GE1/0/2] port trunk allow-pass vlan 20 30
   [*DeviceD-100GE1/0/2] undo port trunk allow-pass vlan 1
   [*DeviceD-100GE1/0/2] quit
   [*DeviceD] interface 100ge 1/0/3
   [*DeviceD-100GE1/0/3] portswitch
   [*DeviceD-100GE1/0/3] port link-type trunk
   [*DeviceD-100GE1/0/3] port trunk allow-pass vlan 20 30
   [*DeviceD-100GE1/0/3] undo port trunk allow-pass vlan 1
   [*DeviceD-100GE1/0/3] quit
   [*DeviceD] interface 100ge 1/0/4
   [*DeviceD-100GE1/0/4] portswitch
   [*DeviceD-100GE1/0/4] port link-type access
   [*DeviceD-100GE1/0/4] port default vlan 20
   [*DeviceD-100GE1/0/4] quit
   [*DeviceD] interface 100ge 1/0/5
   [*DeviceD-100GE1/0/5] portswitch
   [*DeviceD-100GE1/0/5] port link-type access
   [*DeviceD-100GE1/0/5] port default vlan 30
   [*DeviceD-100GE1/0/5] quit
   [*DeviceD] commit
   ```
3. Configure devices to work in VBST mode.
   
   
   
   # Configure DeviceA to work in VBST mode.
   
   ```
   [~DeviceA] stp mode vbst
   [*DeviceA] commit
   ```
   
   # Configure DeviceB to work in VBST mode.
   
   ```
   [~DeviceB] stp mode vbst
   [*DeviceB] commit
   ```
   
   # Configure DeviceC to work in VBST mode.
   
   ```
   [~DeviceC] stp mode vbst
   [*DeviceC] commit
   ```
   
   # Configure DeviceD to work in VBST mode.
   
   ```
   [~DeviceD] stp mode vbst
   [*DeviceD] commit
   ```
4. Configure the root bridges and secondary root bridges in VLANs.
   
   
   
   # Configure DeviceA as the root bridge in VLAN 10.
   
   ```
   [~DeviceA] stp vlan 10 root primary
   [*DeviceA] commit
   ```
   
   # Configure DeviceB as a secondary root bridge in VLAN 10.
   
   ```
   [~DeviceB] stp vlan 10 root secondary
   [*DeviceB] commit
   ```
   
   # Configure DeviceA as the root bridge in VLAN 20.
   
   ```
   [~DeviceA] stp vlan 20 root primary
   [*DeviceA] commit
   ```
   
   # Configure DeviceB as a secondary root bridge in VLAN 20.
   
   ```
   [~DeviceB] stp vlan 20 root secondary
   [*DeviceB] commit
   ```
   
   # Configure DeviceB as the root bridge in VLAN 30.
   
   ```
   [~DeviceB] stp vlan 30 root primary
   [*DeviceB] commit
   ```
   
   # Configure DeviceA as a secondary root bridge in VLAN 30.
   
   ```
   [~DeviceA] stp vlan 30 root secondary
   [*DeviceA] commit
   ```
5. Configure a proper path cost for a port in corresponding VLANs so that the port will be blocked.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   * The path cost range varies depending on the path cost calculation method. In this example, setting the path cost to 2000000 for blocking interfaces complies with the default IEEE 802.1t calculation method.
   * All devices on a network must use the same path cost calculation method.
   
   # Set the path cost of 100GE 1/0/2 on DeviceC to 2000000 in VLAN 10 and VLAN 20.
   
   ```
   [~DeviceC] interface 100ge 1/0/2
   [~DeviceC-100GE1/0/2] stp vlan 10 cost 2000000
   [*DeviceC-100GE1/0/2] stp vlan 20 cost 2000000
   [*DeviceC-100GE1/0/2] quit
   [*DeviceC] commit
   ```
   
   # Set the path cost of 100GE 1/0/2 on DeviceD to 2000000 in VLAN 20 and VLAN 30.
   
   ```
   [~DeviceD] interface 100ge 1/0/2
   [~DeviceD-100GE1/0/2] stp vlan 20 cost 2000000
   [*DeviceD-100GE1/0/2] stp vlan 30 cost 2000000
   [*DeviceD-100GE1/0/2] quit
   [*DeviceD] commit
   ```
6. Enable VBST to eliminate loops.
   
   
   
   Enable VBST globally.
   
   By default, VBST is enabled globally. You can run the [**display stp vlan information**](cmdqueryname=display+stp+vlan+information) command to check the global VBST status. If VBST is disabled globally, run the [**undo stp vlan disable**](cmdqueryname=undo+stp+vlan+disable) command in the system view to enable VBST globally.
   
   Enable VBST in a VLAN.
   
   By default, VBST is enabled in a VLAN. You can run the [**display stp vlan**](cmdqueryname=display+stp+vlan) *vlan-id* **information** command to check the VBST status in a VLAN. If VBST is disabled in the VLAN, run the [**undo stp**](cmdqueryname=undo+stp) **vlan** *vlan-id* **disable** command in the system view to enable VBST in the VLAN.

#### Verifying the Configuration

After the configuration is complete and the network topology becomes stable, perform the following operations to verify the configuration.

# Run the [**display stp vlan bridge local**](cmdqueryname=display+stp+vlan+bridge+local) command on DeviceA to check the spanning tree working mode. In the command output, the Protocol field shows that the device works in VBST mode.

```
[~DeviceA] display stp vlan bridge local
------------------------------------------------------------------
VLANID BridgeID             HelloTime MaxAge ForwardDelay Protocol
------------------------------------------------------------------
   10 10.00e0-fc00-df01            2     20           15     VBST
   20 20.00e0-fc00-df01            2     20           15     VBST
   30 4126.00e0-fc00-df01          2     20           15     VBST
------------------------------------------------------------------
```

# Run the [**display stp vlan information brief**](cmdqueryname=display+stp+vlan+information+brief) command on DeviceA, DeviceB, DeviceC, and DeviceD to check the port status. The command output on DeviceA is used as an example. DeviceA participates in spanning tree calculation in VLAN 10, VLAN 20, and VLAN 30. DeviceA is the root bridge in both VLAN 10 and VLAN 20, so 100GE 1/0/1 and 100GE 1/0/3 are elected as the designated ports in VLAN 10 whereas 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3 are elected as the designated ports in VLAN 20. DeviceA is the secondary root bridge in VLAN 30, so 100GE 1/0/1 and 100GE 1/0/2 are elected as the root port and designated port, respectively, in VLAN 30.

```
[~DeviceA] display stp vlan information brief
--------------------------------------------------------------------------------
VLANID Interface              Role STPState    Protection           Cost Edged
--------------------------------------------------------------------------------
    10 100GE1/0/1             DESI forwarding  none                  200 disable
    10 100GE1/0/3             DESI forwarding  none                  200 disable
    20 100GE1/0/1             DESI forwarding  none                  200 disable
    20 100GE1/0/2             DESI forwarding  none                  200 disable
    20 100GE1/0/3             DESI forwarding  none                  200 disable
    30 100GE1/0/1             ROOT forwarding  none                  200 disable
    30 100GE1/0/2             DESI forwarding  none                  200 disable
--------------------------------------------------------------------------------
```

#### Configuration Scripts

* DeviceA
  ```
  #
  sysname DeviceA
  #
  stp vlan 10 20 root primary
  stp vlan 30 root secondary
  #
  vlan batch 10 20 30
  #
  stp mode vbst
  #
  interface 100GE1/0/1
   port link-type trunk
   undo port trunk allow-pass vlan 1
   port trunk allow-pass vlan 10 20 30
  #
  interface 100GE1/0/2
   port link-type trunk
   undo port trunk allow-pass vlan 1
   port trunk allow-pass vlan 20 30
  #
  interface 100GE1/0/3
   port link-type trunk
   undo port trunk allow-pass vlan 1
   port trunk allow-pass vlan 10 20
  #
  return
  ```
* DeviceB
  ```
  #
  sysname DeviceB
  #
  stp vlan 10 20 root secondary
  stp vlan 30 root primary
  #
  vlan batch 10 20 30
  #
  stp mode vbst
  #
  interface 100GE1/0/1
   port link-type trunk
   undo port trunk allow-pass vlan 1
   port trunk allow-pass vlan 10 20 30
  #
  interface 100GE1/0/2
   port link-type trunk
   undo port trunk allow-pass vlan 1
   port trunk allow-pass vlan 10 20
  #
  interface 100GE1/0/3
   port link-type trunk
   undo port trunk allow-pass vlan 1
   port trunk allow-pass vlan 20 30
  #
  return
  ```
* DeviceC
  ```
  #
  sysname DeviceC
  #
  vlan batch 10 20
  #
  stp mode vbst
  #
  interface 100GE1/0/2
   port link-type trunk
   undo port trunk allow-pass vlan 1
   port trunk allow-pass vlan 10 20
   stp vlan 10 20 cost 2000000
  #
  interface 100GE1/0/3
   port link-type trunk
   undo port trunk allow-pass vlan 1
   port trunk allow-pass vlan 10 20
  #
  interface 100GE1/0/4
   port default vlan 10
  #
  interface 100GE1/0/5
   port default vlan 20
  #
  return
  ```
* DeviceD
  ```
  #
  sysname DeviceD
  #
  vlan batch 20 30
  #
  stp mode vbst
  #
  interface 100GE1/0/2
   port link-type trunk
   undo port trunk allow-pass vlan 1
   port trunk allow-pass vlan 20 30
   stp vlan 20 30 cost 2000000
  #
  interface 100GE1/0/3
   port link-type trunk
   undo port trunk allow-pass vlan 1
   port trunk allow-pass vlan 20 30
  #
  interface 100GE1/0/4
   port default vlan 20
  #
  interface 100GE1/0/5
   port default vlan 30
  #
  return
  ```
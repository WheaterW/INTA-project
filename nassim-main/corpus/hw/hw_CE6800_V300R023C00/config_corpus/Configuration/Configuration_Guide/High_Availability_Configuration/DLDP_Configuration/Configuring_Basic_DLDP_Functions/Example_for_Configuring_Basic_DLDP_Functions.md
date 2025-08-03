Example for Configuring Basic DLDP Functions
============================================

Example for Configuring Basic DLDP Functions

#### Networking Requirements

Device A and Device B are connected by an optical fiber pair as shown in [Figure 1](#EN-US_TASK_0000001465455585__fig_dc_vrp_dldp_cfg_201601). Each fiber in the pair is connected to the Tx end (used for sending packets) on one device and the Rx end (used for receiving packets) on the other device. DLDP is configured on the interfaces connecting the two devices. If the optical fiber connected to the Rx end of DeviceA fails, DeviceA cannot receive optical signals. 100GE1/0/1 on DeviceA goes down and cannot send or receive packets. However, DeviceB can send and receive packets through the optical fibers connected to its Tx and Rx ends, respectively. Therefore, the link of DeviceB remains up. If DeviceB fails to receive DLDPDUs from DeviceA before the Entry Aging timer of the neighbor expires, 100GE1/0/1 of DeviceB becomes unidirectional. DLDP can automatically shut down 100GE1/0/1 on DeviceB to prevent network faults.

**Figure 1** Network diagram of configuring basic DLDP functions  
![](figure/en-us_image_0000001698951613.png)![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 represents 100GE1/0/1.




#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable DLDP to detect unidirectional links.
2. Set an interval for sending Advertisement packets so that DLDP can promptly detect unidirectional links.
3. Set the timeout period of the DelayDown timer to prevent the DLDP-enabled interface from entering the Inactive state and deleting neighbor entries when the neighbor interface frequently alternates between up and down.
4. Configure the authentication mode of DLDPDUs to prevent network attacks.

#### Procedure

1. Enable DLDP globally.
   
   
   
   # Enable DLDP on DeviceA.
   
   ```
   <~HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] dldp enable
   [*DeviceA] commit
   ```
   
   # Enable DLDP on DeviceB.
   
   ```
   <~HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] dldp enable
   [*DeviceB] commit
   ```
2. Enable DLDP on interfaces.
   
   
   
   # Enable DLDP on DeviceA's interface.
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] dldp enable
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
   
   
   
   # Enable DLDP on DeviceB's interface.
   
   ```
   [~DeviceB] interface 100ge 1/0/1
   [~DeviceB-100GE1/0/1] dldp enable
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] commit
   ```
3. Set the working mode of DLDP to normal.
   
   
   
   # Set the working mode of DLDP on DeviceA's interface to normal.
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] [dldp work-mode](cmdqueryname=dldp+work-mode) normal
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
   
   
   
   # Set the working mode of DLDP on DeviceB's interface to normal.
   
   ```
   [~DeviceB] interface 100ge 1/0/1
   [~DeviceB-100GE1/0/1] [dldp work-mode](cmdqueryname=dldp+work-mode) normal
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] commit
   ```
4. Configure a DLDP-compatible mode.
   
   
   
   # Configure the DLDP compatible mode on DeviceA's interface.
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] [dldp compatible-mode enable](cmdqueryname=dldp+compatible-mode+enable) 
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
   
   
   
   # Configure the DLDP compatible mode on DeviceB's interface.
   
   ```
   [~DeviceB] interface 100ge 1/0/1
   [~DeviceB-100GE1/0/1] [dldp compatible-mode enable](cmdqueryname=dldp+compatible-mode+enable)
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] commit
   ```
5. Set the DLDP shutdown mode to manual.
   
   
   
   # Set the DLDP shutdown mode to manual for DeviceA's interface.
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1][dldp unidirectional-shutdown](cmdqueryname=dldp+unidirectional-shutdown) manual 
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
   
   
   
   # Set the DLDP shutdown mode to manual for DeviceB's interface.
   
   ```
   [~DeviceB] interface 100ge 1/0/1
   [~DeviceB-100GE1/0/1] [dldp unidirectional-shutdown](cmdqueryname=dldp+unidirectional-shutdown) manual
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] commit
   ```

#### Verifying the Configuration

# After the configuration is complete, check the status of the DLDP-enabled interface. The command output shows that the interface is in the **advertisement** state.

```
[~DeviceA] display dldp
DLDP global status              : enable 
DLDP work mode                  : normal
DLDP unidirectional shutdown    : manual
The number of enabled ports     : 2
The number of global neighbors  : 2

Interface  100GE1/0/1
DLDP port state                 : advertisement
DLDP link state                 : up 
The neighbor number of the port : 1

   Neighbor  address         : 00-e0-fc-12-34-56
   Neighbor port index          : 5
   Neighbor state               : two way
   Neighbor aged time(s)        : 203
   Neighbor created time        : 2012-04-11 06:16:23

```

As shown in [Figure 1](#EN-US_TASK_0000001465455585__fig_dc_vrp_dldp_cfg_201601), the optical fiber connected to the receive end of DeviceA is removed to simulate a disconnection fault. When a unidirectional link occurs between 100GE1/0/1 on DeviceA and DeviceB, DLDP automatically shuts down 100GE1/0/1 on DeviceB.

# Run the **display dldp** command. The command output shows that the DLDP status of 100GE1/0/1 on DeviceA is **inactive**. The DLDP status of 100GE1/0/1 on Device B is **disable**.

```
[~DeviceA] display dldp interface 100ge 1/0/1
Interface  100GE1/0/1
DLDP port state                 : inactive
DLDP link state                 : down 
The neighbor number of the port : 0
```
```
[~DeviceB] display dldp interface 100ge 1/0/1
Interface  100GE1/0/1 
DLDP port state                 : disable
DLDP link state                 : up 
The neighbor number of the port : 0
```
#### Configuration Scripts

* DeviceA
  ```
  #
   sysname DeviceA
  #
   dldp enable
  #
   dldp work-mode normal
   dldp unidirectional-shutdown manual
  #
  interface 100GE1/0/1
   undo portswitch
   dldp enable
   dldp compatible-mode enable
  #
  return
  ```

* DeviceB
  ```
  #
   sysname DeviceB
  #
   dldp enable
  #
   dldp work-mode normal
   dldp unidirectional-shutdown manual
  #
  interface 100GE1/0/1
   undo portswitch
   dldp enable 
   dldp compatible-mode enable
   #
  return
  ```
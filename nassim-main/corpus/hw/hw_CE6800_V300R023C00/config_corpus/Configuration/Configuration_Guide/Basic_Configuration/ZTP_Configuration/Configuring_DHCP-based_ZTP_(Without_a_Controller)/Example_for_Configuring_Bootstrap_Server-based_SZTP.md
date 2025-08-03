Example for Configuring Bootstrap Server-based SZTP
===================================================

Example for Configuring Bootstrap Server-based SZTP

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001513034414__fig188710432124), DeviceA and DeviceB are two unconfigured devices on the network, and both are connected to DeviceC, which functions as the egress gateway of DeviceA and DeviceB. There are reachable routes between DeviceC and the DHCP server, and between DeviceC and the file server.

The customer requires that DeviceA and DeviceB automatically load the system software and configuration files in SZTP mode after they are powered on.

[Table 1](#EN-US_TASK_0000001513034414__table2075911554408) lists information about DeviceA and DeviceB, and the files to be loaded to them.

**Table 1** Device information and files to be loaded
| New Device | Files to Be Loaded |
| --- | --- |
| DeviceA | * System software: software\_file.cc * Configuration file: conf\_file1.cfg |
| DeviceB | * System software: software\_file.cc * Configuration file: conf\_file2.cfg |


**Figure 1** Network diagram of SZTP![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent 100GE1/0/1, 100GE1/0/2, and 100GE1/0/3, respectively.


  
![](figure/en-us_image_0000001563994697.png)


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure the DHCP server.
2. Configure the DHCP relay agent.
3. Configure the bootstrap server.
4. Configure the HTTPS deployment file server.
5. Power on DeviceA and DeviceB to start the SZTP process.

#### Procedure

1. Configure the DHCP server.
   
   
   
   # Configure the IP address pool that the DHCP server uses to allocate IP addresses to DeviceA and DeviceB and set DHCP options by referring to [Table 2](#EN-US_TASK_0000001513034414__table1812243855410). In this example, a Huawei device is used as the DHCP server.
   
   **Table 2** DHCP server options
   | Option | Description | Value |
   | --- | --- | --- |
   | Option 1 | Subnet mask of an IP address | 255.255.255.0 |
   | Option 3 | Egress gateway of a DHCP client | 10.1.1.1 |
   | Option 143 | IP address of a bootstrap server | 10.1.4.2 |
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname dhcp_server
   [*HUAWEI] commit
   [~dhcp_server] dhcp enable
   [*dhcp_server] ip pool pool1
   [*dhcp_server-ip-pool-pool1] gateway-list 10.1.1.1
   [*dhcp_server-ip-pool-pool1] network 10.1.1.0 mask 255.255.255.0
   [*dhcp_server-ip-pool-pool1] option 143 hex 001268747470733a2f2f31302e312e342e323a31
   [*dhcp_server-ip-pool-pool1] quit
   [~dhcp_server] vlan batch 10
   [*dhcp_server] interface 100ge 1/0/3
   [*dhcp_server-100GE1/0/3] portswitch
   [*dhcp_server-100GE1/0/3] port link-type trunk
   [*dhcp_server-100GE1/0/3] port trunk allow-pass vlan 10
   [*dhcp_server-100GE1/0/3] quit
   [*dhcp_server] interface vlanif 10
   [*dhcp_server-Vlanif10] ip address 10.1.2.2 24
   [*dhcp_server-Vlanif10] quit
   [*dhcp_server] commit
   ```
2. Configure the DHCP relay agent.
   
   
   
   # Configure the DHCP relay function on DeviceC. Set the IP address of the interface connecting DeviceC to DeviceA and DeviceB to 10.1.1.1 to configure DeviceC as the default gateway of DeviceA and DeviceB.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceC
   [*HUAWEI] commit
   [~DeviceC] vlan batch 10
   [*DeviceC] interface 100ge 1/0/1
   [*DeviceC-100GE1/0/1] portswitch
   [*DeviceC-100GE1/0/1] port link-type trunk
   [*DeviceC-100GE1/0/1] port trunk allow-pass vlan 10
   [*DeviceC-100GE1/0/1] port trunk pvid vlan 10
   [*DeviceC-100GE1/0/1] quit
   [*DeviceC] interface 100ge 1/0/2
   [*DeviceC-100GE1/0/2] portswitch 
   [*DeviceC-100GE1/0/2] port link-type trunk
   [*DeviceC-100GE1/0/2] port trunk allow-pass vlan 10
   [*DeviceC-100GE1/0/2] port trunk pvid vlan 10
   [*DeviceC-100GE1/0/2] quit
   [*DeviceC] interface vlanif 10
   [*DeviceC-Vlanif10] ip address 10.1.1.1 24
   [*DeviceC-Vlanif10] quit
   [*DeviceC] dhcp enable
   [*DeviceC] interface vlanif 10
   [*DeviceC-Vlanif10] dhcp select relay
   [*DeviceC-Vlanif10] dhcp relay server-ip 10.1.2.2
   [*DeviceC-Vlanif10] commit
   ```
3. Configure the bootstrap server.
   
   
   
   # Huawei devices do not support the bootstrap server function. In the SZTP networking, a third-party server needs to be deployed. For details about how to configure a third-party server, see the third-party server operation guide.
   
   # Huawei level-2 CA certificate, ownership voucher, and owner certificate need to be built in the bootstrap server.
   
   # On the bootstrap server, set the IP address of the HTTPS file server to 10.1.3.2, and set the deployment files, configuration files, and their paths for DeviceA and DeviceB.
4. Configure the HTTPS deployment file server.
   
   
   
   # Huawei devices do not support the HTTPS server function. In the SZTP networking, a third-party server needs to be deployed. For details about how to configure a third-party server, see the third-party server operation guide.
   
   # After configuring the file server, save the deployment files and configuration files to be loaded to devices to the paths specified on the bootstrap server.
5. Power on DeviceA and DeviceB to start the SZTP process.

#### Verifying the Configuration

# The devices complete the SZTP process in about 15 minutes after they are powered on. Log in to the devices and run the **display startup** command to check whether the current system software and configuration files are the required ones. The following shows the command output of DeviceA.
```
<DeviceA> display startup
MainBoard:                                                                      
  Configured startup system software:        flash:/software_file.cc   
  Startup system software:                   flash:/software_file.cc   
  Next startup system software:              flash:/software_file.cc   
  Startup saved-configuration file:          flash:/conf_file1.cfg
  Next startup saved-configuration file:     flash:/conf_file1.cfg
  Startup paf file:                          default                            
  Next startup paf file:                     default                            
  Startup patch package:                     NULL                               
  Next startup patch package:                NULL                               
  Startup feature software:                  NULL                               
  Next startup feature software:             NULL   
```


#### Configuration Scripts

* DeviceC
  ```
  #
  sysname DeviceC
  #
  vlan batch 10
  #
  dhcp enable
  #
  interface Vlanif10
   ip address 10.1.1.1 255.255.255.0
   dhcp select relay
   dhcp relay server-ip 10.1.2.2
  #
  interface 100GE1/0/1
   port link-type trunk
   port trunk pvid vlan 10
   port trunk allow-pass vlan 10
  #
  interface 100GE1/0/2
   port link-type trunk
   port trunk pvid vlan 10
   port trunk allow-pass vlan 10
  #
  return
  ```
* DHCP server
  ```
  #
  sysname dhcp_server
  #
  dhcp enable
  #
  vlan batch 10
  #
  ip pool pool1
   gateway-list 10.1.1.1
   network 10.1.1.0 mask 255.255.255.0
   option 143 hex 001268747470733a2f2f31302e312e342e323a31
  #
  interface Vlanif10
    ip address 10.1.2.2 255.255.255.0
  #
  interface 100GE1/0/3
   port link-type trunk
   port trunk allow-pass vlan 10
  #
  return
  ```
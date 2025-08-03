Example for Configuring Intermediate File-based ZTP
===================================================

Example for Configuring Intermediate File-based ZTP

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001512675258__fig136901815141415), DeviceA and DeviceB are two unconfigured devices on the network, and both are connected to DeviceC, which functions as the egress gateway of DeviceA and DeviceB. There are reachable routes between DeviceC and the DHCP server, and between DeviceC and the file server.

The customer requires that DeviceA and DeviceB automatically load the system software and configuration files after they are powered on to reduce labor costs and device deployment time.

[Table 1](#EN-US_TASK_0000001512675258__table2075911554408) lists information about DeviceA and DeviceB, and the files to be loaded to them.

**Table 1** Device information and files to be loaded
| New Device | Device ESN | Files to Be Loaded |
| --- | --- | --- |
| DeviceA | 2102311LDL0000000806 | * System software: software\_file.cc * Configuration file: conf\_file.cfg |
| DeviceB | 2102311LDL0000000918 | * System software: software\_file1.cc * Configuration file: conf\_file1.cfg |


**Figure 1** Network diagram of DHCP-based ZTP![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent 100GE1/0/1, 100GE1/0/2, and 100GE1/0/3, respectively.


  
![](figure/en-us_image_0000001512834918.png)


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Edit the intermediate file.
2. Configure the DHCP server.
3. Configure the DHCP relay agent.
4. Configure the file server.
5. Power on DeviceA and DeviceB to start the ZTP process.

#### Procedure

1. Edit the intermediate file. For more information about the fields in an intermediate file, see [Intermediate File in the INI Format](galaxy_ztp_cfg_0031.html) and [Intermediate File in the Python Format](galaxy_ztp_cfg_0132.html). The intermediate file in .ini format is used as an example.
   
   
   
   # Edit the intermediate file in .ini format by referring to [Table 2](#EN-US_TASK_0000001512675258__table1936013581445). The file name is **ztp\_script.ini**. For details about the file content, see [Configuration Scripts](#EN-US_TASK_0000001512675258__postreq24192593172748).
   
   
   
   **Table 2** Fields in an intermediate file in .ini format
   | Field | Description | Value |
   | --- | --- | --- |
   | FILESERVER | Address of the deployment file server. | When deployment files are obtained from an SFTP server, the value is **sftp://sftp\_user:Hyx\_Hy1234@10.1.3.2**. |
   | TIME\_SN | Uniquely identifies a deployment. | 20200526120159 |
   | DEVICE\_TYPE\_NUM | Number of device types. | 2 |
   | ESN | ESN of a device. | The values of DeviceA and DeviceB are as follows:  * 2102311LDL0000000806 * 2102311LDL0000000918 |
   | FILETYPENUM | Number of deployment files to be loaded. | 2 |
   | FILENAME\_*n* | Name of a deployment file. | The values of DeviceA are as follows:  FILENAME\_1=software\_file.cc  FILENAME\_2=cfg\_file.cfg  The values of DeviceB are as follows:  FILENAME\_1=software\_file1.cc  FILENAME\_2=cfg\_file1.cfg |
   | TYPE\_*n* | Type of a deployment file. | TYPE\_1=SOFTWARE  TYPE\_2=CFG |
   | EFFECTIVE\_MODE\_*n* | Activation mode. | EFFECTIVE\_MODE\_1=0  EFFECTIVE\_MODE\_2=0 |
2. Configure the DHCP server.
   
   
   
   # Configure the IP address pool that the DHCP server uses to allocate IP addresses to DeviceA and DeviceB and set DHCP options by referring to [Table 3](#EN-US_TASK_0000001512675258__table1812243855410). In this example, a Huawei device is used as the DHCP server.
   
   **Table 3** DHCP server options
   | Option | Description | Value |
   | --- | --- | --- |
   | Option 1 | Subnet mask of an IP address | 255.255.255.0 |
   | Option 3 | Egress gateway of a DHCP client | 10.1.1.1 |
   | Option 67 | File server address and intermediate file name | sftp://sftp\_user:Hyx\_Hy1234@10.1.3.2/ztp\_script.ini |
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname dhcp_server
   [*HUAWEI] commit
   [~dhcp_server] dhcp enable
   [*dhcp_server] ip pool pool1
   [*dhcp_server-ip-pool-pool1] gateway-list 10.1.1.1
   [*dhcp_server-ip-pool-pool1] network 10.1.1.0 mask 255.255.255.0
   [*dhcp_server-ip-pool-pool1] option 67 cipher sftp://sftp_user:Hyx_Hy1234@10.1.3.2/ztp_script.ini
   [*dhcp_server-ip-pool-pool1] quit
   [*dhcp_server] vlan batch 10
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
3. Configure the DHCP relay agent.
   
   
   
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
4. Configure the file server.
   
   
   
   # If a device is configured as the file server, files will occupy a significant amount of device storage resources. To ensure the device performance, a third-party file server is typically used on a ZTP network. For details about how to configure a third-party file server, see the third-party server operation guide.
   
   # After configuring the file server, save the system software, configuration files, and intermediate files to be loaded to DeviceA and DeviceB in the root directory on the file server.
5. Power on DeviceA and DeviceB to start the ZTP process.

#### Verifying the Configuration

The devices complete the ZTP process in about 15 minutes after they are powered on. Log in to the devices and run the **display startup** command to check whether the current system software and configuration files are the required ones. The following shows the command output of DeviceA.
```
<DeviceA> display startup
MainBoard:                                                                      
  Configured startup system software:        flash:/software_file.cc   
  Startup system software:                   flash:/software_file.cc   
  Next startup system software:              flash:/software_file.cc   
  Startup saved-configuration file:          flash:/conf_file.cfg
  Next startup saved-configuration file:     flash:/conf_file.cfg
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
   option 67 cipher %+%#,nl-3C^(L"r2cE=]>Z[X2Xo+<e0-S;@s"#ReXBA(h>4\4h_@P']"!t4*26):0x31:fqp7Jz4FG'SYLo#%+%#
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
* Intermediate file
  
  The intermediate file in .ini format is used as an example.
  
  ```
  ;BEGIN ZTP CONFIG
  [GLOBAL CONFIG]
  *FILESERVER=sftp://sftp_user:Hyx_Hy1234@10.1.3.2
  *TIME_SN=20200526120159
  *DEVICE_TYPE_NUM=2
  SET_MASTER=
  CLEAR_MASTER=
  EXPORTCFG=
  [DEVICE_TYPE_1 DESCRIPTION]
  DEVICE_TYPE=
  ESN=2102311LDL0000000806
  MAC=
  VRPVER=
  SYSLOG_INFO=
  SPACE_CLEAR=
  DIRECTORY=
  ACTIVE_DELAYTIME=
  ACTIVE_INTIME=
  *FILETYPENUM=2
  *FILENAME_1=software_file.cc
  *TYPE_1=SOFTWARE
  *EFFECTIVE_MODE_1=0
  *FILENAME_2=cfg_file.cfg
  *TYPE_2=CFG
  *EFFECTIVE_MODE_2=0
  
  [DEVICE_TYPE_2 DESCRIPTION]
  DEVICE_TYPE=
  ESN=2102311LDL0000000918
  MAC=
  VRPVER=
  SYSLOG_INFO=
  SPACE_CLEAR=
  DIRECTORY=
  ACTIVE_DELAYTIME=
  ACTIVE_INTIME=
  *FILETYPENUM=2
  *FILENAME_1=software_file1.cc
  *TYPE_1=SOFTWARE
  *EFFECTIVE_MODE_1=0
  *FILENAME_2=cfg_file1.cfg
  *TYPE_2=CFG
  *EFFECTIVE_MODE_2=0
  ;END ZTP CONFIG
  ```
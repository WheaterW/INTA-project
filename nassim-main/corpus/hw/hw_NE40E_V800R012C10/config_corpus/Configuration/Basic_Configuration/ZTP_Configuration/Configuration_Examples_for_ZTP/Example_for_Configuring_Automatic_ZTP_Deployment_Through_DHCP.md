Example for Configuring Automatic ZTP Deployment Through DHCP
=============================================================

Example for Configuring Automatic ZTP Deployment Through DHCP

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172360197__fig_dc_ne_ztp_cfg_0010_01), two devices (RouterA and RouterB) with base configuration are newly added and connected to RouterC. RouterC functions as the egress gateway of RouterA and RouterB. Routes are available for RouterC, the DHCP server, and the file server to communicate with each other.

The customer requires that RouterA and RouterB automatically load system software and configuration files after they are powered on to reduce labor costs and device deployment time.**Figure 1** Configuring automatic ZTP deployment through DHCP![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/1 and GE 0/1/2, respectively.


  
![](images/fig_dc_ne_ztp_cfg_0010_01.png)


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an SFTP server as the file server to save the intermediate file, system software, and configuration files.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   File transfer through FTP is prone to security risks, and therefore the SFTP file transfer mode is recommended.
2. Edit the Python, INI, or CFG intermediate file to enable the routers to obtain their system software packages and configuration files according to the intermediate file.
3. Configure the DHCP server and relay agent to enable RouterA and RouterB to obtain DHCP information.
4. Power on RouterA and RouterB to start the ZTP process.


#### Procedure

1. Configure a file server.
   
   
   * Configure the device to function as a file server. For details, see [Example for Using SFTP to Operate Files](../vrp/dc_vrp_vfm_cfg_0026.html).
   * Configure a third-party server to function as a file server. For details, see the operation guide of the third-party server. On the PC, set the SFTP working directory to D:\ztp. After configuring the file server, save the system software and configuration file to be loaded to the D:\ztp directory.
2. Edit the intermediate file.
   
   
   
   Edit the intermediate file according to [Editing an Intermediate File](dc_ne_ztp_cfg_0004.html). A CFG intermediate file is used as an example. The file is named **ztp\_script.cfg**. See [Intermediate File in the CFG Format](dc_ne_ztp_feature_0011.html) for the file content.
   
   After editing the intermediate file, save the file to the working directory **D:\ztp** on the file server.
3. Configure the DHCP server.
   
   
   
   # Configure the IP address pool from which the DHCP server assigns IP addresses to clients. Configure Option fields according to the instructions in [Table 1](#EN-US_TASK_0172360197__table_02). For configuration details, see the corresponding product documentation and DHCP server configuration section in this document.
   
   **Table 1** Option fields to be configured on the DHCP server
   | Option | Description | Value |
   | --- | --- | --- |
   | 1 | Subnet mask of an IP address | 255.255.225.0 |
   | 3 | Egress gateway of a DHCP client | 10.1.1.1 |
   | 67 | File server address and intermediate file name | sftp://client001:YsHsjx\_202206@10.1.3.2/ztp\_script.cfg |
   
   # Configure an IP address and gateway address for the DHCP server. Ensure that the DHCP server and gateway of RouterA and RouterB have reachable routes to each other.
4. Configure the DHCP relay agent.
   
   
   
   # On RouterC, configure the DHCP relay function and set the IP address of the interface connected to RouterA and RouterB to 10.1.1.1. Configure 10.1.1.1 as the default gateway address of RouterA and RouterB.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname RouterC
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~RouterC] interface GigabitEthernet 0/1/1
   ```
   ```
   [~RouterC-GigabitEthernet0/1/1] ip address 10.2.2.1 255.255.255.0
   ```
   ```
   [*RouterC-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*RouterC-GigabitEthernet0/1/1] commit
   ```
   ```
   [~RouterC-GigabitEthernet0/1/1] quit
   ```
   ```
   [~RouterC] interface GigabitEthernet 0/1/2
   ```
   ```
   [~RouterC-GigabitEthernet0/1/2] ip address 10.1.1.1 255.255.255.0
   ```
   ```
   [*RouterC-GigabitEthernet0/1/2] dhcp select relay
   ```
   ```
   [*RouterC-GigabitEthernet0/1/2] ip relay address 10.1.2.2
   ```
   ```
   [*RouterC-GigabitEthernet0/1/2] undo shutdown
   ```
   ```
   [*RouterC-GigabitEthernet0/1/2] commit
   ```
   ```
   [~RouterC-GigabitEthernet0/1/2] quit
   ```
5. Power on RouterA and RouterB to start the ZTP process.
6. Verify the configuration.
   
   # Log in to the device and run the [**display startup**](cmdqueryname=display+startup) command to check whether the system software and configuration file are as expected. The example uses the command output on RouterA.
   ```
   <RouterA> display startup
   MainBoard:
     Configured startup system software:        cfcard:/V800R023C00SPC500B140_0424_new.cc
     Startup system software:                   cfcard:/V800R023C00SPC500B140_0424_new.cc
     Next startup system software:              cfcard:/V800R023C00SPC500B140_0424_new.cc
     Startup saved-configuration file:          cfcard:/vrpcfg.cfg
     Next startup saved-configuration file:     cfcard:/vrpcfg.cfg
     Startup paf file:                          default
     Next startup paf file:                     default
     Startup patch package:                     cfcard:/NE40EV800R023C00SPC500.PAT
     Next startup patch package:                cfcard:/NE40EV800R023C00SPC500.PAT
   ```

#### Configuration Files

ztp\_script.cfg file

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The SHA256 checksum in the following file is only an example.

```
#sha256sum="fffcd63f5e31f0891a0349686969969c1ee429dedeaf7726ed304f2d08ce1bc7"
fileserver=sftp://username:password@hostname:port/path/;
mac=00e0-fc12-3456;esn=2102351931P0C3000154;devicetype=DEFAULT;system-version=V800R023C00SPC500;boot_python_file=V800R023C00SPC500.py;system-software=V800R023C00SPC500.cc;system-config=test.cfg;system-pat=V800R023C00SPC500SPH001.PAT;
```

vrpcfg.cfg file

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The interface IP address and static route configurations in the file are used as an example. You can modify them as required.

```
#
sysname HUAWEI
#
ip vpn-instance __LOCAL_OAM_VPN__
 ipv4-family
#
interface Ethernet0/0/0
 undo shutdown
 ip binding vpn-instance __LOCAL_OAM_VPN__
 ip address 192.168.130.10 255.255.255.0
#
ip route-static vpn-instance __LOCAL_OAM_VPN__ 0.0.0.0 0.0.0.0 192.168.130.20
#
```

RouterC configuration file

```
#
sysname RouterC
#
interface GigabitEthernet0/1/1
 undo shutdown
 ip address 10.2.2.1 255.255.255.0
#
interface GigabitEthernet0/1/2
 undo shutdown
 ip address 10.1.1.1 255.255.255.0
 dhcp select relay
 ip relay address 10.1.2.2
#
return
```
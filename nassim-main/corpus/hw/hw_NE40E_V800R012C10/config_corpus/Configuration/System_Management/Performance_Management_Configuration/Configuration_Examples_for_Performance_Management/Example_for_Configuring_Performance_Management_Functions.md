Example for Configuring Performance Management Functions
========================================================

This section provides an example for configuring PM functions to record and monitor system performance statistics. The PM functions include creating a performance statistics task, binding an instance to the performance statistics task, and configuring PM servers.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172361262__fig_dc_vrp_pm_cfg_0100601), to monitor the operating status of interfaces and collect performance statistics, configure the PM function. This configuration enables a device to periodically collect performance statistics, save the performance statistics to files, and send the files to a PM server.

**Figure 1** PM application  
![](images/fig_dc_vrp_pm_cfg_0100601.png)
![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 represents GE0/1/1.



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable the performance statistics function.
2. Configure a performance statistics task.
3. Configure the PM server to obtain performance statistics files.

#### Data Preparation

To complete the configuration, you need the following data:

* Basic performance statistics function parameters:
  
  + Performance statistics task name
  + Performance statistics collection interval
  + Performance statistics instance type
  + Performance statistics instance name
  + Performance statistics counter name
  + Number of performance statistics intervals
* PM server parameters:
  
  + Name of the process serving the PM server
  + PM server IP address
  + Number of the PM server listening port
  + User name and password for logging in to the PM server
  + Destination path where performance statistics files are saved on the PM server
  + Number of performance statistics file retransmissions
  + Name of the request for uploading performance statistics files to the PM server

#### Procedure

1. Enable the performance statistics function.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname Device A
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~Device A] pm
   ```
   ```
   [~Device A-pm] statistics enable
   ```
   ```
   [*Device A-pm] commit
   ```
2. Configure basic performance statistics functions.
   
   
   ```
   [~Device A-pm] statistics-task huawei
   ```
   ```
   [*Device A-pm-statistics-huawei] statistics-cycle 5
   ```
   ```
   [*Device A-pm-statistics-huawei] binding instance-type interface instance gigabitethernet0/1/1
   ```
   ```
   [*Device A-pm-statistics-huawei] measure disable instance-type interface measure in-all-pkts
   ```
   ```
   [*Device A-pm-statistics-huawei] record-interval 3
   ```
   ```
   [*Device A-pm-statistics-huawei] commit
   ```
3. Configure the PM server to obtain performance statistics files.
   
   
   ```
   [~Device A-pm] pm-server abc
   ```
   ```
   [*Device A-pm-server-abc] protocol sftp ip-address 192.168.2.1 port 22
   ```
   ```
   [*Device A-pm-server-abc] username a password a
   ```
   ```
   [*Device A-pm-server-abc] path /pmserver
   ```
   ```
   [*Device A-pm-server-abc] retry 2
   ```
   ```
   [*Device A-pm-server-abc] quit
   ```
   ```
   [*Device A-pm] upload-config req1 server abc
   ```
   ```
   [*Device A-pm] commit
   ```
   ```
   [~Device A-pm] upload req1 file a120130525150004.txt 
   ```
   ```
   [*Device A-pm] commit
   ```
4. Verify the configuration.
   
   
   
   After configuring PM functions, run the [**display pm statistics-task**](cmdqueryname=display+pm+statistics-task) [ *task-name* ] command to check the PM configurations. The following example uses the command output for a performance statistics task named **huawei**. The command output shows the performance statistics task name, performance statistics collection interval, and performance statistics instance type. In addition, the performance statistics file a120130525150004.txt has been uploaded to the /pmserver path of the PM server.
   
   ```
   <Device A> display pm statistics-task huawei
   ```
   ```
   Task Name                : huawei
   Task State               : running
   Record-file Status       : enable
   Task Cycle               : 5 minutes
   Sample Interval          : 1 minutes
   Instance Type            : interface
   Record Interval(cycle)   : 3
   File Format              : text
   File Name Prefix         : huawei
   File Transfer Mode       : passive
   Current File Name        : a120130525150004.txt 
   ```

#### Configuration Files

```
#
sysname Device A
#
pm
 statistics enable
 pm-server abc
  protocol sftp ip-address 192.168.2.1 
  username a password %#%#H2uA')+.Y#eq-BZ~MEKG7r1_@L:n0*]&i@Z\/z7#%#%#
  retry 2
  path /pmserver
 upload-config req1 server abc
 statistics-task huawei
  statistics-cycle 5
  record-interval 3  
  binding instance-type interface instance GigabitEthernet0/1/1
  measure disable instance-type interface measure in-all-pkts

#
return
```
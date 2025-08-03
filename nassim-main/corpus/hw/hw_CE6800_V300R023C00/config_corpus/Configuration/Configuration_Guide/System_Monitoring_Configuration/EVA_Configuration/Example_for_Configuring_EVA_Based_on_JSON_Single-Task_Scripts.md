Example for Configuring EVA Based on JSON Single-Task Scripts
=============================================================

Example for Configuring EVA Based on JSON Single-Task Scripts

#### Networking Requirements

A customized JSON script is stored on an SFTP server. O&M personnel want to use EVA to collect device health information from devices. The JSON script is a single-task script. The script defines the commands for collecting device health information.

**Figure 1** Networking diagram of collecting device health information through EVA  
![](../images/en-us_image_0000001513030622.png)

#### Configuration Roadmap

1. Compile a JSON script and define events, strategies, and tasks in the script.
2. Upload the JSON script to the device.
3. Install and register the JSON script.

#### Procedure

1. Compile a JSON script and define events, strategies, and tasks in the script.
   
   
   
   # Compile a customized script **inspection\_1.json** to collect device health information. After the script is executed, you can collect information obtained using the [**display debugging**](cmdqueryname=display+debugging), [**display device**](cmdqueryname=display+device), and [**display health**](cmdqueryname=display+health) commands.
   
   ```
   {
   	"inspection_1": {
   		"description": "Collect system management information",
   		"events": {
   			"e1": {
   				"trigger": "eva.singleCollect()"
   			}
   		},
   		"strategy": "e1",
   		"tasks": {
   			"mainTask": {
   				"parameters": {
   					"Health_cmdArray": ["display debugging", "display device", "display health"]
   				},
   				"action": "eva.cliArray(\"user\",${Health_cmdArray})"
   			}
   		}
   	}
   }
   ```
2. Upload the JSON script to the device.
   
   
   
   # Configure DeviceA functioning as an SFTP client to download the JSON script **inspection\_1.json** from the SFTP server. For details, see "Managing Files Using SFTP" in Configuration Guide > Basic Configuration > File System Management Configuration.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] sftp client-transfile get host-ip 10.2.1.1 username client001 password Helloworld@6789 sourcefile CollectInformation.json
   Trying 10.2.1.1 ... 
   Press CTRL+K to abort 
   Connected to 10.2.1.1 ... 
   Remote file: /inspection_1.json --->  Local file: /inspection_1.json 
   Downloading the file. Please wait.. 
   Downloading file successfully ended.   
   File download is completed in 1 seconds. 
   [~DeviceA] [quit](cmdqueryname=quit)
   ```
3. Install and register the JSON script.
   
   
   ```
   <DeviceA> install eva script inspection_1.json
   ```

#### Verifying the Configuration

# Display the script registration status.

```
<DeviceA> [display eva register-status](cmdqueryname=display+eva+register-status)
Inspection install status: running
Inspection data path: 
Total: 4
--------------------------------------------------------------------------
FileName                         Status     FaultInfo                     
--------------------------------------------------------------------------
SystemExceptionCheck             Success    -      
cpuHigh.py                       Success    -                             
memHigh.py                       Success    -                             
inspection_1                     Success    -    
--------------------------------------------------------------------------
```

# Display the script running status.

```
<DeviceA> [display eva script-item status](cmdqueryname=display+eva+script-item+status)
Inspection running status: running
----------------------------------------------------------------------------------------------------------------
Script-item          Type            RegisterTime             Status         LastExecTime            Result
---------------------------------------------------------------------------------------------------------------
SystemExceptionCheck Build-in        2023-03-10 16:32:17    Idle           -                      -
inspection_1         User-define     2023-03-10 17:51:56    Running        -                      -
-----------------------------------------------------------------------------------------------------------------
```

# After a JSON single-task script is executed, you can view the collected data in the **flash:/eva** directory.


#### Configuration Scripts

DeviceA

```
#
sysname DeviceA
#
interface 100GE1/0/1
 undo portswitch
 ip address 10.1.1.1 255.255.255.0
#
```
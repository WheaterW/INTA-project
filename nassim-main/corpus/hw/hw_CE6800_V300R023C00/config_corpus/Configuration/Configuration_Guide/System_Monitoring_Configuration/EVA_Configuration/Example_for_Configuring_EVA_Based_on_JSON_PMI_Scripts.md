Example for Configuring EVA Based on JSON PMI Scripts
=====================================================

Example for Configuring EVA Based on JSON PMI Scripts

#### Networking Requirements

A customized JSON script is stored on an SFTP server. O&M personnel want to use EVA to collect routing information, interface diagnostic information, and device health information from devices. The JSON script is a PMI script. The script defines the commands for collecting routing information, interface diagnostic information, and device health information.

**Figure 1** Networking diagram of performing a PMI on devices through EVA  
![](../images/en-us_image_0000001513030630.png)

#### Configuration Roadmap

1. Compile a JSON script and define events, strategies, and tasks in the script.
2. Upload the JSON script to the device.
3. Install and register the JSON script.

#### Procedure

1. Compile a JSON script and define events, strategies, and tasks in the script.
   
   
   
   # Compile a customized script **CollectInformation.json** to collect routing information, interface diagnostic information, and device health information. After the script is executed, you can collect information obtained using the [**display bgp peer**](cmdqueryname=display+bgp+peer), [**display isis peer**](cmdqueryname=display+isis+peer), [**display ospf peer**](cmdqueryname=display+ospf+peer), [**display interface troubleshooting**](cmdqueryname=display+interface+troubleshooting), [**display interface counters errors**](cmdqueryname=display+interface+counters+errors), [**display debugging**](cmdqueryname=display+debugging), [**display device**](cmdqueryname=display+device), and [**display health**](cmdqueryname=display+health) commands.
   
   ```
   {"inspection_1":{"description":"Collect IP routing information","events":{"e1":{"trigger":"eva.singleCollect()"}},"strategy":"e1","tasks":{"mainTask":{"parameters":{"IProute_cmdArray":["display bgp peer","display isis peer","display ospf peer"]},"action":"eva.cliArray(\"user\",${IProute_cmdArray})"}}}}
   {"inspection_2":{"description":"Collect statistics on error packets and diagnosis information on the interfaces","events":{"e1":{"trigger":"eva.singleCollect()"}},"strategy":"e1","tasks":{"mainTask":{"parameters":{"Interface_cmdArray":["display interface troubleshooting","display interface counters errors",]},"action":"eva.cliArray(\"user\",${Interface_cmdArray})"}}}}
   {"inspection_3":{"description":"Collect system management information","events":{"e1":{"trigger":"eva.singleCollect()"}},"strategy":"e1","tasks":{"mainTask":{"parameters":{"Health_cmdArray":["display debugging","display device","display health"]},"action":"eva.cliArray(\"user\",${Health_cmdArray})"}}}}
   ```
2. Upload the JSON script to the device.
   
   
   
   # Configure DeviceA functioning as an SFTP client to download the JSON script **CollectInformation.json** from the SFTP server. For details, see "Managing Files Using SFTP" in Configuration Guide > Basic Configuration > File System Management Configuration.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] sftp client-transfile get host-ip 10.2.1.1 username client001 password Helloworld@6789 sourcefile CollectInformation.json
   Trying 10.2.1.1 ... 
   Press CTRL+K to abort 
   Connected to 10.2.1.1 ... 
   Remote file: /CollectInformation.json --->  Local file: /CollectInformation.json 
   Downloading the file. Please wait.. 
   Downloading file successfully ended.   
   File download is completed in 1 seconds. 
   [~DeviceA] [quit](cmdqueryname=quit)
   ```
3. Install and register the JSON script.
   
   
   ```
   <DeviceA> install eva script CollectInformation.json inspection
   ```

#### Verifying the Configuration

# Display the script registration status.

```
<DeviceA> [display eva register-status](cmdqueryname=display+eva+register-status)
Inspection install status: running
Inspection data path: flash:/eva/eva_inspection_20211109154918.zip
Total: 6
--------------------------------------------------------------------------
FileName                         Status     FaultInfo                     
--------------------------------------------------------------------------
SystemExceptionCheck             Success    -      
cpuHigh.py                       Success    -                             
memHigh.py                       Success    -                             
inspection_1                     Success    -    
inspection_2                     Success    -    
inspection_3                     Success    -    
--------------------------------------------------------------------------
```

# Display the script running status.

```
<DeviceA> [display eva script-item status](cmdqueryname=display+eva+script-item+status)
Inspection running status: running
---------------------------------------------------------------------------------------------------------------
Script-item          Type            RegisterTime             Status         LastExecTime            Result
---------------------------------------------------------------------------------------------------------------
SystemExceptionCheck Build-in        2023-5-09 15:50:07    Idle           -                      -
inspection_1         inspection      2023-5-09 15:50:11    Running        -                      -
inspection_2         inspection      2023-5-09 15:50:15    Running        -                      -
inspection_3         inspection      2023-5-09 15:50:18    Idle           -                      -
----------------------------------------------------------------------------------------------------------------
```

# After a PMI script is executed, it is automatically uninstalled. You can view the data collected during the PMI in the **eva\_inspection\_***latest date***.zip** file in the **flash:/eva** directory.

# Display the execution history of the script.

```
<DeviceA> [display eva inspection history](cmdqueryname=display+eva+inspection+history)
------------------------------------------------------------------------------------------------------------------------
RegisterTime          FileName                   ServerType   IpAddress      Port   UserName      Status    ResultFileName
------------------------------------------------------------------------------------------------------------------------
2023-5-09 15:50:10   CollectInformation.json    -            -              -      -             Running   -     
------------------------------------------------------------------------------------------------------------------------
```

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
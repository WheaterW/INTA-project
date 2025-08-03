Example for Configuring NPCC for a Lossless Queue
=================================================

Example for Configuring NPCC for a Lossless Queue

#### Networking Requirements

[Figure 1](#EN-US_TASK_0000001564119693__fig19978171395514) shows a typical DCI scenario where a storage service carried over RoCEv2 is deployed on servers in multiple DCs. DeviceA and DeviceB function as egress devices for DCI, and they are far away from each other. To reduce congestion risks and improve RoCEv2 service performance, configure NPCC on DeviceA and DeviceB.

**Figure 1** Network diagram for NPCC implementation in a DCI scenario![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 represents 100GE1/0/1.


  
![](figure/en-us_image_0000001513159618.png)

#### Precautions

When configuring NPCC for a lossless queue, note the following:

* NICs of the hosts must support RoCEv2 and DCQCN.
* The parameter settings in this example are for reference only. You need to configure each device based on the traffic model on your network.

#### Procedure

1. Configure PFC.
   
   
   
   # In this example, queue 4 carries the RoCEv2 service as planned, so enable PFC for queue 4 on interface 1 of DeviceA. The configurations on DeviceB are similar.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] dcb pfc
   [*DeviceA-dcb-pfc-default] priority 4
   [*DeviceA-dcb-pfc-default] quit
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] dcb pfc enable mode manual
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   For details about other PFC configurations, see [PFC](galaxy_dcb_cfg_0004.html).
2. Configure NPCC for the lossless queue.
   
   
   
   # On DeviceA, enable NPCC for lossless queue 4. In this example, the storage service is deployed on servers, so the default high-throughput mode is used. The configurations on DeviceB are similar.
   
   ```
   [~DeviceA] ai-service
   [*DeviceA-ai-service] npcc
   [*DeviceA-ai-service-npcc] assign queue 4
   [*DeviceA-ai-service-npcc] quit
   [*DeviceA-ai-service] quit
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] npcc enable
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Display the NPCC configuration on DeviceA.

```
[~DeviceA] display npcc configuration slot 1  
NPCC mode: High-throughput
NPCC Enabled Queue: 4
NPCC Enabled Interface:
100ge 1/0/1
```

# Check statistics about CNPs proactively sent by DeviceA.

```
[~DeviceA] display npcc statistics interface 100ge 1/0/1  
Chip Statistics:
  Total Resent CNP Number: 601
  IPv4 Resent CNP Number: 601
  IPv6 Resent CNP Number: 0
  Used Total Flow Entries: 1025
  Used IPv4 Flow Entries: 1025
  Used IPv6 Flow Entries: 0

Interface Statistics:
  Average Queue Length: 25KB
  Total Resent CNP Number: 200
  Associated Total Flow Entries: 1
  IPv4 Info:
    Recent CNP Number: 200
    Associated Flow Entries: 1
    ------------------------------------------
    DIP              SIP              SQP
    ------------------------------------------
    192.168.20.27    192.168.10.29    156243
    ------------------------------------------
  IPv6 Info:
    Recent CNP Number: 0
    Associated Flow Entries: 0
    ------------------------------------------
    DIP              SIP              SQP
    ------------------------------------------
    ------------------------------------------
```

#### Configuration Scripts

DeviceA

```
#
sysname DeviceA
#
dcb pfc
 priority 4
#
interface 100GE1/0/1
 npcc enable
 dcb pfc enable mode manual
#
ai-service 
 #
 npcc
  assign queue 4
#
return

```

DeviceB

```
#
sysname DeviceB
#
dcb pfc
 priority 4
#
interface 100GE1/0/1
 npcc enable
 dcb pfc enable mode manual
#
ai-service 
 #
 npcc
  assign queue 4
#
return

```
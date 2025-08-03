Example for Configuring an NQA TCP Test to Measure the Response Time on an IP Network
=====================================================================================

Example for Configuring an NQA TCP Test to Measure the Response Time on an IP Network

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001176661835__fig_dc_vrp_nqa_cfg_002601), the headquarters and its subsidiary need to communicate with each other across an external network. DeviceA and DeviceD are egress devices of the headquarters and subsidiary, respectively. DeviceB and DeviceC are edge devices of the external network.

The headquarters and its subsidiary often need to use TCP to exchange files with each other. The time taken to respond to a TCP transmission request must be less than 800 ms. An NQA TCP test can be configured to measure the TCP response time between DeviceA and DeviceD.

**Figure 1** Network diagram for an NQA TCP test to measure the response time on an IP network![](../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent 100GE 1/0/1 and 100GE 1/0/2, respectively.


  
![](figure/en-us_image_0000001176741759.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure DeviceD as an NQA client and DeviceA as an NQA server, and configure a TCP test instance on DeviceA.
2. Start the test instance.

#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of DeviceA and DeviceD
* Listening port number of the TCP service

#### Procedure

1. Configure DeviceA as the NQA server.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] nqa server tcpconnect 10.1.1.1 4000
   ```
2. Configure DeviceD as the NQA client, create a TCP test instance, and set the destination IP address to the IP address of DeviceA.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceD
   [*HUAWEI] commit
   [~DeviceD] nqa test-instance admin tcp
   [*DeviceD-nqa-admin-tcp] test-type tcp
   [*DeviceD-nqa-admin-tcp] destination-address ipv4 10.1.1.1
   [*DeviceD-nqa-admin-tcp] destination-port 4000
   ```
3. Start the test instance immediately.
   
   
   ```
   [*DeviceD-nqa-admin-tcp] start now
   [*DeviceD-nqa-admin-tcp] commit
   ```

#### Verifying the Configuration

Verify the test result. The command output indicates that the response time is less than 800 ms.

```
[~DeviceD-nqa-admin-tcp] display nqa results test-instance admin tcp

NQA entry(admin, tcp): test flag is active, test type is TCP
1 . Test 1 result The test is finished
    Send operation times: 3               Receive response times: 3 
    Completion: success                   RTD over thresholds number: 0
    Attempts number: 1                    Drop operation number: 0
    Disconnect operation number: 0        Operation timeout number: 0
    System busy operation number: 0       Connection fail number: 0
    Operation sequence errors number: 0   RTT Status errors number: 0
    Destination IP address: 10.1.1.1
    Min/Max/Average completion time: 600/610/603
    Sum/Square-Sum completion time: 1810/1092100
    Last response packet receiving time: 2020-04-16 12:59:41.6
    Lost packet ratio: 0 %
```

#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  vlan batch 100
  #
  interface Vlanif100
   ip address 10.1.1.1 255.255.255.0
  #
  nqa server tcpconnect 10.1.1.1 4000
  #
  isis 1
   network-entity 00.0000.0000.0001.00
  #
  interface 100GE1/0/1
   port link-type trunk
   port trunk allow-pass vlan 100
   isis enable 1
  #
  return
  ```
* DeviceD
  
  ```
  #
  sysname DeviceD
  #
  vlan batch 100
  #
  interface Vlanif100
   ip address 10.2.2.1 255.255.255.0
  #
  isis 1
   network-entity 00.0000.0000.0002.00
  #
  interface 100GE1/0/1
   port link-type trunk
   port trunk allow-pass vlan 100 
   isis enable 1
  #
  nqa test-instance admin tcp
   test-type tcp
   destination-address ipv4 10.1.1.1
   destination-port 4000
  #
  return
  ```
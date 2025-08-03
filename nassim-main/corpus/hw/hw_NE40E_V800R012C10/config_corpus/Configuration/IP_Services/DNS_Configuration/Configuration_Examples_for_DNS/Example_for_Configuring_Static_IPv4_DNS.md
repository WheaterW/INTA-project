Example for Configuring Static IPv4 DNS
=======================================

This section describes how to configure static DNS.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172364812__fig_dc_vrp_dns_cfg_000801), Device A frequently uses the domain name "host.com" to visit the host. To improve the efficiency of domain name resolution, you can establish a static mapping between the domain name "host.com" and IP address 10.100.1.2 in the static domain name resolution table of Device A.

**Figure 1** Configuring static DNS  
![](images/fig_dc_vrp_dns_cfg_000801.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

* Establish a static mapping between the domain name "host.com" and IP address 10.100.1.2 on Device A.

#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of Device A and the host
* Domain name of the host

#### Procedure

1. Configure a static mapping between the domain name "host.com" and IP address 10.100.1.2.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI]sysname DeviceA
   ```
   ```
   [*HUAWEI]commit
   ```
   ```
   [~DeviceA] ip host host.com 10.100.1.2
   ```
   ```
   [*DeviceA] commit
   ```
2. Verify the configuration.
   
   # Run the **ping host.com** command on Device A. The host can be pinged. The destination IP address for the ping operation is 10.100.1.2.
   ```
   <DeviceA> ping host.com
   ```
   ```
     ping host.com (10.100.1.2):56 data bytes, press CTRL_C to break
        Reply from 10.100.1.2: bytes=56 Sequence=1 ttl=128 time=1 ms
        Reply from 10.100.1.2: bytes=56 Sequence=2 ttl=128 time=4 ms
        Reply from 10.100.1.2: bytes=56 Sequence=3 ttl=128 time=3 ms
        Reply from 10.100.1.2: bytes=56 Sequence=4 ttl=128 time=2 ms
        Reply from 10.100.1.2: bytes=56 Sequence=5 ttl=128 time=3 ms
   
       --- host.com ping statistics ---
        5 packet(s) transmitted
        5 packet(s) received
        0.00% packet loss
        round-trip min/avg/max = 1/2/4 ms
   ```
   
   # Run the [**display ip host**](cmdqueryname=display+ip+host) command on Device A to check static DNS entry information, including mappings between domain names and IP addresses.
   ```
   <DeviceA> display ip host
   ```
   ```
   Host                 Age        Flags  Address
   host.com             0          static 10.100.1.2  
   ```

#### Configuration Files

* Device A configuration file
  
  ```
  #
   sysname DeviceA
  #
   ip host host.com 10.100.1.2
  #
  return
  ```
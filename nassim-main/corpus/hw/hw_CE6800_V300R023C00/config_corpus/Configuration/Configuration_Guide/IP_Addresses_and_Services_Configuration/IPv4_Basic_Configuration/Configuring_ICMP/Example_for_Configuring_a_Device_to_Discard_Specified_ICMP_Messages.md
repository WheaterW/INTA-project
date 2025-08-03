Example for Configuring a Device to Discard Specified ICMP Messages
===================================================================

Example for Configuring a Device to Discard Specified ICMP Messages

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0000001176663317__fig_dc_vrp_ipv4_cfg_003501), DeviceA and DeviceB are connected to PC1 and PC2, respectively. Attackers often send a large number of ICMP messages with TTL of 1, route options, and unreachable destination addresses. As a result, network traffic increases and device performance deteriorates. To reduce network traffic and improve device performance, configure a device to discard such ICMP messages.

**Figure 1** Network diagram of configuring a device to discard specified ICMP messages![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 represents 100GE 1/0/1.


  
![](figure/en-us_image_0000001130623810.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

* Configure DeviceA to discard all ICMP messages with TTL of 1.
* Configure DeviceA to discard all ICMP messages with route options.
* Configure DeviceA to discard all ICMP messages with unreachable destination addresses.


#### Procedure

1. Assign IP addresses 10.1.1.2/24 and 10.1.1.1/24 to the 100GE 1/0/1 interfaces on DeviceA and DeviceB, respectively.
2. Configure DeviceA to discard specified ICMP messages.
   
   
   
   # Configure DeviceA to discard all ICMP messages with TTL of 1.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*DeviceA] commit
   [~DeviceA] icmp ttl-exceeded drop all
   [*DeviceA] commit
   ```
   
   # Configure DeviceA to discard all ICMP messages with route options.
   
   ```
   [~DeviceA] icmp with-options drop all
   [*DeviceA] commit
   ```
   
   # Configure DeviceA to discard all ICMP messages with unreachable destination addresses.
   
   ```
   [~DeviceA] icmp name unreachable receive disable
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Ping DeviceA from DeviceB. The command output shows that DeviceB does not receive any response from DeviceA.

```
[~DeviceB] ping -a 10.1.1.2
PING 10.1.1.2: 56  data bytes, press CTRL_C to break
    Request time out
    Request time out
    Request time out
    Request time out
    Request time out

  --- 10.1.1.2 ping statistics ---
    5 packet(s) transmitted
    0 packet(s) received
    100.00% packet loss
```
#### Configuration Scripts

* DeviceA
  
  ```
  #
   sysname DeviceA
  #
   icmp name unreachable receive disable
   icmp ttl-exceeded drop slot 1
   icmp with-options drop slot 1
  #
  interface 100GE1/0/1
   ip address 10.1.1.2 255.255.255.0
  #
  firewall zone trust
   add interface 100GE1/0/1
   
  #
  return
  ```
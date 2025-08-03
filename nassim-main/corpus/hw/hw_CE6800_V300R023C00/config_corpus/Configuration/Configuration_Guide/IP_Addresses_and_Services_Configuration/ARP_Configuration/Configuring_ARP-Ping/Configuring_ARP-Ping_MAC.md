Configuring ARP-Ping MAC
========================

Configuring ARP-Ping MAC

#### Context

ARP-Ping MAC enables a device to send ICMP messages to a LAN to check whether a MAC address is being used on the LAN.

When a device knows a MAC address on a network segment but does not know the corresponding IP address, the **ping arp mac** command can be run on the device to obtain the corresponding IP address through ICMP messages.


#### Procedure

1. Check whether a MAC address is being used.
   
   
   ```
   [ping arp mac](cmdqueryname=ping+arp+mac) mac-address { { ip-address [ vpn-instance vpn-instance-name ] } | { interface { interface-name | interface-type interface-number } } }
   ```

#### Example

* If the MAC address is not being used, the command output is as follows:
  
  ```
  [~HUAWEI] ping arp mac 00e0-fc7d-f201 interface vlanif 2
    OutInterface: 100GE1/0/1 MAC[00-E0-FC-12-34-56], press CTRL_C to break
  Error: Request timeout.                                                                                                             
  Error: Request timeout.                                                                                                             
  Error: Request timeout.
      ----- ARP-Ping MAC statistics -----
      3 packet(s) transmitted
      0 packet(s) received
      MAC[00-E0-FC-12-34-56]  not be used
  ```
* If the MAC address is being used, the command output displays the IP address corresponding to this MAC address. The command output is as follows:
  
  ```
  [~HUAWEI] ping arp mac 00e0-fc7d-f202 interface vlanif 2
    OutInterface: 100GE1/0/1 MAC[00-E0-FC-12-34-56], press CTRL_C to break
    
  
      ----- ARP-Ping MAC statistics -----
      1 packet(s) transmitted
      1 packet(s) received
  
      IP ADDRESS                MAC ADDRESS
      10.1.1.1                 00-E0-FC-12-34-56
  ```
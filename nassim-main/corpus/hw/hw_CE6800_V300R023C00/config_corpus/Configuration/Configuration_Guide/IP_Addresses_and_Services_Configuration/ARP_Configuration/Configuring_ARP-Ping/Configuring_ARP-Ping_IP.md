Configuring ARP-Ping IP
=======================

Configuring ARP-Ping IP

#### Context

ARP-Ping IP enables a device to send ARP messages to a LAN to check whether an IP address is being used on the LAN.

Before configuring an IP address for a device on a LAN, run the [**ping arp ip**](cmdqueryname=ping+arp+ip) command to check whether the IP address to be configured is being used on the network.

The [**ping**](cmdqueryname=ping) command can also be used to check whether this IP address is used by another device on the network. If the destination host and device that are enabled with the firewall function are configured not to reply to ping messages, they do not reply to ping messages. This means that the ping always fails and the IP address is mistakenly considered available. To resolve this problem, configure ARP-Ping IP. ARP messages are Layer 2 protocol messages and, in most cases, can pass through a device that is configured not to respond to ping messages.


#### Procedure

1. Check whether an IP address is being used.
   
   
   ```
   [ping arp ip](cmdqueryname=ping+arp+ip) ip-host [ interface { interface-name | interface-type interface-number } [ vlan-id vlanId ] ] [ timeout timeout ]
   ```

#### Example

* If the IP address is not being used, the command output is as follows:
  
  ```
  [~HUAWEI] ping arp ip 10.1.1.2
   ARP-Pinging 10.1.1.2:
  
  Error: Request timeout.                                                                                                             
  Error: Request timeout.                                                                                                             
  Error: Request timeout.                                                                                                             
  Info: The IP address is not used by anyone.  
  ```
* If the IP address is being used, the command output is as follows:
  
  ```
  [~HUAWEI] ping arp ip 10.1.1.1
   ARP-Pinging 10.1.1.1:
  
  10.1.1.1 is used by 00e0-fc7d-f202      
  ```
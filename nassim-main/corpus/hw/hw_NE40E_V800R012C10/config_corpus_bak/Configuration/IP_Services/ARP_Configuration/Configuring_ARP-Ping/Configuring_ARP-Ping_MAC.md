Configuring ARP-Ping MAC
========================

ARP-Ping MAC sends ICMP packets onto a LAN to check whether a MAC address is used by another device on the LAN.

#### Procedure

1. Run [**arp-ping
   mac**](cmdqueryname=arp-ping+mac) *mac-address* { *ip-address* [ **vpn-instance** *vpn-instance-name* ] | **interface** *interface-type
   interface-number* }
   
   
   
   ARP-Ping MAC is enabled to check whether a MAC address is being used by another device.
   
   
   
   There are two possible results after the command is run:
   
   * If the MAC address is not being used by another device, the command output is as follows:
     
     ```
     [*HUAWEI] arp-ping mac 00e0-fc7d-f201 interface gigabitethernet 0/1/0
     ```
     ```
       OutInterface: GigabitEthernet0/1/0 MAC[00-E0-FC-7D-F2-01], press CTRL_C to break
       Request timed out
       Request timed out
       Request timed out
     
         ----- ARP-Ping MAC statistics -----
         3 packet(s) transmitted
         0 packet(s) received
         MAC[00-E0-FC-7D-F2-01]  not be used
     ```
   * If the MAC address is being used by another device, the command output displays the IP address corresponding to this MAC address. The command output is as follows:
     
     ```
     [*HUAWEI] arp-ping mac 00e0-fc7d-f202 interface gigabitethernet 0/1/0
     ```
     ```
       OutInterface: GigabitEthernet0/1/0 MAC[00-E0-FC-7D-F2-02], press CTRL_C to break
     
         ----- ARP-Ping MAC statistics -----
         1 packet(s) transmitted
         1 packet(s) received
     
         IP ADDRESS                MAC ADDRESS
         10.1.1.1                 00-E0-FC-7D-F2-02
     ```
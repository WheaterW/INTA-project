Checking Multicast Network Path Information Using MTracert
==========================================================

Multicast trace route (MTrace) is a tool used to trace multicast paths. It can trace the path from a receiver to a multicast source along a multicast distribution tree (MDT).

#### Prerequisites

Before configuring an MTrace test instance, run the [**undo mtrace echo disable**](cmdqueryname=undo+mtrace+echo+disable) command on each device along the multicast or RPF path to be detected to enable the devices to respond to MTrace request and query messages.


#### Context

MTrace mainly has the following uses:

* The [**mtrace**](cmdqueryname=mtrace) command can be used in multicast troubleshooting and routine maintenance to locate a faulty device and reduce configuration errors.
* The [**mtrace**](cmdqueryname=mtrace) command can be used to collect traffic statistics in path tracing and calculate the multicast traffic rate in cyclic path tracing.
* The NMS analyzes faulty device information displayed in the [**mtrace**](cmdqueryname=mtrace) command output and generates alarms.

Perform the following steps in any view on the client.


#### Procedure

1. (Optional) Run [**reset mtrace statistics**](cmdqueryname=reset+mtrace+statistics)
   
   
   
   MTrace message statistics are cleared.
   
   
   
   ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
   
   After the [**reset mtrace statistics**](cmdqueryname=reset+mtrace+statistics) command is run, the statistics cleared cannot be restored.
2. Perform the following operations as required.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) To ensure that the [**mtrace**](cmdqueryname=mtrace) command is run successfully, the current device must have the (S, G) entries and meet either of the following conditions:
   * The current device is directly connected to the destination host.
   * A ping test initiated from the current device to the last-hop device or destination host succeeds.
   * The current device is on the multicast path from the multicast source to the destination host.
   
   The following examples show some parameters. For detailed options and parameter description, see [**mtrace**](cmdqueryname=mtrace).
   
   * Run the [**mtrace**](cmdqueryname=mtrace) **source** *source-address* command to trace the RPF path from a multicast source to the current device.
     
     ```
     <HUAWEI> mtrace source 10.1.0.1
     ```
     ```
     Press Ctrl+C to break multicast traceroute facility
      From the receiver(10.1.5.1), trace reverse path to source (10.1.0.1) according to RPF rules
     
      Num  Reverse-Path    FwdTTL Protocol
       0   10.1.5.1
      -1   10.1.5.1        1      PIM
      -2   10.1.2.1        1      PIM
      -3   10.1.0.1        1      PIM
       In maximum-hop mode, received the response message, and multicast traceroute finished.
     ```
   * Run the [**mtrace**](cmdqueryname=mtrace) **-g** *group* **source** *source-address* command to trace the multicast path from a multicast source to the current device.
     ```
     <HUAWEI> mtrace -g 225.0.0.1 -l 2 -st 10 source 10.1.0.1
     ```
     ```
     Press Ctrl+C to break multicast traceroute facility
      From the receiver(10.1.5.1), trace (10.1.0.1, 225.0.0.1)'s reverse path according to multicast routing-table
      In calculating-rate mode, current statistic times is: 1
     - 1 10.1.5.1
        Incoming Interface Address: 10.1.5.1 Input packets rate: 0xffffffff
        Outgoing Interface Address: 0.0.0.0 Output packets rate: 0xffffffff
        Forwarding Cache (10.1.0.1, 225.0.0.1) Forwarding packets rate: 1500
        Last forwarded packets: 19121341 Current forwarded packets: 19136201
        The packet loss rate of (10.1.0.1, 225.0.0.1) is 0.00%
     - 2 10.1.2.1
        Incoming Interface Address: 10.1.2.1 Input packets rate: 0xffffffff
        Outgoing Interface Address: 10.1.5.2 Output packets rate: 0xffffffff
        Forwarding Cache (10.1.0.1, 225.0.0.1) Forwarding packets rate: 1500
        Last forwarded packets: 149378592 Current forwarded packets: 149393372
        The packet loss rate of (10.1.0.1, 225.0.0.1) is 0.00%
     - 3 10.1.0.1
        Incoming Interface Address: 10.1.0.1 Input packets rate: 0xffffffff
        Outgoing Interface Address: 10.1.2.2 Output packets rate: 0xffffffff
        Forwarding Cache (10.1.0.1, 225.0.0.1) Forwarding packets rate: 1500
        Last forwarded packets: 149454710 Current forwarded packets: 149469582
        The packet loss rate of (10.1.0.1, 225.0.0.1) is 0.00%
      ********************************************************
       In calculating-rate mode, reach the demanded number of statistic,and multicast traceroute finished.
     ```
   * Run the [**mtrace**](cmdqueryname=mtrace) [ **-gw** *last-hop-router* | **-d** ] **-r** *receiver* **source** *source-address* command to trace the RPF path from a multicast source to the destination host.
     
     ```
     <HUAWEI> mtrace -gw 10.1.6.3 -r 10.1.6.4 -v source 10.1.0.1
     ```
     ```
     Press Ctrl+C to break multicast traceroute facility
      From the receiver(10.1.6.4), trace reverse path to source (10.1.0.1) according to RPF rules
      Num  Reverse-Path    FwdTTL Protocol
       0   10.1.6.4
     - 1   10.1.5.1        1      PIM
       Incoming Interface Address: 10.1.5.1 
       Outgoing Interface Address: 10.1.6.3 
       Previous-Hop Router Address: 10.1.5.2 
       Input packet count on incoming interface: 0xffffffff 
       Output packet count on outgoing interface: 0xffffffff 
       Total number of packets for this source-group pair: 0 
       Forwarding TTL: 1 
       Forwarding Code: NO_ERROR
     - 2   10.1.2.1        1      PIM
       Incoming Interface Address: 10.1.2.1 
       Outgoing Interface Address: 10.1.5.2 
       Previous-Hop Router Address: 10.1.2.2 
       Input packet count on incoming interface: 0xffffffff 
       Output packet count on outgoing interface: 0xffffffff 
       Total number of packets for this source-group pair: 0 
       Forwarding TTL: 1 
       Forwarding Code: NO_ERROR
     - 3   10.1.0.1        1      PIM
       Incoming Interface Address: 10.1.0.1 
       Outgoing Interface Address: 10.1.2.2 
       Previous-Hop Router Address: 0.0.0.0 
       Input packet count on incoming interface: 0xffffffff 
       Output packet count on outgoing interface: 0xffffffff 
       Total number of packets for this source-group pair: 0 
       Forwarding TTL: 1 
       Forwarding Code: NO_ERROR 
      In maximum-hop mode, received the response message, and multicast traceroute finished.
     ```
   * Run the [**mtrace**](cmdqueryname=mtrace) [ **-b** | **-gw** *last-hop-router* | **-d** ] **-r** *receiver* **-g** *group* **source** *source-address* command to trace the multicast path from a multicast source to the destination host.
     
     ```
     <HUAWEI> mtrace -b -r 10.1.6.4 -g 225.0.0.1 source 10.1.0.1
     ```
     ```
     Press Ctrl+C to break multicast traceroute facility
      From the receiver(10.1.6.4), trace (10.1.0.1, 225.0.0.1)'s reverse path according to multicast routing-table
      Num  Reverse-Path    FwdTTL Protocol
       0   10.1.6.4
      -1   10.1.5.1        1      PIM
      -2   10.1.2.1        1      PIM
      -3   10.1.0.1        1      PIM
       In maximum-hop mode, received the response message, and multicast traceroute finished.
     ```
3. (Optional) Run [**display mtrace statistics**](cmdqueryname=display+mtrace+statistics)
   
   
   
   MTrace message statistics are displayed.
   
   
   
   Run this command if network connectivity is abnormal or you need to view information about IGMP messages sent and received by devices on the multicast network.
4. (Optional) Run [**mtrace echo disable**](cmdqueryname=mtrace+echo+disable)
   
   
   
   A device is disabled from responding to MTrace request and query messages.
   
   
   
   ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
   
   After the [**mtrace echo disable**](cmdqueryname=mtrace+echo+disable) command is run, a device discards MTrace request and query messages. As a result, MTrace detection is terminated on this device.
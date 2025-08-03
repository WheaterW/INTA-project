Configuring ICMP Message Forwarding
===================================

Configuring ICMP Message Forwarding

#### Prerequisites

Before configuring ICMP message forwarding, configure link layer protocol parameters for interfaces to ensure that the link layer protocol status of the interfaces is up.


#### Context

Under normal circumstances, a device can send and receive ICMP messages properly. However, when network traffic is heavy, host unreachable or port unreachable events frequently occur, leading to a surge in ICMP messages. The increase in the volume of messages not only burdens the network, but also degrades the performance of devices. In addition, attackers usually use ICMP error messages to probe the internal network topology.

To reduce a device's pressure in processing ICMP messages and prevent ICMP message attacks, configure the device to control the sending or receiving of ICMP messages.

The device supports the configuration of ICMP message forwarding based on an ICMP name or specified type and code. [Table 1](#EN-US_TASK_0000001176743233__table109773913198) lists the supported ICMP names. For details about the ICMP messages corresponding to the types and codes, see [Table 1](#EN-US_TASK_0000001176743233__table109773913198).

**Table 1** ICMP names supported by the device
| Value of *icmp-name* | Type | Code | Description | Sending Specified ICMP Messages | Receiving Specified ICMP Messages |
| --- | --- | --- | --- | --- | --- |
| echo-reply | 0 | 0 | Echo reply | Supported | Supported |
| unreachable | 3 | - | Destination unreachable | Not supported | Supported in the system view; not supported in the interface view |
| net-unreachable | 3 | 0 | Destination network unreachable | Supported | Supported |
| host-unreachable | 3 | 1 | Destination host unreachable | Not supported | Supported |
| protocol-unreachable | 3 | 2 | Destination protocol unreachable | Not supported | Supported |
| port-unreachable | 3 | 3 | Destination port unreachable | Supported | Supported |
| fragmentneed-dfset | 3 | 4 | Fragmentation required, and DF flag set | Supported | Supported |
| source-route-failed | 3 | 5 | Source route failed | Supported | Supported |
| source-quench | 4 | 0 | Source quench | Not supported | Supported |
| net-redirect | 5 | 0 | Redirect datagram for the network | Not supported | Supported |
| host-redirect | 5 | 1 | Redirect datagram for the host | Not supported | Supported |
| net-tos-redirect | 5 | 2 | Redirect datagram for the ToS and network | Not supported | Supported |
| host-tos-redirect | 5 | 3 | Redirect datagram for the ToS and host | Not supported | Supported |
| echo | 8 | 0 | Echo request | Supported | Supported |
| ttl-exceeded | 11 | 0 | TTL expired in transit | Supported | Supported |
| reassembly-timeout | 11 | 1 | Fragment reassembly time exceeded | Supported | Supported |
| parameter-problem | 12 | 0 | Parameter problem | Supported | Supported |
| timestamp-request | 13 | 0 | Timestamp | Supported | Supported |
| timestamp-reply | 14 | 0 | Timestamp reply | Supported | Supported |
| information-request | 15 | 0 | Information request | Not supported | Supported |
| information-reply | 16 | 0 | Information reply | Not supported | Supported |



#### Procedure

* Configure ICMP message forwarding in the system view.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Disable the device from sending or receiving ICMP messages as required.
     
     
     + Disable the device from sending ICMP messages.
       ```
       [icmp](cmdqueryname=icmp+type+code+send+disable) type typevalue code codevalue send disable
       ```
     + Disable the device from receiving ICMP messages.
       ```
       [icmp](cmdqueryname=icmp+type+code+receive+disable) type typevalue code codevalue receive disable
       ```
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure ICMP message forwarding in the interface view.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the interface view.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  3. Switch the interface working mode to Layer 3.
     
     
     ```
     [undo portswitch](cmdqueryname=undo+portswitch)
     ```
  4. Disable the device from sending or receiving ICMP messages on the interface as required.
     
     
     + Disable the device from sending ICMP messages.
       ```
       [icmp](cmdqueryname=icmp+type+code+send+disable) type typevalue code codevalue send disable
       ```
       
       By default, an interface's ICMP message sending capability is determined by the system's ICMP message sending capability.
     + Disable the device from receiving ICMP messages.
       ```
       [icmp](cmdqueryname=icmp+type+code+receive+disable) type typevalue code codevalue receive disable
       ```
       
       By default, an interface's ICMP message receiving capability is determined by the system's ICMP message receiving capability.
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* (Optional) Clear the configuration of sending or receiving ICMP messages.
  
  ![](public_sys-resources/note_3.0-en-us.png) 
  
  To clear the configuration of sending or receiving ICMP messages and restore the default configuration, perform the following operations.
  
  
  
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Clear the configuration of sending or receiving ICMP messages.
     
     
     + Clear the configuration of sending ICMP messages.
       ```
       [clear icmp](cmdqueryname=clear+icmp+type+code+send) type typevalue code codevalue send
       ```
     + Clear the configuration of receiving ICMP messages.
       ```
       [clear icmp](cmdqueryname=clear+icmp+type+code+receive) type typevalue code codevalue receive
       ```
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
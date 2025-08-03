Configuring the Encapsulation Mode of 1588v2 Messages
=====================================================

Configuring the Encapsulation Mode of 1588v2 Messages

#### Context

1588v2 messages can be encapsulated into Layer 2 or Layer 3 packets for transmission. Depending on the link type, 1588v2 messages can be transmitted in MAC or UDP encapsulation mode.

* MAC encapsulation
  
  The MAC encapsulation mode is used when 1588v2 messages are transmitted over Layer 2 links, and the corresponding Ethernet type is 0x88F7.
  
  **Figure 1** Untagged MAC-encapsulated messages  
  ![](figure/en-us_image_0000001563759313.png)
  **Figure 2** Tagged MAC-encapsulated messages  
  ![](figure/en-us_image_0000001563878937.png)
* UDP encapsulation
  
  The UDP encapsulation mode is used when 1588v2 messages are transmitted over Layer 3 links, and the corresponding destination UDP port number is 319 (for non-Announce messages) or 320 (for Announce messages).
  
  **Figure 3** Untagged UDP-encapsulated messages  
  ![](figure/en-us_image_0000001513158962.png)  
  
  **Figure 4** Tagged UDP-encapsulated messages  
  ![](figure/en-us_image_0000001563999225.png)

#### Procedure

* Configure the MAC encapsulation mode.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the interface view.
     
     
     ```
     interface interface-type interface-number
     ```
  3. Configure the interface to encapsulate 1588v2 messages in unicast MAC encapsulation mode and set the destination MAC address of 1588v2 messages.
     
     
     
     | MAC Encapsulation Mode | Command | Description |
     | --- | --- | --- |
     | Unicast MAC encapsulation | [**ptp mac-egress**](cmdqueryname=ptp+mac-egress) **destination-mac** *destination-mac* | By default, no destination MAC address is configured for 1588v2 messages.  NOTE:  If an interface has been configured to encapsulate 1588v2 messages in UDP encapsulation mode, clear the existing encapsulation mode configuration on the interface before running this command to change the encapsulation mode. |
     | Multicast MAC encapsulation | - | In multicast MAC encapsulation scenarios, you do not need to run the [**ptp mac-egress**](cmdqueryname=ptp+mac-egress) **destination-mac** *destination-mac* command because 1588v2 messages use the default multicast destination MAC address defined in 1588v2.  When the delay measurement mechanism is Delay, the default multicast destination MAC address is 01-1B-19-00-00-00. |
  4. (Optional) Configure a VLAN ID and 802.1p priority for sending MAC-encapsulated 1588v2 messages.
     
     
     ```
     [ptp mac-egress](cmdqueryname=ptp+mac-egress) vlan vlan-id [ priority priority-value]
     ```
     
     By default, no VLAN ID is configured and the 802.1p priority is 7.
     
     1588v2 services require a higher *priority-value* value than other services. A high transmission priority minimizes the delay or congestion impact on clock signal recovery. Using the default highest priority value is recommended.
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure the UDP encapsulation mode.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the interface view.
     
     
     ```
     interface interface-type interface-number
     ```
  3. Configure the interface to encapsulate 1588v2 messages in UDP encapsulation mode and set the source and destination IP addresses of 1588v2 messages.
     
     
     
     | UDP Encapsulation Mode | Command | Description |
     | --- | --- | --- |
     | Unicast UDP encapsulation | [**ptp udp-egress**](cmdqueryname=ptp+udp-egress) **source-ip** *source-ip* **destination-ip** *destination-ip* | In unicast UDP encapsulation scenarios, the destination IP address of 1588v2 messages must be configured.  By default, the source and destination IP addresses of 1588v2 messages are not configured. |
     | Multicast UDP encapsulation | [**ptp udp-egress**](cmdqueryname=ptp+udp-egress) **source-ip** *source-ip* | In multicast UDP encapsulation scenarios, you do not need to specify the **destination-ip** *destination-ip* parameter because 1588v2 messages use the default multicast destination IP address defined in 1588v2.  When the delay measurement mechanism is Delay, the multicast destination IP address of 1588v2 messages encapsulated in multicast UDP mode is 224.0.1.129. |
  4. (Optional) Configure the next-hop MAC address for the interface to send 1588v2 messages.
     
     
     ```
     [ptp udp-egress](cmdqueryname=ptp+udp-egress) destination-mac destination-mac
     ```
     
     By default, the next-hop MAC address is not configured for an interface to send 1588v2 messages.
  5. (Optional) Configure the DSCP priority for the interface to send UDP-encapsulated 1588v2 packets, and the VLAN ID and priority for the interface to send or receive UDP-encapsulated 1588v2 packets.
     
     
     ```
     [ptp udp-egress](cmdqueryname=ptp+udp-egress) source-ip source-ip [ dscp dscp ] vlan vlan-id [ priority priority-value ]
     ```
     
     By default, the DSCP priority for an interface to send UDP-encapsulated 1588v2 packets is 56, the VLAN ID for an interface to send or receive UDP-encapsulated 1588v2 packets is not configured, and the priority is 7.
     
     1588v2 services require a higher *priority-value* value than other services. A high transmission priority minimizes the delay or congestion impact on clock signal recovery. Using the default highest priority value is recommended.
  6. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
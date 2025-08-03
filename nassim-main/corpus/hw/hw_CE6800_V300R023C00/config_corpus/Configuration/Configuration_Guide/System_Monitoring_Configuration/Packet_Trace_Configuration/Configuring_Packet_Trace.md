Configuring Packet Trace
========================

Configuring Packet Trace

#### Prerequisites

You have determined the device where packets are lost.


#### Context

When configuring packet trace, you need to configure a packet trace profile and then specify the interface for receiving detection packets. After the packet trace function is enabled on a device, the device constructs a detection packet and sends it to the specified interface. During forwarding of the detection packet inside the device, the device records the cause of any discarded service packets.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure a packet trace profile.
   * Specify the target packet content, which can be copied from a packet obtaining tool. This method supports both IPv4 and IPv6 packets.
     ```
     [detector packet-trace profile](cmdqueryname=detector+packet-trace+profile) profile-name packet packet-value
     ```
   * Specify key fields in TCP detection packets. This method supports only IPv4 packets.
     ```
     [detector packet-trace profile](cmdqueryname=detector+packet-trace+profile) profile-name source-mac source-mac-address destination-mac destination-mac-address [ vlan vlan-id [ 8021p 8021p-value ] ] source-ip source-ip-address destination-ip destination-ip-address [ dscp dscp-value ] [ ttl ttl-value ] tcp source-port source-port destination-port destination-port [ payload tcp-payload-value ]
     ```
   * Specify key fields in UDP detection packets. This method supports only IPv4 packets.
     ```
     [detector packet-trace profile](cmdqueryname=detector+packet-trace+profile) profile-name source-mac source-mac-address destination-mac destination-mac-address [ vlan vlan-id [ 8021p 8021p-value ] ] source-ip source-ip-address destination-ip destination-ip-address [ dscp dscp-value ] [ ttl ttl-value ] udp source-port source-port destination-port destination-port [ payload udp-payload-value ]
     ```
   * Specify key fields in ICMP detection packets. This method supports only IPv4 packets.
     ```
     [detector packet-trace profile](cmdqueryname=detector+packet-trace+profile) profile-name source-mac source-mac-address destination-mac destination-mac-address [ vlan vlan-id [ 8021p 8021p-value ] ] source-ip source-ip-address destination-ip destination-ip-address [ dscp dscp-value ] [ ttl ttl-value ] icmp icmp-type icmp-type-value icmp-code icmp-code-value [ payload icmp-payload-value ]
     ```
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   To delete a packet trace profile, run the [**undo detector packet-trace profile**](cmdqueryname=undo+detector+packet-trace+profile) command.
   
   On a device, each packet trace profile must use a unique name, and a new profile will overwrite an existing profile with the same name.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
4. Specify the interface for receiving detection packets to simulate packet forwarding inside the device, and display the simulation result.
   
   
   ```
   [display detector packet-trace profile](cmdqueryname=display+detector+packet-trace+profile) profile-name interface { interface-name | interface-type interface-number } result
   ```
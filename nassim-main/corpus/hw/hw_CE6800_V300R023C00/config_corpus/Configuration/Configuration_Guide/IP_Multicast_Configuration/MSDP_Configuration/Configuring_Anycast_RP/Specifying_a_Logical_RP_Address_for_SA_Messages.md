Specifying a Logical RP Address for SA Messages
===============================================

Specifying a Logical RP Address for SA Messages

#### Context

An MSDP peer performs RPF checks on received SA messages. If the remote RP address carried in an SA message is the same as the local RP address, the MSDP peer discards the SA message. For this reason, you need to specify a logical RP address (that is, the RP address on the logical interface) that differs from the actual RP address for SA messages on the device where anycast RP is to be configured. In this way, SA messages can pass the RPF check.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the MSDP view.
   
   
   ```
   [msdp](cmdqueryname=msdp) [ vpn-instance vpn-instance-name ]
   ```
3. Configure the address of the logical RP interface as the source RP address for SA messages.
   
   
   ```
   [originating-rp](cmdqueryname=originating-rp) interface-type interface-number
   ```
   
   The logical RP interface cannot be the same as the actual RP interface, and you are advised to specify the address of the MSDP peer interface as the logical RP address. After this command is run, the SA message sent by the device carries the logical RP address, which replaces the RP address in the SA message header.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
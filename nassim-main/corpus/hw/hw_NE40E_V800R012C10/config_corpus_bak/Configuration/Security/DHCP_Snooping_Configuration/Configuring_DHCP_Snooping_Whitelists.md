Configuring DHCP Snooping Whitelists
====================================

This section describes how to configure the whitelist function for DHCP snooping so that DHCP packets are filtered based on the whitelist rules.

#### Usage Scenario

Generally, only the trusted and untrusted functions of DHCP snooping can be used to control DHCP packets to be sent to the CPU. On the trusted interface, DHCP request and response packets are sent to the CPU. On the untrusted interface, only request packets are sent to the CPU, and response packets are dropped. To accurately control packets to be sent to the CPU on a trusted client or server, configure the whitelist function for DHCP snooping so that DHCP packets are filtered based on the whitelist rules. After a whitelist is configured for DHCP snooping, only DHCP packets matching the whitelist rules are sent to the CPU, and the DHCP packets that do not match the whitelist rules are simply forwarded. This protects the device against attacks.

In VS mode, this feature is supported only by the admin VS.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable DHCP snooping.
2. Create a whitelist.
3. Configure whitelist rules.
4. Apply the whitelist.

#### Procedure

1. Enable DHCP snooping.
   
   
   1. Run [**system-view**](cmdqueryname=system-view)
      
      The system view is displayed.
   2. Run [**dhcp snooping enable**](cmdqueryname=dhcp+snooping+enable)
      
      DHCP snooping is enabled globally.
2. Create a whitelist.
   
   
   
   Run [**dhcp snooping packet whitelist**](cmdqueryname=dhcp+snooping+packet+whitelist) *whitelist-name*
   
   A whitelist is configured to filter DHCP packets.
3. Configure whitelist rules.
   
   
   1. Run [**dhcp packet-rule**](cmdqueryname=dhcp+packet-rule) *ruleid* { **source-ip** *source-ip-address* { *source-ip-mask* | *source-ip-mask-length* } | **destination-ip** *destination-ip-address* { *destination-ip-mask* | *destination-ip-mask-length* } } \* [ **source-port** { **bootpc** | **bootps** } ] [ **destination-port** { **bootpc** | **bootps** } ]
      
      Whitelist rules are configured.
   2. Run [**commit**](cmdqueryname=commit)
      
      The configuration is committed.
   3. Run [**quit**](cmdqueryname=quit)
      
      Return to the system view.
4. Apply the whitelist.
   
   
   1. Run [**dhcp snooping apply packet whitelist**](cmdqueryname=dhcp+snooping+apply+packet+whitelist) *whitelist-name*
      
      The whitelist is applied to filter DHCP packets.
   2. Run [**commit**](cmdqueryname=commit)
      
      The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, run the [**display dhcp snooping white-list**](cmdqueryname=display+dhcp+snooping+white-list) [ **rule-id** *rule-id* ] [ **slot** *slot-id* ] **statistics** command to check statistics about packets matching a DHCP snooping whitelist rule.
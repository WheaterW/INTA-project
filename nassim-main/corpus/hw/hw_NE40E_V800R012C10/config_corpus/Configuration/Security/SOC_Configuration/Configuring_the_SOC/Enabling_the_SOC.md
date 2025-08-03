Enabling the SOC
================

You can enable the Security Operating Center (SOC) by enabling attack detection, attack source tracing, and attack defense.

#### Context

Attack detection and attack source tracing are key SOC functions. Before using the SOC, ensure that these functions are enabled. If attack detection and attack source tracing are left disabled, the SOC can still be triggered by timers to collect the CPU usage, protocol module's state data, including the number of invalid packets and sessions, and CPCAR-related packet loss statistics. However, the SOC neither performs attack detection and attack source tracing nor generates alarms, and therefore cannot locate attack events.

After attack defense is enabled, the SOC automatically delivers attack defense policies if the NE40E is being attacked. This function isolates attacks or protects the NE40E against attacks.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**soc**](cmdqueryname=soc)
   
   
   
   Attack detection and attack source tracing are enabled, and the SOC view is displayed.
3. (Optional) Run [**attack-defend enable**](cmdqueryname=attack-defend+enable)
   
   
   
   Attack defense is enabled.
   
   If the SOC determines that an attack event has occurred, enable attack defense.
4. (Optional) Specify protocols in a user-defined group for which attack defense is enabled or disabled.
   1. (Optional) Run [**attack-defend user-enable-group**](cmdqueryname=attack-defend+user-enable-group)
      
      
      
      A user-defined group for which attack defense is enabled is configured, and the user-group view is displayed.
   2. (Optional) Run [**attack-defend user-disable-group**](cmdqueryname=attack-defend+user-disable-group)
      
      
      
      A user-defined group for which attack defense is disabled is configured, and the user-group view is displayed.
      
      
      
      You can specify the following protocols for a user-defined group: FTP server, FTP client, SSH server, SSH client, SNMP, Telnet server, Telnet client, TFTP, BGP, LDP, RSVP, OSPFv2, RIP, OSPFv3, MSDP, PIM, IGMP, IS-IS, PIMv6, RADIUS, HWTACACS, LSP ping, ICMP, VRRP, BFD, DHCP, DNS client, Telnetv6 server, Telnetv6 client, ICMPv6, DNSv6, SSHv6 server, FTPv6 server, FTPv6 client, LACP, and BGPv6. For example, to specify DHCP in a user-defined group for which attack defense is enabled or disabled, configure [**dhcp**](cmdqueryname=dhcp) in the command.
      
      ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
      
      One protocol cannot be configured in both the user-defined group for which attack defense is enabled and the user-defined groups for which attack defense is disabled.
      
      The priority of the user-defined group configuration is higher than that of the [**attack-defend enable**](cmdqueryname=attack-defend+enable) command configuration.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
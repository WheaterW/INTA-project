Configuring an IPv6 MPAC Policy
===============================

An IPv6 management plane access control (MPAC) policy can be configured to determine the IPv6 packets that can be sent to the CPU.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**service-security policy**](cmdqueryname=service-security+policy) **ipv6** *security-policy-name*
   
   
   
   An IPv6 MPAC policy is configured, and its view is displayed.
3. Configure a rule for the IPv6 MPAC policy.
   
   
   
   **Table 1** Configuring a rule for the IPv6 MPAC policy
   | Protocol Type | Configuration Command | Remarks |
   | --- | --- | --- |
   | TCP or UDP | [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **permit** | **deny** } **protocol** { **tcp** | *tcp-protocol-number* | **udp** | *udp-protocol-number* } [ [ **source-port** *source-port-number* ] | [ **destination-port** *destination-port-number* ] | [ **source-ip** { *source-ipv6-address* { *source-ipv6-prefix-length* | 0 } | **any** } ] | [ **destination-ip** { *destination-ipv6-address* { *destination-ipv6-prefix-length* | 0 } | **any** } ] ] \* | - |
   | BGP, DHCP-C, DHCP-R, FTP, IP, LDP, LSP ping, NTP, OSPF, PIM, RIP, RSVP, SNMP, SSH, Telnet, or TFTP | [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **permit** | **deny** } **protocol** { *ip-protocol-number* | **bgp** | **dhcp-c** | **dhcp-r** | **ftp** | **ip** | **ldp** | **lsp-ping** | **ntp** | **ospf** | **pim** | **rip** | **rsvp** | **snmp** | **ssh** | **telnet** | **tftp** } [ [ **source-ip** { *source-ipv6-address* { *source-ipv6-prefix-length* | 0 } | **any** } ] | [ **destination-ip** { *destination-ipv6-address* { *destination-ipv6-prefix-length* | 0 } | **any** } ] ] \* | - |
   | Any protocol | [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } **protocol** **any** | Exercise caution when running the [**rule**](cmdqueryname=rule) [ *rule-id* ] **deny** **protocol** **any** command. If a policy containing this rule is applied globally, no protocol packets are sent to the CPU, causing the device to be out of management. |
   | SRH | [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **permit** | **deny** } **ipv6-ext-header** **source-routing-typer** **srh** | - |
4. (Optional) Run [**step**](cmdqueryname=step) *step*
   
   
   
   A step is configured for the rules in the MPAC policy.
5. (Optional) Run [**description**](cmdqueryname=description) *text*
   
   
   
   A description is configured for the MPAC policy.
6. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
7. Apply the IPv6 MPAC policy.
   
   
   * Apply the IPv6 MPAC policy globally.
     
     Run the [**service-security global-binding**](cmdqueryname=service-security+global-binding) **ipv6** *security-policy-name* command.
   * Apply the IPv6 MPAC policy on an interface.
     
     1. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the interface view.
     2. Run the [**service-security policy**](cmdqueryname=service-security+policy) **ipv6** *security-policy-name* command to apply the IPv6 MPAC policy on the interface.![](../../../../public_sys-resources/note_3.0-en-us.png) The MPAC policies on a sub-interface,
   interface, or configured globally are listed in descending order of
   priorities. When different MPAC policies are applied globally, to
   an interface, and to a sub-interface, the MPAC policy on the sub-interface
   takes effect preferentially, and then the MPAC policy on the interface,
   and then the MPAC policy applied globally.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
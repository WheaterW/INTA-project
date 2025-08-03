Configuring an IPv4 MPAC Policy
===============================

An IPv4 Management Plane Access Control (MPAC) policy can
be configured to filter IPv4 packets destined for the CPU.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**service-security policy**](cmdqueryname=service-security+policy) **ipv4** *security-policy-name*
   
   
   
   An IPv4 MPAC policy is created, and the IPv4 MPAC policy
   view is displayed.
3. Add a rule to the IPv4 MPAC policy. See the following table.
   
   
   
   **Table 1** Rules for an IPv4 MPAC policy
   | Protocol Type | Command | Remarks |
   | --- | --- | --- |
   | TCP or UDP | [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **permit** | **deny** } **protocol** { **tcp** | *tcp-protocol-number* | **udp** | *udp-protocol-number* } [ [ **source-port** *source-port-number* ] | [ **destination-port** *destination-port-number* ] | [ **source-ip** { *source-ipv4-address* { *source-ipv4-mask* | 0 } | **any** } ] | [ **destination-ip** { *destination-ipv4-address* { *destination-ipv4-mask* | 0 } | **any** } ] ] \* | - |
   | BGP, Dynamic Host Configuration Protocol-C(DHCP-C), Dynamic Host Configuration Protocol-R(DHCP-R), FTP, IP, LDP, LSP ping, NTP, OSPF, PIM, RIP, RSVP, SNMP, SSH, Telnet, TFTP, or IGMP | [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **permit** | **deny** } **protocol** { *ip-protocol-number* | **bgp** | **dhcp-c** | **dhcp-r** | **ftp** | **ip** | **ldp** | **lsp-ping** | **ntp** | **ospf** | **pim** | **rip** | **rsvp** | **snmp** | **ssh** | **telnet** | **tftp** | **igmp** } [ [ **source-ip** { *source-ipv4-address* { *source-ipv4-mask* | 0 } | **any** } ] | [ **destination-ip** { *destination-ipv4-address* { *destination-ipv4-mask* | 0 } | **any** } ] ] \* | - |
   | IS-IS or any other protocol | [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } **protocol** { **any** | **isis** } | Exercise caution when using the [**rule**](cmdqueryname=rule) [ *rule-id* ] **deny** **protocol** **any** command. After this command is applied globally, no protocol packets are sent to the CPU, causing the device to be out of management. |
4. (Optional) Run [**step**](cmdqueryname=step) *step*
   
   
   
   The step is configured for rules
   in the MPAC policy.
5. (Optional) Run [**description**](cmdqueryname=description) *text*
   
   
   
   The description is configured
   for the MPAC policy.
6. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
7. Apply an IPv4 MPAC policy.
   
   
   * Apply an IPv4 MPAC policy globally.
     
     Run [**service-security global-binding**](cmdqueryname=service-security+global-binding) **ipv4** *security-policy-name*
     
     An MPAC policy is applied globally.
   * Apply an IPv4 MPAC policy to an interface.
     
     1. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
        
        The interface view is displayed.
     2. Run [**service-security binding**](cmdqueryname=service-security+binding) **ipv4** *security-policy-name*
        
        The MPAC policy
        is applied to the interface.![](../../../../public_sys-resources/note_3.0-en-us.png) The MPAC policies on a sub-interface,
   interface, or configured globally are listed in descending order of
   priorities. When different MPAC policies are applied globally, to
   an interface, and to a sub-interface, the MPAC policy on the sub-interface
   takes effect preferentially, and then the MPAC policy on the interface,
   and then the MPAC policy applied globally.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is
   committed.
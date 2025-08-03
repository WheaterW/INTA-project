Configuring an Address Assignment Mode
======================================

The address assignment modes supported by the NE40E include NDRA, DHCPv6 (IA\_NA), DHCPv6 (IA\_PD), DHCPv6 (IA\_NA)+DHCPv6 (IA\_PD), and NDRA+DHCPv6 (IA\_PD). You can configure an address assignment mode as required.

#### Context

* If an IPv4 network is upgraded to an IPv6 network, the CPE working mode and authentication mode do not need to be changed unless there are special service requirements.![](../../../../public_sys-resources/note_3.0-en-us.png) 
  + Layer 2 IPv6 leased line access is equivalent to the situation where a CPE works in unnumbered or numbered routing mode.
  + Layer 3 IPv6 users of a leased line obtain their addresses from the access router. The NE40E is in charge of only authentication and accounting, not address assignment.
* In PPP authentication mode, either ND or DHCPv6 can be used for address assignment.

#### Procedure

1. The address assignment mode varies according to the CPE working mode. For details, see the following table.
   
   
   
   | CPE Working Mode | Scenario | IPv6 Address Configuration Mode |
   | --- | --- | --- |
   | Bridging mode | A host initiates a connection request. A CPE transparently forwards user request packets, and the NE40E assigns an IPv6 address to the host. | [NDRA](dc_ne_ipv6_address_cfg_0020.html) |
   | [DHCPv6 (IA\_NA)](dc_ne_ipv6_address_cfg_0027.html) |
   | Unnumbered routing mode | A CPE initiates a connection request. After receiving the request, the NE40E assigns a prefix to the CPE to generate IPv6 addresses for the hosts attached to the CPE. | [DHCPv6 (IA\_PD)](dc_ne_ipv6_address_cfg_0035.html) |
   | Numbered routing mode | A CPE initiates a connection request. After receiving the request, the NE40E assigns an IPv6 address to the WAN interface on the CPE and a prefix to the CPE to generate IPv6 addresses for the hosts attached to the CPE. | [DHCPv6 (IA\_NA)+DHCPv6 (IA\_PD)](dc_ne_ipv6_address_cfg_0053.html) |
   | [NDRA+DHCPv6 (IA\_PD)](dc_ne_ipv6_address_cfg_0043.html) |
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In a home broadband scenario where CU separation is deployed, if PPPoEv6 authentication is used for user access, users may fail to obtain IPv6 addresses due to limited hardware parsing capability after the [**load-balance identify pppoe**](cmdqueryname=load-balance+identify+pppoe) command is run in the slot view of the UP.
2. (Optional) In addition to choosing an address assignment mode, perform the following steps on the NE40E if needed:
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**aaa**](cmdqueryname=aaa)
      
      
      
      The AAA view is displayed.
   3. Run [**domain**](cmdqueryname=domain) *domain-name*
      
      
      
      An AAA domain is created, and its view is displayed.
   4. Run **commit**
      
      
      
      The configuration is committed.
   5. Run [**user-basic-service-ip-type**](cmdqueryname=user-basic-service-ip-type) { **ipv4** | **ipv6** | **ipv6-pd** } \*
      
      
      
      An IP type is configured for the main service of a user who goes online from the domain. In this case, if the IP address of this type fails to be assigned, users of other IP types are forced to go offline, and the user fails to go online.
   6. Run [**ipv6 nd ra halt**](cmdqueryname=ipv6+nd+ra+halt)
      
      
      
      The NE40E is suppressed from sending RA messages to IPv6 access users.
   7. Run [**ppp address-release separate**](cmdqueryname=ppp+address-release+separate)
      
      
      
      PPP dual-stack users are allowed to go offline from a single stack.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      This command and the [**any-address-release offline**](cmdqueryname=any-address-release+offline) command are mutually exclusive.
   8. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
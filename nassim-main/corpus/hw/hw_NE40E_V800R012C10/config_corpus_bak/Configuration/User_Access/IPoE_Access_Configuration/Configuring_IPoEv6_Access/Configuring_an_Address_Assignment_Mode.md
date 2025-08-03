Configuring an Address Assignment Mode
======================================

The address assignment modes supported by the NE40E include NDRA, DHCPv6 (IA\_NA), DHCPv6 (IA\_PD), DHCPv6 (IA\_NA)+DHCPv6 (IA\_PD), and NDRA+DHCPv6 (IA\_PD). Configure an address assignment mode based on networking requirements.

#### Context

* If an IPv4 network is upgraded to an IPv6 network, the CPE working mode and authentication mode do not need to be changed unless there are special service requirements.![](../../../../public_sys-resources/note_3.0-en-us.png) 
  + Layer 3 users of a leased line obtain their addresses from the access router. The NE40E is in charge of only authentication and accounting, not address assignment.
* In binding authentication mode, using DHCPv6 for address assignment is recommended.
* In web authentication mode, using DHCPv6 for address assignment is recommended if user terminals support ND+PD.

#### Procedure

1. The address assignment mode varies according to CPE working modes. For details, see the following table.
   
   
   
   | CPE Working Mode | Scenario | IPv6 Address Configuration Mode |
   | --- | --- | --- |
   | Bridging mode | A host initiates a connection request. The CPE transparently forwards the user request packet, and the NE40E assigns an IPv6 address to the host. | [NDRA](dc_ne_ipv6_address_cfg_0020.html) |
   | [DHCPv6(IA\_NA)](dc_ne_ipv6_address_cfg_0027.html) |
   | Unnumbered routing mode | The CPE initiates a connection request. After receiving the request, the NE40E assigns a prefix to the CPE to generate IPv6 addresses for hosts attached to the CPE. | [DHCPv6(IA\_PD)](dc_ne_ipv6_address_cfg_0035.html) |
   | Numbered routing mode | The CPE initiates a connection request. After receiving the request, the NE40E assigns an IPv6 address to the WAN interface on the CPE and a prefix to generate IPv6 addresses for hosts attached to the CPE. | [DHCPv6(IA\_NA)+DHCPv6(IA\_PD)](dc_ne_ipv6_address_cfg_0053.html) |
   | [NDRA+DHCPv6(IA\_PD)](dc_ne_ipv6_address_cfg_0043.html) |
2. (Optional) Configure the device to separately release PD addresses for IPoE users.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**aaa**](cmdqueryname=aaa)
      
      
      
      The AAA view is displayed.
   3. Run [**domain**](cmdqueryname=domain) *domain-name*
      
      
      
      The AAA domain view is displayed.
   4. Run [**ipv6 pd-address-release separate user-type ipoe**](cmdqueryname=ipv6+pd-address-release+separate+user-type+ipoe)
      
      
      
      The device is enabled to release only the assigned PD addresses in scenarios where CPEs work in numbered routing mode.
   5. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
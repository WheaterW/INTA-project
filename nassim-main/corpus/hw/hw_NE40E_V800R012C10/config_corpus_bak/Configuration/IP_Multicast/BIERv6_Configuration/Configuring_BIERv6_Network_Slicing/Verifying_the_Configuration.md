Verifying the Configuration
===========================

After configuring BIERv6 network slicing, check the committed configurations and whether they have taken effect.

#### Procedure

* Run the [**display network-slice**](cmdqueryname=display+network-slice) [ *slice-id* ] **binding-list** [ **interface** *ifIndex* ] command to check the binding relationships between the basic and network slice interfaces in a network slice instance.
* Run the **[**display mvpn**](cmdqueryname=display+mvpn)** { **vpn-instance** *vpn-instance-name* | **all-instance** | **public** } **ingress** **bier** **ipv6** [ **group** *group-address* **source** *source-address* ] command to check stream information on the ingress in NG MVPNv4 over BIERv6 and GTMv4 over BIERv6 scenarios.
* Run the **[**display mvpn ipv6**](cmdqueryname=display+mvpn+ipv6)** { **vpn-instance** *vpn-instance-name* | **all-instance** | **public** } **ingress** **bier** **ipv6** [ **group** *group-address* **source** *source-address* ] command to check stream information on the ingress in NG MVPNv6 over BIERv6 and GTMv6 over BIERv6 scenarios.
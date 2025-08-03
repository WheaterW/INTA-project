Configuring Dynamic Domain Name Resolution
==========================================

Configuring Dynamic Domain Name Resolution

#### Prerequisites

Before configuring dynamic domain name resolution, you have completed the following task:

* Configure a route between the device and DNS server.


#### Context

Dynamic domain name resolution requires a dedicated DNS server, which receives domain name resolution requests from DNS clients, for DNS query. Upon receiving a request, the DNS server searches for the corresponding IP address of the domain name in its DNS database. If no matching entry is found, it sends the request to a higher-level DNS server. This process continues until the DNS server finds the corresponding IP address or detects that the corresponding IP address of the domain name does not exist. The DNS server then returns a result to the DNS client.

![](public_sys-resources/note_3.0-en-us.png) 

The CE6885-LL supports IPv6 domain name resolution only in standard forwarding mode.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable dynamic domain name resolution.
   
   
   ```
   [dns resolve](cmdqueryname=dns+resolve)
   ```
3. Configure the IPv4 or IPv6 address of the DNS server to be accessed by the device.
   
   
   
   Configure the IPv4 or IPv6 address of the DNS server statically.
   
   
   
   * Configure the IPv4 address of the DNS server.
     ```
     [dns server](cmdqueryname=dns+server) ip-address [ vpn-instance vpn-instance-name ]
     ```
   * Configure the IPv6 address of the DNS server.
     ```
     [dns server ipv6](cmdqueryname=dns+server+ipv6) ipv6-address [ interface-type interface-number ] [ vpn-instance vpn-instance-name ]
     ```
4. (Optional) Configure the source IPv4 or IPv6 address used by the device to communicate with the DNS server.
   * Configure the source IPv4 address used by the device to communicate with the DNS server.
     ```
     [dns server source-ip](cmdqueryname=dns+server+source-ip) [ vpn-instance vpn-instance-name ] ip-address
     ```
     
     You can also configure the device to use the IP address of a specified interface as the source IP address.
     
     ```
     [dns server source-interface](cmdqueryname=dns+server+source-interface) { interface-type interface-number | interface-name }
     ```
     
     By default, the source interface IP address is used as the source IP address of DNS query packets. This function is supported only if the device performs a DNS query through the DNS server with an IPv4 address and is not supported if the device performs a DNS query through the DNS server with an IPv6 address.
   * Configure the source IPv6 address used by the device to communicate with the DNS server.
     ```
     [dns server ipv6 source-ip](cmdqueryname=dns+server+ipv6+source-ip) [ vpn-instance vpn-instance-name ] ipv6-address
     ```
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   Ensure that the source IP address is an IP address on the device and that the route between the IP address and the DNS server is reachable.
   
   Ensure that the source IP address and the IP address of the DNS server are on the same VPN or public network.
5. (Optional) Configure the device to send DNS query requests to the DNS server on a specified VPN.
   
   
   ```
   [dns server vpn-instance](cmdqueryname=dns+server+vpn-instance) vpn-instance-name
   ```
   
   
   
   By default, a device can only send DNS query requests to a DNS server on a public network.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If this command is run more than once, the latest configuration overrides the previous one.
   
   A device can send DNS query requests to a DNS server on a public network or VPN.
   
   A device can respond to DNS query requests sent by DNS clients on multiple VPNs.
6. (Optional) Configure a domain name suffix list.
   
   
   ```
   [dns domain](cmdqueryname=dns+domain) domain-name [ vpn-instance vpn-instance-name ]
   ```
   
   
   
   Pre-defining some domain name suffixes allows you to enter only parts of a domain name. The system automatically adds a specific suffix to resolve the domain name.
   
   For instance, if you configure "com" in the suffix list and enter "example" in a domain name query, the system automatically associates "example" with the suffix "com" and searches for "example.com." You may encounter the following situations during a resolution process:
   * If you enter a domain name without a period (.), such as "example", the system considers it as a hostname and adds suffixes for a search. If there is no matched domain name, the system searches for an IP address mapped to "example."
   * If you enter a domain name with a period (.), such as "www.example", the system immediately searches for it. If the system does not find a matched entry, it adds every configured suffix to search for an IP address mapped to the domain name.
   * If you enter a domain name with a period (.) at the end, such as "example.com.", the system removes the last period (.) before searching for an IP address mapped to the domain name. If the search fails, the system adds every configured suffix to the domain name without the last period to search for an IP address mapped to the domain name.
7. (Optional) Customize a DNS.
   
   
   
   Perform this step to customize DNS configurations.
   
   **Table 1** Customizing a DNS
   | Operation | Command | Description |
   | --- | --- | --- |
   | Configure the maximum and minimum life cycles of the DNS cache for applications. | [**dns application cache ttl**](cmdqueryname=dns+application+cache+ttl) **maximum** *max-seconds* **minimum** *min-seconds* | By default, the maximum and minimum life cycles of the DNS cache for applications are 86400s and 600s, respectively.  The DNS cache for applications refers to that used by other modules (such as SIP and GRE) of the device to resolve domain names. |
   | Configure a mode for the device to select a DNS server. | [**dns-server-select-algorithm**](cmdqueryname=dns-server-select-algorithm) { **fixed** | **auto** } | By default, the mode for a device to select a DNS server is **auto**. |
   | Configure the number of times that the device retransmits query requests to the destination DNS server. | [**dns forward retry-number**](cmdqueryname=dns+forward+retry-number) *number* | By default, a device retransmits query requests to the destination DNS server twice. |
   | Configure a retransmission timeout period for query requests to the destination DNS server. | [**dns forward retry-timeout**](cmdqueryname=dns+forward+retry-timeout) *timeout-value* | By default, the retransmission timeout period for query requests to the destination DNS server is 3s. |
   
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The total timeout period for DNS query requests obtained using the [**dns forward retry-number**](cmdqueryname=dns+forward+retry-number) and [**dns forward retry-timeout**](cmdqueryname=dns+forward+retry-timeout) commands cannot be too short. Generally, default values are used. If services become abnormal because a long time is taken to wait for a resolution response from the DNS server, you can prolong the total timeout period.
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display dns configuration**](cmdqueryname=display+dns+configuration) command to check global DNS configurations.
* Run the [**display dns dynamic-host**](cmdqueryname=display+dns+dynamic-host) [ **ip** ] [ *domain-name* ] [ **vpn-instance** *vpn-instance-name* ] command to check dynamic IPv4 DNS entries.
* Run the [**display dns ipv6 dynamic-host**](cmdqueryname=display+dns+ipv6+dynamic-host) [ *domain-name* ] [ **vpn-instance** *vpn-instance-name* ] command to check dynamic IPv6 DNS entries.
* Run the [**display dns server**](cmdqueryname=display+dns+server) [ **vpn-instance** *vpn-instance-name* ] [ **verbose** ] command to check DNS server information.
* Run the [**display dns domain**](cmdqueryname=display+dns+domain) [ **vpn-instance** *vpn-instance-name* ] [ **verbose** ] command to check domain name suffix information.
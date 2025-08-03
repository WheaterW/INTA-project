Configuring Static Domain Name Resolution
=========================================

Configuring Static Domain Name Resolution

#### Context

A static domain name resolution table is used for DNS query based on the manually created mappings between domain names and IP addresses. Common domain names can be added to the table for static domain name resolution. A DNS client first searches the static domain name resolution table for a domain name to resolve it into an IP address. This is an efficient method for domain name resolution.

![](public_sys-resources/note_3.0-en-us.png) 

The CE6885-LL supports IPv6 domain name resolution only in standard forwarding mode.



#### Procedure

* Configure IPv4 static domain name resolution.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Configure a static IPv4 DNS entry.
     
     
     ```
     [ip host](cmdqueryname=ip+host) host-name ip-address [ vpn-instance vpn-instance-name ]
     ```
     
     By default, no static IPv4 DNS entry is configured.
     
     Each hostname can be mapped to only one IPv4 address. If a hostname is mapped to multiple IPv4 addresses, only the latest configuration takes effect. If multiple hostnames need to be resolved, repeat this step. A maximum of 50 static IPv4 DNS entries can be configured.
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure IPv6 static domain name resolution.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Configure a static IPv6 DNS entry.
     
     
     ```
     [ipv6 host](cmdqueryname=ipv6+host) host-name ipv6-address [ vpn-instance vpn-instance-name ]
     ```
     
     By default, no static IPv6 DNS entry is configured.
     
     Each hostname can be mapped to only one IPv6 address. If a hostname is mapped to multiple IPv6 addresses, only the latest configuration takes effect. If multiple hostnames need to be resolved, repeat this step. A maximum of 50 static IPv6 DNS entries can be configured.
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```

#### Verifying the Configuration

* Run the [**display ip host**](cmdqueryname=display+ip+host) [ **vpn-instance** *vpn-instance-name* ] command to check static IPv4 DNS entries.
* Run the [**display ipv6 host**](cmdqueryname=display+ipv6+host) [ **vpn-instance** *vpn-instance-name* ] command to check static IPv6 DNS entries.
Configuring an HTTPS Client
===========================

Configuring an HTTPS Client

#### Prerequisites

Before configuring an HTTPS client, you have completed the following task:

* There are reachable routes between the device and HTTPS server.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable HTTP and enter the HTTP view.
   
   
   ```
   [http](cmdqueryname=http)
   ```
3. Configure an SSL policy for the HTTPS client.
   
   
   ```
   [client ssl-policy](cmdqueryname=client+ssl-policy) policy-name
   ```
4. Configure the HTTPS client to authenticate the server.
   
   
   ```
   [client ssl-verify peer](cmdqueryname=client+ssl-verify+peer)
   ```
5. (Optional) Configure the source interface bound to the HTTPS client.
   
   
   ```
   [client source-interface](cmdqueryname=client+source-interface) { interface-name | interface-type interface-number }
   ```
   
   By default, no source interface is bound to the HTTPS client.
6. (Optional) Configure the source IPv6 address and VPN for the HTTP client.
   
   
   ```
   [client ipv6 source-address](cmdqueryname=client+ipv6+source-address) ipv6-address [ vpn-instance ipv6-vpn-instance-name ]
   ```
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
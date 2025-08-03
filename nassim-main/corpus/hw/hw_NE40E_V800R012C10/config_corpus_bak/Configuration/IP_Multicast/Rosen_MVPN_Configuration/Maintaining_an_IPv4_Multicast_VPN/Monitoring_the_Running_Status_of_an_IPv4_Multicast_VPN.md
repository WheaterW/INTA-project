Monitoring the Running Status of an IPv4 Multicast VPN
======================================================

During routine maintenance of an IPv4 multicast VPN, you can run the **display** commands in any view to obtain the running status of the IPv4 multicast VPN.

#### Context

You can run the following commands in any view to check the running status of an IPv4 multicast VPN.


#### Procedure

* Run the [**display multicast-domain vpn-instance**](cmdqueryname=display+multicast-domain+vpn-instance) *vpn-instance-name* **share-group** [ **local** ] command in any view to check Share-Group information about a specified VPN instance in a multicast domain (MD).
* Run the following commands in any view to check switch-group information received by a specified VPN instance in an MD.
  
  
  + [**display multicast-domain vpn-instance**](cmdqueryname=display+multicast-domain+vpn-instance) *vpn-instance-name* **switch-group** **receive** **brief**
  + [**display multicast-domain vpn-instance**](cmdqueryname=display+multicast-domain+vpn-instance) *vpn-instance-name* **switch-group** **receive** [ **active** | **group** *group-address* | **sender** *source-address* | *vpn-source-address* [ **mask** { *source-mask-length* | *source-mask* } ] | *vpn-group-address* [ **mask** { *group-mask-length* | *group-mask* } ] ] \*
* Run the [**display multicast-domain vpn-instance**](cmdqueryname=display+multicast-domain+vpn-instance) *vpn-instance-name* **switch-group** **send** [ **group** *group-address* | **reuse** *interval* | *vpn-source-address* [ **mask** { *source-mask-length* | *source-mask* } ] | *vpn-group-address* [ **mask** { *group-mask-length* | *group-mask* } ] ] \* command in any view to check the switch-group information sent by a specified VPN instance in an MD.
* Run the [**display multicast-domain**](cmdqueryname=display+multicast-domain) { **vpn-instance** *vpn-instance-name* | **all-instance** } **control-message counters** command in any view to check the statistics about sent and received MDT switch messages in a specified VPN instance or all VPN instances.
* Run the [**display multicast-domain**](cmdqueryname=display+multicast-domain) { **vpn-instance** *vpn-instance-name* | **all-instance** } **invalid-packet** command in any view to check the statistics about invalid MDT switch messages received by a device.
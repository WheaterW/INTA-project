Verifying the MD VPN Configuration
==================================

After configuring a multicast domain (MD) VPN, verify the Share-Group and multicast tunnel interface (MTI) information about a specified VPN instance.

#### Procedure

* Run the [**display multicast-domain vpn-instance**](cmdqueryname=display+multicast-domain+vpn-instance) *vpn-instance-name* **share-group** [ **local** ] command to check the Share-Group information about the MD for a specified VPN instance.
* Run the [**display pim vpn-instance**](cmdqueryname=display+pim+vpn-instance) *vpn-instance-name* **interface** **mtunnel** *interface-number* [ **verbose** ] command to check MTI information.
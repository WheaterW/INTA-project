Configuring HTTPS for System Software Download
==============================================

Configuring HTTPS for System Software Download

#### Prerequisites

Before configuring HTTPS for system software download, you have completed the following task:

* Configure an SSL policy.


#### Context

The device can download system software using HTTPS. If no SSL policy is specified, the SSL policy configured on the HTTPS client is used.


#### Procedure

1. Download a file.
   
   
   ```
   [download](cmdqueryname=download) file-url [ save-as file-path | [ ssl-policy policy-name [ ssl-verify peer [ verify-dns ] ] | verify-dns ] | vpn-instance vpn-name | source-ip ip-address ] *
   ```
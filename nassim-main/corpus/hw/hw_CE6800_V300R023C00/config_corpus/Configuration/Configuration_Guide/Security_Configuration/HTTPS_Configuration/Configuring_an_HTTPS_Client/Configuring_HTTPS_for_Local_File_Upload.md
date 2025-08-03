Configuring HTTPS for Local File Upload
=======================================

Configuring HTTPS for Local File Upload

#### Prerequisites

Before configuring HTTPS for local file upload, you have completed the following task:

* Configure an SSL policy.


#### Context

The device can upload a local file to a server using HTTPS. If no SSL policy is specified, the SSL policy configured on the HTTPS client is used. You can analyze the device running status on the server based on the local file.


#### Procedure

1. Upload a file.
   
   
   ```
   [upload](cmdqueryname=upload) file-url local-file file-path [ [ ssl-policy policy-name [ ssl-verify peer [ verify-dns ] ] | verify-dns ] | user-name name-value password password-value | vpn-instance vpn-name | source-ip ip-address ] *
   ```
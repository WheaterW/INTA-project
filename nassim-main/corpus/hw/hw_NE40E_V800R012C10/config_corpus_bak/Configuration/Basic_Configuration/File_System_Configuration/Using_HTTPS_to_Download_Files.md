Using HTTPS to Download Files
=============================

You can download the version package using HTTPS.

#### Prerequisites

You have logged in to the HTTPS server using HTTPS. For details, see [Using HTTP to Log In to Other Devices](dc_vrp_http_cfg_0010.html).


#### Context

When the device functions as a client, you can use HTTPS to obtain the version package from the remote HTTPS server and save it to the local device for version upgrade.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

HTTPS is supported, whereas HTTP is not.



#### Procedure

1. Run the [**download**](cmdqueryname=download) *file-url* [ **save-as** *file-path* | [ **ssl-policy** *policy-name* [ **ssl-verify** **peer** [ **verify-dns** ] ] | **verify-dns** ] | **vpn-instance** *vpn-name* | **source-ip** *ip-address* ]\*command to download the version package of the specified URL to the corresponding path of the device.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Only .cc version packages can be downloaded in this case.
   
   The value of source-ip can be an IPv4 or IPv6 address.
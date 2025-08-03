Setting Parameters for Configuring the Device to Send Test Results to the FTP Server
====================================================================================

Before starting a test instance, set the IP address of the FTP server that receives test results, username and password for logging in to the FTP server, name of the file in which test results are saved, interval at which test results are uploaded, and number of retransmissions.

#### Context

Perform the following operations on the NQA client.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**nqa upload**](cmdqueryname=nqa+upload) **test-type** { **icmp** | **icmpjitter** | **jitter** | **udp** } **ftp** **ipv4** *ipv4-address* **file-name** *file-name* [ **vpn-instance** *vpn-instance-name* ] [ **port** *port-number* ] **username** *user-name* **password** *password* [ **interval** *upload-interval* ] [ **retry** *retry-times* ]
   
   
   
   The function to upload the result of a test instance of a specified type to a specified server is enabled.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
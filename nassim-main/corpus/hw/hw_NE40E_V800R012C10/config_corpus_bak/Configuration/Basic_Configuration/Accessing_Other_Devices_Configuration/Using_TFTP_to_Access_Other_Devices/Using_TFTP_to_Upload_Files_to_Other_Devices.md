Using TFTP to Upload Files to Other Devices
===========================================

You can run the **tftp** command to upload files from the local device to a remote server.

#### Context

To upload a file, the TFTP client sends a write request to the TFTP server. After receiving data, the TFTP client sends an acknowledgement to the server.

Perform one of the following operations based on the IP address type of the server:


#### Procedure

* Run [**tftp**](cmdqueryname=tftp) [ **-a** *source-ip-address* | **-i** *interface-type interface-number* ] *host-ip-address* [ **vpn-instance** *vpn-instance-name* ] **put** *source-filename* [ *destination-filename* ]
  
  
  
  A file is uploaded using TFTP.
  
  The interface type specified by *interface-type* must be loopback.
* Run [**tftp ipv6**](cmdqueryname=tftp+ipv6) [ **-a** *source-ipv6âaddress* ] *tftp-server-ipv6* [ [ **vpn-instance** *vpn-instance-name* | **public-net** ] ] [**-oi** *interface-type interface-number* ] **put** *source-filename* [ *destination-filename* ]
  
  
  
  TFTP is used to upload files.
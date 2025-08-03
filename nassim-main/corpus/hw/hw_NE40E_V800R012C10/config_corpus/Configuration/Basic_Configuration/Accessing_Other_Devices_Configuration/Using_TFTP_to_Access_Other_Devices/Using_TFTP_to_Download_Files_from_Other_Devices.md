Using TFTP to Download Files from Other Devices
===============================================

You can run the **tftp** command to download files from a remote server to the local device.

#### Context

A virtual private network (VPN) is connected to remote devices or terminals over the Internet. After a TFTP session is established, you can specify *vpn-instance-name* in the **tftp** command to connect to a remote TFTP server.

To download a file, the TFTP client sends a read request to the TFTP server. After receiving data, the TFTP client sends an acknowledgement message to the server.

Perform one of the following operations based on the IP address type of the server:


#### Procedure

* Run [**tftp**](cmdqueryname=tftp) [ **-a** *source-ip-address* | **-i** *interface-type interface-number* ] *host-ip-address* [ **vpn-instance** *vpn-instance-name* | **public-net** ] **get** *source-filename* [ *destination-filename* ]
  
  
  
  A file is downloaded using TFTP.
  
  The interface type specified by *interface-type* must be loopback.
* Run [**tftp ipv6**](cmdqueryname=tftp+ipv6) [ **-a** *source-ipv6-address* ] *tftp-server-ipv6* [ **vpn-instance** *vpn-instance-name* | public-net ] [ **-oi** *interface-type interface-number* ] **get** *source-filename* [ *destination-filename* ]
  
  
  
  TFTP is used to download files.
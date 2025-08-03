Using Telnet to Log In to Other Devices
=======================================

Telnet is a client/server application that allows you to log in to remote devices to manage and maintain the devices.

#### Context

Telnet uses the client/server model to present a user interface that enables a terminal to remotely log in to a server. You can log in to a device, and then log in to another device on the network through Telnet to configure and manage the device. You do not need to connect a hardware terminal to each device.

An IP address can be configured for an interface on the device and specified as the source IP address of a Telnet connection for security verification.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Telnet does not have a secure authentication mode, and transmits data using TCP in plaintext. This is not safe. On a network with high security requirements, STelnet is recommended.



#### Procedure

* Perform either of the following operations based on the source IP address type:
  
  
  + IPv4 source address:
    
    Run the [**telnet**](cmdqueryname=telnet) [ **-i** { *interface-type* *interface-number* | *interface-name* } | [ **vpn-instance** *vpn-instance-name* ] [ **-a** *source-ip-address* ] ] *host-ip-address* [ *port-number* ] command to use Telnet to log in to the Telnet server through the specified IPv4 address.
  + IPv6 source address:
    
    Run the [**telnet**](cmdqueryname=telnet) **ipv6** [ **-a** *source-ip6* ] [ **public-net** | **vpn-instance** *ipv6-vpn-name* ] *ipv6-address* [ **-oi** { *interface-type interface-number* | *interface-name* } ] [ *port-number* ] command to use Telnet to log in to the Telnet server through the specified IPv6 address.
(Optional) Configuring DHCPv4 User-Defined Options
==================================================

You can configure DHCPv4 user-defined options to provide more control information and parameters for clients.

#### Context

If both the [**dhcp option125**](cmdqueryname=dhcp+option125) and [**option**](cmdqueryname=option) *125* commands are run, the [**dhcp option125**](cmdqueryname=dhcp+option125) command configuration takes effect.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**ip pool**](cmdqueryname=ip+pool) *pool-name* [ **bas** **local** | **server** ] command to create an address pool and enter the address pool view.
3. Run the **[**option**](cmdqueryname=option)** **code** { ****hex**** **hex-string** | { ****ip**** *ip-address-1* [ **ip-address-2**] } | ****string*****ascii-string* | **cipher** *cipher-text* } | { ****suboption*****sub-code* { ****ip**** *ip-address-1* | ****string**** **sub-ascii-string** } } &<1-16> } command to configure DHCPv4 options.
4. (Optional) Run the [**dhcp option125**](cmdqueryname=dhcp+option125) [ **enterprise-code** *enterprise-code* ] *option125-string* command to configure the telecom device vendor's enterprise code and related description to be encapsulated into DHCP Option 125.
   
   
   
   DHCP Option 125 that carries the device vendor's enterprise code and related description will be encapsulated into a DHCP reply message.
5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
6. Run the [**option force-reply**](cmdqueryname=option+force-reply) { *option-code* }&<1-16> command to configure the Option to be forcibly replied to the client by the DHCP server.
   
   
   
   Some DHCP option information is not replied by a server if a client does not initiate a request. However, without these DHCP option information, such as the IP address, the client cannot access the Internet. To resolve this problem, you can run this command to configure the option to be forcibly replied to the client.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * A maximum of 16 options to be forcibly replied can be configured in an IP address pool.
   * Information about the configured DHCP option code must be supported by the DHCP server. Otherwise, the server cannot forcibly reply the DHCP option to the client.
7. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Follow-up Procedure

The Option fields in DHCPv4 packets carry the control information and parameters that are not defined in common protocols. If the DHCPv4 server is configured with an Option, the DHCPv4 client obtains the configuration information saved in the Option field of DHCPv4 response packets.

You need to add the options to the attribute list of the DHCPv4 servers. For example:

* To configure the IP address of a log server to 10.110.204.1, run the **option 7 ip 10.110.204.1** command.
* To configure the DHCPv4 Option 129 field to represent "huawei", run the **option 129 string huawei** command.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The value of a common option (such as DNS or lease) is fixed. Such a value can be 3, 6, 15, 44, 46, 50-54, 57-59, 82, or 119. When the option value is re-set, the system prompts that re-setting the value is not allowed.

The **option** command enables the DHCPv4 packets replied by the server to carry specific options.

Before using this command, you need to know the function of the specific option. For example, Option 77 identifies a user class or application type for DHCPv4 clients. Based on User Class in the Option field, the DHCPv4 server selects a proper address pool to assign IP addresses and related configuration parameters for clients. Option 77 is commonly configured on the client, with no need for running the **option** command on the server.
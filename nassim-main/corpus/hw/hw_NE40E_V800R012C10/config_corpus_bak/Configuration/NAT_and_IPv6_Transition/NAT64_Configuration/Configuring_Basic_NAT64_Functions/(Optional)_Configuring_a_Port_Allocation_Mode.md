(Optional) Configuring a Port Allocation Mode
=============================================

Configuring a port allocation mode helps manage port resources.

#### Context

NAT64 supports three port allocation modes:

* Port pre-allocation: A NAT64 device pre-allocates an IPv4 address and a port range to an IPv6 address when mapping the IPv6 address to the IPv4 address. The IPv4 address and ports in the port range are used in the NAT64 mapping of the IPv6 address.
* Semi-dynamic port pre-allocation: When a host with an IPv6 address accesses an IPv4 network, a NAT64 device allocates an initial port range and then allocates the ports within the port range to the IPv6 address. If the number of ports used by the terminal exceeds the initial port range, the device allocates an extended port range. The maximum number of times the port range is extended determines the number of times the extended port range can be allocated.
* Dynamic port allocation: When mapping a private IP address to a public IP address, a NAT64 device pre-allocates a public IP address and a port range with a fixed size of 64 to the private IP address. If the number of used ports exceeds the initial port range, the NAT64 device assigns another port range with a fixed size of 64 to the user. The allocation process repeats without a limit on the maximum number of extended port ranges.

Configure a port allocation mode based on the service scale during network deployment.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**nat64 instance**](cmdqueryname=nat64+instance) *instance-name* **id** *id*
   
   
   
   The NAT64 instance view is displayed.
3. Run [**port-range**](cmdqueryname=port-range) *initial-port-range* [ **extended-port-range** *extended-port-range* **extended-times** *extended-times* ]
   
   
   
   The port pre-allocation mode is configured.
   
   
   
    If this configuration is performed, the port pre-allocation mode is enabled.
   * Pre-allocation mode: The **extended-port-range** *extended-port-range* **extended-times** *extended-times* parameter is not required when running this command.
   * To configure the semi-dynamic port pre-allocation mode, run the command with **extended-port-range** *extended-port-range* **extended-times** *extended-times* configured.
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the port pre-allocation mode or incremental port allocation mode has been configured, you can change the *port-range* parameter values in overriding mode. The change takes effect only for new users.
4. (Optional) Run [**port-reuse enable**](cmdqueryname=port-reuse+enable)
   
   
   
   The port reuse for TCP and other protocols is enabled.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * By default, sessions of different protocols using the same private IP address cannot share the same public port during port pre-allocation. After port reuse is enabled, for the same private IP address, TCP sessions can share a public port with sessions of other protocols.
   * The [**port-reuse enable**](cmdqueryname=port-reuse+enable) and [**port-single**](cmdqueryname=port-single) **enable** commands are mutually exclusive.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
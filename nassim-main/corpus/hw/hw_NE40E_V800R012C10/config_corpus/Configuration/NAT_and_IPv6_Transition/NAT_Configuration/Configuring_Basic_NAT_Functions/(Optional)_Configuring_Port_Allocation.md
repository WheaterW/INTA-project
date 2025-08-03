(Optional) Configuring Port Allocation
======================================

Configuring a port allocation mode helps manage port resources.

#### Context

The available port allocation modes are dynamic allocation, static pre-allocation, semi-dynamic pre-allocation, and per-port allocation. During network deployment, a port allocation mode is configured based on the service deployment scale.

* Port pre-allocation, also called the port range mode, enables a CGN device to pre-allocate a public IP address and port range to a private IP address for the CGN device to map the private IP address to the public IP address and a port in the port range.
* The semi-dynamic port allocation (semi-dynamic) mode is an extension of the port range mode. Semi-dynamic port allocation extends a single port segment used in the port range mode to three parameters: initial port range, extended port range, and maximum number of times a port range can be extended. Before users go online, a CGN device assigns an initial port segment and ports in the initial segment to users. If the number of used ports exceeds the initial port segment size, the device assigns an extended port segment, which can repeat for a specified maximum number of times.
* Dynamic port pre-allocation (port dynamic) enables a CGN device to pre-allocate a public IP address and a port range with 64 ports to a private IP address. If the number of used ports exceeds the initial port range size, the CGN device assigns another port range with 64 ports to the user. The allocation process repeats without a limit on the maximum number of extended port ranges. This mode features high usage of public network IP addresses, but involves a huge amount of log information. This requires a log server to handle logs.
* Per-port allocation, a type of dynamic port mode, enables a device to assign a port, not a port range each time the device creates a session. With per-port allocation enabled, port usage of public IP addresses is maximized. The per-port allocation mode applies when a few IPv4 or IPv6 public addresses are available.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Only the NE40E-M2K and NE40E-M2K-B support this configuration.


![](../../../../public_sys-resources/note_3.0-en-us.png) 

Only [dedicated boards](dc_ne_nat_feature_0008.html#EN-US_CONCEPT_0172359138__li1033371595) support this function.




#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**nat instance**](cmdqueryname=nat+instance+id) *instance-name* [ **id** *id* ]
   
   
   
   The NAT instance view is displayed.
3. (Optional) Run [**nat ip access-user limit**](cmdqueryname=nat+ip+access-user+limit) *max-number*
   
   
   
   The maximum number of users sharing the same NAT public IP address in PAT mode is set.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The [**nat ip access-user limit**](cmdqueryname=nat+ip+access-user+limit) command is mandatory in per-port allocation mode and is recommended in dynamic port allocation mode and semi-dynamic port allocation mode. Otherwise, a large number of users use the same public IP address, affecting subsequent user services.
4. Configure a port allocation mode. Modes 1 and 2 are mutually exclusive for a NAT instance. Before changing the port allocation mode, disable the existing mode first.
   
   
   * Mode 1: To configure the port pre-allocation mode, run the [**port-range**](cmdqueryname=port-range+extended-port-range+extended-times) *initial-port-range* [ **extended-port-range** *extended-port-range* **extended-times** *extended-times* ] command.Note the following when running the preceding command:
     + For port pre-allocation, the command does not need to carry the **extended-port-range** *extended-port-range* or **extended-times** *extended-times* parameters.
     + For semi-dynamic pre-allocation, the command must carry the **extended-port-range** *extended-port-range* and **extended-times** *extended-times* parameters.
   * Mode 2: To configure the per-port allocation mode, run the [**port-single**](cmdqueryname=port-single+enable) **enable** command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * By default, the dynamic port allocation mode is used. In this case, the number of ports to be allocated is not limited.
   * A port allocation mode works only for new online users in a NAT instance.
   * After a NAT instance is bound to a service board, the [**port-single**](cmdqueryname=port-single+enable) **enable** and [**undo port-single**](cmdqueryname=undo+port-single+enable) **enable** commands cannot both be run within 1 minute.
5. (Optional) Run [**port-reuse enable**](cmdqueryname=port-reuse+enable)
   
   
   
   The port multiplexing function is enabled for TCP and other protocols.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * By default, sessions of different protocols using the same private IP address cannot share the same public port during port pre-allocation. After the port multiplexing function is enabled, for the same private IP address, TCP sessions can share a public port with sessions of other protocols.
   * The [**port-reuse enable**](cmdqueryname=port-reuse+enable+enable) and [**port-single**](cmdqueryname=port-single+enable) **enable** commands are mutually exclusive.
6. (Optional) Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
7. (Optional) Run [**nat port-range algorithm round-robin**](cmdqueryname=nat+port-range+algorithm+round-robin)
   
   
   
   The round-robin algorithm is configured for port range allocation.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   A port range specified in the port-range command that is assigned in cursor-based port allocation mode will not be immediately used after being released. In some special scenarios, such a port range may be used immediately after being released.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
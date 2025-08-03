(Optional) Configuring a DS-Lite Port Allocation Mode
=====================================================

Configuring a port allocation mode helps manage port resources.

#### Context

DS-Lite supports the following port allocation modes:

* Dynamic port pre-allocation (Port Dynamic) enables a DS-Lite device to pre-allocate a public IP address and a port range with 64 ports to a private IP address. If the number of used ports exceeds the initial port range size, the DS-Lite device assigns another port range with 64 ports to the user. The allocation process repeats without a limit on the maximum number of extended port ranges. This mode features high usage of public network IP addresses, but involves a huge amount of log information. This requires a log server to handle logs.
* The semi-dynamic port allocation (Semi-Dynamic) mode is an extension of the port range mode. Semi-dynamic port allocation extends a single port segment used in the port range mode to three parameters:
  + Initial port range
  + Extended port range
  + Maximum number of times a port range can be extended
  
  Before users go online, a DS-Lite device assigns an initial port segment and ports in the initial segment to users. If the number of used ports exceeds the initial port segment size, the device assigns an extended port segment, which can repeat for a specified maximum number of times.
* Port pre-allocation: A port number range is pre-allocated on a DS-Lite device. When the first flow of a specific user arrives, the DS-Lite device selects a public IP address and associates the configured port number range with the user. Then ports are selected from this port number range to perform address-port replacement for all subsequent traffic of the user. The DS-Lite device records log information during the allocation and reclamation of the port number range. This mode involves a small amount of DS-Lite log information, facilitating log checking.

During network deployment, a port allocation mode is configured based on the service scale.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Select a port allocation mode as needed. Perform one of the following operations:
   
   
   * Configure a port allocation mode in the DS-Lite instance view.
     
     1. Run [**ds-lite instance**](cmdqueryname=ds-lite+instance) *instance-name* [ **id** *id* ]
        
        The DS-Lite instance view is displayed.
     2. Configure the port allocation mode.
        
        Run [**port-range**](cmdqueryname=port-range) *initial-port-range* [ **extended-port-range** *extended-port-range* **extended-times** *extended-times* ]
        
        The port pre-allocation mode is configured.
        
        After this command is run, ports work in pre-allocation modes.
        + To configure the static port pre-allocation mode, run the [**port-range**](cmdqueryname=port-range) command without **extended-port-range** *extended-port-range* or **extended-times** *extended-times* configured.
        + To configure the semi-dynamic port pre-allocation mode, run the [**port-range**](cmdqueryname=port-range) command with **extended-port-range** *extended-port-range* and **extended-times** *extended-times* configured.
        
        The port allocation mode takes effect only on new users in a DS-Lite instance.
   * Configure a port allocation mode in a NAT policy template.
     
     1. Run [**nat-policy template**](cmdqueryname=nat-policy+template) *template-name*
        
        A NAT policy template is created.
     2. Run [**port-range**](cmdqueryname=port-range) *initial-port-range* [ **extended-port-range** *extended-port-range* **extended-times** *extended-times* ]
        
        The port pre-allocation mode is configured.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If the [**port-range**](cmdqueryname=port-range) command is run in both the NAT policy template view and DS-Lite instance view, the configuration in the NAT policy template view takes effect. If the [**port-range**](cmdqueryname=port-range) command is not run in the NAT policy template view, the configuration in the DS-Lite instance view takes effect.
     
     If the [**port-single enable**](cmdqueryname=port-single+enable) command is run in the NAT instance view, the per-port allocation mode configured in the instance takes effect, regardless of whether the [**port-range**](cmdqueryname=port-range) command is run in the NAT policy template view. If the [**port-single enable**](cmdqueryname=port-single+enable) command is not run in the NAT instance view, the [**port-range**](cmdqueryname=port-range) command run in the NAT policy template view takes effect.
     
     The configurations in a NAT policy template take effect only after the NAT policy template is issued by a RADIUS server. If packets of users to go online match the NAT policy template, the configuration in the template takes effect on the users.
3. (Optional) Run [**port-reuse enable**](cmdqueryname=port-reuse+enable)
   
   
   
   The port reuse function is enabled for TCP and other protocols.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * By default, sessions of different protocols using the same private IP address cannot share the same public port during port pre-allocation. After port reuse is enabled, for the same private IP address, TCP sessions can share a public port with sessions of other protocols.
   * The [**port-reuse enable**](cmdqueryname=port-reuse+enable) and [**port-single**](cmdqueryname=port-single) **enable** commands are mutually exclusive.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
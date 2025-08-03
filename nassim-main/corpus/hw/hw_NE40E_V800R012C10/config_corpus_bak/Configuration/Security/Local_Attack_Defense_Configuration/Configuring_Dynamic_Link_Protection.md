Configuring Dynamic Link Protection
===================================

You can configure dynamic link protection to allow protocol packets used to establish sessions to be preferentially sent to the CPU when the bandwidth is guaranteed.

#### Usage Scenario

As various network protocol packets exist on a network, protocol packets that require sessions to be established, such as BGP, IS-IS, and FTP protocol packets, need sufficient bandwidth for session establishment. In the case of insufficient bandwidth, packets used to establish sessions are dropped, causing the protocol sessions not to be established. When the dynamic link protection function is enabled, after a protocol session is established, sufficient bandwidth can be allocated to ensure uninterrupted protocol sessions.

In VS mode, this feature is supported only by the admin VS.


#### Prerequisites

None


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**cpu-defend policy**](cmdqueryname=cpu-defend+policy) *policy-number*
   
   
   
   The attack defense policy view is displayed.
3. Run [**undo dynamic-link-protection disable**](cmdqueryname=undo+dynamic-link-protection+disable)
   
   
   
   The dynamic link protection function is enabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Checking the Configurations

After configuring interface-based CAR, check the configurations.

Run the [**display cpu-defend policy**](cmdqueryname=display+cpu-defend+policy) *policy-number* command to view information about the user-defined attack defense policy.
Configuring an MCP
==================

A Measurement Control Point (MCP) collects statistics reported by Data Collecting Points (DCPs), summarizes and calculates the statistics, and reports measurement results to user terminals or the network management system (NMS).

#### Context

On the network shown in [Figure 1](#EN-US_TASK_0172372884__fig_dc_vrp_ipfpm_cfg_000601), IP Flow Performance Measurement (FPM) end-to-end performance statistics collection is implemented. The target flow enters the transport network through DeviceA, travels across DeviceB, and leaves the transport network through DeviceC. To monitor transport network performance or diagnose faults, configure IP FPM end-to-end performance statistics collection on both DeviceA and DeviceC. DeviceA functions as an MCP to collect statistics reported by DCP1 and DCP3, summarize and calculate the statistics, and report measurement results to user terminals or the NMS.**Figure 1** IP FPM end-to-end performance statistics collection  
![](images/fig_dc_vrp_ipfpm_cfg_000601.png)

Perform the following steps on DeviceA:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**nqa ipfpm mcp**](cmdqueryname=nqa+ipfpm+mcp)
   
   
   
   MCP is enabled globally, and the IPFPM-MCP view is displayed.
3. Run [**mcp id**](cmdqueryname=mcp+id) *mcp-id*
   
   
   
   An MCP ID is configured.
   
   
   
   Using the Router ID of a device that is configured as an MCP as its MCP ID is recommended.
   
   The MCP ID must be an IP address reachable to DCPs. The MCP ID configured on an MCP must be the same as that specified in the [**mcp**](cmdqueryname=mcp) *mcp-id* [ **port** *port-number* ] command run in the IP FPM instance view of all DCPs associated with this MCP. If an MCP ID is changed on an MCP, it must be changed for all DCPs associated with this MCP in an IP FPM instance. Otherwise, the MCP cannot process the statistics reported by the DCPs.
4. (Optional) Run [**protocol udp port**](cmdqueryname=protocol+udp+port) *port-number*
   
   
   
   A UDP port number is specified for the MCP to communicate with DCPs.
   
   The UDP port number configured on an MCP must be the same as that specified in the [**mcp**](cmdqueryname=mcp) *mcp-id* [ **port** *port-number* ] command run in the IP FPM instance view of all DCPs associated with this MCP. If a UDP port number is changed on an MCP, it must be changed for all DCPs associated with this MCP in an IP FPM instance. Otherwise, the MCP cannot process the statistics reported by the DCPs.
5. (Optional) Run [**authentication-mode**](cmdqueryname=authentication-mode) **hmac-sha256** **key-id** *key-id* [ **cipher** ] [ *password* | **password** ]
   
   
   
   An authentication mode and password are configured on the MCP.
   
   
   
   The authentication mode and password configured on the MCP must be the same as those configured using the [**authentication-mode**](cmdqueryname=authentication-mode) **hmac-sha256** **key-id** *key-id* [ **cipher** ] [ *password* | **password** ] command on the DCPs associated with the MCP. Otherwise, the MCP cannot obtain the statistics reported by the DCPs.
6. Run [**instance**](cmdqueryname=instance) *instance-id*
   
   
   
   An IP FPM instance is created, and the instance view is displayed.
   
   *instance-id* must be unique on an MCP and all its associated DCPs. The MCP and all its associated DCPs must have the same IP FPM instance configured. Otherwise, statistics collection does not take effect.
7. (Optional) Run [**description**](cmdqueryname=description) *text*
   
   
   
   The description is configured for the IP FPM instance.
   
   The description of an IP FPM instance can contain the functions of the instance, facilitating applications.
8. Run [**dcp**](cmdqueryname=dcp) *dcp-id*
   
   
   
   A DCP ID is specified in the IP FPM instance.
   
   The DCP ID configured in an IP FPM instance must be the same as that specified in the [**dcp id**](cmdqueryname=dcp+id) *dcp-id* command run on a DCP. Otherwise, the MCP associated with this DCP cannot process the statistics reported by the DCP.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Follow-up Procedure

When DCP configurations are being changed, the MCP may receive incorrect statistics from the DCP. To prevent this, run the [**measure disable**](cmdqueryname=measure+disable) command to disable IP FPM performance statistics collection of a specified instance on the MCP. After the DCP configuration change is complete, run the [**undo measure disable**](cmdqueryname=undo+measure+disable) or [**measure enable**](cmdqueryname=measure+enable) command to enable IP FPM performance statistics collection for the specified instance on the MCP. This ensures accurate measurement.
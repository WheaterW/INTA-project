Using 802.1ag MAC Ping to Check Link Connectivity on a Layer 2 Network
======================================================================

802.1ag MAC ping monitors connectivity between MEPs or between MEPs and MIPs within an MA.

#### Context

Similar to the ping operation, 802.1ag MAC ping checks whether the destination device is reachable by sending test packets and receiving response packets. In addition, the ping operation time can be calculated at the transmit end for network performance analysis.

Before performing 802.1ag MAC ping, ensure that 802.1ag has been configured. For details, see [Configuring Basic Ethernet CFM Functions](dc_vrp_cfm_cfg_000004.html).


#### Procedure

1. A device is usually configured with multiple MDs and MAs. To monitor the connectivity of a link between two or more devices, perform either of the following steps on the NE40E with a MEP on one end of the link to be monitored.
   
   
   * In the MA view:
     
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**cfm enable**](cmdqueryname=cfm+enable)
        
        CFM is globally enabled on the device.
     3. Run [**cfm md**](cmdqueryname=cfm+md) *md-name*
        
        The MD view is displayed.
     4. Run [**ma**](cmdqueryname=ma) ma-name
        
        The MA view is displayed.
     5. Run [**ping mac-8021ag**](cmdqueryname=ping+mac-8021ag) **mep** **mep-id** *mep-id* [ **md** *md-name* **ma** *ma-name* ] { **mac** *mac-address* | **remote-mep** **mep-id** *mep-id* } [ **-c** *count* | **-s** *packetsize* | **-t** *timeout* | **-p** *priority-value* ] \*
        
        The connectivity between a MEP and an RMEP or between a MEP and a MIP on other devices is monitored.
        
        The following shows an example:
        
        ```
        <HUAWEI> system-view 
        [~HUAWEI] cfm enable
        [*HUAWEI] cfm md md1 
        [*HUAWEI-md-md1] ma ma1 
        [*HUAWEI-md-md1-ma-ma1] ping mac-8021ag mep mep-id 1 md md1 ma ma1 remote-mep mep-id 2 
        Pinging 00e0-fc12-3456 with 95 bytes of data: 
        Reply from 00e0-fc12-3456: bytes = 95, time = 11ms 
        Reply from 00e0-fc12-3456: bytes = 95, time = 2ms 
        Reply from 00e0-fc12-3456: bytes = 95, time = 3ms 
        Reply from 00e0-fc12-3456: bytes = 95, time = 3ms 
        Reply from 00e0-fc12-3456: bytes = 95, time = 2ms 
        Packets: Sent = 5, Received = 5, Lost = 0 (0% loss) 
        Minimum = 2ms, Maximum = 11ms, Average = 4ms
        ```
   * In all views except the MA view:
     
     Run [**ping mac-8021ag**](cmdqueryname=ping+mac-8021ag) **mep** **mep-id** *mep-id* **md** *md-name* **ma** *ma-name* { **mac** *mac-address* | **remote-mep** **mep-id** *mep-id* } [ **-c** *count* | **-s** *packetsize* | **-t** *timeout* | **-p** *priority-value* ] \*
     
     The connectivity between a MEP and an RMEP or between a MEP and a MIP on other devices is monitored.
   
   When implementing 802.1ag MAC ping, ensure that:
   
   * The MEP is configured in the MA.
   * If the destination node is an RMEP, either **mac** *mac-address* or **remote-mep** **mep-id** *mep-id* can be specified. If **remote-mep** **mep-id** *mep-id* is selected, the remote maintenance association end point (RMEP) must already be created using the [**remote-mep**](cmdqueryname=remote-mep) command.
   * If the destination node is a MIP, select **mac** *mac-address*.
   
   The intermediate device on the link to be tested only forwards LBMs and LBRs. Therefore, the MD, MA, or MEP does not need to be configured on the intermediate device.
2. (Optional) Run the [**display cfm statistics lblt**](cmdqueryname=display+cfm+statistics+lblt) command to check 802.1ag protocol packet statistics.
   
   
   
   If the test using the [**ping mac-8021ag**](cmdqueryname=ping+mac-8021ag) command fails, you can run this command to check whether a link fault or a device fault occurs.
3. (Optional) Run the [**reset cfm statistics lblt**](cmdqueryname=reset+cfm+statistics+lblt) command to clear the 802.1ag protocol packet statistics.
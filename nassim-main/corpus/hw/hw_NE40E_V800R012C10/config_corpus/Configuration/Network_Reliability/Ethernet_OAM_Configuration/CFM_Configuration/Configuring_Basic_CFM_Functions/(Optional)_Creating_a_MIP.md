(Optional) Creating a MIP
=========================

A maintenance association intermediate point (MIP) is a node inside an MA. Each MEP periodically multicasts CCMs. MIPs are used to locate the fault.

#### Context

MIPs can be automatically generated based on rules or manually configured on interfaces. [Table 1](#EN-US_TASK_0172361945__tab_dc_vrp_cfm_cfg_00001001) describes MIP creation modes.

**Table 1** MIP generation modes
| Creation Mode | Description |
| --- | --- |
| Automatic generation | A device automatically generates MIPs based on a configured creation rule in the maintenance domain (MD) or default MD view.  Configuring a creation rule is complex, but a configured creation rule can ensure correct MIP settings. |
| Manual configuration | You must specify a MIP level. Manually configured MIPs are preferable to automatically generated MIPs. Although configuring MIPs manually is easy, managing many manually configured MIPs is difficult and errors may be inadvertently introduced into the configurations. |

MIP creation rules are classified into three types: explicit, default, and none. [Table 2](#EN-US_TASK_0172361945__tab_dc_vrp_cfm_cfg_00001002) describes these MIP creation rules.

**Table 2** MIP creation rules
| Manually Configured MIPs Exist on an Interface | Creation Rule Type | MEPs Are Configured for Low-Level MDs | MIPs Are Created |
| --- | --- | --- | --- |
| Yes | â | â | No |
| No | default | No | Yes |
| explicit | Yes | Yes |
| none | â | â |


![](../../../../public_sys-resources/note_3.0-en-us.png) 

If the defer MIP generation rule is configured in the MA view, MIPs are created in an MA using rules configured in the MD to which MIPs belong.


After you configure a MIP creation rule, either of the following conditions can trigger MIP generation or deletion:

* Connectivity fault management (CFM) is enabled or disabled.
* The configured MIP creation rule changes.

Perform either of the following operations on each device on which a MIP needs to be created:


#### Procedure

* Configure a MIP manually.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**cfm mip**](cmdqueryname=cfm+mip) **level** *level-value*
     
     
     
     A MIP is manually configured.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a MIP automatically
  
  
  
  MIP generation rules in compliance with either IEEE 802.1ag Draft 7 or IEEE Std 802.1ag-2007 can be configured on a device.
  
  
  
  1. Configure a MIP generation rule in accordance with IEEE 802.1ag/Draft 7 in the system view.
     
     
     1. Run [**cfm enable**](cmdqueryname=cfm+enable)
        
        CFM is enabled globally.
     2. Run [**cfm md**](cmdqueryname=cfm+md) *md-name*
        
        The MD view is displayed.
        
        Alternatively, run the [**cfm default md**](cmdqueryname=cfm+default+md) [ **level** *level* ] command to enter the default MD view.
        
        Select either of the views.
     3. Run [**mip create-type**](cmdqueryname=mip+create-type) { **default** | **explicit** | **none**}
        
        A MIP generation rule in accordance with IEEE 802.1ag Draft 7 is configured.
  2. Configure a MIP generation rule in accordance with IEEE Standard 802.1ag-2007 in the MD view.
     
     
     1. Run [**cfm enable**](cmdqueryname=cfm+enable)
        
        CFM is enabled globally.
     2. Run either of the following commands:
        
        To enter the MD view, run the [**cfm md**](cmdqueryname=cfm+md) *md-name* command.
        
        To enter the default MD view, run the [**cfm default md**](cmdqueryname=cfm+default+md) [ **level** *level* ] command.
     3. Run [**mip create-type**](cmdqueryname=mip+create-type) { **default** | **explicit** | **none** }
        
        A MIP generation rule in accordance with IEEE Standard 802.1ag-2007 is configured in a specific MD.
  3. Configure a MIP generation rule in accordance with IEEE Standard 802.1ag-2007 in the MA view.
     
     
     1. Run [**cfm md**](cmdqueryname=cfm+md) *md-name*
        
        The MD view is displayed.
     2. Run [**ma**](cmdqueryname=ma) *ma-name*
        
        The MA view is displayed.
     3. Run [**mip create-type**](cmdqueryname=mip+create-type) { **default** | **explicit** | **none** | **defer** }
        
        A MIP generation rule in accordance with IEEE Standard 802.1ag-2007 is configured in a specific MA.
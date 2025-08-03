Configure the CFM CCM Statistics Function
=========================================

To collect statistics about CFM CCMs sent and received on a device, configure the CFM CCM statistics function.

#### Pre-configuration Tasks

Before configuring the CFM CCM statistics function, configure basic CFM functions.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**cfm ccm statistic enable**](cmdqueryname=cfm+ccm+statistic+enable)
   
   
   
   The CFM CCM statistics function is enabled globally.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed. The device starts to collect statistics about sent and received CFM CCMs.
4. (Optional) Run [**display ccm-send statistics**](cmdqueryname=display+ccm-send+statistics)
   
   
   
   The number of CFM CCMs sent by the device after the [**cfm ccm statistic enable**](cmdqueryname=cfm+ccm+statistic+enable) command is run is displayed.
5. (Optional) Run [**display ccm-recv statistics**](cmdqueryname=display+ccm-recv+statistics)
   
   
   
   The number of CFM CCMs received by the device after the [**cfm ccm statistic enable**](cmdqueryname=cfm+ccm+statistic+enable) command is run is displayed.
6. (Optional) Run [**reset ccm-send statistics**](cmdqueryname=reset+ccm-send+statistics)
   
   
   
   The statistics about CFM CCMs sent by the device are reset.
7. (Optional) Run [**reset ccm-recv statistics**](cmdqueryname=reset+ccm-recv+statistics)
   
   
   
   The statistics about CFM CCMs received by the device are reset.
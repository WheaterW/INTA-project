Enabling Attack Source Tracing
==============================

If attack source tracing is manually disabled, you need do as follows to enable it.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**cpu-defend policy**](cmdqueryname=cpu-defend+policy) *policy-number*
   
   
   
   The attack defense policy view is displayed.
3. Run [**attack-source-trace enable**](cmdqueryname=attack-source-trace+enable)
   
   
   
   The attack source tracing function is enabled.
   
   After the [**attack-source-trace enable**](cmdqueryname=attack-source-trace+enable) command is run, attack source tracing is enabled on all functional modules. After the [**undo attack-source-trace enable**](cmdqueryname=undo+attack-source-trace+enable) command is run, attack source tracing is disabled on all functional modules.
4. Run [**attack-source-trace**](cmdqueryname=attack-source-trace+car+tcpip-defend+ma-defend) { **car** | **tcpip-defend** | **ma-defend** | **application-apperceive** | **totalcar** } **enable**
   
   
   
   Attack defense tracing is enabled for a certain local attack defense feature.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
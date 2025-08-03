(Optional) Enabling a Serial Interface to Use RML Bits in PW Control Words to Transparently Transmit Alarms
===========================================================================================================

When configuring the remote TDMoPSN service or remote CEP service, you can enable the serial interface to use RML bits in PW control words to transparently transmit alarms as required.

#### Prerequisites

The [**link-protocol**](cmdqueryname=link-protocol) **tdm** command has been already configured on the serial interface.


#### Context

In a TDM PWE3 usage scenario, the [**pw-control-word rml-bit enable**](cmdqueryname=pw-control-word+rml-bit+enable) command configures whether the serial interface uses RML bits in PW control words to transparently transmit alarms. If alarms indicating continuous loss of frames are generated, the serial interface can transparently transmit alarms.

On the network shown in [Figure 1](#EN-US_TASK_0176506757__fig_01) where an LMSP group works in single-node or two-node 1+1 unidirectional mode, after the [**pw-control-word rml-bit enable**](cmdqueryname=pw-control-word+rml-bit+enable) command is run in the Trunk-Serial interface view, a single-fiber failure in the RSG -> RNC direction may interrupt services. Specifically, after a single-fiber failure occurs in the RSG (active interface) -> RNC direction, the RNC sends an MS-RDI alarm to the RSG. If the RSG and CSG both have transparent alarm transmission enabled, the MS-RDI alarm will be transparently transmitted over a TDM PWE3 PW to the base station NODE\_B. BTS services will then detect the E1 RDI alarm. **Figure 1** TDM PWE3 single-fiber failure  
![](figure/en-us_image_0176518870.png)

If the base stations are insensitive to RDI alarms, services will not be affected. Otherwise, E2E services will be interrupted. To prevent this problem, disable transparent alarm transmission when an LMSP group works in single-node or two-node 1+1 unidirectional mode. If you have to enable transparent alarm transmission in such a situation, customize the MS-RDI alarm on the CPOS1 and CPOS2 interfaces in the LMSP group to prevent this problem.


#### Procedure

1. Run [**interface serial**](cmdqueryname=interface+serial) *interface-number*
   
   
   
   The serial interface view is displayed.
2. Run [**pw-control-word rml-bit enable**](cmdqueryname=pw-control-word+rml-bit+enable)
   
   
   
   The serial interface is enabled to use RML bits in PW control words to transparently transmit alarms.
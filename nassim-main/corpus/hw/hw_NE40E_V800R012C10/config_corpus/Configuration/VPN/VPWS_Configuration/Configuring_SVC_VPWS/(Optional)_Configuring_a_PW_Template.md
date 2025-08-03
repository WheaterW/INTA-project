(Optional) Configuring a PW Template
====================================

A PW template is a collection of common PW attributes. Configuring PWs using a PW template helps save configuration workload.

#### Context

Before configuring PWs with similar attributes, you can define a PW template that contains the common attributes of these PWs. Then, you can configure these PWs based on the PW template to simplify the configuration process. For example, if multiple VPWS connections with the same MTU, peer address, control word setting, and tunnel policy need to be configured between two PEs, you can define these common attributes in a PW template and use the PW template to configure these PWs on different PE interfaces.

Perform the following configurations on the endpoint PEs of a PW.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls l2vpn**](cmdqueryname=mpls+l2vpn)
   
   
   
   MPLS L2VPN is configured.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. Run [**pw-template**](cmdqueryname=pw-template) *pwname*
   
   
   
   A PW template is created, and its view is displayed.
   
   
   
   If some PW attributes configured using the [**mpls l2vc**](cmdqueryname=mpls+l2vc) command on an interface are different from those specified in the PW template, the PW attributes configured using the [**mpls l2vc**](cmdqueryname=mpls+l2vc) command take precedence.
5. Configure PW attributes. The following steps are optional and can be selected as required.
   
   
   * Run the [**peer-address**](cmdqueryname=peer-address) *ip-address* command to specify the IP address of the remote PE on the PW.
   * Run the [**control-word**](cmdqueryname=control-word) command to enable the control word function.
   * Run the [**mtu**](cmdqueryname=mtu) *mtu-value* command to configure the MTU in the PW template.
   * Run the [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name* command to specify the tunnel policy to be used by the PW.
   * Run the [**flow-label**](cmdqueryname=flow-label) { **both** | **send** | **receive** } [ **static** ] command to configure flow label-based load balancing.
   * Run the [**jitter-buffer depth**](cmdqueryname=jitter-buffer+depth) *depth* command to configure the depth of the jitter buffer for the TDMoPSN application.
   * Run the [**idle-code**](cmdqueryname=idle-code) *idleCodeValue* command to set the idle code that is filled when a jitter buffer underflow occurs.
   * Run the [**rtp-header**](cmdqueryname=rtp-header) command to add the RTP header to transparently transmitted TDM frames.
   * Run the [**tdm-encapsulation-number**](cmdqueryname=tdm-encapsulation-number) *tdmEncapNumber* command to configure the number of TDM frames encapsulated into a Circuit Emulation Services over Packet Switch Network (CESoPSN) or Structure-Agnostic Time Division Multiplexing over Packet (SAToP) packet in the TDMoPSN application.
   * (Optional) Run the following commands so that ATM services can be transmitted:
     + Run the [**atm-pack-overtime**](cmdqueryname=atm-pack-overtime) *atm-pack-overtime* command to configure the ATM cell encapsulation period.
     + Run the [**max-atm-cells**](cmdqueryname=max-atm-cells) *max-atm-cell-value* command to configure the maximum number of ATM cells that can be transmitted.
     + Run the [**transmit-atm-cells**](cmdqueryname=transmit-atm-cells) *transmit-atm-cell-value* command to configure the maximum number of ATM cells to be encapsulated into a packet that can be sent by a device.
     + Run the [**cc seq-number**](cmdqueryname=cc+seq-number) command to enable the control word sequence number function.
   * (Optional) Run the following commands if CEP services need to be transmitted:
     + Run the [**jitter-buffer-cep depth**](cmdqueryname=jitter-buffer-cep+depth) *cep-depth* command to configure jitter buffer depth for CEP services.
     + Run the [**payload-compression dba**](cmdqueryname=payload-compression+dba) **uneq** command to configure payload compression DBA for CEP services.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Follow-up Procedure

After the PW attributes in a PW template are modified, run the [**reset pw**](cmdqueryname=reset+pw) **pw-template** *pw-template-name* command for the modifications to take effect. Running this command will cause PWs referencing this PW template to reset. If multiple PWs are referencing this template, system operation is affected.
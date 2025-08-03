Verifying the DS-TE Configuration
=================================

After configuring DS-TE, you can verify DS-TE information and CT information of a tunnel.

#### Prerequisites

All DS-TE functions have been configured.
#### Procedure

* Run the [**display mpls te ds-te**](cmdqueryname=display+mpls+te+ds-te) { **summary** | **te-class-mapping** [ **default** | **config** | **verbose** ] } command to check DS-TE information.
* Run the [**display mpls te
  te-class-tunnel**](cmdqueryname=display+mpls+te+te-class-tunnel) { **all** |{ **ct0** | **ct1** | **ct2** | **ct3** | **ct4** | **ct5** | **ct6** | **ct7** } **priority** *priority* } command to check information about the TE tunnel associated with TE-classes.
* Run the [**display interface tunnel**](cmdqueryname=display+interface+tunnel) *interface-number* command to check CT traffic information on a specified tunnel interface.
* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **mpls-te** [ **area** *area-id* ] [ **self-originated** ] command to check OSPF TE information.
* Run either of the following commands to check the IS-IS TE status:
  + [**display
    isis traffic-eng advertisements**](cmdqueryname=display+isis+traffic-eng+advertisements) [ *lsp-id* | **local** ] [ **level-1** | **level-2** | **level-1-2** ] [ *process-id* | **vpn-instance** *vpn-instance-name* ]
  + [**display isis
    traffic-eng statistics**](cmdqueryname=display+isis+traffic-eng+statistics) [ *process-id* | **vpn-instance** *vpn-instance-name* ]
Configuring the Server
======================

This section describes how to configure the TWAMP server, which responds to the control-client's request for establishing, starting, or stopping a TWAMP session.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**nqa twamp**](cmdqueryname=nqa+twamp)
   
   
   
   The TWAMP view is displayed.
3. Run [**server**](cmdqueryname=server)
   
   
   
   The server function is enabled, and the server view is displayed.
4. Run either of the following commands to set the TCP listening mode for the TWAMP server:
   
   
   * Run the [**tcp listen-mode**](cmdqueryname=tcp+listen-mode) **any-ip** command to set the TCP listening mode of the TWAMP server to any IP.
   * Run the [**tcp listen-mode**](cmdqueryname=tcp+listen-mode) **assign-ip** command to set the TCP listening mode of the TWAMP server to assigned IP. In this mode, you need to run the [**tcp listen-address**](cmdqueryname=tcp+listen-address) *ip-address* command to set a TCP listening address.
5. (Optional) Run [**tcp port**](cmdqueryname=tcp+port) *port-number* [ **all** | **vpn-instance** *vpn-instance-name* ]
   
   
   
   A TCP port is specified.
6. (Optional) Run [**control-session inactive**](cmdqueryname=control-session+inactive) *time-out*
   
   
   
   An inactive interval is configured for a control session.
7. (Optional) Run [**client acl**](cmdqueryname=client+acl) { *aclnumBasic* | *aclnumAdv* | *aclname* }
   
   
   
   The ACL rule to be referenced is configured.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
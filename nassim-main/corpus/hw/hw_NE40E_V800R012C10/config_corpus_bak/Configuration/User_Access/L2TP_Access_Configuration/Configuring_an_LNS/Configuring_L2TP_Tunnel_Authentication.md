Configuring L2TP Tunnel Authentication
======================================

An L2TP tunnel can be successfully established only after L2TP tunnel authentication succeeds.

#### Context

Tunnel authentication improves tunnel security. An L2TP tunnel supports local, remote (RADIUS), and forcible RADIUS authentication.

In local authentication mode, a tunnel password, instead of a tunnel name, is used for a LAC or LNS to authenticate a tunnel. The tunnel name is used only by the LNS to select an L2TP group to respond to a connection request from the LAC. There is no special requirement on the format of the tunnel name, but the tunnel name configured on the LAC must be the same as the LAC tunnel name configured on the LNS. No LNS tunnel name needs to be configured on the LNS.

In remote authentication mode, a LAC or LNS takes an L2TP tunnel as a user; therefore, the format of the tunnel name must be username@domain. When a tunnel is set up, the LAC or LNS sends the received username and password from each other to the AAA server (RADIUS server) for authentication. To perform authentication, a username and password must be configured in advance on the AAA server

In forcible RADIUS authentication mode, a RADIUS server determines whether tunnel authentication is performed. If the attributes delivered by the RADIUS server contain a tunnel password, the tunnel password is used for tunnel authentication; otherwise, tunnel authentication is not performed.

Select proper configuration procedure based on the authenticate mode you want to configure.


#### Procedure

* Local authentication
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**l2tp-group**](cmdqueryname=l2tp-group) *group-name*
     
     
     
     An L2TP group is created, and its view is displayed.
  3. (Optional) Run [**tunnel name**](cmdqueryname=tunnel+name) *tunnel-name* [ **lns-ip** *lns-ip-address* ]
     
     
     
     A local tunnel name is specified.
  4. Run [**tunnel authentication**](cmdqueryname=tunnel+authentication) [ **strict** ]
     
     
     
     Tunnel authentication is enabled.
     
     You can decide whether to enable tunnel authentication before creating a tunnel connection. To ensure tunnel security, it is recommended that tunnel authentication be enabled.
     
     A tunnel authentication request can be initiated either by a LAC or an LNS. As long as one end is enabled with tunnel authentication, identity authentication is performed in the tunnel setup process. A tunnel can be set up only if the passwords of both ends are the same and not empty; otherwise, the local end automatically tears down the tunnel. If tunnel authentication is disabled on both ends, tunnel authentication is not performed, irrespective of whether passwords on both ends are the same.
     
     The [**tunnel authentication**](cmdqueryname=tunnel+authentication) **strict** command configuration takes effect only for the L2TP group on a LAC. After strict tunnel authentication is configured, the LAC performs validity check on the remote LNS's tunnel name and password. If the LNS tunnel name and password delivered by the RADIUS server or locally configured are different from those of the remote LNS, tunnel establishment fails. After strict tunnel authentication is configured, you can configure the RADIUS server to deliver the Tunnel-Server-Auth-ID attribute or configure an LNS tunnel name in the L2TP group view of the LAC based on site requirements.
  5. Run [**tunnel password**](cmdqueryname=tunnel+password) [ **lns-ip** *lns-ip-address* ] { **simple** *password* | **cipher** *cipher-password* }
     
     
     
     A password for tunnel authentication is set.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Remote (RADIUS) authentication
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**l2tp-group**](cmdqueryname=l2tp-group) *group-name*
     
     
     
     An L2TP group is created, and its view is displayed.
  3. Run [**tunnel authentication**](cmdqueryname=tunnel+authentication)
     
     
     
     Tunnel authentication is enabled.
     
     You can decide whether to enable tunnel authentication before creating a tunnel connection. To ensure tunnel security, it is recommended that tunnel authentication be enabled.
     
     A tunnel authentication request can be initiated either by a LAC or an LNS. As long as one end is enabled with tunnel authentication, identity authentication is performed in the tunnel setup process. A tunnel can be set up only if the passwords of both ends are the same and not empty; otherwise, the local end automatically tears down the tunnel. If tunnel authentication is disabled on both ends, tunnel authentication is not performed, irrespective of whether passwords on both ends are the same.
  4. Run [**tunnel aaa-authentication**](cmdqueryname=tunnel+aaa-authentication)
     
     
     
     Remote authentication is enabled.
     
     Remote authentication indicates that the L2TP tunnel is not authenticated locally, but authenticated on an AAA server (RADIUS server).
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Forcible RADIUS authentication
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**l2tp-group**](cmdqueryname=l2tp-group) *group-name*
     
     
     
     An L2TP group is created, and its view is displayed.
  3. Run [**tunnel radius-force**](cmdqueryname=tunnel+radius-force)
     
     
     
     Forcible RADIUS authentication is enabled.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
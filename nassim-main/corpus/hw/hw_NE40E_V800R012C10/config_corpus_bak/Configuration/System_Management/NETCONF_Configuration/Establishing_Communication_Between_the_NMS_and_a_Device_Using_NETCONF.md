Establishing Communication Between the NMS and a Device Using NETCONF
=====================================================================

To ensure secure and smooth communication between the network management system (NMS) and a device managed by the NMS, enable the Secure Shell (SSH) service on the server and deploy the NMS on the client. This section describes only the configuration of the server. For details about the NMS configuration, see the related NMS configuration manual.

#### Usage Scenario

NETCONF ensures security and extensibility. When the NMS is used to manage network devices, you can use NETCONF to ensure communication between the NMS and the devices.

As shown in [Figure 1](#EN-US_TASK_0139427564__fig_dc_vrp_netconf_cfg_000201), the NMS is deployed on the client that functions as the SSH client. The server functions as the SSH server that receives connection requests from and establishes the connection with the SSH client. SSH is a security protocol at the application layer, enhancing the reliability of NETCONF. In this networking, NETCONF is used to manage the configuration of the SSH server.

**Figure 1** Networking diagram for establishing communication between the NMS and a device using NETCONF  
![](images/fig_dc_vrp_netconf_cfg_000201.png)  
#### Pre-configuration Tasks

Before establishing communication between the NMS and a device using NETCONF, deploy NMS on the client.



[Configuring an SSH User](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_netconf_cfg_0003.html)

When specifying a secure shell protocol (SSH) as the transport protocol of NETCONF, you must configure an SSH user, configure the SSH server to generate a local key pair, configure a user authentication mode, and specify a service type for the SSH user.

[Enabling NETCONF](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_netconf_cfg_0004.html)

A NETCONF connection can be established between the client and the server using the well-known port 22 only after NETCONF is enabled on the server.

[(Optional) Enabling Proactive NETCONF Registration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_netconf_cfg_0019.html)

Proactive NETCONF registration enables a device to send a NETCONF connection request to the NMS when the device goes online.

[(Optional) Configuring NETCONF Authorization](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_netconf_cfg_0016.html)

You can configure NETCONF authorization to authorize specific users to perform NETCONF operations or access NETCONF resources. NETCONF authorization ensures the device security.

[(Optional) Configuring NETCONF YANG Model Switching](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_netconf_cfg_0018.html)

You can switch between different NETCONF YANG models. 

[Logging in to the Server Using the NMS](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_netconf_cfg_0006.html)

After the preceding configuration is complete, you can log in to the server from the client using the NMS. This allows you to remotely configure the device.

[Verifying the Configuration of Communication Between the NMS and a Device Using NETCONF](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_netconf_cfg_0007.html)

After NETCONF is configured to allow the NMS to remotely manage device configurations, check detailed SSH session information, the SSH connection between the SSH server and client, and the capabilities that the server supports.
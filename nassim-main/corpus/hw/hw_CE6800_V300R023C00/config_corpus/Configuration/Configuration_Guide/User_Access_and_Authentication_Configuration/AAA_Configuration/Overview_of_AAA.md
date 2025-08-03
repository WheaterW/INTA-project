Overview of AAA
===============

Access control is the way you control who is allowed access to the network server and what services they are allowed to use once they have access. Authentication, authorization, and accounting (AAA) network security services provide the primary framework through which you set up access control on the Network Access Server (NAS).

#### Definition

AAA is an architectural framework for configuring a set of three independent security functions in a consistent manner. AAA provides a modular way of performing the following services:

* Authentication: confirms the identities of users accessing the network and determines whether the users are authorized.
* Authorization: assigns differentiated rights to authorize users to use specific services.
* Accounting: records all the operations of a user during the network service process, including the used service type, start time, and data traffic, to collect and record the network resource usage of the user for implementing time- or traffic-based accounting and network monitoring.

#### Basic Architecture

AAA uses the client/server structure. The access device on which an AAA client runs is usually called an NAS. The NAS is responsible for user identity verification and user access management. An AAA server provides a collection of authentication, authorization, and accounting functions and is responsible for centralized user information management. [Figure 1](#EN-US_CONCEPT_0000001564115705__fig1) shows the basic AAA architecture.

**Figure 1** Basic architecture of AAA  
![](figure/en-us_image_0000001512676598.png)

For the AAA server in [Figure 1](#EN-US_CONCEPT_0000001564115705__fig1), you can determine which protocols that the AAA server uses to implement authentication, authorization, and accounting functions respectively based on actual networking requirements. Users can use only one or two security services provided by AAA. For example, if a company only wants to authenticate employees who access certain network resources, the network administrator only needs to configure an authentication server. If the company also wants to record operations performed by employees on the network, an accounting server is required.


#### Purpose

AAA provides authentication, authorization, and accounting functions for users, preventing unauthorized users from logging in to a switch and improving system security.
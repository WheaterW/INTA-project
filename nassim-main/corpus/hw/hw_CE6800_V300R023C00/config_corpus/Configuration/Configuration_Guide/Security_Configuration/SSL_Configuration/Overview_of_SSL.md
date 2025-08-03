Overview of SSL
===============

Overview of SSL

#### Definition

Secure Sockets Layer (SSL) is a cryptographic protocol that provides communication security over the Internet. SSL prevents eavesdropping on communications between the client and server, and verifies the identities of communicating parties, guaranteeing secure data transmission over the Internet.


#### Purpose

New Internet-based applications such as e-commerce and online banking have increased due to the convenience they offer in people's daily lives. As these applications require online transactions on the Internet, they pose higher requirements on network communication security. However, the traditional Hypertext Transfer Protocol (HTTP) for web-based communication does not have a security mechanism. This protocol transmits data in clear text. It is unable to verify the identities of communicating parties or prevent transmitted data from being tampered with. As a result, HTTP does not meet the security requirements of new applications. In this case, SSL, developed by Netscape, provides data encryption, identity authentication, and message integrity verification mechanisms, improving data transmission security. Specifically, SSL provides secure connections for HTTP, significantly improving web-based communication security.

In addition, SSL can secure data transmission for any application layer protocol based on Transmission Control Protocol (TCP) connections, because it functions between the application and transport layers.
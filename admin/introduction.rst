Introduction
============

About this manual
-----------------

This manual describes the installation and configuration of Veyon in a computer network and is addressed to system administrators and technically skilled users. For end users a separate user manual exists explaining usage and specific functions of the user program (Veyon Master).

The further sections of this chapter contain basic information about Veyon and its components which are of fundamental importance for putting Veyon into operation.

Chapter :ref:`Installation` deals with the installation of Veyon on a Windows or Linux computer. It also contains information on how to perform or implement an automated installation.

Chapter :ref:`Configuration` explains how to configure and integrate Veyon using the graphical configuration tool, whereas the :ref:`ConfigurationReference` describes all available configuration options in detail. Information and examples on how to connect Veyon to an LDAP or ActiveDirectory server can be found in chapter :ref:`LDAP`.

Veyon is furthermore equipped with a command line interface (:index:`CLI`) that can be used for modifying the configuration, automate Veyon-related tasks and for using or controlling specific program functions. All modules and commands of the command line tool are listed and explained in chapter :ref:`CommandLineInterface`.

In case Veyon causes problem during its installation or configuration actions can be taken as described in chapter :ref:`Troubleshooting`. Frequently asked questions are answered in chapter :ref:`FAQ`.


About Veyon
-----------

Veyon is a free and open source software for computer monitoring and class room management. It allows to monitor and control computer rooms as well as to interact with users, e.g. students. The following functions are available in Veyon:

* Overview of a (class) room with screen contents of computers being shown in thumbnails
* Remote view or control computers
* Broadcast the teacher's sceen to all other computers in real time (full screen/window demo)
* Lock computers to control attention
* Send text messages to students
* Power on, reboot or shutdown computers remotely
* Log out users
* Launch programs and open websites

.. index:: teacher computer, student computer, master computer, client computer

.. _Components:

Components
----------

Veyon basically consists of of a master and a service component which realize the interaction between teacher and student computers (also referred as *master computer* and *client computer*):

.. image:: images/service-master-components.png
   :scale: 50 %
   :align: center

In detail there are several :index:`program components` that interact with each other in different ways:

.. image:: images/architecture.png
   :scale: 50 %
   :align: center

:index:`Veyon Master`
	An application program that can be used for monitoring and controlling other computers as well as for accessing Veyon features. Usually the program is started by the end user. It accesses other computers through the Veyon Service.

:index:`Veyon Service`
	A non-graphical service application which monitors user sessions on a computer and starts Veyon Server instances within these sessions. The service and its server subprocesses are required to run on all computers including teacher computers.

:index:`Veyon Server`
	A server application which provides access to a computer as well as control and application functions. Under normal conditions this program is started by the Veyon Service automatically and with elevated privileges so it can't be terminated by users.

:index:`Veyon Worker`
	A helper program started by the server to provide specific functions in an isolated environment or in the context of the user that is currently logged in. Those specific functions include the demo server for the teacher computer and the demo client on the student computers.

:index:`Veyon Configurator`
	A :index:`configuration tool` which allows to configure and customize all components of a local Veyon installation through a graphical user interface. The program is started by the administrator with elevated privileges whenever necessary.

:index:`Veyon Control`
	A command line tool that in addition to the Veyon Configurator allows various configuration adjustments, automated tasks and the use of some Veyon functions without graphical interaction. The program is run either interactively on the command line or script controlled with usually elevated privileges.


Network architecture
--------------------

From a network perspective the following components and TCP ports are involved:

.. image:: images/network-architecture.png
   :scale: 50 %
   :align: center


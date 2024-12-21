############
TerminalAlert
############

|contributors| |forks| |stars| |issues| |license|

Command Completion Alerts – Stay Notified, Stay Productive!

`Explore the repo <https://github.com/Jemeni11/TerminalAlert>`_

Table of Contents
================
* `Introduction`_
* `Features`_
* `Installation`_
* `Usage`_
* `Examples`_
* `Roadmap`_
* `Why did I build this?`_
* `Contributing`_
* `Wait a minute, who are you?`_
* `License`_
* `Changelog`_

Introduction
===========
TerminalAlert is a command-line application that keeps you informed about the
completion of your terminal commands.

Once a command completes, TerminalAlert sends a desktop notification indicating whether it succeeded or failed.

Perfect for multitaskers, this tool helps you stay productive without
having to monitor the terminal constantly.

Features
--------
* **Command Completion Alerts**: Receive desktop notifications when your terminal commands finish executing.
* **Detailed Command Summary**: After execution, the terminal displays:
    * ``Output``: Standard output (if any).
    * ``Error``: Standard error (if any).
    * ``Execution time``: The time taken in seconds.
* **Success & Failure Indicators**: Notifications clearly indicate whether the command succeeded or encountered errors.
* **Cross-Platform Support**: Works on Windows, macOS, and Linux.

.. note::
   Some applications may output error messages to ``stderr`` even when they execute successfully. For example:

   ``terminalalert "git clone https://github.com/Jemeni11/TerminalAlert.git TADupl"``

   May produce the following:

      Output: None

      Error: Cloning into 'TADupl'...

      Execution time: 4.45 seconds

   This behavior depends on how the specific application writes to ``stdout`` and ``stderr``.

.. warning::
   This tool is only partially complete on Windows. When it sends notifications,
   it will **NOT** display TerminalAlert as the notification title. The title will likely display 'Python' or a similar
   default. The same goes for the icon next to the title. If you mute TerminalAlert notifications
   on Windows, you will be unable to enable them again. This is a known Windows bug with a fix in progress.

Installation
===========

From PyPI (Using PIP)
--------------------
::

   pip install TerminalAlert``


Usage
=====
TerminalAlert is easy to use. Simply pass the command you want to
execute as an argument, and you'll receive a desktop notification upon its completion.

*TerminalAlert does not save any of your commands.*

::

   usage: terminalalert [-h] [-u] command

   Command Completion Alerts – Stay Notified, Stay Productive!

   positional arguments:
     command       The command to run.

   options:
     -h, --help    show this help message and exit
     -u, --update  Check if a new version is available.

Examples
========
Hello World
----------
::

   terminalalert "echo 'Hello World!'"

Clone a repo
-----------
::

   terminalalert "git clone https://github.com/Jemeni11/TerminalAlert.git"

Check for an update
-----------------
::

   terminalalert -u

Roadmap
=======
* [✓] Initial MVP with desktop notifications
* [ ] Fix Windows specific issues

See the `open issues <https://github.com/Jemeni11/TerminalAlert/issues>`_ for a full list of proposed features (and known
issues).

Why did I build this?
====================
I was cloning a big git repo while coding. I didn't want to monitor it 24/7, so I minimized the terminal and continued
coding. To my surprise, when I checked after 10 minutes, the process had failed. My network connection was unreliable
that day (let's not name the ISP). I retried multiple times, and it failed multiple times. This experience inspired me
to create a tool that could notify me when a terminal command completes.

Contributing
===========
Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any
contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also
simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (``git checkout -b feature/AmazingFeature``)
3. Commit your Changes (``git commit -m 'Add some AmazingFeature'``)
4. Push to the Branch (``git push origin feature/AmazingFeature``)
5. Open a Pull Request

Wait a minute, who are you?
==========================
`TerminalAlert <https://github.com/Jemeni11/TerminalAlert>`_ was built by Emmanuel Jemeni, a Frontend Developer with a
passion for Python.

You can find me on various platforms:

* `LinkedIn <https://www.linkedin.com/in/emmanuel-jemeni/>`_
* `GitHub <https://github.com/Jemeni11>`_
* `Twitter <https://twitter.com/Jemeni11_>`_

If you'd like, you can support me on `GitHub Sponsors <https://github.com/sponsors/Jemeni11/>`_
or `Buy Me A Coffee <https://www.buymeacoffee.com/jemeni11>`_.

License
=======
`MIT License <https://github.com/Jemeni11/TerminalAlert/blob/main/LICENSE>`_.

Changelog
========
`Changelog <https://github.com/Jemeni11/TerminalAlert/blob/main/CHANGELOG.md>`_

.. |contributors| image:: https://img.shields.io/github/contributors/Jemeni11/TerminalAlert.svg?style=for-the-badge
   :target: https://github.com/Jemeni11/TerminalAlert/graphs/contributors

.. |forks| image:: https://img.shields.io/github/forks/Jemeni11/TerminalAlert.svg?style=for-the-badge
   :target: https://github.com/Jemeni11/TerminalAlert/network/members

.. |stars| image:: https://img.shields.io/github/stars/Jemeni11/TerminalAlert.svg?style=for-the-badge
   :target: https://github.com/Jemeni11/TerminalAlert/stargazers

.. |issues| image:: https://img.shields.io/github/issues/Jemeni11/TerminalAlert.svg?style=for-the-badge
   :target: https://github.com/Jemeni11/TerminalAlert/issues

.. |license| image:: https://img.shields.io/github/license/Jemeni11/TerminalAlert.svg?style=for-the-badge
   :target: https://github.com/Jemeni11/TerminalAlert/blob/main/LICENSE
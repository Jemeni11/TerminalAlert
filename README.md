<a id="readme-top"></a>

<!-- PROJECT SHIELDS -->

[//]: # ([![Contributors][contributors-shield]][contributors-url])

[//]: # ([![Forks][forks-shield]][forks-url])

[//]: # ([![Stargazers][stars-shield]][stars-url])

[//]: # ([![Issues][issues-shield]][issues-url])

[//]: # ([![MIT License][license-shield]][license-url])



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Jemeni11/TerminalAlert">
    <img src="/TerminalAlert/icons/logo.png" alt="Logo" width="128" height="128">
  </a>

  <h1 align="center">TerminalAlert</h1>

  <p align="center">
    Command Completion Alerts – Stay Notified, Stay Productive!
    <br />
    <a href="https://github.com/Jemeni11/TerminalAlert"><strong>Explore the repo »</strong></a>
  </p>
</div>




Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Roadmap](#roadmap)
- [Why did I build this?](#why-did-i-build-this)
- [Contributing](#contributing)
- [Wait a minute, who are you?](#wait-a-minute-who-are-you)
- [License](#license)
- [Changelog](#changelog)

## Introduction

TerminalAlert is a command-line application that keeps you informed about the
completion of your terminal commands.

Once a command completes, TerminalAlert sends a desktop notification indicating whether it succeeded or failed.

Perfect for multitaskers, this tool helps you stay productive without
having to monitor the terminal constantly.

### Features

- **Command Completion Alerts**: Receive desktop notifications when your terminal commands finish executing.
- **Detailed Command Summary**: After execution, the terminal displays:
    - `Output`: Standard output (if any).
    - `Error`: Standard error (if any).
    - `Execution time`: The time taken in seconds.
- **Success & Failure Indicators**: Notifications clearly indicate whether the command succeeded or encountered errors.
- **Cross-Platform Support**: Works on Windows, macOS, and Linux.

> [!NOTE]
>
> Some applications may output error messages to `stderr` even when they execute successfully. For example:
>
> ```bash
> terminalalert "git clone https://github.com/Jemeni11/TerminalAlert.git TADupl"
> ```
> May produce the following:
> ```
> Output: None  
> Error: Cloning into 'TADupl'...  
> Execution time: 4.45 seconds  
> ```
> This behavior depends on how the specific application writes to `stdout` and `stderr`.


> [!WARNING]
>
> This tool is only partially complete on Windows. When it sends notifications,
> it will **NOT** display TerminalAlert as the notification title. The title will likely display 'Python' or a similar
> default.
> The same goes for the icon next to the title. If you mute TerminalAlert notifications
> on Windows, you will be unable to enable them again. This is a known Windows bug with a fix in progress.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Installation

### From PyPI (Using PIP)

```
pip install TerminalAlert
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage

TerminalAlert is easy to use. Simply pass the command you want to
execute as an argument, and you'll receive a desktop notification upon its completion.

_TerminalAlert does not save any of your commands._

```
usage: terminalalert [-h] [-u] command

Command Completion Alerts – Stay Notified, Stay Productive!

positional arguments:
  command       The command to run.

options:
  -h, --help    show this help message and exit
  -u, --update  Check if a new version is available.
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Examples

- Hello World

    ```
    terminalalert "echo 'Hello World!'"
    ```

- Clone a repo

    ```
    terminalalert "git clone https://github.com/Jemeni11/TerminalAlert.git"
    ```

- Check for an update

    ```
    terminalalert -u
    ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Roadmap

- [x] Initial MVP with desktop notifications
- [ ] Fix Windows specific issues

See the [open issues](https://github.com/Jemeni11/TerminalAlert/issues) for a full list of proposed features (and known
issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Why did I build this?

I was cloning a big git repo while coding. I didn't want to monitor it 24/7, so I minimized the terminal and continued
coding. To my surprise, when I checked after 10 minutes, the process had failed. My network connection was unreliable
that day (let's not name the ISP). I retried multiple times, and it failed multiple times. This experience inspired me
to create a tool that could notify me when a terminal command completes.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any
contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also
simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Wait a minute, who are you?

[TerminalAlert](https://github.com/Jemeni11/TerminalAlert) was built by Emmanuel Jemeni, a Frontend Developer with a
passion for Python.

You can find me on various platforms:

- [LinkedIn](https://www.linkedin.com/in/emmanuel-jemeni/)
- [GitHub](https://github.com/Jemeni11)
- [Twitter](https://twitter.com/Jemeni11_)

If you'd like, you can support me on [GitHub Sponsors](https://github.com/sponsors/Jemeni11/)
or [Buy Me A Coffee](https://www.buymeacoffee.com/jemeni11).


<p align="right">(<a href="#readme-top">back to top</a>)</p>

## License

[MIT License](/LICENSE).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Changelog

[Changelog](/CHANGELOG.md)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


[contributors-shield]: https://img.shields.io/github/contributors/Jemeni11/TerminalAlert.svg?style=for-the-badge

[contributors-url]: https://github.com/Jemeni11/TerminalAlert/graphs/contributors

[forks-shield]: https://img.shields.io/github/forks/Jemeni11/TerminalAlert.svg?style=for-the-badge

[forks-url]: https://github.com/Jemeni11/TerminalAlert/network/members

[stars-shield]: https://img.shields.io/github/stars/Jemeni11/TerminalAlert.svg?style=for-the-badge

[stars-url]: https://github.com/Jemeni11/TerminalAlert/stargazers

[issues-shield]: https://img.shields.io/github/issues/Jemeni11/TerminalAlert.svg?style=for-the-badge

[issues-url]: https://github.com/Jemeni11/TerminalAlert/issues

[license-shield]: https://img.shields.io/github/license/Jemeni11/TerminalAlert.svg?style=for-the-badge

[license-url]: https://github.com/Jemeni11/TerminalAlert/blob/master/LICENSE.txt

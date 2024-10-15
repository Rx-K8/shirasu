# shirasu

![logo](site/assets/logo.jpeg)

This is a tool to notify you of the completion of program processing.

## Description
When running long processes, it can feel like waiting for paint to dry.
Especially with machine learning, predicting the exact finish time is like trying to guess the weather a month in advance.
Shirasu is here to save the day by notifying you when your program has finally finished.
With this tool, you can relax and enjoy your coffee without constantly peeking at your screen to see if the process is done.

## Requirements
- python: 3.11

## Preparation
### Discord
1. Create bot account(Please enable the Send Messages permission for Bot Permissions)
2. Invite bot

Please refer to the details [here](https://discordpy.readthedocs.io/ja/latest/discord.html)

## Usage
### setup
```sh
Usage: shirasu setup [OPTIONS]

Options:
  --delete  -d        Delete the settings.
  --help              Show this message and exit.
```

### notify
```sh
Usage: shirasu notify [OPTIONS] "COMMAND"

Arguments:
  COMMAND   the command for processing

Options:
  --discord  -d        Enable discord notification. 
  --help               Show this message and exit.
```

## Example
Commands containing spaces must be enclosed in single or double quotation marks.

```sh
$ shirasu notify -d "ls -l"
```

## About

### Authors
* Keito Fukuoka ([Rx-K8](https://github.com/Rx-K8))

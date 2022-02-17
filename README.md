# rich-click

**Format [click](https://click.palletsprojects.com/) help output nicely with [Rich](https://github.com/Textualize/rich).**

- Click is a _"Python package for creating beautiful command line interfaces"_.
- Rich is a _"Python library for rich text and beautiful formatting in the terminal"_.

The intention of `rich-click` is to provide attractive help output from
click, formatted with rich, with minimal customisation required.

## Features

- 🌈 Rich command-line formatting of click help and error messages
- 💫 Nice styles be default, usage is simply `import rich_click as click`
- 🔢 Easily give custom sort order for options and commands
- 🎁 Group commands and options into named panels
- 🎨 Extensive customisation of styling and behaviour possible

![rich-click](docs/images/command_groups.png)

## Installation

You can install `rich-click` from the Python Package Index (PyPI) with `pip` or equivalent.

```bash
python -m pip install rich-click
```

## Usage

To use `rich-click`, switch out your normal `click` import with `rich-click`, using the same namespace:

```python
import rich_click as click
```

That's it. Then continue to use `click` as you would normally.
See [`examples/01_simple.py`](examples/01_simple.py) for an example.

The intention is to maintain most / all of the normal click functionality and arguments.
If you spot something that breaks or is missing once you start using the plugin, please create an issue about it.

Alternatively, if you prefer you can `RichGroup` or `RichCommand` with the `cls` argument in your click usage instead.
This means that you can continue to use the unmodified `click` package in parallel.
See [`examples/02_declarative.py`](examples/02_declarative.py) for an example.

## Groups and sorting

`rich-click` gives functionality to list options and subcommands in groups, printed as separate panels.
It accepts a list of options / commands which means you can also choose a custom sorting order.

- For options (flags), set `click.rich_click.OPTION_GROUPS`
- For subcommands (groups), set `click.rich_click.COMMAND_GROUPS`

See [`examples/03_groups_sorting.py`](examples/03_groups_sorting.py) for a full example.

### Options

To group option flags into two sections with custom names, see the following example:

```python
click.rich_click.OPTION_GROUPS = {
    "mytool": [
        {
            "name": "Simple options",
            "options": ["--name", "--description", "--version", "--help"],
        },
        {
            "name": "Advanced options",
            "options": ["--force", "--yes", "--delete"],
        },
    ]
}
```

If you omit `name` it will use `Commands` (can be configured with `OPTIONS_PANEL_TITLE`, see _Customisation_ below).

### Commands

Here we create two groups of commands for the base command of `mytool`.
Any subcommands not listed will automatically be printed in a panel at the end labelled "Commands" as usual.

```python
click.rich_click.COMMAND_GROUPS = {
    "mytool": [
        {
            "name": "Commands for uploading",
            "commands": ["sync", "upload"],
        },
        {
            "name": "Download data",
            "commands": ["get", "fetch", "download"],
        },
    ]
}
```

If you omit `name` it will use `Commands` (can be configured with `COMMANDS_PANEL_TITLE`, see _Customisation_ below).

### Multiple commands

If you use multiple nested subcommands, you can specify their commands using the top-level dictionary keys:

```python
click.rich_click.COMMAND_GROUPS = {
    "mytool": ["commands": ["sync", "auth"]],
    "mytool sync": [
        {
            "name": "Commands for uploading",
            "commands": ["sync", "upload"],
        },
        {
            "name": "Download data",
            "commands": ["get", "fetch", "download"],
        },
    ],
    "mytool auth":[{"commands": ["login", "logout"]}],
}
```

## Customisation

You can customise most things that are related to formatting.

For example, to limit the maximum width of the help output to 100 characters:

```python
click.rich_click.MAX_WIDTH = 100
```

To print the option flags in a different colour, use:

```python
click.rich_click.STYLE_OPTION = "magenta"
```

### Full list of config options

```python
# Default styles
STYLE_OPTION = "bold cyan"
STYLE_SWITCH = "bold green"
STYLE_METAVAR = "bold yellow"
STYLE_USAGE = "yellow"
STYLE_USAGE_COMMAND = "bold"
STYLE_DEPRECATED = "red"
STYLE_HELPTEXT_FIRST_LINE = ""
STYLE_HELPTEXT = "dim"
STYLE_METAVAR = "bold yellow"
STYLE_OPTION_HELP = ""
STYLE_OPTION_DEFAULT = "dim"
STYLE_REQUIRED_SHORT = "red"
STYLE_REQUIRED_LONG = "dim red"
STYLE_OPTIONS_PANEL_BORDER = "dim"
ALIGN_OPTIONS_PANEL = "left"
STYLE_COMMANDS_PANEL_BORDER = "dim"
ALIGN_COMMANDS_PANEL = "left"
STYLE_ERRORS_PANEL_BORDER = "red"
ALIGN_ERRORS_PANEL = "left"
MAX_WIDTH = None  # Set to an int to limit to that many characters

# Fixed strings
DEPRECATED_STRING = "(Deprecated) "
DEFAULT_STRING = "[default: {}]"
REQUIRED_SHORT_STRING = "*"
REQUIRED_LONG_STRING = "[required]"
RANGE_STRING = " [{}]"
ARGUMENTS_PANEL_TITLE = "Arguments"
OPTIONS_PANEL_TITLE = "Options"
COMMANDS_PANEL_TITLE = "Commands"
ERRORS_PANEL_TITLE = "Error"

# Behaviours
SHOW_ARGUMENTS = False
GROUP_ARGUMENTS_OPTIONS = False
USE_MARKDOWN = False
USE_RICH_MARKUP = False
COMMAND_GROUPS = {}
OPTION_GROUPS = {}
```

## Contributing

Contributions and suggestions for new features are welcome, as are bug reports!
Please create a new [issue](https://github.com/ewels/rich-click/issues)
or better still, dive right in with a pull-request.

## Credits

This package was written by Phil Ewels ([@ewels](http://github.com/ewels/)),
based on initial code by Will McGugan ([@willmcgugan](https://github.com/willmcgugan)).
